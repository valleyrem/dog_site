import logging
from datetime import datetime

import requests
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(
        label=_("Name"),
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    email = forms.EmailField(
        label=_("E-mail"), widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    content = forms.CharField(
        label=_("Message"), widget=forms.Textarea(attrs={"cols": 60, "rows": 3})
    )

    def send_message_to_telegram(self):
        current_time = datetime.now().strftime("%H:%M, %d %b %Y")
        message = (
            f"{current_time}\n"
            f"Contact:\n"
            f"Name: {self.cleaned_data['name']}\n"
            f"Email: {self.cleaned_data['email']}\n"
            f"Message: {self.cleaned_data['content']}"
        )

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        response = requests.post(
            url, data={"chat_id": settings.TELEGRAM_CHAT_ID, "text": message}, timeout=10
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
