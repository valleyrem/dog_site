from django.db import migrations

from woof.migrations import (
    _en_1, _en_2, _en_3, _en_5, _en_6, _en_7, _en_8, _en_9, _en_11, _en_12,
)

PARTS = (_en_1, _en_2, _en_3, _en_5, _en_6, _en_7, _en_8, _en_9, _en_11, _en_12)


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for part in PARTS:
        for slug, block in part.EN.items():
            Dogs.objects.filter(slug=slug).update(
                summary_en=block["summary"],
                care_en="\n".join(block["care"]),
                quirks_en="\n".join(block["quirks"]),
            )


class Migration(migrations.Migration):
    dependencies = [("woof", "0097_misc_group_translations_from_ru")]

    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
