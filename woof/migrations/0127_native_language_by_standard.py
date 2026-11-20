from django.db import migrations

# The language of the FCI standard ("Official language") for breeds whose name
# does not say it: Azawakh and Sloughi are written in French, Xoloitzcuintle in
# Spanish. (The Saluki standard names no language.)
BY_STANDARD = {
    "azawakh": "French",
    "sloughi": "French",
    "xoloitzcuintli": "Spanish",
}


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    Dogs = apps.get_model("woof", "Dogs")
    for slug, name in BY_STANDARD.items():
        lang = NativeLanguage.objects.filter(name=name).first()
        if lang:
            Dogs.objects.filter(slug=slug).update(native_language=lang)


class Migration(migrations.Migration):
    dependencies = [("woof", "0126_arabic_native_language")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
