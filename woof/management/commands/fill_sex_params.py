"""Заполняет рост и вес по полу (male / female) для всех пород.

Данные лежат в woof/sex_params_data.py.

    python manage.py fill_sex_params
    python manage.py fill_sex_params --slug dobermann
"""

from django.core.management.base import BaseCommand

from woof.models import Dogs
from woof.sex_params_data import SEX_PARAMS

FIELDS = ("height_male", "height_female", "weight_male", "weight_female")


class Command(BaseCommand):
    help = "Заполняет рост и вес отдельно для самцов и самок"

    def add_arguments(self, parser):
        parser.add_argument("--slug", help="обработать только одну породу")

    def handle(self, *args, **options):
        qs = Dogs.objects.all().order_by("id")
        if options.get("slug"):
            qs = qs.filter(slug=options["slug"])

        updated, skipped = 0, []
        for dog in qs:
            data = SEX_PARAMS.get(dog.slug)
            if not data:
                skipped.append(dog.slug)
                continue
            for field, value in zip(FIELDS, data):
                setattr(dog, field, value)
            dog.save(update_fields=list(FIELDS))
            updated += 1

        self.stdout.write(self.style.SUCCESS(f"обновлено пород: {updated}"))
        if skipped:
            self.stdout.write(self.style.WARNING(f"без данных: {', '.join(skipped)}"))
