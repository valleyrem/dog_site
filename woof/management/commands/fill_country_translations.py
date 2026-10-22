"""Fill Country translation fields (RU/UK/DE/IT/SR/ES) for every known country.

Picks the English name from the Country model and fills the four
translations from the same dictionaries the content-fill commands use.
Only empty translations are written, so existing manual values survive.

Usage:
    python manage.py fill_country_translations
"""

from django.core.management.base import BaseCommand

from woof import lang_data
from woof.models import Country

MAPPINGS = (
    ("name_ru", lang_data.load("ru")["countries"]),
    ("name_uk", lang_data.load("uk")["countries"]),
    ("name_de", lang_data.load("de")["countries"]),
    ("name_it", lang_data.load("it")["countries"]),
    ("name_sr_latn", lang_data.load("sr_latn")["countries"]),
    ("name_es", lang_data.load("es")["countries"]),
)

# The content dictionaries were built from the old free-text values and
# still carry typo'd / split spellings; map them onto the canonical rows
# instead of creating ghost countries.
KEY_FIXES = {
    "Afganistan": "Afghanistan",
    "Irleand": "Ireland",
    "Northern Russia": "Northern Russia, Siberia",
    "Siberia": "Northern Russia, Siberia",
}


class Command(BaseCommand):
    help = "Fill Country translations (RU/UK/DE/IT/SR/ES) for all known countries."

    def handle(self, *args, **options):
        all_keys = set().union(*(mapping for _attr, mapping in MAPPINGS))
        known = sorted(KEY_FIXES.get(k, k) for k in all_keys)
        added = updated = 0

        for en in known:
            country, created = Country.objects.get_or_create(name=en)
            if created:
                added += 1
            for attr, mapping in MAPPINGS:
                # pick the dict value for this spelling (raw key first,
                # fall back to the fixed key)
                raw = next(
                    (v for k, v in mapping.items() if KEY_FIXES.get(k, k) == en),
                    None,
                )
                if raw and not getattr(country, attr):
                    setattr(country, attr, raw)
                    country.save(update_fields=[attr])
                    updated += 1
        if added:
            self.stdout.write(f"Countries added: {added}")
        self.stdout.write(f"Dictionary covers {len(known)} countries;")
        self.stdout.write("translation fields filled where they were empty.")

        missing = [c for c in Country.objects.all() if not c.name_ru]
        if missing:
            self.stdout.write(
                self.style.WARNING(
                    f"{len(missing)} countries still lack name_ru: "
                    f"{', '.join(c.name for c in missing)}"
                )
            )
