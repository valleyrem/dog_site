from django import template

register = template.Library()


@register.filter
def lang_name_local(value):
    """Lowercase localized language name, shortening "latinica" to "lat"."""
    name = str(value).lower()
    return name.replace("latinica", "lat")