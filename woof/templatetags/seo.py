"""Structured data helpers."""

from django import template
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.inclusion_tag("woof/includes/breadcrumbs_schema.html", takes_context=True)
def breadcrumbs_schema(
    context,
    current,
    section=None,
    parent_label=None,
    parent_url=None,
    sub_label=None,
    sub_url=None,
):
    """BreadcrumbList JSON-LD for the crumbs rendered by includes/breadcrumbs.html.

    Positions are counted here rather than in the template: a page can have
    Home, Guides, a group and the breed itself, and every level needs its own
    index.
    """
    request = context.get("request")
    base = f"{request.scheme}://{request.get_host()}" if request else ""
    home_url = f"{base}{reverse('home')}"

    items = [{"name": str(_("Home")), "url": home_url}]

    if section == "guides":
        items.append({"name": str(_("Dog guides")), "url": f"{base}{reverse('guides')}"})

    if parent_label:
        items.append({"name": parent_label, "url": f"{base}{parent_url}"})

    if sub_label:
        items.append({"name": sub_label, "url": f"{base}{sub_url}"})

    items.append({"name": current, "url": ""})

    return {
        "items": [
            {"position": index + 1, "name": item["name"], "url": item["url"]}
            for index, item in enumerate(items)
        ]
    }
