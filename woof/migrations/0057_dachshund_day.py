from django.db import migrations

EN = (
    "Morning: A Dachshund loves to sleep under the covers beside you, and wakes you quietly but firmly with a cold nose against your cheek.\n"
    "Walks: Two or three unhurried walks a day. The nose does more work than the legs, so every bush deserves a proper sniff, and birds or cats can spark a sudden chase. Keep it on a lead outdoors.\n"
    "- Protect the back: do not let it leap off the sofa or high steps, and walk it on a steady lead without sharp tugs.\n"
    "Breakfast: Dachshunds love food, so keep an eye on portion sizes.\n"
    "Daytime: While you are busy it curls up on a blanket, an armchair or a sunny spot by the window. Left alone for long, it gets bored and may voice an opinion, with barking or a chewed shoe.\n"
    "Evening: Time for games, hide-and-seek with a toy and a good chase. A small dog with firm self-belief and a very big heart.\n"
    "Kids and other animals: Loyal and playful with children who handle it gently. It usually accepts other dogs but sees small pets as prey.\n"
    "Bedtime: The best place is right beside you on the sofa while you watch a series."
)
RU = (
    "Утро: Такса любит спать под одеялом рядом с вами, а будит тихо, но настойчиво — холодным носом в щёку.\n"
    "Прогулки: Две–три неспешные прогулки в день. Нос у неё работает больше лап, поэтому каждый куст нужно обнюхать, а птицы и кошки могут вызвать внезапную погоню. На улице лучше держать её на поводке.\n"
    "- Берегите спину: не позволяйте резко прыгать с дивана и высоких ступенек, гуляйте на ровном поводке без рывков.\n"
    "Завтрак: Такса любит поесть, поэтому за размером порций стоит следить.\n"
    "День: Пока вы заняты, она устроится клубком на пледе, в кресле или на солнечном пятне у окна. Если остаётся одна надолго, скучает и может высказать своё мнение лаем или погрызенным ботинком.\n"
    "Вечер: Время игр, поисков спрятанной игрушки и догонялок. Маленькая собака с твёрдой уверенностью в себе и очень большим сердцем.\n"
    "Дети и другие животные: С детьми, которые обращаются бережно, преданная и игривая. С другими собаками обычно ладит, а мелких питомцев считает добычей.\n"
    "Перед сном: Лучшее место — рядом с вами на диване, пока вы смотрите сериал."
)


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="dachshund").update(
        daily_life=EN, daily_life_en=EN, daily_life_ru=RU
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0056_life_back_to_text")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
