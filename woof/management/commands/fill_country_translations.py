"""Fill Country translation fields (RU/DE/IT/SR) for every known country.

Picks the English name from the Country model and fills the four
translations from the same dictionaries the content-fill commands use.
Only empty translations are written, so existing manual values survive.

Usage:
    python manage.py fill_country_translations
"""

from django.core.management.base import BaseCommand

from woof.models import Country
from woof.management.commands.fill_ru_content import COUNTRY
from woof.management.commands.fill_de_content import COUNTRY_DE
from woof.management.commands.fill_it_content import COUNTRY_IT
from woof.management.commands.fill_sr_content import COUNTRY_SR

MAPPINGS = (
    ("name_ru", COUNTRY),
    ("name_de", COUNTRY_DE),
    ("name_it", COUNTRY_IT),
    ("name_sr_latn", COUNTRY_SR),
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
    help = "Fill Country translations (RU/DE/IT/SR) for all known countries."

    def handle(self, *args, **options):
        all_keys = set(COUNTRY) | set(COUNTRY_DE) | set(COUNTRY_IT) | set(COUNTRY_SR)
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
