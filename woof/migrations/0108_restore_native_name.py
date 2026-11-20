from django.db import migrations, models

from ._native_names import NATIVE_NAMES


def fill(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, name in NATIVE_NAMES.items():
        Dogs.objects.filter(slug=slug, native_name="").update(native_name=name)


class Migration(migrations.Migration):
    dependencies = [("woof", "0107_remove_purpose")]

    operations = [
        migrations.AddField(
            model_name="dogs",
            name="native_name",
            field=models.CharField(
                blank=True,
                help_text="Name in the country of origin (FCI original name). Not translated.",
                max_length=120,
                verbose_name="Native name",
            ),
        ),
        migrations.RunPython(fill, migrations.RunPython.noop),
    ]
