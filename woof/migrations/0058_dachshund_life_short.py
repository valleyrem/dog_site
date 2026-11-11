from django.db import migrations

EN = (
    "Walks: two or three a day, about an hour in total. It sniffs more than it runs.\n"
    "Alone: a few hours is fine, longer and it gets bored, barks and chews.\n"
    "At home: suits a flat. The voice is loud and it barks at sounds outside the door.\n"
    "Training: stubborn. It learns commands but obeys when it chooses to.\n"
    "Children: gets along with kids who know how to handle a dog.\n"
    "Other animals: usually lives well with dogs. Cats and rodents count as prey."
)
RU = (
    "Прогулки: два–три раза в день, около часа в сумме. Больше нюхает, чем бегает.\n"
    "Одиночество: несколько часов переносит нормально, дольше скучает, лает и грызёт вещи.\n"
    "Дома: подходит для квартиры. Голос громкий, лает на звуки за дверью.\n"
    "Дрессировка: упрямая. Команды учит, но выполняет, когда сама захочет.\n"
    "Дети: ладит с детьми, которые умеют обращаться с собакой.\n"
    "Другие животные: с собаками обычно уживается. Кошек и грызунов считает добычей."
)


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="dachshund").update(
        daily_life=EN, daily_life_en=EN, daily_life_ru=RU
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0057_dachshund_day")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
