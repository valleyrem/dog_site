from django.db import migrations

HOVAWART = {
    "en": "Color variations: black-gold, black, blond",
    "ru": "Цветовые вариации: чёрно-золотистый, чёрный, блонд",
    "de": "Farbvarianten: Schwarzmarken, Schwarz, Blond",
    "it": "Varianti di colore: nero focato, nero, biondo",
    "es": "Variantes de color: negro y dorado, negro, rubio",
    "sr_latn": "Varijante boje: crno-zlatni, crni, plavi",
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    dog = Dogs.objects.filter(slug="hovawart").first()
    if dog:
        for lang, text in HOVAWART.items():
            setattr(dog, f"varieties_{lang}", text)
        dog.varieties = HOVAWART["en"]
        dog.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0117_rename_kangal")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
