"""Cleanup after the 0025 country migration.

0025's RunPython runs inside a modeltranslation-patched model registry,
which skews historical-model reads/writes. Symptoms on both dev and prod:

1. duplicate Country rows created for the same name ("USA" twice);
2. ``name_en`` columns left with the pre-normalization English spellings
   ("Irleand", "Afganistan") while the base ``name`` is correct — and
   ``name_en`` is what the site displays for English.

This migration repairs everything with plain SQL (deterministic, no ORM
translation redirects), so it behaves identically on any database.
"""

from django.db import migrations

NAME_FIXES = {
    "Irleand": "Ireland",
    "Afganistan": "Afghanistan",
    # one breed had the Russian spelling stored in the English base field
    "США": "USA",
}

DE_FIXES = {
    "Russian Federation": "Russische Föderation",
    "The Netherlands": "Niederlande",
    "Northern Russia, Siberia": "Nordrussland, Sibirien",
}


def cleanup(apps, schema_editor):
    cur = schema_editor.connection.cursor()

    # 1) dedupe identical country names (keep the lowest id)
    cur.execute(
        "SELECT name, MIN(id) AS keep, MAX(id) AS dup "
        "FROM woof_country GROUP BY name HAVING COUNT(*) > 1"
    )
    dups = cur.fetchall()
    for _name, keep, dup in dups:
        cur.execute(
            "UPDATE woof_dogs SET country_id = %s WHERE country_id = %s", (keep, dup)
        )
        cur.execute("DELETE FROM woof_country WHERE id = %s", (dup,))

    # 2) normalize typo'd English names (name + name_en together)
    for old, new in NAME_FIXES.items():
        cur.execute(
            "UPDATE woof_dogs SET country_id = (SELECT id FROM woof_country WHERE name = %s) "
            "WHERE country_id = (SELECT id FROM woof_country WHERE name = %s)",
            (new, old),
        )
        cur.execute(
            "UPDATE woof_country SET name = %s, name_en = %s "
            "WHERE name = %s AND NOT EXISTS (SELECT 1 FROM woof_country WHERE name = %s)",
            (new, new, old, new),
        )

    # 3) always keep name_en in sync with the base name (English display)
    cur.execute(
        "UPDATE woof_country SET name_en = name WHERE name_en IS DISTINCT FROM name"
    )

    # 3.5) drop orphaned country rows (e.g. a renamed duplicate)
    cur.execute(
        "DELETE FROM woof_country WHERE id NOT IN "
        "(SELECT DISTINCT country_id FROM woof_dogs WHERE country_id IS NOT NULL)"
    )

    # 4) fix German typos carried over from the content dictionaries
    for name, de in DE_FIXES.items():
        cur.execute(
            "UPDATE woof_country SET name_de = %s WHERE name = %s AND name_de IS DISTINCT FROM %s",
            (de, name, de),
        )


class Migration(migrations.Migration):

    dependencies = [
        ("woof", "0025_country_of_origin"),
    ]

    operations = [
        migrations.RunPython(cleanup, migrations.RunPython.noop),
    ]
