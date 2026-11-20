from django.db import migrations

from ._purposes import BREED_PURPOSE, LANGS, PURPOSES


def fill(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, key in BREED_PURPOSE.items():
        texts = dict(zip(LANGS, PURPOSES[key]))
        Dogs.objects.filter(slug=slug).update(
            **{f"purpose_{lang}": text for lang, text in texts.items()}
        )


class Migration(migrations.Migration):
    dependencies = [("woof", "0103_dogs_purpose")]

    operations = [migrations.RunPython(fill, migrations.RunPython.noop)]
