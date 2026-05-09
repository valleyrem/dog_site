from django.db.models import Count
from django.core.cache import cache
from .models import Category

menu = [
    {"title": "About us", "url_name": "about"},
    {"title": "Groups", "url_name": "groups"},
    {"title": "Explore", "url_name": "dog-explore"},
    {"title": "Contact", "url_name": "contact"},
]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get("cats")
        if not cats:
            cats = Category.objects.annotate(Count("dogs"))
            cache.set("cats", cats, 60 * 15)

        user_menu = menu.copy()

        context["menu"] = user_menu

        context["cats"] = cats
        if "cat_selected" not in context:
            context["cat_selected"] = 0

        return context
