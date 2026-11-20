"""Branded 1200x630 share cards (photo on the left, title on a doodle panel).

Rendered with Pillow from the committed og fonts and the site doodles; used
for breeds, groups and guides. The views cache the result.
"""

from io import BytesIO
from pathlib import Path

from django.conf import settings

OG_CARD_BRAND = "woof dogs"

OG_CARD_W = 1200
OG_CARD_H = 630
OG_CARD_HALF = 600  # left half: photo; right half: title panel
OG_CARD_PAD = 60
OG_CARD_SEAM_W = 26  # soft shadow strip at the photo edge

GREEN = "#028d6a"
TEXT_DARK = "#22272f"
GRAY = (134, 137, 143)

# (file, centre x, centre y, size, rotation) on the right panel
OG_CARD_DOODLES = [
    ("heart_pink_3", 668, 66, 72, -14),
    ("dashes_yellow_2", 800, 44, 62, 20),
    ("dashes_pink_3", 1000, 46, 66, -25),
    ("heart_mint_4", 1128, 72, 60, 12),
    ("dashes_mint_4", 1162, 190, 52, -20),
    ("heart_yellow_5", 664, 560, 74, 10),
    ("dashes_pink_6", 790, 588, 60, -30),
    ("heart_mint_1", 935, 588, 56, -8),
    ("heart_pink_6", 1055, 584, 50, 15),
    ("dashes_yellow_5", 1150, 560, 66, 18),
]


def _static_path(*parts):
    return Path(settings.BASE_DIR).joinpath("static", *parts)


def _og_font(size, wght):
    from PIL import ImageFont

    font = ImageFont.truetype(
        str(_static_path("fonts", "og", "Nunito-Variable.ttf")), size
    )
    font.set_variation_by_axes([wght])
    return font


def _paste_doodle(canvas, name, cx, cy, size, rot):
    from PIL import Image

    im = Image.open(_static_path(f"doodle_{name}.webp")).convert("RGBA")
    k = size / max(im.size)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    canvas.paste(im, (round(cx - im.width / 2), round(cy - im.height / 2)), im)


def build_og_card_bytes(photo_file, title, subtitle="", credit=None):
    """Render the share card as JPEG bytes.

    Photo cover-cropped on the left; on the right the ``title`` in the site's
    green, an optional ``subtitle``, the brand line and scattered doodles.
    With ``credit`` a small "* credit" chip sits at the bottom of the photo.
    """
    from PIL import Image, ImageDraw, ImageOps

    W, H, HALF = OG_CARD_W, OG_CARD_H, OG_CARD_HALF

    img = ImageOps.exif_transpose(Image.open(photo_file))
    canvas = Image.new("RGB", (W, H), "#ffffff")
    if "A" in img.getbands():
        # a cut-out picture (group tiles): centred on a soft panel, not cropped
        panel = Image.new("RGB", (HALF, H), "#f6f1ec")
        k = min(540 / img.width, 570 / img.height)
        img = img.convert("RGBA").resize(
            (round(img.width * k), round(img.height * k)), Image.LANCZOS
        )
        panel.paste(img, ((HALF - img.width) // 2, (H - img.height) // 2), img)
        canvas.paste(panel, (0, 0))
    else:
        img = img.convert("RGB")
        scale = max(HALF / img.width, H / img.height)
        sw, sh = round(img.width * scale), round(img.height * scale)
        img = img.resize((sw, sh), Image.LANCZOS)
        left, top = (sw - HALF) // 2, (sh - H) // 2
        canvas.paste(img.crop((left, top, left + HALF, top + H)), (0, 0))

    # soft shadow at the seam
    grad = Image.new("L", (OG_CARD_SEAM_W, H), 0)
    for i in range(OG_CARD_SEAM_W):
        a = int(255 * 0.10 * (1 - i / OG_CARD_SEAM_W) ** 2)
        grad.paste(a, (i, 0, i + 1, H))
    canvas.paste(
        Image.new("RGB", (OG_CARD_SEAM_W, H), (28, 43, 39)),
        (HALF - OG_CARD_SEAM_W, 0),
        grad,
    )

    for doodle in OG_CARD_DOODLES:
        _paste_doodle(canvas, *doodle)

    d = ImageDraw.Draw(canvas)

    def measure(text, font, tr):
        return sum(d.textlength(ch, font=font) for ch in text) + tr * (len(text) - 1)

    def wrap(text, font, tr, maxw):
        lines, cur = [], ""
        for word in text.split():
            trial = f"{cur} {word}".strip()
            if cur and measure(trial, font, tr) > maxw:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        return lines + [cur]

    maxw = W - HALF - 2 * OG_CARD_PAD
    # biggest type that fits in two lines, else in three
    for max_lines in (2, 3):
        for size in range(84, 41, -2):
            font_title = _og_font(size, 600)
            tr_title = size * (7 / 96)
            lines = wrap(title, font_title, tr_title, maxw)
            if len(lines) <= max_lines and all(
                measure(x, font_title, tr_title) <= maxw for x in lines
            ):
                break
        else:
            continue
        break

    blocks = [(line, font_title, GREEN, tr_title, round(size * 0.22)) for line in lines]
    if subtitle:
        font_sub = _og_font(30, 400)
        sub_lines = wrap(subtitle, font_sub, 30 * 0.09, maxw)[:2]
        blocks[-1] = blocks[-1][:4] + (40,)
        blocks += [(x, font_sub, TEXT_DARK, 30 * 0.09, 10) for x in sub_lines]
        blocks[-1] = blocks[-1][:4] + (34,)
    else:
        blocks[-1] = blocks[-1][:4] + (34,)
    blocks.append((OG_CARD_BRAND, _og_font(20, 300), GRAY, 20 * 0.16, 0))

    def ink(text, font, tr):
        probe = Image.new("L", (W, 300), 0)
        pd = ImageDraw.Draw(probe)
        x = 0
        for ch in text:
            pd.text((x, 0), ch, font=font, fill=255)
            x += d.textlength(ch, font=font) + tr
        return probe.getbbox()

    boxes = [ink(t, f, tr) for t, f, _c, tr, _g in blocks]
    total = sum(b[3] - b[1] for b in boxes) + sum(b[4] for b in blocks)
    y = (H - total) / 2
    cx = HALF + (W - HALF) / 2
    for (text, font, color, tr, gap), bb in zip(blocks, boxes):
        x = cx - measure(text, font, tr) / 2
        for ch in text:
            d.text((x, y - bb[1]), ch, font=font, fill=color)
            x += d.textlength(ch, font=font) + tr
        y += bb[3] - bb[1] + gap

    if credit:
        font_c = _og_font(13, 300)
        line = f"* {credit}"
        bc = ink(line, font_c, 0)
        pad_x, pad_y = 10, 5
        chip_w = int(measure(line, font_c, 0) + 2 * pad_x)
        chip_h = int((bc[3] - bc[1]) + 2 * pad_y)
        cx0, cy0 = 10, H - chip_h - 10
        mask = Image.new("L", (chip_w, chip_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [0, 0, chip_w - 1, chip_h - 1], radius=5, fill=51
        )
        canvas.paste(Image.new("RGB", (chip_w, chip_h), (28, 43, 39)), (cx0, cy0), mask)
        d.text(
            (cx0 + pad_x, cy0 + pad_y - bc[1]), line, font=font_c, fill=(255, 255, 255)
        )

    out = BytesIO()
    canvas.save(out, "JPEG", quality=92, optimize=True)
    return out.getvalue()
