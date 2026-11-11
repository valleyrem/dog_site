from django.db import migrations

REPLACE = {
    "jack-russell-terrier": {
        "en": (
            "A Jack Russell can jump about a metre high from a standing start, so fences need to be high and the garden secure.",
            "A Jack Russell can jump up to about one and a half metres, so a low fence will not hold it: make the fences high and the garden secure.",
        ),
        "ru": (
            "Джек-рассел может подпрыгнуть примерно на метр с места, поэтому заборы должны быть высокими, а двор надёжно закрытым.",
            "Джек-рассел может прыгнуть примерно на полтора метра, поэтому низкий забор его не удержит: делайте заборы высокими, а двор надёжно закрытым.",
        ),
    },
    "bull-terrier": {
        "en": (
            "including Bullseye, the mascot of a large US store chain, and Spuds MacKenzie in the 1980s.",
            "including Bullseye, the Miniature Bull Terrier mascot of a large US store chain, and Spuds MacKenzie in the 1980s.",
        ),
        "ru": (
            "бультерьер Буллзай стал талисманом большой американской сети магазинов",
            "миниатюрный бультерьер Буллзай стал талисманом большой американской сети магазинов",
        ),
    },
    "yorkshire-terrier": {
        "en": (
            "and the coat gradually turns steel-blue and tan with age.",
            "and over the first one to two years the black gradually turns steel-blue while the tan turns golden.",
        ),
        "ru": (
            "а с возрастом шерсть становится стально-голубой с рыжим.",
            "а за первый–второй год чёрный цвет постепенно становится стально-голубым, а рыжий светлеет до золотистого.",
        ),
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, langs in REPLACE.items():
        dog = Dogs.objects.filter(slug=slug).first()
        if not dog:
            continue
        values = {}
        for lang, (old, new) in langs.items():
            text = getattr(dog, f"quirks_{lang}") or ""
            if old in text:
                values[f"quirks_{lang}"] = text.replace(old, new)
                if lang == "en":
                    values["quirks"] = text.replace(old, new)
        if values:
            Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0071_terrier_fun_facts")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
