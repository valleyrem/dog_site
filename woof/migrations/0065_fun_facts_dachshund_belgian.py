from django.db import migrations

REPLACE = {
    "dachshund": {
        "en": (
            "Its bark is surprisingly deep, as if it came from a much bigger dog: a large chest gives the little hunter a big voice.",
            "The long body, short legs and broad front paws were made for badger burrows, which is why a Dachshund still tunnels into blankets and cushions.",
        ),
        "ru": (
            "У неё на удивление низкий голос, будто лает собака покрупнее: большая грудная клетка даёт маленькому охотнику мощный бас.",
            "Длинное тело, короткие лапы и широкие передние лапы созданы для барсучьих нор, поэтому такса до сих пор зарывается в одеяла и подушки.",
        ),
    },
    "belgian-shepherd-dog": {
        "en": (
            "A Belgian Malinois named Cairo took part in the 2011 raid on Osama bin Laden's compound, and the breed is widely used by police and the military.",
            "It moves with a light, proud step and an elegant head carriage, and the Malinois is a favourite in agility and obedience for its speed and spring.",
        ),
        "ru": (
            "Малинуа по кличке Каир участвовал в рейде 2011 года на дом Усамы бен Ладена, а порода широко используется в полиции и армии.",
            "Она двигается лёгким гордым шагом с изящно посаженной головой, а малинуа любят в аджилити и послушании за скорость и пружинистость.",
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
    dependencies = [("woof", "0064_breed_fun_facts")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
