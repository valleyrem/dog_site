from django.db import migrations

OUTSIDE_SLUG = "breeds-outside-fci-classification"


def move_outside_group_last(apps, schema_editor):
    """«Breeds outside FCI classification» is not an FCI group, so it belongs
    after groups 1–10, not before them (fci_number=0 sorted it first)."""
    Category = apps.get_model("woof", "Category")
    Category.objects.filter(slug=OUTSIDE_SLUG).update(fci_number=11)


def move_outside_group_first(apps, schema_editor):
    Category = apps.get_model("woof", "Category")
    Category.objects.filter(slug=OUTSIDE_SLUG).update(fci_number=0)


class Migration(migrations.Migration):

    dependencies = [
        ("woof", "0033_remove_dogs_height_remove_dogs_height_de_and_more"),
    ]

    operations = [
        migrations.RunPython(move_outside_group_last, move_outside_group_first),
    ]
