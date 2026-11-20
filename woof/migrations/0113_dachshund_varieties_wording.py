from django.db import migrations

SLUG = "dachshund"

TEXT = {
    "en": "Combined size (Rabbit, Miniature, Standard) and coat (Smooth-haired, Long-haired, Wire-haired) varieties: 9 in total",
    "ru": "Комбинированные разновидности по размеру (кроличья, миниатюрная, стандартная) и шерсти (гладкошёрстная, длинношёрстная, жёсткошёрстная): всего 9",
    "de": "Kombinierte Varietäten nach Größe (Kaninchen-, Zwerg-, Normalschlag) und Haar (Kurzhaar, Langhaar, Rauhaar): insgesamt 9",
    "it": "Varietà combinate per taglia (nano, miniatura, standard) e pelo (a pelo corto, a pelo lungo, a pelo duro): 9 in totale",
    "es": "Variedades combinadas por tamaño (conejero, miniatura, estándar) y pelo (de pelo corto, de pelo largo, de pelo duro): 9 en total",
    "sr_latn": "Varijeteti kombinovani prema veličini (kunićarski, patuljasti, standardni) i dlaci (kratkodlaki, dugodlaki, oštrodlaki): ukupno 9",
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for dog in Dogs.objects.filter(slug=SLUG):
        for lang, text in TEXT.items():
            setattr(dog, f"varieties_{lang}", text)
        dog.varieties = TEXT["en"]
        dog.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0112_spitz_varieties_wording")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
