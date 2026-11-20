import re

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django import template

from woof.utils import nobreak_range as utils_nobreak_range, sex_pair

register = template.Library()


@register.filter
def nobreak_range(value):
    """См. woof.utils.nobreak_range (общая логика с API сравнения)."""
    return utils_nobreak_range(value)


@register.filter
def day_weight(dog):
    """Weight of a breed as "♂ 25–32 kg" and "♀ 22–28 kg" on two lines."""
    text = escape(
        "\n".join(sex_pair(dog.weight_male, dog.weight_female, "kg").split(", "))
    )
    for sign, cls in (("♂", "m"), ("♀", "f")):
        text = text.replace(
            sign, f'<span class="sex-mark sex-mark--{cls}">{sign}</span>'
        )
    return mark_safe(text)


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


def _rich(value, labels):
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
        if labels:
            head, sep, rest = text.partition(":")
            if (
                sep
                and 0 < len(head) <= 40
                and not any(c in head for c in ".!?")
                and "**" not in head
            ):
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


@register.filter
def rich_lines(value):
    """Plain text with light formatting, one paragraph per line.

    A line starting with "- " or "• " becomes a bullet; "Label: text" gets a
    bold label (a short phrase before the first colon); **word** is bold.
    Everything else is escaped, so the field cannot inject markup.
    """
    return _rich(value, labels=True)
