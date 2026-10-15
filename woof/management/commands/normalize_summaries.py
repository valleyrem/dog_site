"""Normalize the length of breed summaries to ~713 characters.

Every breed summary (EN + RU/DE/IT/SR translations) is brought into the
same length band (713 chars, tolerance 690-735):

* too long  -> trimmed at the nearest sentence boundary;
* too short -> padded with sentences from the breed's own FCI-group
               description (`Category.desc`, translated), so the added
               text is real, group-specific and already translated —
               nothing is invented. The starting sentence rotates by
               breed id so neighbouring breeds do not end identically.

Usage:
    python manage.py normalize_summaries
"""

import re

from django.core.management.base import BaseCommand

from woof.models import Dogs

TARGET = 713
MIN_OK = 690
MAX_OK = 735

FIELDS = ("summary", "summary_ru", "summary_de", "summary_it", "summary_sr_latn")

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _sentences(text):
    return [s.strip() for s in _SENTENCE_SPLIT.split(text.strip()) if s.strip()]


def _group_desc(dog, field):
    """Translated description of the breed's FCI group, if any."""
    cat = dog.cat
    if not cat:
        return ""
    if field == "summary":
        return cat.desc or ""
    return getattr(cat, f"desc_{field[len('summary_'):]}", None) or cat.desc or ""


def _cut_at_word(text, limit):
    return text[:limit].rsplit(" ", 1)[0].rstrip()


def _pools(dog, field, group_desc):
    """Padding sources for the same language: the FCI-group description,
    then the breed's own care and living-conditions texts."""
    pools = []
    if group_desc:
        pools.append(group_desc)
    suffix = "" if field == "summary" else field[len("summary_") :]
    for attr in ("care", "living_conditions"):
        val = getattr(dog, attr if not suffix else f"{attr}_{suffix}", None)
        if val:
            pools.append(val)
    return pools


def _pad(text, n, pools, start_hint):
    added = 0
    for pool in pools:
        if n >= TARGET:
            break
        sentences = _sentences(pool)
        if not sentences:
            continue
        first = start_hint % len(sentences)
        ordered = sentences[first:] + sentences[:first]
        for s in ordered:
            if n >= TARGET or added >= 12:
                break
            if len(s) < 40:
                continue
            if n + len(s) + 1 > MAX_OK + 10:
                continue  # too big for the band — skip, try next
            text = f"{text} {s}".rstrip()
            n = len(text)
            added += 1
    if n > MAX_OK:
        return _cut_at_word(text, MAX_OK), min(n, MAX_OK)
    return text, n


def normalize(text, group_desc, dog=None, field="", start_hint=0):
    text = (text or "").strip()
    if not text:
        return text
    n = len(text)

    if n > MAX_OK:
        parts = _sentences(text)
        if len(parts) <= 1:
            cut = _cut_at_word(text, MAX_OK)
        else:
            cut = ""
            for s in parts:
                if len(cut) + len(s) + 1 <= MAX_OK:
                    cut = f"{cut} {s}".strip()
                else:
                    break
            if not cut:
                cut = _cut_at_word(text, MAX_OK)
        if len(cut) >= MIN_OK:
            return cut
        # trimmed text fell below the band — pad it back up
        text, _ = _pad(cut, len(cut), _pools(dog, field, group_desc), start_hint)
        return text

    if n < MIN_OK:
        text, _ = _pad(text, n, _pools(dog, field, group_desc), start_hint)
        return text

    return text


class Command(BaseCommand):
    help = "Bring all breed summaries (and translations) to ~713 characters."

    def handle(self, *args, **options):
        changed = 0
        report = []
        breeds = Dogs.objects.filter(is_published=True).order_by("title")
        for dog in breeds:
            for field in FIELDS:
                old = getattr(dog, field) or ""
                new = normalize(
                    old,
                    _group_desc(dog, field),
                    dog=dog,
                    field=field,
                    start_hint=dog.id,
                )
                if new != old:
                    setattr(dog, field, new)
                    report.append(f"{dog.title}: {field} {len(old)} -> {len(new)}")
                    changed += 1
            dog.save(update_fields=list(FIELDS))
        for line in report:
            self.stdout.write(line)
        self.stdout.write(
            self.style.SUCCESS(
                f"Updated {changed} fields across {breeds.count()} breeds."
            )
        )
