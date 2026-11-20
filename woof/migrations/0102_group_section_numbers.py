import re

from django.db import migrations

NUMBERED = re.compile(r"^(Group|Section) (\d+):")

WORDS = {
    "ru": {"Group": "Группа", "Section": "Секция"},
    "de": {"Group": "Gruppe", "Section": "Sektion"},
    "it": {"Group": "Gruppo", "Section": "Sezione"},
    "es": {"Group": "Grupo", "Section": "Sección"},
    "sr_latn": {"Group": "Grupa", "Section": "Sekcija"},
}


def number_names(apps, schema_editor):
    """Copy the official FCI numbering from the English name into the other languages."""
    for model_name in ("Category", "Section"):
        Model = apps.get_model("woof", model_name)
        for obj in Model.objects.all():
            match = NUMBERED.match(obj.name_en or "")
            if not match:
                continue
            kind, number = match.groups()
            for lang, words in WORDS.items():
                name = getattr(obj, f"name_{lang}") or ""
                if not name or NUMBERED.match(name) or name.startswith(words[kind]):
                    continue
                setattr(obj, f"name_{lang}", f"{words[kind]} {number}: {name}")
            obj.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0101_borzoi_title")]

    operations = [migrations.RunPython(number_names, migrations.RunPython.noop)]
