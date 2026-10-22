"""Cache invalidation hooks.

The groups/breeds navigation caches ``Category`` rows (with per-category dog
counts) under a per-language key ``cats:<lang>`` for 15 minutes — see
``CATS_CACHE_KEY`` in ``woof.utils``. Whenever a Category or a Dog is saved,
that snapshot can go stale. The most visible symptom was after a translation
fill: the new text would not appear until the TTL lapsed or the ``cache/``
directory was wiped by hand.

Clearing every language key on save keeps the pages correct immediately.
"""

from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from woof.models import Category, Dogs
from woof.utils import CATS_CACHE_KEY


def clear_categories_cache():
    """Drop the cached Category snapshot for every configured language."""
    for lang_code, _name in settings.LANGUAGES:
        cache.delete(f"{CATS_CACHE_KEY}:{lang_code}")


@receiver(post_save, sender=Category)
def category_saved(sender, instance, **kwargs):
    clear_categories_cache()


@receiver(post_save, sender=Dogs)
def dogs_saved(sender, instance, **kwargs):
    # dog counts are embedded in the cached Category snapshot
    clear_categories_cache()
