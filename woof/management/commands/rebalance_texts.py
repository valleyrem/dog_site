"""Keep the breed summary and the History & origin band from repeating each other.

The summary tells what a breed is like (look, coat, temperament, needs), the
History band tells where, when and why it was created.  Origin, creators,
dates and original working purpose therefore belong to the History band only.

The replacements live in `woof/summary_edits.py`:

    EDITS = {"en": {"afghan-hound": [("old text", "new text"), ...]}, ...}

Every pair is a plain text replacement inside one summary field: the text is
found and swapped, so the command is safe to run twice (an edit whose new
text is already present counts as applied).  A pair whose replacement is
`None` was later refined by another batch and is only kept for the record.

Usage:
    python manage.py rebalance_texts --dry-run
    python manage.py rebalance_texts
"""

from django.core.management.base import BaseCommand

from woof.models import Dogs
from woof.summary_edits import EDITS

FIELDS = {
    "en": "summary",
    "ru": "summary_ru",
    "de": "summary_de",
    "it": "summary_it",
    "sr_latn": "summary_sr_latn",
}


class Command(BaseCommand):
    help = "Remove origin/history facts from breed summaries (they live in the History band)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", action="store_true", help="Only report, change nothing."
        )

    def handle(self, *args, **options):
        dry = options["dry_run"]
        for lang, field in FIELDS.items():
            edits = EDITS.get(lang, {})
            applied = already = 0
            missing = []
            for slug, pairs in edits.items():
                dog = Dogs.objects.filter(slug=slug).first()
                if dog is None:
                    missing.append("%s (нет породы)" % slug)
                    continue
                text = getattr(dog, field) or ""
                new_text = text
                for old, new in pairs:
                    if new is None:
                        # superseded by a later batch (kept for documentation)
                        already += 1
                    elif old in new_text:
                        new_text = new_text.replace(old, new, 1)
                        applied += 1
                    elif new in new_text:
                        already += 1
                    else:
                        missing.append("%s: %s" % (slug, old[:58]))
                if new_text != text and not dry:
                    setattr(dog, field, new_text)
                    dog.save(update_fields=[field])
            print(
                "%-8s заменено: %3d | уже было: %3d | не найдено: %d"
                % (lang, applied, already, len(missing))
            )
            for m in missing:
                print("        ! %s" % m)
        if dry:
            print("\n(--dry-run: база не изменена)")
