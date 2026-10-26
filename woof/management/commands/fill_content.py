"""Fill the site's translated content from ``woof/content/``.

One command for everything textual: the dictionaries (FCI groups, sections,
countries, coat types, coat lengths, temperaments) and every breed text in
every language. The data itself lives in two generated modules — see
``tools/build_content.py`` — so the site's content has a single source.

Idempotent by design: only empty fields are written, so re-running never
overwrites something edited by hand in the admin. The two exceptions are the
admin-added breeds that carry ``traits``/``scalars`` in their entry: their
five traits are applied as-is and ``size`` is authoritative (that is how a
freshly added breed gets finished in one step).

    python manage.py fill_content                 # everything, all languages
    python manage.py fill_content --slug saluki    # one breed
    python manage.py fill_content --lang ru        # one language
    python manage.py fill_content --dry-run        # report only, no writes
"""

from django.core.management.base import BaseCommand, CommandError

from woof.content import BREEDS, VOCABULARY
from woof.models import Category, CoatLength, CoatType, Country, Dogs, Temperament

# modeltranslation suffix per language code in woof/content/
SUFFIX = {
    "en": "",
    "ru": "_ru",
    "uk": "_uk",
    "de": "_de",
    "it": "_it",
    "es": "_es",
    "sr_latn": "_sr_latn",
}

VOCABULARY_MODELS = {
    "coat_types": (CoatType, "name"),
    "coat_lengths": (CoatLength, "name"),
    "temperaments": (Temperament, "name"),
    "countries": (Country, "name"),
}


class Command(BaseCommand):
    help = "Fill translated content (vocabulary + breed texts) from woof/content/."

    def add_arguments(self, parser):
        parser.add_argument("--slug", help="Only fill a single breed, by slug.")
        parser.add_argument(
            "--lang",
            choices=sorted(SUFFIX),
            help="Only fill a single language.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report what would change without writing anything.",
        )

    def handle(self, *args, **options):
        self.dry_run = options["dry_run"]
        self.pending = 0

        langs = [options["lang"]] if options["lang"] else list(SUFFIX)

        if options["slug"]:
            if options["slug"] not in BREEDS:
                raise CommandError(
                    f"Unknown slug {options['slug']!r}. Known: {', '.join(sorted(BREEDS))}"
                )
            slugs = [options["slug"]]
        else:
            slugs = sorted(BREEDS)

        if not options["slug"]:
            self._vocabulary(langs)
        self._breeds(slugs, langs)

        tail = " (dry run, nothing written)" if self.dry_run else ""
        style = self.style.WARNING if self.dry_run else self.style.SUCCESS
        self.stdout.write(style(f"pending changes: {self.pending}{tail}"))

    # -- helpers ---------------------------------------------------------

    def _write(self, obj, field, value):
        """Assign one field, unless it already holds the same value."""
        if getattr(obj, field) == value:
            return False
        self.pending += 1
        if not self.dry_run:
            setattr(obj, field, value)
        return True

    def _save(self, obj, fields):
        if fields and not self.dry_run:
            obj.save(update_fields=sorted(set(fields)))

    # -- vocabulary ------------------------------------------------------

    def _vocabulary(self, langs):
        self.stdout.write(self.style.MIGRATE_HEADING("--- vocabulary ---"))

        # categories (by slug, with descriptions)
        changed = 0
        for slug, translations in VOCABULARY["categories"].items():
            category = Category.objects.filter(slug=slug).first()
            if category is None:
                self.stdout.write(self.style.WARNING(f"  category {slug}: not found"))
                continue
            fields = self._apply(category, ("name", "desc"), translations, langs)
            self._save(category, fields)
            changed += bool(fields)
        self.stdout.write(f"  categories: {changed} updated")

        # sections (per category, by English name)
        changed = 0
        for cat_slug, sections in VOCABULARY["sections"].items():
            category = Category.objects.filter(slug=cat_slug).first()
            if category is None:
                continue
            for name_en, translations in sections.items():
                section = category.sections.filter(name_en=name_en).first()
                if section is None:
                    self.stdout.write(
                        self.style.WARNING(f"  section {cat_slug}/{name_en}: not found")
                    )
                    continue
                fields = self._apply(section, ("name",), translations, langs)
                self._save(section, fields)
                changed += bool(fields)
        self.stdout.write(f"  sections: {changed} updated")

        # small dictionaries keyed by English name
        for key, (model, field) in VOCABULARY_MODELS.items():
            changed = 0
            for name_en, translations in VOCABULARY[key].items():
                obj = model.objects.filter(name_en=name_en).first()
                if obj is None:
                    self.stdout.write(self.style.WARNING(f"  {key} {name_en}: not found"))
                    continue
                fields = self._apply(obj, (field,), translations, langs)
                self._save(obj, fields)
                changed += bool(fields)
            self.stdout.write(f"  {key}: {changed} updated")

    def _apply(self, obj, fields, translations, langs):
        """Write the missing translations of ``fields``; return saved fields."""
        touched = []
        for lang in langs:
            values = translations.get(lang)
            if not values:
                continue
            for field in fields:
                value = values.get(field)
                if not value:
                    continue
                if not getattr(obj, field + SUFFIX[lang], ""):
                    if self._write(obj, field + SUFFIX[lang], value):
                        touched.append(field + SUFFIX[lang])
        return touched

    # -- breeds ----------------------------------------------------------

    def _breeds(self, slugs, langs):
        self.stdout.write(self.style.MIGRATE_HEADING("--- breeds ---"))

        for slug in slugs:
            entry = BREEDS[slug]
            dog = Dogs.objects.filter(slug=slug).first()
            if dog is None:
                self.stdout.write(self.style.WARNING(f"  {slug}: not found, skipped"))
                continue

            fields = []
            for lang in langs:
                translations = entry.get("texts", {}).get(lang)
                if not translations:
                    continue
                for field, value in translations.items():
                    if not getattr(dog, field + SUFFIX[lang], ""):
                        if self._write(dog, field + SUFFIX[lang], value):
                            fields.append(field + SUFFIX[lang])

            for field, value in entry.get("scalars", {}).items():
                current = getattr(dog, field)
                if field == "size" or not current:
                    if self._write(dog, field, value):
                        fields.append(field)

            for field, value in entry.get("traits", {}).items():
                if self._write(dog, field, value):
                    fields.append(field)

            self._save(dog, fields)

            relations = 0
            for field, names in entry.get("m2m", {}).items():
                relation = getattr(dog, field)
                if relation.exists():
                    continue
                model = relation.model
                objects = list(model.objects.filter(name_en__in=names))
                if len(objects) != len(names):
                    self.stdout.write(
                        self.style.WARNING(
                            f"  {slug}: unknown {field} names {sorted(names)}"
                        )
                    )
                if objects:
                    self.pending += 1
                    relations += 1
                    if not self.dry_run:
                        relation.set(objects)

            if fields or relations:
                self.stdout.write(
                    f"  {slug}: {len(fields)} fields"
                    + (f", {relations} relation(s)" if relations else "")
                )
