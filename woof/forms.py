import logging

from django import forms
from django.core.cache import cache
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import ContactMessage
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
        cache_key = f"contact_captcha:{token}"
        expected = cache.get(cache_key) if token else None
        value = self.cleaned_data.get("captcha")
        if expected is None or value is None or value != expected:
            raise forms.ValidationError(_("Incorrect answer. Please try again."))
        # One token, one message: otherwise a single solved captcha could be
        # replayed for the whole 10-minute lifetime of the token.
        cache.delete(cache_key)
        return value

    def save_message(self):
        """Store the message in the database; Telegram only gets a notice.

        The notice carries no text and no e-mail — the message itself lives
        only in the site database and is read in the admin.
        """
        try:
            message = ContactMessage.objects.create(
                email=self.cleaned_data.get("email", ""),
                message=self.cleaned_data["content"],
            )
        except Exception:
            logger.exception("Failed to save a contact message")
            return False
        local = timezone.localtime(message.created_at)
        send_telegram_message(
            f"New contact message #{message.pk} ({local.strftime('%H:%M, %d %b %Y')}).\n"
            "Open the admin to read it."
        )
        return True
