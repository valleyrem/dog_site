from django.db import migrations

TITLES = {
    "en": "Borzoi – Russian Hunting Sighthound",
    "ru": "Борзая – русская охотничья борзая",
    "de": "Borzoi – Russischer Jagdwindhund",
    "it": "Borzoi – Levriero da caccia russo",
    "es": "Borzoi – Galgo ruso de caza",
    "sr_latn": "Borzoj – ruski lovački hrt",
}


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="borzoi").update(
        **{f"title_{lang}": text for lang, text in TITLES.items()}
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0100_dogs_native_name")]

    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
