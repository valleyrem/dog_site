"""Fill Spanish long texts (summary/history/care/living) for all breeds.

Source of truth: woof/es_breed_data.py. Idempotent: only fills empty
fields, so it is safe to run repeatedly. Run:
    python manage.py fill_es_breeds
"""

from django.core.management.base import BaseCommand

from woof.es_breed_data import BREED_TEXTS_ES
from woof.models import Dogs


class Command(BaseCommand):
    help = "Fill Spanish summary/history/care/living_conditions for dog breeds."

    def handle(self, *args, **options):
        filled = {k: 0 for k in ("summary", "history", "care", "living_conditions")}
        missing = []
        for dog in Dogs.objects.all():
            texts = BREED_TEXTS_ES.get(dog.title)
            if not texts:
                if dog.is_published:
                    missing.append(dog.title)
                continue
            update_fields = []
            for field, value in texts.items():
                if value and not getattr(dog, field + "_es"):
                    setattr(dog, field + "_es", value)
                    update_fields.append(field + "_es")
                    filled[field] += 1
            if update_fields:
                dog.save(update_fields=update_fields)
        for field, count in filled.items():
            self.stdout.write(f"Dogs.{field}_es filled: {count}")
        if missing:
            self.stdout.write(self.style.WARNING(f"No translations for: {missing}"))
