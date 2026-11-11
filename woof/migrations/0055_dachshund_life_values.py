from django.db import migrations

EN = "A small dog with a big personality that wants to be part of everything you do."
RU = "Маленькая собака с большим характером, которая хочет участвовать во всём, что вы делаете."


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="dachshund").update(
        daily_life=EN,
        daily_life_en=EN,
        daily_life_ru=RU,
        alone_tolerance="medium",
        good_with_dogs="socialised",
        aggression_level="situational",
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0054_life_with_breed_fields")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
