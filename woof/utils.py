import logging

import requests
from django.conf import settings
from django.core.cache import cache
from django.db.models import Count
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from .models import Category, Dogs

logger = logging.getLogger(__name__)

menu = [
    {"title": _("About us"), "url_name": "about"},
    {"title": _("Groups"), "url_name": "groups"},
    {"title": _("Breeds"), "url_name": "breeds"},
    {"title": _("Guides"), "url_name": "guides"},
    {"title": _("Contact"), "url_name": "contact"},
]

# Open Graph locales are "xx_YY"; Django language codes are lowercase.
OG_LOCALES = {
    "en": "en_US",
    "sr-latn": "sr_RS",
    "ru": "ru_RU",
    "de": "de_DE",
    "it": "it_IT",
    "es": "es_ES",
}

CATS_CACHE_KEY = "cats"
CATS_CACHE_TIMEOUT = 60 * 15  # 15 minutes

DEFAULT_META_DESCRIPTION = _(
    "Woof Dogs — the world's dog breeds grouped by FCI classification: "
    "temperament, size, care and more."
)


SITEMAP_CACHE_KEY = "sitemap"
SITEMAP_CACHE_TIMEOUT = 60 * 60  # 1 hour; a save bumps the version below


def sitemap_cache_key(request):
    """One cached sitemap per scheme+host, invalidated by a version counter."""
    version = cache.get(SITEMAP_CACHE_KEY + "_version", 0)
    return f"{SITEMAP_CACHE_KEY}:{request.scheme}://{request.get_host()}:{version}"


def bump_sitemap_version():
    """Make every cached sitemap stale after content changed."""
    key = SITEMAP_CACHE_KEY + "_version"
    try:
        cache.incr(key)
    except ValueError:
        cache.set(key, 1, None)


def send_telegram_message(text):
    """Send a plain-text message to the site's Telegram chat.

    Used by the contact form and by the cookie-consent report. Returns True
    when Telegram accepted the message, False otherwise (missing credentials
    or API error — logged, never raised).
    """
    if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
        logger.error(
            "Telegram credentials are not configured (TOKEN/CHAT_ID); "
            "message was not delivered"
        )
        return False
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            url,
            data={"chat_id": settings.TELEGRAM_CHAT_ID, "text": text},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to deliver Telegram message")
        return False
    return True


def nobreak_range(value):
    """«63–68» → «63–68» без возможности переноса после тире.

    U+2060 (word joiner) не даёт браузеру разорвать диапазон
    «63–68» на две строки, но остаётся невидимым для читателя.
    """
    if not value:
        return value
    return str(value).replace("\u2013", "\u2013\u2060")


def sex_pair(male, female, unit_key):
    """Рост/вес по полу в том же виде, что и в карточках параметров:
    «♂\u00a068–72\u00a0см, ♀\u00a063–68\u00a0см». unit_key — "cm" или "kg"."""
    unit = str(_(unit_key))

    def one(symbol, value):
        if not value:
            return ""
        return f"{symbol}\u00a0{nobreak_range(value)}\u00a0{unit}"

    parts = [p for p in (one("♂", male), one("♀", female)) if p]
    return ", ".join(parts)


def _lang_prefixes():
    """Prefixes of all non-default languages, e.g. ["ru", "de"]"""
    default = settings.LANGUAGE_CODE
    return [code for code, _ in settings.LANGUAGES if code != default]


def switch_lang_url(path, target):
    """Add/remove the language prefix for the alternate-language link."""
    base = path
    for code in _lang_prefixes():
        prefix = "/" + code
        if base == prefix or base.startswith(prefix + "/"):
            base = base[len(prefix) :] or "/"
            break
    if target == settings.LANGUAGE_CODE:
        return base
    if base == "/":
        return "/" + target + "/"
    return "/" + target + base


class DataMixin:
    """Shared context for every page: menu, categories, published breeds."""

    def get_user_context(self, **kwargs):
        context = kwargs

        context["menu"] = menu.copy()
        context["cats"] = self._get_categories()
        context.setdefault("cat_selected", 0)
        context.setdefault("is_home", False)
        context.setdefault(
            "all_breeds", Dogs.objects.filter(is_published=True).order_by("title")
        )

        # SEO: description + hreflang alternates
        path = self.request.path
        context.setdefault("meta_description", DEFAULT_META_DESCRIPTION)
        # Open Graph locale: the page's own plus every other language
        context["og_locale"] = OG_LOCALES.get(
            get_language(), OG_LOCALES[settings.LANGUAGE_CODE]
        )
        # Only languages the site actually serves: OG_LOCALES may list more.
        context["og_locale_alternates"] = [
            OG_LOCALES[code]
            for code, _ in settings.LANGUAGES
            if code in OG_LOCALES and OG_LOCALES[code] != context["og_locale"]
        ]

        context["page_urls"] = [
            {
                "code": code,
                # BCP 47: Serbian Latin is written "sr-Latn" (Django code:
                # sr-latn). Other codes are already valid BCP 47 tags.
                "hreflang": "sr-Latn" if code == "sr-latn" else code,
                "url": self.request.build_absolute_uri(switch_lang_url(path, code)),
            }
            for code, _ in settings.LANGUAGES
        ]
        return context

    @staticmethod
    def _get_categories():
        # translation-aware cache key: the first request (en or ru) would
        # otherwise seed the shared cache with only one language
        lang = get_language()
        return cache.get_or_set(
            f"{CATS_CACHE_KEY}:{lang}",
            lambda: list(Category.objects.annotate(Count("dogs"))),
            CATS_CACHE_TIMEOUT,
        )
