import re

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django import template

from woof.utils import nobreak_range as utils_nobreak_range

register = template.Library()

# One soft accent colour per FCI group number (0 = outside classification).
FCI_COLORS = {
    0: "#B9B4C7",  # misty grey-lilac
    1: "#B39DFF",  # soft lilac
    2: "#7CA6F0",  # muted blue
    3: "#93C5A1",  # sage
    4: "#63B08C",  # cold green (sea/emerald)
    5: "#4E9FE6",  # clear calm azure (distinct in the blue family)
    6: "#94A8CF",  # slate blue
    7: "#86C5C1",  # soft teal
    8: "#A7C6EB",  # ice blue
    9: "#E3A6C9",  # candy pink
    10: "#C9A8E8",  # wisteria
}

# Same hues, deepened until they contrast ~3.0 on white — used for TEXT
# (labels on cards, breed tag) while FCI_COLORS stays for decorative strip.
FCI_DARK = {
    0: "#9890AC",
    1: "#9B7EFF",
    2: "#6093EC",
    3: "#58A46D",
    4: "#52A27C",
    5: "#2E7BC9",
    6: "#7B93C3",
    7: "#4DA19C",
    8: "#5C95D9",
    9: "#D373AA",
    10: "#AF7FDD",
}


@register.filter
def fci_color(value):
    """Soft accent colour for a dog's FCI group number (decorative strip)."""
    return FCI_COLORS.get(value, "#B9B4C7")


@register.filter
def fci_pale(value):
    """Same hue, mixed with white (60%) — barely-there pale background
    for group cards. Computed in Python so it works in every browser
    (no color-mix needed)."""
    hexc = FCI_COLORS.get(value, "#B9B4C7").lstrip("#")
    r, g, b = (int(hexc[i : i + 2], 16) for i in (0, 2, 4))
    w = 0.60
    r2 = round(r + (255 - r) * w)
    g2 = round(g + (255 - g) * w)
    b2 = round(b + (255 - b) * w)
    return f"#{r2:02X}{g2:02X}{b2:02X}"


@register.filter
def fci_dark(value):
    """Readable version of the same hue (contrast ~3.0 on white) for text."""
    return FCI_DARK.get(value, "#9890AC")


@register.filter
def nobreak_range(value):
    """См. woof.utils.nobreak_range (общая логика с API сравнения)."""
    return utils_nobreak_range(value)



SCALE_DOTS = 5


@register.inclusion_tag("woof/includes/scale.html")
def scale(dog, field, invert=False):
    """A row of five dots for a choice field, with its value written underneath.

    Every scale has the same number of dots, whatever its number of choices,
    so they can be compared by eye: the choice's place in the list is spread
    over the five dots. ``invert`` flips the order for fields whose first
    choice is the most (shedding: "heavy" comes first).
    """
    choices = dog._meta.get_field(field).choices
    keys = [key for key, _label in choices]
    value = getattr(dog, field)
    filled = 0
    if value in keys:
        index = keys.index(value)
        if invert:
            index = len(keys) - 1 - index
        steps = len(keys) - 1
        filled = round(index / steps * (SCALE_DOTS - 1)) + 1 if steps else SCALE_DOTS
    return {
        "filled": range(filled),
        "empty": range(SCALE_DOTS - filled),
        "label": getattr(dog, f"get_{field}_display")(),
    }


@register.filter
def rich_lines(value):
    """Plain text with light formatting, one paragraph per line.

    A line starting with "- " or "• " becomes a bullet; "Label: text" gets a
    bold label (a short phrase before the first colon); **word** is bold.
    Everything else is escaped, so the field cannot inject markup.
    """
    out = []
    in_list = False
    for raw in (value or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        bullet = line[:2] in ("- ", "• ") or line[:1] == "•"
        if bullet:
            line = line.lstrip("-• ").strip()
        text = escape(line)
        head, sep, rest = text.partition(":")
        if sep and 0 < len(head) <= 40 and not any(c in head for c in ".!?") and "**" not in head:
            text = f"<strong>{head}:</strong>{rest}"
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        if bullet:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{text}</li>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{text}</p>")
    if in_list:
        out.append("</ul>")
    return mark_safe("".join(out))
