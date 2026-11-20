from django.db import migrations

# the Russian names of the languages, shortened the way they are written in
# dictionaries; Afrikaans has no short form
RU = {
    "English": "англ.",
    "German": "нем.",
    "French": "франц.",
    "Italian": "итал.",
    "Spanish": "исп.",
    "Portuguese": "португ.",
    "Dutch": "нидерл.",
    "Frisian": "фриз.",
    "Hungarian": "венг.",
    "Slovak": "словац.",
    "Croatian": "хорв.",
    "Swedish": "швед.",
    "Norwegian": "норв.",
    "Russian": "рус.",
    "Russian (transliterated)": "рус., транслит.",
    "Turkish": "тур.",
    "Japanese": "яп.",
    "Chinese": "кит.",
    "Tibetan": "тибет.",
}


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    for name, short in RU.items():
        NativeLanguage.objects.filter(name=name).update(name_ru=short)


class Migration(migrations.Migration):
    dependencies = [("woof", "0121_russian_transliterated")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
