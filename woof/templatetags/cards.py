from django import template

register = template.Library()

# One soft accent colour per FCI group number (0 = outside classification).
FCI_COLORS = {
    0: "#B9B4C7",  # misty grey-lilac
    1: "#B39DFF",  # soft lilac
    2: "#7CA6F0",  # muted blue
    3: "#93C5A1",  # sage
    4: "#63B08C",  # cold green (sea/emerald)
    5: "#E2A6B4",  # rose quartz (похож на candy pink компаньонов, мягче)
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
    5: "#D2778D",
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
def fci_dark(value):
    """Readable version of the same hue (contrast ~3.0 on white) for text."""
    return FCI_DARK.get(value, "#9890AC")