from django.db import migrations


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="samoyed").update(native_name="Samoiedskaïa Sabaka")


class Migration(migrations.Migration):
    dependencies = [("woof", "0123_russian_transliterated_wording")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
