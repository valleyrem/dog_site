from django.db import migrations

REPLACE = {
    "en": (
        "It moves with a light, proud step and an elegant head carriage, and the Malinois is a favourite in agility and obedience for its speed and spring.",
        "The Malinois is prized in agility and obedience competitions for its speed, nimbleness, energy and excellent trainability.",
    ),
    "ru": (
        "Она двигается лёгким гордым шагом с изящно посаженной головой, а малинуа любят в аджилити и послушании за скорость и пружинистость.",
        "Малинуа ценят в аджилити и соревнованиях по послушанию за скорость, ловкость, энергичность и отличную обучаемость.",
    ),
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    dog = Dogs.objects.filter(slug="belgian-shepherd-dog").first()
    if not dog:
        return
    values = {}
    for lang, (old, new) in REPLACE.items():
        text = getattr(dog, f"quirks_{lang}") or ""
        if old in text:
            values[f"quirks_{lang}"] = text.replace(old, new)
            if lang == "en":
                values["quirks"] = text.replace(old, new)
    if values:
        Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0065_fun_facts_dachshund_belgian")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
