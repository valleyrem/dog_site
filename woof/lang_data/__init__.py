"""Per-language short-content dictionaries for the ``fill_content`` command.

Each submodule (``ru.py``, ``de.py``, …) exports a ``DATA`` dict with a
normalised shape so one generic command can apply any language idempotently:

    LANG_CODE   -- value for ``translation.override`` (e.g. "sr-latn")
    SUFFIX      -- django-modeltranslation field suffix (e.g. "sr_latn")
    titles        {en_dog_title: translated_title}
    category_names{en_category_name: translated_name}
    category_desc {slug_or_en_name: translated_desc}
    section_names {en_section_name: translated_name}
    coat_types    {en_coat_type: translated}
    coat_lengths  {en_coat_length: translated}
    temperaments  {en_trait: translated}
    countries     {en_country: translated}
    varieties     {en_variety: translated}
    colors        {en_color: translated}

Any key may be omitted (e.g. ru has no coat/temperament dicts) — the command
simply skips what is absent.
"""

from importlib import import_module

# modeltranslation suffix -> submodule name
LANGUAGES = {
    "ru": "ru",
    "de": "de",
    "it": "it",
    "sr_latn": "sr_latn",
    "uk": "uk",
    "es": "es",
}


def load(suffix):
    """Return the DATA dict for a language suffix, or None if unknown."""
    module = LANGUAGES.get(suffix)
    if module is None:
        return None
    return import_module(f"{__name__}.{module}").DATA
