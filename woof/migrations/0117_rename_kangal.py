from django.db import migrations

TITLES = {
    "en": "Kangal Shepherd Dog",
    "ru": "Кангал",
    "de": "Kangal-Hirtenhund",
    "it": "Pastore Kangal",
    "es": "Pastor Kangal",
    "sr_latn": "Kangal",
}

# first words of the history text, old -> new, per language
HISTORY = {
    "en": (
        "The Anatolian Shepherd Dog is",
        "The Kangal Shepherd Dog, known outside the FCI as the Anatolian Shepherd Dog, is",
    ),
    "ru": (
        "Анатолийская овчарка — древний",
        "Кангал, известный в других странах как анатолийская овчарка, — древний",
    ),
    "de": (
        "Der Anatolische Hirtenhund ist ein alter",
        "Der Kangal, anderswo als Anatolischer Hirtenhund bekannt, ist ein alter",
    ),
    "it": (
        "Il pastore dell'Anatolia è un antico",
        "Il Kangal, noto altrove come pastore dell'Anatolia, è un antico",
    ),
    "es": (
        "El pastor de Anatolia es un antiguo",
        "El kangal, conocido en otros países como pastor de Anatolia, es un antiguo",
    ),
    "sr_latn": (
        "Anadolski ovčar je drevni",
        "Kangal, u drugim zemljama poznat kao anadolski ovčar, je drevni",
    ),
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    dog = Dogs.objects.filter(slug="anatolian-shepherd-dog").first()
    if not dog:
        return
    for lang, title in TITLES.items():
        setattr(dog, f"title_{lang}", title)
    dog.title = TITLES["en"]
    for lang, (old, new) in HISTORY.items():
        field = f"history_{lang}"
        text = getattr(dog, field) or ""
        if text.startswith(old):
            setattr(dog, field, new + text[len(old) :])
    if dog.history.startswith(HISTORY["en"][0]):
        dog.history = HISTORY["en"][1] + dog.history[len(HISTORY["en"][0]) :]
    dog.slug = "kangal-shepherd-dog"
    dog.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0116_hovawart_varieties_kangal")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
