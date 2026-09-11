import logging
from datetime import datetime

import requests
from django import forms
from django.conf import settings
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    email = forms.EmailField(
        label=_("E-mail"), widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    content = forms.CharField(
        label=_("Message"), widget=forms.Textarea(attrs={"cols": 60, "rows": 3})
    )
    # Math captcha: the answer is stored in the cache keyed by a random
    # token — no session, no cookies for anonymous visitors.
    captcha_token = forms.CharField(widget=forms.HiddenInput(), required=False)
    captcha = forms.IntegerField(
        label=_("Math captcha result"),
        widget=forms.NumberInput(
            attrs={
                "class": "form-input",
                "min": 0,
                "max": 18,
                "inputmode": "numeric",
                "autocomplete": "off",
                "aria-label": _("Math captcha result"),
            }
        ),
    )

    def clean_captcha(self):
        token = self.cleaned_data.get("captcha_token", "")
        expected = cache.get(f"contact_captcha:{token}") if token else None
        value = self.cleaned_data.get("captcha")
        if expected is None or value is None or value != expected:
            raise forms.ValidationError(_("Incorrect answer. Please try again."))
        return value

    def send_message_to_telegram(self):
        current_time = datetime.now().strftime("%H:%M, %d %b %Y")
        message = (
            f"{current_time}\n"
            f"Email: {self.cleaned_data['email']}\n"
            f"Message: {self.cleaned_data['content']}"
        )

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        response = requests.post(
            url,
            data={"chat_id": settings.TELEGRAM_CHAT_ID, "text": message},
            timeout=10,
        )
        response.raise_for_status()

    def process_form(self):
        """Send the message to Telegram. Returns True on success."""
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            logger.error(
                "Telegram credentials are not configured (TOKEN/CHAT_ID); "
                "contact message was not delivered"
            )
            return False
        try:
            self.send_message_to_telegram()
        except requests.RequestException:
            logger.exception("Failed to deliver contact message to Telegram")
            return False
        return True
