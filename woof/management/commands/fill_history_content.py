"""Fill the "History & origin" field for every breed in all five languages.

Idempotent: fills only empty values. Run:
    python manage.py fill_history_content
"""

from django.core.management.base import BaseCommand
from django.utils import translation

from woof.history_data import (
    HISTORY_DE,
    HISTORY_EN,
    HISTORY_IT,
    HISTORY_RU,
    HISTORY_SR,
)
from woof.models import Dogs


class Command(BaseCommand):
    help = "Fill Dogs.history (and its translations) for every breed."

    def handle(self, *args, **options):
        pairs = (
            ("history", HISTORY_EN, "en"),
            ("history_ru", HISTORY_RU, "ru"),
            ("history_de", HISTORY_DE, "de"),
            ("history_it", HISTORY_IT, "it"),
            ("history_sr_latn", HISTORY_SR, "sr-latn"),
        )

        for field, mapping, lang in pairs:
            if not mapping:
                continue
            with translation.override(lang):
                filled = 0
                missing = []
                for slug, text in mapping.items():
                    dog = Dogs.objects.filter(slug=slug).first()
                    if dog is None:
                        missing.append(slug)
                        continue
                    if getattr(dog, field):
                        continue
                    setattr(dog, field, text)
                    dog.save(update_fields=[field])
                    filled += 1
            self.stdout.write(
                f"Dogs.{field}: filled {filled}"
                + (f", unknown slugs: {', '.join(missing)}" if missing else "")
            )
