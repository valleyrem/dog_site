"""Fill translated short content (names, traits, group descriptions).

One idempotent command for every language. The per-language dictionaries live
in ``woof/lang_data/<lang>.py`` (see that package for the data shape); this
command applies whatever a language provides and skips what it omits.

    python manage.py fill_content            # every language with data
    python manage.py fill_content --lang es  # one language

Only empty fields are written, so it is safe to re-run and will never
overwrite values you edited by hand in the admin.
"""

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation

from woof.legacy import lang_data
from woof.models import (
    Category,
    CoatLength,
    CoatType,
    Country,
    Dogs,
    Section,
    Temperament,
)

# vocabulary model -> DATA key holding {en_name: translated}
VOCAB = (
    (CoatType, "coat_types"),
    (CoatLength, "coat_lengths"),
    (Temperament, "temperaments"),
    (Country, "countries"),
)


class Command(BaseCommand):
    help = "Fill translated names, traits and group descriptions for a language."

    def add_arguments(self, parser):
        parser.add_argument(
            "--lang",
            choices=sorted(lang_data.LANGUAGES),
            help="Language suffix to fill (default: all).",
        )

    def handle(self, *args, **options):
        suffixes = [options["lang"]] if options["lang"] else list(lang_data.LANGUAGES)
        for suffix in suffixes:
            data = lang_data.load(suffix)
            if data is None:
                raise CommandError(f"No language data module for {suffix!r}")
            self._fill_language(suffix, data)

    def _fill_language(self, suffix, data):
        code = data["LANG_CODE"]
        with translation.override(code):
            self.stdout.write(self.style.MIGRATE_HEADING(f"--- {code} ({suffix}) ---"))
            self._fill_names(Category, "name", data.get("category_names", {}), suffix)
            self._fill_names(Section, "name", data.get("section_names", {}), suffix)
            for model, key in VOCAB:
                self._fill_names(model, "name", data.get(key, {}), suffix)
            self._fill_category_desc(data.get("category_desc", {}), data.get("category_names", {}), suffix)
            self._fill_dog_titles(data.get("titles", {}), suffix)
            self._fill_dog_short(data.get("varieties", {}), "varieties", suffix)
            self._fill_dog_short(data.get("colors", {}), "colors", suffix)

    def _fill_names(self, model, base_field, mapping, suffix):
        """Translate ``<base_field>_<suffix>`` on vocabulary rows keyed by EN name."""
        if not mapping:
            return
        fname = f"{base_field}_{suffix}"
        updated = 0
        for obj in model.objects.all():
            val = mapping.get(obj.name)  # obj.name is EN when still empty
            if val and not getattr(obj, fname):
                setattr(obj, fname, val)
                obj.save(update_fields=[fname])
                updated += 1
        self.stdout.write(f"{model.__name__}.{fname} filled: {updated}")

    def _fill_category_desc(self, desc_map, name_map, suffix):
        """Category.desc_<suffix>, keyed by slug or by the English category name."""
        if not desc_map:
            return
        fname = f"desc_{suffix}"
        # it/sr dictionaries are keyed by the English name; map translated -> EN
        rev_names = {v: k for k, v in name_map.items()}
        updated = 0
        for cat in Category.objects.all():
            en_key = rev_names.get(cat.name) or cat.name
            val = desc_map.get(cat.slug) or desc_map.get(en_key)
            if val and not getattr(cat, fname):
                setattr(cat, fname, val)
                cat.save(update_fields=[fname])
                updated += 1
        self.stdout.write(f"Category.{fname} filled: {updated}")

    def _fill_dog_titles(self, mapping, suffix):
        if not mapping:
            return
        fname = f"title_{suffix}"
        updated = 0
        for dog in Dogs.objects.all():
            val = mapping.get(dog.title)  # dog.title is EN when still empty
            if val and not getattr(dog, fname):
                setattr(dog, fname, val)
                dog.save(update_fields=[fname])
                updated += 1
        self.stdout.write(f"Dogs.{fname} filled: {updated}")

    def _fill_dog_short(self, mapping, base_field, suffix):
        """Translate varieties/colors from the English value of the base field."""
        if not mapping:
            return
        fname = f"{base_field}_{suffix}"
        updated = 0
        for dog in Dogs.objects.all():
            en = getattr(dog, base_field)
            val = mapping.get(en)
            if val and not getattr(dog, fname):
                setattr(dog, fname, val)
                dog.save(update_fields=[fname])
                updated += 1
        self.stdout.write(f"Dogs.{fname} filled: {updated}")
