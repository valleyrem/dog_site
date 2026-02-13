from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Filters", 'url_name': 'filters'},
    {'title': "Contact", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('dogs'))

        user_menu = menu.copy()

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context