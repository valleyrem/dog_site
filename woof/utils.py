from django.core.cache import cache
from django.db.models import Count
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

        return context

    @staticmethod
    def _get_categories():
        return cache.get_or_set(
            CATS_CACHE_KEY,
            lambda: list(Category.objects.annotate(Count("dogs"))),
            CATS_CACHE_TIMEOUT,
        )
