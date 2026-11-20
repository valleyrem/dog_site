from django.db import migrations

FACTS = {
    "dachshund": {
        "en": [
            "A Dachshund digs into blankets, cushions and the sofa on purpose: this is the instinct of a badger-burrow hunter, and it is very typical of the breed.",
            "Its nose leads the walk: it may stop at one spot for a minute and refuse to move on, because it is reading the smells.",
            "A Dachshund called Waldi was the first official mascot of the Olympic Games, at Munich in 1972.",
        ],
        "ru": [
            "Такса зарывается в одеяла, подушки и диван не случайно: это инстинкт норной охотницы, и для породы он очень типичен.",
            "На прогулке её ведёт нос: она может минуту стоять на одном месте и не идти дальше, потому что «читает» запахи.",
            "Такса по кличке Вальди стала первым официальным талисманом Олимпийских игр, в Мюнхене в 1972 году.",
        ],
    },
    "australian-shepherd": {
        "en": [
            "Despite the name, the breed was shaped in the United States, on western ranches.",
            "Some puppies are born with a naturally short tail, and the eyes can be blue, brown, amber or even two different colours.",
            "Aussies often shadow one person, even into the bathroom, and watch every move you make.",
        ],
        "ru": [
            "Несмотря на название, порода сформировалась в США, на ранчо Запада.",
            "Часть щенков рождается с естественно коротким хвостом, а глаза бывают голубыми, карими, янтарными и даже разного цвета.",
            "Австралийские овчарки часто «приклеиваются» к одному человеку, ходят за ним даже в ванную и следят за каждым движением.",
        ],
    },
    "belgian-shepherd-dog": {
        "en": [
            "The four varieties are named after Belgian places: Malinois (Mechelen), Tervuren, Laeken (Laekenois) and Groenendael, a village near Brussels.",
            "The Malinois is prized in agility and obedience competitions for its speed, nimbleness, energy and excellent trainability.",
            "It notices every change at home and reads your mood, so it often reacts before you have given a command.",
        ],
        "ru": [
            "Четыре разновидности названы по бельгийским местам: малинуа (Мехелен), тервюрен, лакенуа (Лакен) и грюнендаль, деревня близ Брюсселя.",
            "Малинуа ценят в аджилити и соревнованиях по послушанию за скорость, ловкость, энергичность и отличную обучаемость.",
            "Она замечает любые перемены дома и чувствует ваше настроение, поэтому часто реагирует раньше, чем вы подали команду.",
        ],
    },
    "border-collie": {
        "en": [
            "It tops the best-known ranking of dog intelligence, by the psychologist Stanley Coren.",
            "A Border Collie named Chaser learned the names of more than 1,000 objects, a record confirmed in scientific tests.",
            'Its famous "eye", a fixed intent stare, is how it herds sheep, and it may use the same stare on children, cats and bikes.',
        ],
        "ru": [
            "Возглавляет самый известный рейтинг интеллекта собак психолога Стэнли Корена.",
            "Бордер-колли по кличке Чейзер выучила названия более 1000 предметов, и это подтвердили научные тесты.",
            "Его знаменитый «взгляд», неподвижный и пристальный, нужен, чтобы пасти овец, и такой же взгляд он может направить на детей, кошек и велосипеды.",
        ],
    },
    "collie-rough": {
        "en": [
            "Lassie, the most famous Collie, was always played by male dogs, because they are bigger and keep their coat through the year.",
            "Collies are talkative: they bark, chatter and howl to tell you things.",
            "A Collie is very sensitive to tone of voice, and shouting upsets it much more than it would many other breeds.",
        ],
        "ru": [
            "Лесси, самую известную колли, всегда играли кобели: они крупнее и сохраняют пышную шерсть круглый год.",
            "Колли разговорчивы: они лают, «болтают» и воют, чтобы вам что-то сообщить.",
            "Колли очень чувствительна к тону голоса, и крик расстраивает её заметно сильнее, чем собак многих других пород.",
        ],
    },
    "czechoslovakian-wolfdog": {
        "en": [
            "It began as a scientific experiment in 1955: Czechoslovak border guards crossed a German Shepherd called Cézar with a Carpathian she-wolf, Brita.",
            "It communicates more by howling and body language than by barking.",
            "It is a tireless trotter that loves cold weather and can cover long distances without getting tired.",
        ],
        "ru": [
            "Порода началась с научного эксперимента 1955 года: чехословацкие пограничники скрестили немецкую овчарку Цезаря с карпатской волчицей Бритой.",
            "Она общается скорее воем и языком тела, чем лаем.",
            "Это неутомимый рысак, который любит холод и может пройти большое расстояние, не уставая.",
        ],
    },
    "dutch-shepherd-dog": {
        "en": [
            "The only colour allowed is brindle, in shades from gold to silver, which gives the dog its tiger-stripe look.",
            "There are three coat types in one breed: short, long and rough, and the grooming is different for each.",
            "It is alert to every sound and often watches the street from a window.",
        ],
        "ru": [
            "Допускается только тигровый окрас, от золотистого до серебристого, из-за него собака похожа на тигра.",
            "В одной породе три типа шерсти: короткая, длинная и жёсткая, и уход за каждой разный.",
            "Она реагирует на каждый звук и часто наблюдает за улицей из окна.",
        ],
    },
    "german-shepherd-dog": {
        "en": [
            "It is regularly ranked in the top three of the smartest dogs, with the Border Collie and the Poodle.",
            "The first Seeing Eye guide dog in the United States, Buddy, was a German Shepherd, and so was the film star Rin Tin Tin.",
            "The ears of a puppy stand up by themselves at about four to six months, sometimes one at a time.",
        ],
        "ru": [
            "Её регулярно называют в тройке самых умных собак вместе с бордер-колли и пуделем.",
            "Первой собакой-поводырём в США была овчарка Бадди, а кинозвездой стал Рин Тин Тин, тоже немецкая овчарка.",
            "Уши щенка встают сами примерно к четырём–шести месяцам, иногда по одному.",
        ],
    },
    "old-english-sheepdog": {
        "en": [
            "For decades it was the face of Dulux paints in British advertising, which made it one of the best-known dogs in the country.",
            "It walks with a rolling, bear-like gait.",
            "The fringe over its eyes looks thick, but the dog sees perfectly well. Many owners tie it back.",
        ],
        "ru": [
            "Десятилетиями она была лицом британской рекламы красок Dulux и стала одной из самых узнаваемых собак страны.",
            "Она ходит вперевалку, как медведь.",
            "Чёлка на глазах кажется густой, но собака прекрасно видит. Многие владельцы подвязывают её.",
        ],
    },
    "pembroke-welsh-corgi": {
        "en": [
            "Queen Elizabeth II owned more than thirty Corgis during her reign, and the breed became a symbol of the British royal family.",
            "Corgis love to lie flat like a frog, with the back legs stretched out behind them.",
            "Unlike the Cardigan, the Pembroke often has a very short tail or none at all from birth.",
        ],
        "ru": [
            "Королева Елизавета II держала за время правления более тридцати корги, и порода стала символом британской королевской семьи.",
            "Корги любят лежать «лягушкой»: плашмя, вытянув задние лапы назад.",
            "В отличие от кардигана, у пемброка часто очень короткий хвост или его нет с рождения.",
        ],
    },
    "puli": {
        "en": [
            "The cords form slowly: a puppy has a soft fluffy coat, and cords start to appear at about a year old.",
            'A Puli can leap straight up on the spot, sometimes at head height. Owners call it "popping".',
            "It is an alert watchdog and announces every visitor loudly.",
        ],
        "ru": [
            "Шнуры формируются медленно: у щенка мягкая пушистая шерсть, а шнуры начинают появляться примерно к году.",
            "Пули может подпрыгнуть вверх на месте, порой до уровня головы человека. Владельцы называют это «попингом».",
            "Это бдительный сторож, который громко объявляет о каждом госте.",
        ],
    },
    "boxer": {
        "en": [
            "Boxers use their front paws in play, like little boxers, and this may be where the name comes from.",
            'When happy, a Boxer wiggles its whole body into a "kidney bean" shape and may jump with joy.',
            "It matures slowly and keeps a playful, puppy-like character well into adulthood.",
        ],
        "ru": [
            "В играх боксёры работают передними лапами, как настоящие боксёры, и, возможно, отсюда и название.",
            "Когда боксёр рад, он извивается всем телом, изгибаясь «бобом», и может подпрыгивать от радости.",
            "Он взрослеет медленно и надолго сохраняет игривый, почти щенячий характер.",
        ],
    },
    "bulldog": {
        "en": [
            "The Bulldog is a national symbol of Britain, used in cartoons and posters for its determined look.",
            "Snoring, snorting and snuffling are part of its charm and are normal for the breed.",
            "Despite the grumpy face, a Bulldog is one of the sweetest and most affectionate breeds.",
        ],
        "ru": [
            "Бульдог — национальный символ Великобритании: его изображают в карикатурах и на плакатах за решительный вид.",
            "Храп, сопение и пыхтение — часть его обаяния и для породы нормальны.",
            "Несмотря на угрюмый вид, бульдог — одна из самых добрых и ласковых пород.",
        ],
    },
    "dobermann": {
        "en": [
            'Dobermanns are often called "Velcro dogs" because they stick close to their person.',
            "A short coat with almost no undercoat means a Dobermann feels the cold, so many wear a jacket in winter.",
            "It is very sensitive and learns best from calm, fair training with plenty of praise.",
        ],
        "ru": [
            "Доберманов часто называют «собаками-липучками»: они держатся рядом со своим человеком.",
            "Короткая шерсть почти без подшёрстка означает, что доберман мёрзнет, поэтому многие зимой носят попону.",
            "Он очень чуткий и лучше всего учится на спокойных справедливых занятиях с щедрой похвалой.",
        ],
    },
    "great-dane": {
        "en": [
            "A Great Dane called Zeus held the record as the world's tallest dog, at about 112 cm at the shoulder.",
            "Many Great Danes sleep up to 16 hours a day, so a giant is often the calmest dog on the sofa.",
            "The cartoon dog Scooby-Doo is a Great Dane.",
        ],
        "ru": [
            "Дог по кличке Зевс считался самой высокой собакой в мире: около 112 см в холке.",
            "Многие доги спят до 16 часов в сутки, так что великан часто оказывается самой спокойной собакой на диване.",
            "Мультяшный пёс Скуби-Ду — немецкий дог.",
        ],
    },
    "hovawart": {
        "en": [
            'The name Hovawart means "yard keeper": the dog watches over the farm.',
            "It comes in three colours: black, black and gold, and blond.",
            "It is slow to mature and may keep a puppy's playfulness until about three years old.",
        ],
        "ru": [
            "Название «ховаварт» означает «хранитель двора»: собака следит за хозяйством.",
            "Бывает трёх окрасов: чёрный, чёрно-подпалый и блонд.",
            "Он взрослеет медленно и может сохранять щенячью игривость до трёх лет.",
        ],
    },
    "cane-corso": {
        "en": [
            "It comes in black, grey, fawn and red, often with a dark mask on the face.",
            "A Cane Corso tends to watch quietly before it reacts, and does not bark for no reason.",
            "It matures slowly and often needs two to three years to become a calm adult.",
        ],
        "ru": [
            "Бывает чёрного, серого, рыжего и красного окраса, часто с тёмной маской на морде.",
            "Кане-корсо обычно сначала спокойно наблюдает, а потом реагирует, и зря не лает.",
            "Он взрослеет медленно, и до спокойного взрослого ему часто нужно два–три года.",
        ],
    },
    "miniature-pinscher": {
        "en": [
            'Its nickname is the "King of Toys", for its confident, proud attitude.',
            "It has a high-stepping gait, like a little trotting horse.",
            "Many Min Pins like to climb on furniture, and some find their way onto the highest shelf.",
        ],
        "ru": [
            "Его называют «королём игрушечных пород» за уверенный гордый вид.",
            "У него высокая «лошадиная» походка с поднятыми лапами, как у маленького рысака.",
            "Многие цвергпинчеры любят забираться на мебель, а некоторые находят путь на самую высокую полку.",
        ],
    },
    "rottweiler": {
        "en": [
            "Many Rottweilers lean against your legs, and may try to sit on your lap despite their size.",
            'Rottweilers "talk": a low, rumbling sound that owners compare to purring.',
            "A Rottweiler grows up slowly and can stay playful like a puppy until two or three years old.",
        ],
        "ru": [
            "Многие ротвейлеры прислоняются к ногам и пытаются сесть на колени, несмотря на размер.",
            "Ротвейлеры «разговаривают»: издают низкий рокочущий звук, который владельцы сравнивают с мурлыканьем.",
            "Ротвейлер взрослеет медленно и может оставаться игривым, как щенок, до двух–трёх лет.",
        ],
    },
    "saint-bernard": {
        "en": [
            "The most famous Saint Bernard, Barry, lived at the Alpine hospice in the early 1800s and is said to have helped to save dozens of travellers.",
            "The little brandy barrel under its chin is a myth, popularised by a painting from 1820.",
            "It loves cold weather and snow, and finds warm weather much harder.",
        ],
        "ru": [
            "Самый известный сенбернар, Барри, жил в альпийском приюте в начале 1800-х годов и, как говорят, помог спасти десятки путников.",
            "Бочонок с бренди на шее — выдумка, которую распространила картина 1820 года.",
            "Он обожает холод и снег, а в тепле ему намного тяжелее.",
        ],
    },
    "shar-pei": {
        "en": [
            'The name Shar Pei means "sand skin", for its rough, bristly coat.',
            "The tongue is blue-black, a distinctive feature that few other breeds share.",
            "A puppy is the most wrinkled, and the folds are deepest on the head and neck.",
        ],
        "ru": [
            "Название «шарпей» означает «песчаная кожа»: так назвали за жёсткую щетинистую шерсть.",
            "Язык у него сине-чёрный, и такая особенность есть лишь у немногих пород.",
            "Больше всего морщин у щенка, а самые глубокие складки остаются на голове и шее.",
        ],
    },
    "tibetan-mastiff": {
        "en": [
            "The thick mane around its neck gives it a lion-like look.",
            "It is traditionally a night guard: it rests by day and stays alert after dark.",
            "It sheds the thick undercoat once a year, usually in spring, and the coat comes out in large clumps.",
        ],
        "ru": [
            "Густая грива вокруг шеи придаёт ему сходство со львом.",
            "Традиционно это ночной сторож: днём он отдыхает, а после наступления темноты остаётся настороже.",
            "Раз в год, обычно весной, он сбрасывает густой подшёрсток, и шерсть выходит крупными клочьями.",
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
    dependencies = [("woof", "0068_group2_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
