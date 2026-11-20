from django.db import migrations

NAME = "Russian (transliterated)"
TITLES = ["Samoyed", "Borzoi (Russian Hunting Sighthound)", "Yakutian Laika"]


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    Dogs = apps.get_model("woof", "Dogs")
    lang, _ = NativeLanguage.objects.get_or_create(name=NAME)
    lang.name_en = NAME
    lang.name_ru = "русский, транслит."
    lang.name_de = "Russisch, transliteriert"
    lang.name_it = "russo, traslitterato"
    lang.name_es = "ruso, transliterado"
    lang.name_sr_latn = "ruski, transliterovano"
    lang.save()
    Dogs.objects.filter(title__in=TITLES).update(native_language=lang)


class Migration(migrations.Migration):
    dependencies = [("woof", "0120_fill_native_language")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
