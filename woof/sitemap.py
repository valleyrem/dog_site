"""Sitemap and robots.txt.

The sitemap lists every page in every language with xhtml alternates. It is
cached (one entry per scheme+host) and invalidated by the post_save /
post_delete receivers in ``woof.signals``.
"""

from io import StringIO

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.xmlutils import SimplerXMLGenerator
from django.views.decorators.http import require_GET

from .models import Category, Dogs
from .utils import SITEMAP_CACHE_TIMEOUT, sitemap_cache_key
from django.core.cache import cache

@require_GET
def sitemap_xml(request):
    """Serve the sitemap from the cache; it only changes when content does."""

    key = sitemap_cache_key(request)
    xml_text = cache.get(key)
    if xml_text is None:
        xml_text = _build_sitemap_xml(request)
        cache.set(key, xml_text, SITEMAP_CACHE_TIMEOUT)

    return HttpResponse(xml_text, content_type="application/xml; charset=utf-8")


def _build_sitemap_xml(request):
    """Hand-written sitemap: breeds + categories + static pages, all languages."""

    scheme = request.scheme
    host = request.get_host()

    def abs_url(path):
        return f"{scheme}://{host}{path}"

    def absolute(url):
        """Storage URLs are already absolute (S3); local ones need the host."""
        return url if url.startswith(("http://", "https://")) else abs_url(url)

    def lang_urls(path):
        """The path from reverse() has no language prefix (default language)."""
        urls = {}
        for code, _ in settings.LANGUAGES:
            if code == settings.LANGUAGE_CODE:
                urls[code] = abs_url(path)
            elif path == "/":
                urls[code] = abs_url("/" + code + "/")
            else:
                urls[code] = abs_url("/" + code + path)
        return urls

    content_updated = timezone.datetime.fromisoformat(settings.SITE_CONTENT_UPDATED)

    out = StringIO()
    xml = SimplerXMLGenerator(out, encoding="utf-8")
    xml.startDocument()
    xml.startElement(
        "urlset",
        {
            "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
            "xmlns:xhtml": "http://www.w3.org/1999/xhtml",
            "xmlns:image": "http://www.google.com/schemas/sitemap-image/1.1",
        },
    )

    def add_url(loc, lastmod=None, changefreq="weekly", priority="0.6"):
        xml.startElement("url", {})
        xml.addQuickElement("loc", loc)
        if lastmod:
            xml.addQuickElement("lastmod", lastmod.strftime("%Y-%m-%d"))
        xml.addQuickElement("changefreq", changefreq)
        xml.addQuickElement("priority", priority)
        xml.endElement("url")

    def add_bilingual(
        path, lastmod=None, changefreq="weekly", priority="0.6", images=()
    ):
        urls = lang_urls(path)
        for code, loc in urls.items():
            xml.startElement("url", {})
            xml.addQuickElement("loc", loc)
            if lastmod:
                xml.addQuickElement("lastmod", lastmod.strftime("%Y-%m-%d"))
            xml.addQuickElement("changefreq", changefreq)
            xml.addQuickElement("priority", priority)
            # image sitemap: helps photos of breeds show up in image search
            for image_url in images:
                if not image_url:
                    continue
                xml.startElement("image:image", {})
                xml.addQuickElement("image:loc", image_url)
                xml.endElement("image:image")
            # xhtml:alternate for every other language
            for other_code, other_loc in urls.items():
                xml.startElement(
                    "xhtml:link",
                    {
                        "rel": "alternate",
                        "hreflang": (
                            "sr-Latn" if other_code == "sr-latn" else other_code
                        ),
                        "href": other_loc,
                    },
                )
                xml.endElement("xhtml:link")
            xml.endElement("url")

    # static pages
    for name, priority in (
        ("home", "1.0"),
        ("dogs_list", "0.8"),
        ("breeds", "0.8"),
        ("groups", "0.8"),
        ("guides", "0.7"),
        ("about", "0.5"),
        ("contact", "0.5"),
    ):
        add_bilingual(reverse(name), lastmod=content_updated, priority=priority)

    # guide articles
    for name, priority in (
        ("guide-choosing-dog", "0.7"),
        ("guide-training", "0.7"),
        ("guide-health", "0.7"),
        ("guide-behavior", "0.7"),
        ("guide-living", "0.7"),
        ("guide-puppy", "0.7"),
        ("guide-feeding", "0.7"),
        ("guide-games", "0.7"),
    ):
        add_bilingual(reverse(name), lastmod=content_updated, priority=priority)

    # legal pages (low priority so search engines still see them)
    for name, priority in (
        ("privacy-policy", "0.3"),
        ("terms-of-use", "0.3"),
        ("cookie-policy", "0.3"),
    ):
        add_bilingual(reverse(name), lastmod=content_updated, priority=priority)

    # categories
    for cat in Category.objects.all():
        add_bilingual(
            cat.get_absolute_url(), lastmod=content_updated, priority="0.7"
        )

    # breeds, with their photos
    for dog in (
        Dogs.objects.filter(is_published=True)
        .select_related("cat")
        .prefetch_related("gallery")
    ):
        images = []
        if dog.photo:
            images.append(absolute(dog.photo_card.url))
        for gallery_photo in list(dog.gallery.all())[:2]:
            if gallery_photo.image:
                images.append(absolute(gallery_photo.image_large.url))

        add_bilingual(
            dog.get_absolute_url(),
            lastmod=dog.time_update or timezone.now(),
            priority="0.6",
            images=images,
        )

    xml.endElement("urlset")
    xml.endDocument()
    return out.getvalue()


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}{reverse('sitemap')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")
