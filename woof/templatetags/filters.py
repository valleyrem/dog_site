from django import template

register = template.Library()

@register.filter
def get_item_by_id(queryset, id):
    try:
        return queryset.get(pk=id)
    except queryset.model.DoesNotExist:
        return None
