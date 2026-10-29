"""Static assets with a cache-busting stamp in development."""

import os

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def asset(path):
    """URL of a static file, with a version stamp while DEBUG is on.

    In production the manifest storage already puts a content hash into the
    file name, so a plain {% static %} is enough. Locally the names never
    change, and a browser happily keeps an old scripts.js or styles.css — the
    stamp makes every saved file a new URL and removes that class of
    "it doesn't work, but the code is right" confusion.
    """
    url = static(path)

    if not settings.DEBUG:
        return url

    found = finders.find(path)
    if not found:
        return url

    try:
        stamp = int(os.path.getmtime(found))
    except OSError:
        return url

    return f"{url}?v={stamp}"
