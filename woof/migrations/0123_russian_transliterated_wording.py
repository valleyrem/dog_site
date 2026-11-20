from django.db import migrations


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    NativeLanguage.objects.filter(name="Russian (transliterated)").update(
        name="Russian, transliterated", name_en="Russian, transliterated"
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0122_native_language_ru_abbreviations")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
