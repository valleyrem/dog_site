from django.db import migrations

NAME = "Arabic, transliterated"


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    Dogs = apps.get_model("woof", "Dogs")
    lang, _ = NativeLanguage.objects.get_or_create(name=NAME)
    lang.name_en = NAME
    lang.name_ru = "араб., транслит."
    lang.name_de = "Arabisch, transliteriert"
    lang.name_it = "arabo, traslitterato"
    lang.name_es = "árabe, transliterado"
    lang.name_sr_latn = "arapski, transliterovano"
    lang.save()
    Dogs.objects.filter(slug__in=["saluki", "sloughi"]).update(native_language=lang)


class Migration(migrations.Migration):
    dependencies = [("woof", "0125_patronage_sentences")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
