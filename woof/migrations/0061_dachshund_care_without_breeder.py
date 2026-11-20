from django.db import migrations

CUT = {
    "en": (
        " Book routine vet visits, and ask the breeder about the parents' health checks.",
        " Book routine vet visits.",
    ),
    "ru": (
        " Ходите на плановые осмотры к ветеринару и спросите заводчика о проверках здоровья родителей.",
        " Ходите на плановые осмотры к ветеринару.",
    ),
    "de": (
        " Planen Sie regelmäßige Tierarztbesuche ein und fragen Sie den Züchter nach den Gesundheitsuntersuchungen der Elterntiere.",
        " Planen Sie regelmäßige Tierarztbesuche ein.",
    ),
    "it": (
        " Programmate visite veterinarie regolari e chiedete all'allevatore dei controlli sanitari dei genitori.",
        " Programmate visite veterinarie regolari.",
    ),
    "es": (
        " Programe revisiones veterinarias periódicas y pregunte al criador por las pruebas de salud de los padres.",
        " Programe revisiones veterinarias periódicas.",
    ),
    "sr_latn": (
        " Planirajte redovne posete veterinaru i pitajte uzgajivača za zdravstvene preglede roditelja.",
        " Planirajte redovne posete veterinaru.",
    ),
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    dog = Dogs.objects.filter(slug="dachshund").first()
    if not dog:
        return
    values = {}
    for lang, (old, new) in CUT.items():
        fields = ["care_" + lang] + (["care"] if lang == "en" else [])
        for field in fields:
            text = getattr(dog, field) or ""
            if old in text:
                values[field] = text.replace(old, new)
    if values:
        Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0060_dachshund_translations")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
