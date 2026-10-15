"""Remove "filler" sentences from breed summaries.

Breed summaries were once padded with sentences taken from the FCI group
description (`Category.desc`) so that every summary had a similar length.
The same group sentences therefore repeat in many breeds of the same group:
duplicate content that says nothing about the individual breed (and often
repeats the breed's origin, which belongs to the History band).

This command removes, from every summary, any sentence that

* appears in more than one breed of the same language, or
* comes from the breed's own FCI group description.

Only whole sentences are removed, the rest of the text is untouched and at
least MIN_KEEP sentences are always kept.

Usage:
    python manage.py clean_summary_filler --dry-run
    python manage.py clean_summary_filler
"""

import re

from django.core.management.base import BaseCommand
from django.utils import translation

from woof.models import Dogs

FIELDS = ("summary", "summary_ru", "summary_de", "summary_it", "summary_sr_latn")
LANGS = {f: f.replace("summary", "en").replace("_", "-") for f in FIELDS}
LANGS["summary"] = "en"
MIN_KEEP = 2

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def sentences(text):
    return [s.strip() for s in _SENTENCE_SPLIT.split((text or "").strip()) if s.strip()]


def norm(sentence):
    """Comparable form of a sentence (case, spaces and dashes are ignored)."""
    s = sentence.lower().replace("\u2014", " ").replace("\u2013", " ")
    s = re.sub(r"[^0-9a-zà-ÿ\u0400-\u04ff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def signature(sentence, words=8):
    """First words of a sentence — catches filler that was cut mid-sentence."""
    return " ".join(norm(sentence).split()[:words])


def is_incomplete(sentence):
    """True for a sentence that was truncated by an earlier padding pass."""
    return not re.search(r"[.!?\"»”]\s*$", sentence.strip())


class Command(BaseCommand):
    help = "Delete duplicated / group-inherited filler sentences from breed summaries."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run", action="store_true", help="Only report, change nothing."
        )

    def handle(self, *args, **options):
        dry = options["dry_run"]
        for field in FIELDS:
            lang = LANGS[field]
            with translation.override(lang):
                dogs = list(Dogs.objects.select_related("cat").order_by("slug"))
                counts = {}
                for dog in dogs:
                    for s in set(sentences(getattr(dog, field))):
                        counts[norm(s)] = counts.get(norm(s), 0) + 1
                        counts[signature(s)] = counts.get(signature(s), 0) + 1
                group_text = {}
                for dog in dogs:
                    cat = dog.cat
                    desc = getattr(cat, "desc_%s" % lang, "") if cat else ""
                    group_text[dog.pk] = norm(desc)

                removed_total = 0
                short = []
                for dog in dogs:
                    text = getattr(dog, field) or ""
                    parts = sentences(text)
                    # a summary must not end in the middle of a sentence
                    trimmed = 0
                    if len(parts) > MIN_KEEP and is_incomplete(parts[-1]):
                        parts = parts[:-1]
                        trimmed = 1
                    keep, dropped = [], []
                    for idx, s in enumerate(parts):
                        rest = len(parts) - idx - 1
                        shared = (
                            counts.get(norm(s), 0) > 1
                            or counts.get(signature(s), 0) > 1
                        )
                        from_group = norm(s) and norm(s) in group_text[dog.pk]
                        if (shared or from_group) and len(keep) + rest >= MIN_KEEP:
                            dropped.append(s)
                        else:
                            keep.append(s)
                    if len(keep) < MIN_KEEP:
                        keep = parts[:MIN_KEEP]
                        dropped = parts[MIN_KEEP:]
                    if not dropped and not trimmed:
                        continue
                    new = " ".join(keep)
                    removed_total += len(dropped) + trimmed
                    if len(new) < 400:
                        short.append((dog.slug, len(new)))
                    if not dry:
                        with translation.override(lang):
                            setattr(dog, field, new)
                            dog.save(update_fields=[field])
                print(
                    "%-18s удалено предложений: %3d | суммари короче 400 симв.: %d %s"
                    % (field, removed_total, len(short), short[:5] if short else "")
                )
        if dry:
            print("\n(--dry-run: база не изменена)")
