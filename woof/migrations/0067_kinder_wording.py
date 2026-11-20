from django.db import migrations

CHANGES = {
    "old-english-sheepdog": {
        "summary": {
            "en": (
                "Shaggy, cheerful and a little clownish.",
                "Warm, cheerful and friendly.",
            ),
            "ru": (
                "Лохматый, жизнерадостный и немного клоун.",
                "Тёплый, жизнерадостный и дружелюбный.",
            ),
        },
        "good_fit": {
            "en": (
                "Want a cheerful, goofy family dog",
                "Want a cheerful, friendly family dog",
            ),
            "ru": (
                "Хотите весёлую забавную семейную собаку",
                "Хотите весёлую дружелюбную семейную собаку",
            ),
        },
        "daily_life": {
            "en": (
                "A big, clumsy dog needs room to play.",
                "A big dog needs room to play.",
            ),
            "ru": (
                "Большой неуклюжей собаке нужно место для игр.",
                "Большой собаке нужно место для игр.",
            ),
        },
    },
    "pembroke-welsh-corgi": {
        "daily_life": {
            "en": (
                "though it can be strong-willed.",
                "though it has a mind of its own.",
            ),
            "ru": ("хотя бывает упрямой.", "хотя у неё свой характер."),
        },
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, fields in CHANGES.items():
        dog = Dogs.objects.filter(slug=slug).first()
        if not dog:
            continue
        values = {}
        for field, langs in fields.items():
            for lang, (old, new) in langs.items():
                text = getattr(dog, f"{field}_{lang}") or ""
                if old in text:
                    values[f"{field}_{lang}"] = text.replace(old, new)
                    if lang == "en":
                        values[field] = text.replace(old, new)
        if values:
            Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0066_belgian_fact_wording")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
