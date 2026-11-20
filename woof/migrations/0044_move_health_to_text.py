from django.db import migrations

LANGS = ("en", "ru", "de", "it", "es", "sr_latn")


def copy(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for dog in Dogs.objects.all():
        conditions = list(dog.health.all())
        if not conditions:
            continue
        values = {}
        for lang in LANGS:
            suffix = "" if lang == "en" else f"_{lang}"
            lines = [getattr(c, f"name{suffix}", None) or c.name for c in conditions]
            field = f"health_weak{suffix}"
            if not getattr(dog, field, None):
                values[field] = "\n".join(lines)
        # update() instead of save(): the "Last updated" date must not move
        Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0043_dog_health_text")]

    operations = [migrations.RunPython(copy, migrations.RunPython.noop)]
