import re

from django.db import migrations

from woof.migrations import _fix_g1, _fix_g2, _fix_g3, _fix_g45, _fix_g6, _fix_x1, _fix_x2

FIELDS = ("title", "colors", "varieties", "summary", "history", "care", "good_fit", "think_twice", "daily_life", "quirks")
LANGS = ("ru", "en", "de", "it", "es", "sr_latn")


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for part in (_fix_g1, _fix_g2, _fix_g3, _fix_g45, _fix_g6, _fix_x1, _fix_x2):
        for slug, lang, field, old, new in part.FIX:
            dog = Dogs.objects.filter(slug=slug).first()
            if dog is None:
                continue
            name = f"{field}_{lang}"
            value = getattr(dog, name) or ""
            if old in value:
                Dogs.objects.filter(pk=dog.pk).update(**{name: value.replace(old, new)})
    for dog in Dogs.objects.all():
        values = {}
        for lang in LANGS:
            pairs = list(_fix_x2.GENERIC) if lang == "ru" else []
            pairs += _fix_x2.GENERIC_LANG.get(lang, [])
            for field in FIELDS:
                name = f"{field}_{lang}"
                value = getattr(dog, name) or ""
                fixed = value
                for old, new in pairs:
                    fixed = fixed.replace(old, new)
                fixed = re.sub(r"[ \t]{2,}", " ", fixed)
                fixed = re.sub(r"[ \t]+\n", "\n", fixed).rstrip(" \t")
                if fixed != value:
                    values[name] = fixed
        if values:
            Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0091_hound_group_translations_from_ru")]
    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
