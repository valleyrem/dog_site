"""URL configuration for the woofdogs.world project."""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from config.views import set_language
from woof.views import page_not_found

# URLs that must NOT get a language prefix.
urlpatterns = [
    path("i18n/setlang/", set_language, name="set_language"),
    path("admin/", admin.site.urls),
    path("chaining/", include("smart_selects.urls")),
    re_path(
        r"^media/(?P<path>.*)$", serve, kwargs={"document_root": settings.MEDIA_ROOT}
    ),
]

# Language-prefixed pages. English is the default language and keeps the
# prefix-less URLs (prefix_default_language=False), so all indexed URLs
# stay valid: /dogs/, /guides/, /groups/<slug>/... Russian gets /ru/.
urlpatterns += i18n_patterns(
    path("", include("woof.urls")),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

handler404 = page_not_found
