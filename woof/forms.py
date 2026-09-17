import logging
from datetime import datetime

from django import forms
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from .utils import send_telegram_message

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    email = forms.EmailField(
        label=_("E-mail"),
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": _("Optional"),
                "autocomplete": "email",
            }
        ),
    )
    content = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea(
            attrs={
                "cols": 60,
                "rows": 3,
                "placeholder": _("Write what you're interested in…"),
            }
        ),
    )
    # Math captcha: the answer is stored in the cache keyed by a random
    # token — no session, no cookies for anonymous visitors.
    captcha_token = forms.CharField(widget=forms.HiddenInput(), required=False)
    captcha = forms.IntegerField(
        # Not ``required=True`` on purpose: the HTML5 ``required`` attribute
        # would block the first "Send" click before the captcha is revealed.
        # The server (``clean_captcha``) still enforces a correct answer.
        required=False,
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
        lines = [current_time]
        if self.cleaned_data.get("email"):
            lines.append(f"Email: {self.cleaned_data['email']}")
        lines.append(f"Message: {self.cleaned_data['content']}")
        return send_telegram_message("\n".join(lines))

    def process_form(self):
        """Send the message to Telegram. Returns True on success."""
        return self.send_message_to_telegram()
