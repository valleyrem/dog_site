"""Move Dogs.country from a per-language CharField to a Country FK.

Countries are created from the existing data (English base value per breed)
and the per-language translations are copied into the new Country rows, so
the admin can later pick a single country from a dropdown and every language
keeps working automatically.
"""

from django.db import migrations, models
import django.db.models.deletion

# Typos present in the old free-text data — normalize them once.
NAME_FIXES = {
    "Irleand": "Ireland",
    "Afganistan": "Afghanistan",
}


def build_countries(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Country = apps.get_model("woof", "Country")
    langs = ("en", "ru", "de", "it", "sr_latn")
    cache = {}
    updated = 0
    for dog in Dogs.objects.all().iterator():
        en = (dog.country or "").strip()
        if not en:
            continue
        en = NAME_FIXES.get(en, en)
        country = cache.get(en)
        if country is None:
            country, _ = Country.objects.get_or_create(name=en)
            cache[en] = country
            for lang in langs:
                val = getattr(dog, f"country_{lang}", None)
                if val:
                    setattr(country, f"name_{lang}", val)
            if not getattr(country, "name_en", None):
                country.name_en = en
            country.save()
        dog.country_ref = country
        dog.save(update_fields=["country_ref"])
        updated += 1
    print(f"Countries created/mapped: {len(cache)} (dogs linked: {updated})")


class Migration(migrations.Migration):

    dependencies = [
        ("woof", "0024_alter_consentlog_consent_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        db_index=True,
                        verbose_name="Country (English)",
                    ),
                ),
                (
                    "name_en",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Country (English)"
                    ),
                ),
                (
                    "name_ru",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Country (English)"
                    ),
                ),
                (
                    "name_de",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Country (English)"
                    ),
                ),
                (
                    "name_it",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Country (English)"
                    ),
                ),
                (
                    "name_sr_latn",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Country (English)"
                    ),
                ),
                (
                    "sort_order",
                    models.PositiveIntegerField(default=0, blank=True),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "Country of origin",
                "verbose_name_plural": "Countries of origin",
            },
        ),
        migrations.AddField(
            model_name="dogs",
            name="country_ref",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="dogs",
                to="woof.country",
                verbose_name="Country of origin",
            ),
        ),
        migrations.RunPython(build_countries, migrations.RunPython.noop),
        migrations.RemoveField(model_name="dogs", name="country_en"),
        migrations.RemoveField(model_name="dogs", name="country_ru"),
        migrations.RemoveField(model_name="dogs", name="country_de"),
        migrations.RemoveField(model_name="dogs", name="country_it"),
        migrations.RemoveField(model_name="dogs", name="country_sr_latn"),
        migrations.RemoveField(model_name="dogs", name="country"),
        migrations.RenameField(
            model_name="dogs", old_name="country_ref", new_name="country"
        ),
    ]
