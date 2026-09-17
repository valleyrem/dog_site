import logging
from pathlib import Path

import requests
from django.conf import settings
from django.core.cache import cache
from django.db.models import Count
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from .models import Category, Dogs

logger = logging.getLogger(__name__)

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
    "Woof Dogs — the world's dog breeds grouped by FCI classification: "
    "temperament, size, care and more."
)


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
            (
                DEFAULT_META_DESCRIPTION
                if not self.request.path.startswith("/ru")
                else DEFAULT_META_DESCRIPTION
            ),
        )
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
        context["page_url_en"] = context["page_urls"][0]["url"]
        if len(context["page_urls"]) > 1:
            context["page_url_ru"] = context["page_urls"][1]["url"]

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


# ---------------------------------------------------------------------------
# Branded OG share cards (1200x630)
# ---------------------------------------------------------------------------

OG_CARD_TITLE = "woof dogs"
OG_CARD_SUBTITLE = "A little mess, a lot of love"
OG_CARD_FOOTER = "breeds · groups · guides"

OG_CARD_W = 1200
OG_CARD_H = 630
OG_CARD_HALF = 600  # left half: photo; right half: brand panel
OG_CARD_PAD = 44
OG_CARD_GAP1 = 48  # title -> subtitle
OG_CARD_GAP2 = 34  # subtitle -> footer
OG_CARD_SEAM_W = 26  # soft shadow strip at the photo edge


def _og_font(name, size):
    """Load a Pillow font from the committed og fonts (repo static/fonts/og)."""
    from PIL import ImageFont

    path = Path(settings.BASE_DIR) / "static" / "fonts" / "og" / name
    return ImageFont.truetype(str(path), size)


def build_og_card_bytes(photo_file, credit=None):
    """Render the 1200x630 share card (photo left, brand right) as JPEG bytes.

    Mirrors the homepage hero: photo column (object-fit: cover) on the left,
    "woof dogs" + slogan + footer in the site's fonts and colors on the right.
    When ``credit`` is given, a small "* credit" footnote is drawn below the
    footer.
    """
    from io import BytesIO

    from PIL import Image, ImageChops, ImageDraw, ImageOps

    W, H = OG_CARD_W, OG_CARD_H
    HALF = OG_CARD_HALF
    GREEN = "#028d6a"
    TEXT_DARK = "#22272f"
    GRAY = (134, 137, 143)

    # ---- left: photo, cover-cropped to 600x630 (like .hero-photo) ----
    img = Image.open(photo_file)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")
    pw, ph = img.size
    scale = max(HALF / pw, H / ph)
    sw, sh = int(pw * scale + 0.5), int(ph * scale + 0.5)
    img = img.resize((sw, sh), Image.LANCZOS)
    img = img.crop(
        (
            (sw - HALF) // 2,
            (sh - H) // 2,
            (sw - HALF) // 2 + HALF,
            (sh - H) // 2 + H,
        )
    )

    canvas = Image.new("RGB", (W, H), "#ffffff")
    canvas.paste(img, (0, 0))

    # soft shadow at the seam (echoes .hero-photo box-shadow)
    grad = Image.new("L", (OG_CARD_SEAM_W, H), 0)
    for i in range(OG_CARD_SEAM_W):
        a = int(255 * 0.10 * (1 - i / OG_CARD_SEAM_W) ** 2)
        for y in range(H):
            grad.putpixel((i, y), a)
    canvas.paste(
        Image.new("RGB", (OG_CARD_SEAM_W, H), (28, 43, 39)),
        (HALF - OG_CARD_SEAM_W, 0),
        grad,
    )

    d = ImageDraw.Draw(canvas)

    def widths_and_total(font, text, tracking):
        ws = [d.textlength(ch, font=font) for ch in text]
        return sum(ws) + tracking * (len(text) - 1), ws

    # title: auto-fit (like the homepage 96px title, proportional tracking)
    size_title = 94
    while size_title >= 70:
        font_title = _og_font("ClashDisplay-Semibold.ttf", size_title)
        tr = size_title * (7 / 96)
        total_t, widths_t = widths_and_total(font_title, OG_CARD_TITLE, tr)
        if total_t <= HALF - 2 * OG_CARD_PAD:
            break
        size_title -= 2

    font_sub = _og_font("SpaceGrotesk-Bold.ttf", 30)
    sub_tr = 30 * 0.09
    total_s, widths_s = widths_and_total(font_sub, OG_CARD_SUBTITLE, sub_tr)

    font_f = _og_font("SpaceGrotesk-Bold.ttf", 16)
    f_tr = 16 * 0.16
    total_f, widths_f = widths_and_total(font_f, OG_CARD_FOOTER, f_tr)

    credit_line = None
    if credit:
        font_c = _og_font("SpaceGrotesk-Bold.ttf", 13)
        c_tr = 0
        credit_line = f"* {credit}"
        total_c, widths_c = widths_and_total(font_c, credit_line, c_tr)

    def probe_y(font, color, text, tracking):
        probe = Image.new("RGB", (W, H), "#ffffff")
        dd = ImageDraw.Draw(probe)
        x = HALF + OG_CARD_PAD
        for ch, w in [(c, d.textlength(c, font=font)) for c in text]:
            dd.text((x, 0), ch, font=font, fill=color)
            x += w + tracking
        diff = ImageChops.difference(
            probe, Image.new("RGB", probe.size, (255, 255, 255))
        ).convert("L")
        return diff.getbbox()  # (left, top, right, bottom) painted at y=0

    _, t0, _, b0 = probe_y(font_title, GREEN, OG_CARD_TITLE, tr)
    _, ts0, _, bs0 = probe_y(font_sub, TEXT_DARK, OG_CARD_SUBTITLE, sub_tr)
    _, tf0, _, bf0 = probe_y(font_f, GRAY, OG_CARD_FOOTER, f_tr)
    if credit_line:
        _, tc0, _, bc0 = probe_y(font_c, GRAY, credit_line, c_tr)

    block_h = (b0 - t0) + OG_CARD_GAP1 + (bs0 - ts0) + OG_CARD_GAP2 + (bf0 - tf0)
    y_title = (H - block_h) / 2 - t0
    y_sub = y_title + (b0 - t0) + OG_CARD_GAP1 - ts0
    y_footer = y_sub + (bs0 - ts0) + OG_CARD_GAP2 - tf0

    def draw_line(text, widths, tracking, y, font, color):
        x = HALF + OG_CARD_PAD
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=font, fill=color)
            x += w + tracking

    draw_line(OG_CARD_TITLE, widths_t, tr, y_title, font_title, GREEN)
    draw_line(OG_CARD_SUBTITLE, widths_s, sub_tr, y_sub, font_sub, TEXT_DARK)
    draw_line(OG_CARD_FOOTER, widths_f, f_tr, y_footer, font_f, GRAY)

    # photo credit: small chip pinned to the bottom-left of the photo
    # (mirrors .post-photo-author on the site: translucent, rounded, ~13px)
    if credit_line:
        pad_x, pad_y = 10, 5
        radius = 5
        chip_w = int(total_c + 2 * pad_x)
        chip_h = int((bc0 - tc0) + 2 * pad_y)
        cx = 10
        cy = HALF - chip_h - 10
        chip = Image.new("RGB", (chip_w, chip_h), (28, 43, 39))
        chip_mask = Image.new("L", (chip_w, chip_h), 0)
        ImageDraw.Draw(chip_mask).rounded_rectangle(
            [0, 0, chip_w - 1, chip_h - 1], radius=radius, fill=51
        )
        canvas.paste(chip, (cx, cy), chip_mask)
        y_c = cy + (chip_h - (bc0 - tc0)) / 2 - tc0
        x = cx + pad_x
        for ch, w in zip(credit_line, widths_c):
            d.text((x, y_c), ch, font=font_c, fill=(255, 255, 255))
            x += w + c_tr

    out = BytesIO()
    canvas.save(out, "JPEG", quality=92, optimize=True)
    return out.getvalue()
