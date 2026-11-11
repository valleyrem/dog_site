from django.db import migrations

FACTS = {
    "airedale-terrier": {
        "en": [
            "The Airedale stays playful long into adulthood and matures only at two or three years old.",
            "Its wiry coat sheds very little, which makes it popular with owners who dislike dog hair around the house.",
            "Most Airedales love water and mud, so expect a wet, dirty dog after a walk near a stream and keep a towel ready.",
        ],
        "ru": [
            "Эрдельтерьер остаётся игривым и во взрослом возрасте и окончательно взрослеет только к двум–трём годам.",
            "Жёсткая шерсть почти не линяет, поэтому породу любят те, кому не нравится собачья шерсть в доме.",
            "Большинство эрделей обожают воду и грязь, так что после прогулки у ручья готовьтесь к мокрой грязной собаке и держите наготове полотенце.",
        ],
    },
    "border-terrier": {
        "en": [
            "It is often called the most easy-going terrier: friendly with visitors, adaptable and happy in a house or a flat.",
            "Its loose, thick skin protects it from bites and lets it squeeze into tight spaces.",
            "It loves to dig and can slip under a fence, so check the garden carefully.",
        ],
        "ru": [
            "Бордер-терьера часто называют самым покладистым из терьеров: он дружелюбен к гостям, легко приспосабливается и хорошо живёт и в доме, и в квартире.",
            "Свободная плотная кожа защищает его от укусов и помогает пролезать в узкие места.",
            "Он любит рыть землю и может подкопаться под забор, поэтому внимательно проверяйте сад.",
        ],
    },
    "jack-russell-terrier": {
        "en": [
            "A Jack Russell can jump about a metre high from a standing start, so fences need to be high and the garden secure.",
            "A Jack Russell named Moose played Eddie in the TV series Frasier and made the breed's clever, expressive look famous.",
            "With good care, many live to 14 to 16 years or even longer.",
        ],
        "ru": [
            "Джек-рассел может подпрыгнуть примерно на метр с места, поэтому заборы должны быть высокими, а двор надёжно закрытым.",
            "Джек-рассел по кличке Мус сыграл пса Эдди в сериале «Фрейзер» и прославил умный выразительный взгляд породы.",
            "При хорошем уходе многие живут 14–16 лет и больше.",
        ],
    },
    "welsh-terrier": {
        "en": [
            "It looks like a smaller Airedale, but the Welsh Terrier is lighter, more compact and has a more easy-going nature.",
            "The hard, wiry coat sheds very little and stays clean easily: dry mud brushes off once it has dried.",
            "It is an alert watchdog and will tell you when someone is at the door.",
        ],
        "ru": [
            "Он похож на маленького эрдельтерьера, но вельш-терьер легче, компактнее и спокойнее по характеру.",
            "Жёсткая шерсть почти не линяет и легко остаётся чистой: засохшая грязь просто счищается щёткой.",
            "Он внимательный сторож и обязательно сообщит, что кто-то пришёл.",
        ],
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, data in FACTS.items():
        values = {}
        for lang in ("en", "ru"):
            text = "\n".join(data[lang])
            values[f"quirks_{lang}"] = text
            if lang == "en":
                values["quirks"] = text
        for lang in ("de", "it", "es", "sr_latn"):
            values[f"quirks_{lang}"] = ""
        Dogs.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0070_group3_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
