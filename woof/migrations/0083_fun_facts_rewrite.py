from importlib import import_module

from django.db import migrations

FIXES = ["_fun_fix_a", "_fun_fix_b"]
PARTS = [
    "_fun_1",
    "_fun_2",
    "_fun_3",
    "_fun_5",
    "_fun_6",
    "_fun_7",
    "_fun_8",
    "_fun_9",
    "_fun_11",
    "_fun_12",
]
LANGS = ("en", "ru", "de", "it", "es", "sr_latn")


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    facts = {}
    for name in PARTS:
        facts.update(import_module(f"woof.migrations.{name}").FACTS)
    for name in FIXES:
        for slug, changes in import_module(f"woof.migrations.{name}").FIX.items():
            items = list(facts[slug])
            for idx, item in changes.items():
                items[idx] = item
            facts[slug] = items
    for slug, items in facts.items():
        values = {}
        for pos, lang in enumerate(LANGS):
            values[f"quirks_{lang}"] = "\n".join(item[pos] for item in items)
        values["quirks"] = values["quirks_en"]
        Dogs.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0082_daily_life_longer")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
