"""Project-level views."""

import hashlib
import json
import logging
import re
from uuid import uuid4

from django.conf import settings
from django.core.cache import cache
from django.http import (
    HttpResponseBadRequest,
    HttpResponseRedirect,
    JsonResponse,
)
from django.urls import translate_url
from django.utils import timezone, translation
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from woof.models import ConsentLog
from woof.utils import send_telegram_message

logger = logging.getLogger(__name__)

# Human-readable labels for cookie-banner decisions reported by the banner.
CONSENT_ACTIONS = {
    "accepted_all": "Accepted all (analytics granted)",
    "declined": "Declined (necessary only)",
    "closed": "Closed the banner with the X (= declined)",
    "saved_analytics": "Saved in settings: analytics granted",
    "saved_necessary": "Saved in settings: necessary only",
}


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


@csrf_exempt
@require_POST
def consent_log(request):
    """Record a cookie-banner decision and forward it to the Telegram chat.

    The banner sends only the decision type, the analytics flag, and the
    page path — no cookies, no identifiers, no IP. A short-lived cached
    hash of the client IP throttles the endpoint so the chat cannot be
    flooded (one report per action per minute per visitor).
    """
    try:
        payload = json.loads(request.body or b"{}")
    except (ValueError, TypeError):
        return HttpResponseBadRequest("Invalid JSON.")

    action = payload.get("action")
    if action not in CONSENT_ACTIONS:
        return HttpResponseBadRequest("Unknown consent action.")

    analytics = bool(payload.get("analytics"))
    page = str(payload.get("path") or "")[:200]
    notice = int(payload.get("notice") or 0)

    # The visitor's own consent ID (Art. 7 GDPR evidence). Only the
    # character set and length are checked — it is not a session, and it is
    # not used to track the visitor across visits.
    consent_id = str(payload.get("id") or "")[:64]
    if consent_id and not re.fullmatch(r"[A-Za-z0-9-]+", consent_id):
        return HttpResponseBadRequest("Invalid consent id.")

    client_ip = ""
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    remote = request.META.get("REMOTE_ADDR", "")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    elif remote:
        client_ip = remote

    # Flood guard only: cap the number of consent events per client per
    # minute (20 is far beyond any human usage). Repeated *decisions* are
    # deduplicated by the register state below, never by this counter — so
    # flipping the choice several times in a row always lands in the log.
    rate_key = "consent_rate:" + hashlib.sha256(client_ip.encode()).hexdigest()[:16]
    count = cache.get(rate_key, 0)
    if count >= 20:
        return JsonResponse({"ok": True, "skipped": True})
    cache.set(rate_key, count + 1, 60)

    # The register keeps ONE current record per consent ID (Art. 7 GDPR).
    # A repeated, unchanged choice is not logged again (and not reported);
    # a changed choice replaces the previous entry in place.
    if not consent_id:
        consent_id = "srv-" + str(uuid4())
    record, created = ConsentLog.objects.get_or_create(
        consent_id=consent_id,
        defaults={
            "action": action,
            "analytics": analytics,
            "notice_version": notice,
            "page": page,
        },
    )

    if not created:
        choice_changed = (
            bool(record.analytics) != analytics or record.notice_version != notice
        )
        if not choice_changed:
            return JsonResponse({"ok": True, "skipped": True})
        # Replace the previous entry with the new choice.
        record.action = action
        record.analytics = analytics
        record.notice_version = notice
        record.page = page
        record.created_at = timezone.now()
        record.save(
            update_fields=[
                "action",
                "analytics",
                "notice_version",
                "page",
                "created_at",
            ]
        )

    updated = not created and True
    local = timezone.localtime()
    message = (
        "Cookie consent" + (" (updated)" if updated else "") + "\n"
        f"Action: {CONSENT_ACTIONS[action]}\n"
        f"Analytics: {'yes' if analytics else 'no'}\n"
        f"Consent ID: {consent_id}\n"
        f"Notice v: {notice}\n"
        f"Page: {page or '/'}\n"
        f"Time: {local.strftime('%H:%M, %d %b %Y')} ({settings.TIME_ZONE})"
    )
    send_telegram_message(message)

    return JsonResponse({"ok": True})
