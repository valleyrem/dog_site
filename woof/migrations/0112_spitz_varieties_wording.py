from django.db import migrations

SLUGS = ["keeshond-wolfspitz", "pomeranian"]

TEXT = {
    "en": "This breed is a variety of the German Spitz",
    "ru": "Эта порода является разновидностью немецкого шпица",
    "de": "Diese Rasse ist eine Varietät des Deutschen Spitzes",
    "it": "Questa razza è una varietà dello Spitz Tedesco",
    "es": "Esta raza es una variedad del Spitz alemán",
    "sr_latn": "Ova rasa je varijetet nemačkog špica",
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for dog in Dogs.objects.filter(slug__in=SLUGS):
        for lang, text in TEXT.items():
            setattr(dog, f"varieties_{lang}", text)
        dog.varieties = TEXT["en"]
        dog.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0111_section_position_other_breeds")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
