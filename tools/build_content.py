"""Собирает woof/content/{breeds,vocabulary}.py из текущего состояния базы.

База — источник истины: всё, что редактор поправил в админке, попадает в модуль
как есть. Для 25 пород, добавленных через админку, дополнительно переносятся
traits/scalars из старого woof/supplement_breed_data.py (там же остаётся
поведение «size — авторитетно»).
"""

import io
import os
import sys
from pathlib import Path

import django

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# the previous content module: its traits/scalars are hand-written (they are not
# derivable from the database in a lossless way), so they are carried over as-is
try:
    from woof.content.breeds import BREEDS as PREVIOUS  # noqa: E402
except ImportError:  # first run
    PREVIOUS = {}
from woof.models import (  # noqa: E402
    Category,
    CoatLength,
    CoatType,
    Country,
    Dogs,
    Temperament,
)

FIELDS = (
    "title",
    "varieties",
    "life_expectancy",
    "colors",
    "summary",
    "history",
    "care",
    "living_conditions",
    "photo_author",
)
LANGS = {"en": "", "ru": "_ru", "uk": "_uk", "de": "_de", "it": "_it", "es": "_es", "sr_latn": "_sr_latn"}


def build_breeds():
    breeds = {}
    dogs = Dogs.objects.prefetch_related(
        "coat_type", "coat_length", "temperament"
    ).order_by("slug")

    for dog in dogs:
        entry = {}

        old = PREVIOUS.get(dog.slug, {})
        if old.get("traits"):
            entry["traits"] = dict(old["traits"])
        if old.get("scalars"):
            entry["scalars"] = dict(old["scalars"])

        m2m = {
            "coat_type": [o.name_en or o.name for o in dog.coat_type.all()],
            "coat_length": [o.name_en or o.name for o in dog.coat_length.all()],
            "temperament": [o.name_en or o.name for o in dog.temperament.all()],
        }
        entry["m2m"] = {k: v for k, v in m2m.items() if v}

        texts = {}
        for lang, suffix in LANGS.items():
            values = {}
            for field in FIELDS:
                value = getattr(dog, field + suffix, "") or ""
                value = value.strip()
                if value:
                    values[field] = value
            if values:
                texts[lang] = values
        entry["texts"] = texts

        breeds[dog.slug] = entry

    return breeds


def build_vocabulary():
    def per_language(obj, extra=()):
        out = {}
        for lang, suffix in LANGS.items():
            values = {}
            for field in ("name",) + tuple(extra):
                value = (getattr(obj, field + suffix, "") or "").strip()
                if value:
                    values[field] = value
            if values:
                out[lang] = values
        return out

    return {
        "categories": {
            c.slug: per_language(c, extra=("desc",))
            for c in Category.objects.order_by("fci_number")
        },
        "sections": {
            c.slug: {
                (s.name_en or s.name): per_language(s)
                for s in c.sections.all().order_by("name_en")
            }
            for c in Category.objects.prefetch_related("sections").order_by("fci_number")
        },
        "countries": {
            (c.name_en or c.name): per_language(c) for c in Country.objects.order_by("name")
        },
        "coat_types": {
            (c.name_en or c.name): per_language(c) for c in CoatType.objects.order_by("name")
        },
        "coat_lengths": {
            (c.name_en or c.name): per_language(c) for c in CoatLength.objects.order_by("name")
        },
        "temperaments": {
            (c.name_en or c.name): per_language(c)
            for c in Temperament.objects.order_by("name")
        },
    }


def _emit(value, indent, out):
    """Compact emitter: one string per line, no wrapping (pprint splits long
    strings into fragments, which triples the file size)."""
    pad = " " * indent
    if isinstance(value, dict):
        if not value:
            out.append("{}")
            return
        out.append("{\n")
        items = list(value.items())
        for index, (key, item) in enumerate(items):
            out.append(f"{pad} {key!r}: ")
            _emit(item, indent + 1, out)
            out.append(",\n" if index < len(items) - 1 else ",\n")
        out.append(pad + "}")
    elif isinstance(value, (list, tuple)):
        out.append("[" + ", ".join(repr(item) for item in value) + "]")
    else:
        out.append(repr(value))


def dump(path, docstring, variable, payload):
    out = []
    _emit(payload, 0, out)
    body = "".join(out)
    text = f'"""{docstring}"""\n\n{variable} = {body}\n'
    compile(text, path, "exec")  # синтаксис
    io.open(path, "w", encoding="utf-8").write(text)
    print(f"{path}: {len(text)/1024:.0f} KB, строк {text.count(chr(10))}")


breeds = build_breeds()
vocabulary = build_vocabulary()

os.makedirs(BASE_DIR / "woof" / "content", exist_ok=True)

dump(
    str(BASE_DIR / "woof" / "content" / "breeds.py"),
    "Per-breed content, one entry per slug.\n\n"
    "  texts    -- per language: title, varieties, life_expectancy, colors, summary,\n"
    "              history, care, living_conditions, photo_author (empty values omitted)\n"
    "  m2m      -- coat_type / coat_length / temperament, by English name\n"
    "  traits   -- the five single-select traits (only for admin-added breeds)\n"
    "  scalars  -- size / life_expectancy / colors (only for admin-added breeds;\n"
    "              size is authoritative, the rest fill empty fields)\n\n"
    "Generated from the database by tools/build_content.py; applied by\n"
    "`manage.py fill_content`, which only writes empty fields.",
    "BREEDS",
    breeds,
)

dump(
    str(BASE_DIR / "woof" / "content" / "vocabulary.py"),
    "Translated names of every dictionary the site shows: FCI groups, sections,\n"
    "countries, coat types, coat lengths, temperaments.\n\n"
    "Keyed by the English name (categories by their slug), then by language;\n"
    "applied by `manage.py fill_content` (empty fields only).",
    "VOCABULARY",
    vocabulary,
)
