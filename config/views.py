"""Project-level views."""

from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import translate_url
from django.utils import translation
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST


@require_POST
def set_language(request):
    """Switch the site language.

    Like django.views.i18n.set_language, but also handles `next` URLs that
    carry another language's prefix. With prefix_default_language=False
    Django's version validates `next` against the *currently active*
    language, so switching from /ru/groups/ back to English failed to
    translate the URL (i18n_patterns only resolve an /ru/ prefix while
    Russian is active). Activating the URL's own language first fixes
    both directions.
    """
    language = request.POST.get("language")
    next_url = request.POST.get("next") or "/"

    if not url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = "/"

    if not language or not translation.check_for_language(language):
        return HttpResponseBadRequest("Invalid language code.")

    url_language = translation.get_language_from_path(next_url)
    with translation.override(url_language or settings.LANGUAGE_CODE):
        next_url = translate_url(next_url, language)

    response = HttpResponseRedirect(next_url)
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        language,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response
