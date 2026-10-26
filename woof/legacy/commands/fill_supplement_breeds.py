"""Fill supplementary content for breeds added through the admin.

One idempotent command for every admin-added breed whose full content lives in
``woof/supplement_breed_data.py`` (keyed by the stable breed slug, so title
renames never break it). For each breed it applies:

  * physical fields (``size`` is enforced; height/weight/life/colors fill when
    empty),
  * coat_type / coat_length / temperament selections (fill when empty),
  * the five trait values the admin leaves at their defaults,
  * translated titles, long texts, colors and varieties (fill when empty).

    python manage.py fill_supplement_breeds
    python manage.py fill_supplement_breeds --slug saluki
"""

from django.core.management.base import BaseCommand, CommandError

from woof.models import CoatLength, CoatType, Dogs, Temperament
from woof.sex_params_data import SEX_PARAMS
from woof.legacy.supplement_breed_data import BREEDS

LONG_FIELDS = ("summary", "history", "care", "living_conditions")
SHORT_FIELDS = ("colors", "varieties")
SUFFIX = {
    "ru": "_ru",
    "de": "_de",
    "it": "_it",
    "sr_latn": "_sr_latn",
    "uk": "_uk",
    "es": "_es",
}
M2M_MODELS = {"coat_type": CoatType, "coat_length": CoatLength, "temperament": Temperament}


class Command(BaseCommand):
    help = "Fill supplementary content (traits, fields, translated texts) for admin-added breeds."

    def add_arguments(self, parser):
        parser.add_argument("--slug", help="Only fill a single breed, by slug.")

    def handle(self, *args, **options):
        slug = options.get("slug")
        if slug:
            if slug not in BREEDS:
                raise CommandError(f"Unknown slug {slug!r}. Known: {', '.join(BREEDS)}")
            items = [(slug, BREEDS[slug])]
        else:
            items = BREEDS.items()

        for breed_slug, breed in items:
            try:
                dog = Dogs.objects.get(slug=breed_slug)
            except Dogs.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"{breed_slug}: not found, skipped"))
                continue
            self.stdout.write(self.style.MIGRATE_HEADING(f"--- {dog.title} ({breed_slug}) ---"))
            self._scalars(dog, breed.get("scalars", {}))
            self._m2m(dog, breed.get("m2m", {}))
            self._traits(dog, breed.get("traits", {}))
            self._sex_params(dog)
            self._texts(dog, breed["texts"])

    def _scalars(self, dog, scalars):
        updated = []
        for field, value in scalars.items():
            current = getattr(dog, field)
            # size is authoritative; the rest only fill empty fields
            if field == "size" or not current:
                if current != value:
                    setattr(dog, field, value)
                    updated.append(field)
        if updated:
            dog.save(update_fields=updated)
        self.stdout.write("scalars: " + (", ".join(updated) or "unchanged"))

    def _m2m(self, dog, m2m):
        for field, names in m2m.items():
            rel = getattr(dog, field)
            if rel.exists():
                continue
            model = M2M_MODELS[field]
            objs = []
            for name in names:
                try:
                    objs.append(model.objects.get(name=name))
                except model.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"no {model.__name__} '{name}'"))
            if objs:
                rel.set(objs)
                self.stdout.write(f"{field}: set {names}")

    def _traits(self, dog, traits):
        for field, value in traits.items():
            if getattr(dog, field) != value:
                setattr(dog, field, value)
        dog.save(update_fields=list(traits))
        self.stdout.write("traits: " + ", ".join(f"{k}={v}" for k, v in traits.items()))

    def _sex_params(self, dog):
        """Рост и вес по полу — из woof/sex_params_data.py (общий источник)."""
        data = SEX_PARAMS.get(dog.slug)
        if not data:
            return
        for field, value in zip(("height_male", "height_female", "weight_male", "weight_female"), data):
            setattr(dog, field, value)
        dog.save(update_fields=["height_male", "height_female", "weight_male", "weight_female"])
        self.stdout.write("sex params: " + ", ".join(data))

    def _cols(self, lang, field):
        if lang == "en":
            return [field, field + "_en"]
        return [field + SUFFIX[lang]]

    def _texts(self, dog, texts):
        for lang, data in texts.items():
            updated = []
            for col in self._cols(lang, "title"):
                if not getattr(dog, col):
                    setattr(dog, col, data["title"])
                    updated.append(col)
            for field in LONG_FIELDS + SHORT_FIELDS:
                for col in self._cols(lang, field):
                    if not getattr(dog, col):
                        setattr(dog, col, data[field])
                        updated.append(col)
            if updated:
                dog.save(update_fields=updated)
            self.stdout.write(f"{lang}: filled {len(updated)} field(s)")
