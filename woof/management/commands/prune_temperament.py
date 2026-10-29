"""Reduce the temperament vocabulary to the most-used traits.

The dictionary grew to 51 words while the site shows five per breed, and half
of them appeared in one or two records only — that makes the character line
read inconsistently. This command:

  1. maps every breed's traits to a shorter list (synonyms collapse into the
     word people actually search for: Smart -> Intelligent, Sociable -> Friendly),
  2. tops a breed up to five traits when a collapse left duplicates,
  3. removes the words that no longer appear anywhere.

Idempotent: running it twice changes nothing.

    python manage.py prune_temperament --dry-run
    python manage.py prune_temperament
"""

from django.core.management.base import BaseCommand
from django.db import transaction

from woof.models import Dogs, Temperament

# Kept words, in the order used to top a breed up to five traits.
KEEP = [
    "Intelligent",
    "Loyal",
    "Affectionate",
    "Alert",
    "Playful",
    "Energetic",
    "Gentle",
    "Friendly",
    "Independent",
    "Active",
    "Brave",
    "Protective",
    "Confident",
    "Calm",
    "Courageous",
    "Dignified",
    "Eager",
    "Even-tempered",
]

# Synonyms folded into a kept word (everything not listed here and not in KEEP
# falls back to "Friendly", which is the safest neutral description).
SYNONYMS = {
    "Devoted": "Loyal",
    "Loving": "Affectionate",
    "Social": "Friendly",
    "Sociable": "Friendly",
    "Outgoing": "Friendly",
    "Cheerful": "Playful",
    "Happy": "Playful",
    "Charming": "Playful",
    "Spirited": "Energetic",
    "Sensitive": "Gentle",
    "Reserved": "Calm",
    "Aloof": "Independent",
    "Quiet": "Calm",
    "Laid-back": "Calm",
    "Patient": "Gentle",
    "Stubborn": "Independent",
    "Strong-willed": "Independent",
    "Determined": "Confident",
    "Self-important": "Confident",
    "Hardworking": "Eager",
    "Trainable": "Eager",
    "Focused": "Eager",
    "Persistent": "Eager",
    "Game": "Eager",
    "Plucky": "Courageous",
    "Fearless": "Courageous",
    "Brave-hearted": "Brave",
    "Agile": "Active",
    "Fast": "Active",
    "Hardy": "Active",
    "Adaptable": "Even-tempered",
    "Good-natured": "Even-tempered",
    "Smart": "Intelligent",
    "Inquisitive": "Alert",
}


class Command(BaseCommand):
    help = "Collapse the temperament dictionary to the most-used traits."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", action="store_true", help="Report without writing."
        )

    def handle(self, *args, **options):
        dry = options["dry_run"]
        by_name = {t.name_en or t.name: t for t in Temperament.objects.all()}

        missing = [name for name in KEEP if name not in by_name]
        if missing:
            raise SystemExit(f"нет в словаре: {missing}")

        changed = 0
        for dog in Dogs.objects.prefetch_related("temperament"):
            current = [t.name_en or t.name for t in dog.temperament.all()]
            if not current:
                continue

            mapped = []
            for name in current:
                target = name if name in KEEP else SYNONYMS.get(name, "Friendly")
                if target not in mapped:
                    mapped.append(target)

            for name in KEEP:
                if len(mapped) >= 5:
                    break
                if name not in mapped:
                    mapped.append(name)

            if mapped != current:
                changed += 1
                self.stdout.write(f"  {dog.slug}: {', '.join(current)} -> {', '.join(mapped)}")
                if not dry:
                    dog.temperament.set([by_name[name] for name in mapped[:5]])

        unused = [name for name in by_name if name not in KEEP]
        if not dry:
            with transaction.atomic():
                for name in unused:
                    Temperament.objects.filter(pk=by_name[name].pk).delete()

        tail = " (dry run)" if dry else ""
        style = self.style.WARNING if dry else self.style.SUCCESS
        self.stdout.write(
            style(
                f"пород изменено: {changed}, слов удалено: {len(unused)}, "
                f"словарь: {len(KEEP)}{tail}"
            )
        )
