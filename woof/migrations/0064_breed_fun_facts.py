from django.db import migrations

FACTS = {
    "dachshund": {
        "en": [
            "A Dachshund called Waldi was the first official mascot of the Olympic Games, at Munich in 1972.",
            "Its bark is surprisingly deep, as if it came from a much bigger dog: a large chest gives the little hunter a big voice.",
            "In Germany, size classes are set by chest measurement, not weight or height: standard, miniature and rabbit Dachshunds.",
        ],
        "ru": [
            "Такса по кличке Вальди стала первым официальным талисманом Олимпийских игр, в Мюнхене в 1972 году.",
            "У неё на удивление низкий голос, будто лает собака покрупнее: большая грудная клетка даёт маленькому охотнику мощный бас.",
            "В Германии размер таксы определяют по обхвату груди, а не по весу или росту: стандартная, миниатюрная и кроличья.",
        ],
    },
    "australian-shepherd": {
        "en": [
            "Despite the name, the breed was shaped in the United States. The name likely comes from the Basque shepherds who arrived with their dogs via Australia.",
            "Some puppies are born with a naturally short tail, and the eyes can be blue, brown, amber or even two different colours.",
            "In the 1950s Aussies became rodeo stars: their tricks and herding shows travelled the American circuit and made the breed famous.",
        ],
        "ru": [
            "Несмотря на название, порода сформирована в США. Имя, вероятно, пошло от баскских пастухов, которые приехали со своими собаками через Австралию.",
            "Часть щенков рождается с естественно коротким хвостом, а глаза бывают голубыми, карими, янтарными и даже разного цвета.",
            "В 1950-х годах овчарки стали звёздами родео: их трюки и пастушьи шоу объезжали американские арены и прославили породу.",
        ],
    },
    "belgian-shepherd-dog": {
        "en": [
            "The four varieties are named after Belgian places: Malinois (Mechelen), Tervuren, Laeken (Laekenois) and Groenendael, a village near Brussels.",
            "In 1891 a veterinary professor, Adolphe Reul, examined 117 Belgian herding dogs and described the types that became the breed.",
            "A Belgian Malinois named Cairo took part in the 2011 raid on Osama bin Laden's compound, and the breed is widely used by police and the military.",
        ],
        "ru": [
            "Четыре разновидности названы по бельгийским местам: малинуа (Мехелен), тервюрен, лакенуа (Лакен) и грюнендаль, деревня близ Брюсселя.",
            "В 1891 году профессор ветеринарной школы Адольф Рёль осмотрел 117 бельгийских пастушьих собак и описал типы, из которых сложилась порода.",
            "Малинуа по кличке Каир участвовал в рейде 2011 года на дом Усамы бен Ладена, а порода широко используется в полиции и армии.",
        ],
    },
    "border-collie": {
        "en": [
            "It tops the best-known ranking of dog intelligence, by the psychologist Stanley Coren,.",
            "A Border Collie named Chaser learned the names of more than 1,000 objects, a record confirmed in scientific tests.",
            "Nearly every modern Border Collie traces back to one sheepdog, Old Hemp, born in Northumberland in 1893.",
        ],
        "ru": [
            "Возглавляет самый известный рейтинг интеллекта собак психолога Стэнли Корена.",
            "Бордер-колли по кличке Чейзер выучила названия более 1000 предметов, и это подтвердили научные тесты.",
            "Почти все современные бордер-колли происходят от одной пастушьей собаки, Олд Хемпа, родившегося в Нортумберленде в 1893 году.",
        ],
    },
    "collie-rough": {
        "en": [
            "Lassie, the most famous Collie, was always played by male dogs, because they are bigger and keep their coat through the year.",
            "Queen Victoria kept Collies at Balmoral, and her fondness made the breed fashionable well beyond Scotland.",
            "One theory links the name to the black-faced Scottish sheep known as colleys, which these dogs herded.",
        ],
        "ru": [
            "Лесси, самую известную колли, всегда играли кобели: они крупнее и сохраняют пышную шерсть круглый год.",
            "Королева Виктория держала колли в Балморале, и её увлечение сделало породу модной далеко за пределами Шотландии.",
            "По одной из версий, название происходит от чернолицых шотландских овец, которых называли «колли» и которых эти собаки пасли.",
        ],
    },
    "czechoslovakian-wolfdog": {
        "en": [
            "It began as a scientific experiment in 1955: Czechoslovak border guards crossed a German Shepherd called Cézar with a Carpathian she-wolf, Brita.",
            "The breed was recognised as a national breed in 1982, and the international federation (FCI) recognised it in 1999.",
            "It communicates more by howling and body language than by barking, and often keeps wolf-like habits, such as moving in a pack.",
        ],
        "ru": [
            "Порода началась с научного эксперимента 1955 года: чехословацкие пограничники скрестили немецкую овчарку Цезаря с карпатской волчицей Бритой.",
            "В 1982 году порода признана национальной в Чехословакии, а в 1999 году её признала международная федерация (FCI).",
            "Она общается скорее воем и языком тела, чем лаем, и сохраняет волчьи привычки, например держится стаей.",
        ],
    },
    "dutch-shepherd-dog": {
        "en": [
            "The only colour allowed is brindle, in shades from gold to silver, which gives the dog its tiger-stripe look.",
            "Farmers used it for everything: herding sheep, pulling milk carts and guarding the yard.",
            "After the Second World War the breed was close to disappearing, and a small number of dogs rebuilt it.",
        ],
        "ru": [
            "Допускается только тигровый окрас, от золотистого до серебристого, из-за него собака похожа на тигра.",
            "Фермеры использовали её для всего: пасти овец, возить тележки с молоком и сторожить двор.",
            "После Второй мировой войны порода была на грани исчезновения, и её восстановило небольшое число собак.",
        ],
    },
    "german-shepherd-dog": {
        "en": [
            "It is regularly ranked in the top three of the smartest dogs, with the Border Collie and the Poodle.",
            "The first Seeing Eye guide dog in the United States, Buddy, was a German Shepherd, and so was the film star Rin Tin Tin.",
            "The breed began in 1899 with a captain, Max von Stephanitz, and a dog called Horand, the first one registered.",
        ],
        "ru": [
            "Её регулярно называют в тройке самых умных собак вместе с бордер-колли и пуделем.",
            "Первой собакой-поводырём в США была овчарка Бадди, а кинозвездой стал Рин Тин Тин, тоже немецкая овчарка.",
            "Порода началась в 1899 году с капитана Макса фон Штефаница и собаки Хоранд, первой записанной в книгу.",
        ],
    },
    "old-english-sheepdog": {
        "en": [
            "For decades it was the face of Dulux paints in British advertising, which made it one of the best-known dogs in the country.",
            'A popular story says that tails were docked to show a working dog, hence the nickname "Bobtail". Today many are born with a short tail.',
            'The breed standard describes its bark as a "pot-casse": a loud, ringing sound, like a cracked pot.',
        ],
        "ru": [
            "Десятилетиями она была лицом британской рекламы красок Dulux и стала одной из самых узнаваемых собак страны.",
            "По популярной легенде, хвосты купировали, чтобы показать рабочую собаку, отсюда прозвище «Бобтейл». Сегодня многие рождаются с коротким хвостом.",
            "Стандарт породы описывает лай как «пот-кассе»: громкий звенящий звук, словно треснувший горшок.",
        ],
    },
    "pembroke-welsh-corgi": {
        "en": [
            "Queen Elizabeth II owned more than thirty Corgis during her reign, and the breed became a symbol of the British royal family.",
            "A Welsh legend says that Corgis were the steeds of fairies and warriors; the markings on their shoulders were seen as the marks of a saddle.",
            "Unlike the Cardigan, the Pembroke often has a very short tail or none at all from birth.",
        ],
        "ru": [
            "Королева Елизавета II держала за время правления более тридцати корги, и порода стала символом британской королевской семьи.",
            "По валлийской легенде, корги были скакунами фей и воинов, а отметины на плечах считали следом от седла.",
            "В отличие от кардигана, у пемброка часто очень короткий хвост или его нет с рождения.",
        ],
    },
    "puli": {
        "en": [
            "Hungarian herders say the breed came with the Magyars over a thousand years ago; the plural of Puli is Pulik.",
            "The cords form slowly: a puppy has a soft fluffy coat, and cords start to appear at about a year old.",
            'A Puli can leap straight up on the spot, sometimes at head height, a habit nicknamed "popping".',
        ],
        "ru": [
            "Венгерские пастухи говорят, что порода пришла с мадьярами более тысячи лет назад; множественное число от «пули» — «пулик».",
            "Шнуры формируются медленно: у щенка мягкая пушистая шерсть, а шнуры начинают появляться примерно к году.",
            "Пули может подпрыгнуть вверх на месте, порой до уровня головы человека. Владельцы называют это «попингом».",
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
    dependencies = [("woof", "0063_herding_breeds_longer_day")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
