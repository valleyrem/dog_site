from importlib import import_module

from django.db import migrations

PARTS = ["_add_a", "_add_b", "_add_c"]
LANGS = ("en", "ru", "de", "it", "es", "sr_latn")


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    additions = {}
    for part in PARTS:
        for slug, topics in import_module(f"woof.migrations.{part}").ADD.items():
            additions.setdefault(slug, {}).update(topics)
    for slug, topics in additions.items():
        dog = Dogs.objects.filter(slug=slug).first()
        if not dog:
            continue
        values = {}
        for pos, lang in enumerate(LANGS):
            blocks = (getattr(dog, f"daily_life_{lang}") or "").split("\n\n")
            if len(blocks) != 7:
                continue
            for idx, texts in topics.items():
                blocks[idx] = f"{blocks[idx]} {texts[pos]}"
            values[f"daily_life_{lang}"] = "\n\n".join(blocks)
            if lang == "en":
                values["daily_life"] = values["daily_life_en"]
        Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0081_fix_breeder_facts")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
