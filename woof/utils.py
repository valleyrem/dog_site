from django.core.cache import cache
from django.db.models import Count
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from .models import Category, Dogs

menu = [
    {"title": _("All groups"), "url_name": "groups"},
    {"title": _("About us"), "url_name": "about"},
    {"title": _("Guides"), "url_name": "guides"},
    {"title": _("Explore"), "url_name": "dog-explore"},
    {"title": _("Contact"), "url_name": "contact"},
]

CATS_CACHE_KEY = "cats"
CATS_CACHE_TIMEOUT = 60 * 15  # 15 minutes

DEFAULT_META_DESCRIPTION = _(
    "Woof Dogs — the world's dog breeds grouped by American Kennel Club "
    "standards: temperament, size, care and more."
)


def switch_lang_url(path, target):
    """Add/remove the /ru prefix for the alternate-language link."""
    if path.startswith("/ru"):
        base = path[3:] or "/"
    else:
        base = path
    if target == "ru" and not base.startswith("/ru"):
        return "/ru" + ("" if base == "/" else base)
    return base


class DataMixin:
    """Shared context for every page: menu, categories, published breeds."""

    paginate_by = 4

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
        context.setdefault(
            "meta_description",
            DEFAULT_META_DESCRIPTION if not self.request.path.startswith("/ru")
            else DEFAULT_META_DESCRIPTION,
        )
        context["page_url_en"] = self.request.build_absolute_uri(
            switch_lang_url(path, "en")
        )
        context["page_url_ru"] = self.request.build_absolute_uri(
            switch_lang_url(path, "ru")
        )

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
