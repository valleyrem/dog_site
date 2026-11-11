from django.db import migrations

from woof.migrations._content import TR_LABELS
from woof.migrations import _fix_g7, _tr_ptr_a, _tr_ptr_b, _tr_ptr_c

TEXT_FIELDS = ("title", "colors", "varieties", "summary", "history")


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for part in (_tr_ptr_a, _tr_ptr_b, _tr_ptr_c):
        for slug, langs in part.TR.items():
            values = {}
            for lang, block in langs.items():
                for field in TEXT_FIELDS:
                    if field in block:
                        values[f"{field}_{lang}"] = block[field]
                values[f"care_{lang}"] = "\n".join(block["care"])
                values[f"good_fit_{lang}"] = "\n".join(block["good_fit"])
                values[f"think_twice_{lang}"] = "\n".join(block["think_twice"])
                values[f"daily_life_{lang}"] = "\n\n".join(
                    f"{label}: {text}" for label, text in zip(TR_LABELS[lang], block["daily"])
                )
                values[f"quirks_{lang}"] = "\n".join(block["quirks"])
            Dogs.objects.filter(slug=slug).update(**values)
    for slug, lang, field, old, new in _fix_g7.FIX:
        dog = Dogs.objects.filter(slug=slug).first()
        value = getattr(dog, f"{field}_{lang}") if dog else ""
        if value and old in value:
            Dogs.objects.filter(pk=dog.pk).update(**{f"{field}_{lang}": value.replace(old, new)})


class Migration(migrations.Migration):
    dependencies = [("woof", "0092_translation_polish")]
    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
