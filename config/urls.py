"""URL configuration for the woofdogs.world project."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from woof.views import page_not_found

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chaining/", include("smart_selects.urls")),
    path("", include("woof.urls")),
    re_path(
        r"^media/(?P<path>.*)$", serve, kwargs={"document_root": settings.MEDIA_ROOT}
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

handler404 = page_not_found
