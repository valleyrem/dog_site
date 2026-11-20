from django.db import migrations, models

SLUG = "breeds-outside-fci-classification"

# The recognised-by-other-clubs section goes first, the unrecognised one after it.
LAST_SECTION = "Unrecognized but Documented Breeds"

# The visible first sentence says these breeds are popular, not second-rate.
INSERT = {
    "en": (
        "by the FCI, but are officially registered",
        "by the FCI, but are popular and loved by many people around the world, and are officially registered",
    ),
    "ru": (
        "не признанные FCI, но официально зарегистрированные",
        "не признанные FCI, но популярные и любимые многими людьми по всему миру, официально зарегистрированные",
    ),
    "de": (
        "aber offiziell registriert",
        "aber weltweit beliebt und bei vielen Menschen geschätzt sind und zugleich offiziell registriert",
    ),
    "it": (
        "non riconosciute dalla FCI, ma registrate ufficialmente",
        "non riconosciute dalla FCI, ma popolari e amate da molte persone in tutto il mondo, registrate ufficialmente",
    ),
    "es": (
        "pero que están oficialmente registradas",
        "pero que son populares y queridas por muchas personas de todo el mundo, y que están oficialmente registradas",
    ),
    "sr_latn": (
        "ali su zvanično registrovane",
        "ali su popularne i omiljene kod mnogih ljudi širom sveta, zvanično registrovane",
    ),
}


def forwards(apps, schema_editor):
    Category = apps.get_model("woof", "Category")
    Section = apps.get_model("woof", "Section")
    try:
        category = Category.objects.get(slug=SLUG)
    except Category.DoesNotExist:
        return
    Section.objects.filter(category=category, name_en=LAST_SECTION).update(position=1)
    for lang, (old, new) in INSERT.items():
        field = f"desc_{lang}"
        text = getattr(category, field, None)
        if text and old in text and new not in text:
            setattr(category, field, text.replace(old, new, 1))
    category.desc = category.desc_en or category.desc
    category.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0110_other_breeds_desc_clubs")]
    operations = [
        migrations.AddField(
            model_name="section",
            name="position",
            field=models.PositiveSmallIntegerField(
                default=0,
                help_text="Sections with a lower number come first; equal ones go by name.",
                verbose_name="Position",
            ),
        ),
        migrations.AlterModelOptions(
            name="section",
            options={
                "ordering": ["position", "name"],
                "verbose_name": "Section",
                "verbose_name_plural": "Sections",
            },
        ),
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
