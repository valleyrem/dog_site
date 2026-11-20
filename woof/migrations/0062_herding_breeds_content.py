from django.db import migrations

LABELS = {
    "en": [
        "Walks",
        "Being alone",
        "At home",
        "Children",
        "Other animals",
        "Play and activities",
        "Daily routine",
    ],
    "ru": [
        "Прогулки",
        "Одиночество",
        "Дома",
        "Дети",
        "Другие животные",
        "Игры и занятия",
        "Распорядок дня",
    ],
}

DOGS = {
    "australian-shepherd": {
        "prey": "moderate",
        "en": {
            "summary": "Quick, loyal and always ready for a job. The Australian Shepherd is a ranch dog that wants to be busy, and it brings that energy to everything it does with you.",
            "care": 'Brush two or three times a week, daily while the coat is shedding. Plan for around two hours of activity a day, mixing walks with training, games and a task for the head.\nTeach a calm "off switch" early, and socialise the puppy widely so that its natural reserve with strangers stays relaxed.',
            "good_fit": [
                "Are active every day and enjoy dog sports, hiking or running",
                "Like training and will keep teaching new things",
                "Have a house with a garden or lots of outdoor time",
                "Want a dog that stays close and watches what you do",
            ],
            "think_twice": [
                "Work long hours and are away most of the day",
                "Live in a small flat with little time outdoors",
                "Want a calm sofa dog",
                "Dislike a lot of shedding and brushing",
            ],
            "daily": [
                "Around two hours a day in total, with off-lead running where it is safe. A walk alone is not enough: add training, fetch or a puzzle.",
                "A few hours is possible once it is used to it, but a bored Aussie finds its own jobs, such as digging, barking or herding the furniture.",
                "Happiest with a garden and a family that is at home. In a flat it can cope if its exercise really is delivered every day.",
                "Devoted and playful with children who respect it. It may nip at heels or try to round up running kids, so teach manners early.",
                "Usually fine with dogs it grew up with. It may try to herd cats and small animals, and can be reserved with unfamiliar dogs.",
                "Agility, obedience, frisbee, herding and trick training suit it well. It loves to learn and is happiest when it has a task.",
                "Active mornings and evenings, with rest between. It follows you around the house and likes to be wherever the family is.",
            ],
            "quirks": [
                "Aussies often shadow one person, even to the bathroom, and watch your every move.",
                "Despite the name, the breed was shaped in the United States, on western ranches.",
                "Eyes can be blue, brown or two different colours, and the coat comes in several patterns.",
            ],
        },
        "ru": {
            "summary": "Быстрая, преданная и всегда готовая к делу. Австралийская овчарка — ранчо-собака, которой нужно быть при деле, и всю свою энергию она отдаёт вам.",
            "care": "Расчёсывайте два–три раза в неделю, а в период линьки каждый день. Рассчитывайте примерно на два часа активности в день: прогулки вместе с тренировкой, играми и заданиями для ума.\nРано научите её спокойно отдыхать и хорошо социализируйте щенка, чтобы сдержанность с чужими не переросла в настороженность.",
            "good_fit": [
                "Активны каждый день и любите собачьи виды спорта, походы или бег",
                "Любите заниматься и готовы учить собаку новому",
                "Живёте в доме с участком или много бываете на природе",
                "Хотите собаку, которая держится рядом и следит за тем, что вы делаете",
            ],
            "think_twice": [
                "Много работаете и большую часть дня не бываете дома",
                "Живёте в маленькой квартире и мало гуляете",
                "Хотите спокойную диванную собаку",
                "Не любите много шерсти и расчёсывания",
            ],
            "daily": [
                "Около двух часов в день в сумме, с бегом без поводка там, где это безопасно. Одной прогулки мало: добавьте тренировку, апорт или игрушку-головоломку.",
                "Несколько часов выдержит, когда привыкнет, но заскучавшая австралийская овчарка находит себе занятия сама: роет, лает, пасёт мебель.",
                "Счастлива в доме с участком и с семьёй, которая бывает дома. В квартире справится, если нагрузка действительно есть каждый день.",
                "Преданна и игрива с детьми, которые её уважают. Может хватать за пятки и пытаться собрать бегающих детей, поэтому манеры лучше воспитывать рано.",
                "Обычно ладит с собаками, с которыми выросла. Может пытаться пасти кошек и мелких животных и сдержанна с незнакомыми собаками.",
                "Ей подходят аджилити, послушание, фрисби, пастушьи тесты и обучение трюкам. Она любит учиться и счастлива, когда у неё есть задача.",
                "Активные утро и вечер, между ними отдых. Ходит за вами по дому и хочет быть там, где семья.",
            ],
            "quirks": [
                "Австралийские овчарки часто «приклеиваются» к одному человеку, ходят за ним даже в ванную и следят за каждым движением.",
                "Несмотря на название, порода сформирована в США, на ранчо Запада.",
                "Глаза бывают голубыми, карими или разного цвета, а окрасы разнообразны.",
            ],
        },
    },
    "belgian-shepherd-dog": {
        "prey": "moderate",
        "en": {
            "summary": "Intense, watchful and deeply bonded to its family. The Belgian Shepherd, in four coat varieties, is a serious working dog that gives everything to an owner who gives it a purpose.",
            "care": "Brush weekly, more often for long coats and during the heavy shed. Plan for at least two hours of exercise and training every day.\nSocialise widely from puppyhood, and keep training calm and consistent: this breed notices everything and is sensitive to harsh handling.",
            "good_fit": [
                "Have experience with working or herding breeds",
                "Can give two hours of exercise and training every day",
                "Enjoy dog sports or structured activities",
                "Want a loyal dog that sticks close to its person",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Are away from home most of the day",
                "Want a relaxed dog that greets every guest",
                "Live in a small flat without time outdoors",
            ],
            "daily": [
                "Two hours or more, including real running and training. The Malinois variety needs the most, but all four are tireless.",
                "Does not like long isolation. Left bored and alone, it can become anxious, noisy or destructive.",
                "Calm in the house only after its exercise is done. It likes a clear routine and a place close to the family.",
                "Loyal and protective with its own children, but its speed and herding habits call for supervision with small kids.",
                "Often fine with dogs and pets it grew up with. It can be intense with unfamiliar dogs and may chase running animals.",
                "Obedience, agility, tracking and protection sports are a good home for its brain. It learns fast and enjoys structured work.",
                "Active mornings and evenings with firm rest times in between. It does best with routines and a regular training session.",
            ],
            "quirks": [
                "The four varieties (Groenendael, Tervueren, Malinois, Laekenois) are one breed with different coats.",
                "It reads your mood and often reacts before you give a command.",
                "Many circle and herd family members at play, with a famous bounce and speed.",
            ],
        },
        "ru": {
            "summary": "Интенсивная, внимательная и глубоко привязанная к семье. Бельгийская овчарка в четырёх вариантах шерсти — серьёзная рабочая собака, которая отдаётся владельцу, умеющему дать ей цель.",
            "care": "Расчёсывайте раз в неделю, чаще при длинной шерсти и в сильную линьку. Планируйте не меньше двух часов нагрузки и занятий в день.\nХорошо социализируйте с щенячьего возраста и занимайтесь спокойно и последовательно: эта порода замечает всё и чувствительна к грубому обращению.",
            "good_fit": [
                "Уже держали рабочих или пастушьих собак",
                "Можете каждый день давать два часа нагрузки и занятий",
                "Любите собачьи виды спорта или структурированные занятия",
                "Хотите преданную собаку, которая держится рядом со своим человеком",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Большую часть дня не бываете дома",
                "Хотите расслабленную собаку, которая радуется каждому гостю",
                "Живёте в маленькой квартире и мало бываете на улице",
            ],
            "daily": [
                "Два часа и больше, включая настоящий бег и занятия. Малинуа требуется больше всех, но все четыре разновидности неутомимы.",
                "Плохо переносит долгую изоляцию. Если оставить одну и без дела, может тревожиться, шуметь или портить вещи.",
                "Спокойна дома только после нагрузки. Любит понятный распорядок и место рядом с семьёй.",
                "Предана и защищает своих детей, но скорость и пастушьи привычки требуют присмотра рядом с малышами.",
                "Обычно ладит с собаками и животными, с которыми выросла. С незнакомыми собаками бывает напористой и может гнаться за бегущими животными.",
                "Послушание, аджилити, следовая работа и защитные виды спорта дают её уму хорошее применение. Быстро учится и любит чёткую работу.",
                "Активные утро и вечер, между ними строгие периоды отдыха. Лучше всего с режимом и регулярными занятиями.",
            ],
            "quirks": [
                "Четыре разновидности (грюнендаль, тервюрен, малинуа, лакенуа) — одна порода с разной шерстью.",
                "Она считывает ваше настроение и часто реагирует раньше, чем вы подали команду.",
                "В играх многие кружат и «пасут» членов семьи, отличаясь скоростью и знаменитой пружинистостью.",
            ],
        },
    },
    "border-collie": {
        "prey": "moderate",
        "en": {
            "summary": "Brilliant, focused and always watching you. The Border Collie is the herding specialist of the dog world, and it needs a job as much as it needs food.",
            "care": "Brush a few times a week, more in the shed. Plan for two hours or more of exercise every day, with real mental work such as training, scent games or a sport.\nTeach it to settle early. Without a clear off switch, this breed can turn its brain on anything, including you.",
            "good_fit": [
                "Are very active and want a partner for sports or long outdoor days",
                "Enjoy training and will teach new tricks every week",
                "Work from home or have a flexible schedule",
                "Have a garden or a secure place to run",
            ],
            "think_twice": [
                "Want a relaxed dog for a quiet life",
                "Are away from home most of the day",
                "Have a small flat and little time for activities",
                "Do not have time for daily training",
            ],
            "daily": [
                "Two hours or more, with running and a task. Short, repetitive walks are not enough for this brain.",
                "Does not do well alone for long. A bored Border Collie may bark, dig or invent herding games with the sofa.",
                "Needs to settle between activities, which usually has to be taught. In a flat it can work if exercise is generous.",
                "Gentle and playful with respectful children, but it may try to herd running kids, nipping at heels.",
                "Often fine with other dogs. It may fixate on cats, joggers, bikes and cars and try to control them.",
                "Agility, flyball, frisbee, obedience, scent work and trick training suit it well. It loves to solve problems.",
                "Active periods with training, and rest only after a good workout. It thrives on routine and a clear job.",
            ],
            "quirks": [
                'Its "eye" is famous: a fixed, intense stare used to control sheep, and sometimes people.',
                "It can learn the names of dozens of toys and objects.",
                "It may crouch and stalk before dashing after a ball, a bike or a drone.",
            ],
        },
        "ru": {
            "summary": "Гениальный, сосредоточенный и всегда следящий за вами. Бордер-колли — специалист по выпасу среди собак, и работа нужна ему так же сильно, как еда.",
            "care": "Расчёсывайте несколько раз в неделю, чаще в линьку. Планируйте два часа и больше нагрузки в день, обязательно с умственной работой: занятиями, играми на нюх или спортом.\nРано научите его успокаиваться. Без чёткого «выключателя» эта порода применяет свой ум к чему угодно, и к вам тоже.",
            "good_fit": [
                "Очень активны и хотите партнёра для спорта или долгих дней на природе",
                "Любите заниматься и каждую неделю будете учить новым трюкам",
                "Работаете из дома или у вас гибкий график",
                "Есть участок или безопасное место для бега",
            ],
            "think_twice": [
                "Хотите спокойную собаку для тихой жизни",
                "Большую часть дня не бываете дома",
                "Живёте в маленькой квартире и мало времени для занятий",
                "Нет времени на ежедневные тренировки",
            ],
            "daily": [
                "Два часа и больше, с бегом и заданием. Коротких однообразных прогулок такому уму мало.",
                "Плохо переносит долгое одиночество. Заскучавший бордер-колли может лаять, рыть и придумывать пастушьи игры с диваном.",
                "Между занятиями ему нужно научиться успокаиваться, и обычно этому приходится учить. В квартире получится, если нагрузка щедрая.",
                "Мягкий и игривый с уважительными детьми, но может пытаться пасти бегающих детей, хватая за пятки.",
                "Часто ладит с другими собаками. Может зациклиться на кошках, бегунах, велосипедах и машинах и пытаться ими управлять.",
                "Ему подходят аджилити, флайбол, фрисби, послушание, работа по запаху и трюки. Он любит решать задачи.",
                "Периоды активности с занятиями, отдых только после хорошей нагрузки. Любит режим и понятное дело.",
            ],
            "quirks": [
                "Знаменит его «взгляд»: неподвижный пристальный взгляд, которым он управляет овцами, а иногда и людьми.",
                "Может выучить названия десятков игрушек и предметов.",
                "Перед броском за мячом, велосипедом или дроном может присесть и подкрадываться.",
            ],
        },
    },
    "collie-rough": {
        "prey": "low",
        "en": {
            "summary": "Gentle, graceful and very attached to its family. The Rough Collie is a sensitive herding dog with a flowing coat, happiest when it is part of everything at home.",
            "care": "Brush the long coat two or three times a week, and daily while it sheds, paying attention to behind the ears and the feathering. Plan for about an hour of walks and play a day.\nUse a calm voice: this breed reacts to tone and is easily upset by shouting.",
            "good_fit": [
                "Want a gentle, affectionate dog that likes to be near the family",
                "Enjoy walks and calm activities rather than intense sport",
                "Are at home for much of the day",
                "Are happy to brush a long coat regularly",
            ],
            "think_twice": [
                "Dislike dog hair on the floor and the furniture",
                "Are away from home most of the day",
                "Have a noisy or tense household",
                "Want a guard dog that stays quiet",
            ],
            "daily": [
                "About an hour a day in total, with space to run. It enjoys long walks and moderate play more than intense training.",
                "Does not like being alone for long. Lonely Collies may bark or become withdrawn.",
                "Peaceful in the house and happy to lie close to its people. It can live in a flat when walks are regular.",
                "Gentle and patient with children, and often protective. It may nudge and herd running kids.",
                "Usually friendly with other dogs and pets. Some are shy with strangers, so early socialisation helps.",
                "Enjoys walks, fetch, herding games, obedience and tricks. It learns quickly and responds to praise.",
                "A steady rhythm of walks, play and long periods of rest close to the family suits it best.",
            ],
            "quirks": [
                "Collies are often talkative and may bark, chatter or howl to tell you things.",
                "The coat looks glamorous but gets dirty fast, so expect mud in the feathering.",
                "Many Collies rest their long nose on your lap for hours.",
            ],
        },
        "ru": {
            "summary": "Нежный, грациозный и очень привязанный к семье. Колли длинношёрстный — чуткая пастушья собака с роскошной шерстью, которая счастлива, когда участвует во всём, что происходит дома.",
            "care": "Расчёсывайте длинную шерсть два–три раза в неделю, а в линьку каждый день, уделяя внимание зоне за ушами и «штанам». Планируйте около часа прогулок и игр в день.\nГоворите спокойным голосом: порода реагирует на тон и расстраивается от крика.",
            "good_fit": [
                "Хотите нежную ласковую собаку, которая любит быть рядом с семьёй",
                "Любите прогулки и спокойные занятия, а не интенсивный спорт",
                "Бываете дома значительную часть дня",
                "Готовы регулярно расчёсывать длинную шерсть",
            ],
            "think_twice": [
                "Не любите собачью шерсть на полу и мебели",
                "Большую часть дня не бываете дома",
                "У вас шумный или напряжённый дом",
                "Хотите сторожа, который не лает",
            ],
            "daily": [
                "Около часа в день в сумме и место для бега. Любит долгие прогулки и умеренные игры больше, чем интенсивные тренировки.",
                "Не любит долго оставаться одна. Одинокие колли могут лаять или замыкаться.",
                "Спокойна в доме и охотно лежит рядом с людьми. В квартире жить может, если прогулки регулярны.",
                "Нежна и терпелива с детьми, часто защищает их. Может подталкивать и пасти бегающих детей.",
                "Обычно дружелюбна к другим собакам и животным. Некоторые застенчивы с чужими, поэтому полезна ранняя социализация.",
                "Любит прогулки, апорт, пастушьи игры, послушание и трюки. Быстро учится и отзывается на похвалу.",
                "Ей подходит ровный ритм: прогулки, игры и долгий отдых рядом с семьёй.",
            ],
            "quirks": [
                "Колли часто разговорчивы: лают, «болтают» и воют, чтобы вам что-то сообщить.",
                "Шерсть выглядит как с обложки, но быстро пачкается, так что грязь в «штанах» обычное дело.",
                "Многие колли часами лежат, положив длинный нос вам на колени.",
            ],
        },
    },
    "czechoslovakian-wolfdog": {
        "prey": "high",
        "en": {
            "summary": "Wolf-like, tireless and fiercely loyal to its pack. The Czechoslovakian Wolfdog is a rare, independent working breed for experienced, active owners.",
            "care": "Brush weekly, daily during the two heavy sheds each year. Plan for two hours or more of walking, running or hiking, on a long line or in a secure area.\nSocialise widely and early, then keep going all its life. Training is based on trust, not on force.",
            "good_fit": [
                "Have experience with strong, independent breeds",
                "Spend a lot of time outdoors, hiking or running",
                "Have a high, secure fence and a house with a garden",
                "Can be around most of the day",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Want a dog that obeys at once and off lead",
                "Share a home with cats or small pets",
                "Live in a flat in a busy city",
            ],
            "daily": [
                "Two hours or more, with real distance. It loves long hikes and cold weather. Off-lead is risky because of its strong prey drive.",
                "A strongly pack-minded dog that suffers when left alone. Long absences lead to howling, digging and destroyed furniture.",
                "Calm indoors after exercise, but needs space and a high, secure fence. It can climb and dig out.",
                "Loyal to its family, including children it knows, but it is not a play-all-day breed and needs supervision with small kids.",
                "Often reserved with unfamiliar dogs. Small animals, including cats, can trigger a chase.",
                "Tracking, long hikes, bikejoring, canicross and obedience suit it. It learns quickly but only does what it sees a point in.",
                "Active mornings and evenings with long stretches of rest. It likes to stay close to the family, indoors and out.",
            ],
            "quirks": [
                "It howls and uses body language far more than it barks.",
                "It was created in 1950s Czechoslovakia by crossing German Shepherds with Carpathian wolves.",
                "Many are cautious with strangers and need time to decide if a visitor is welcome.",
            ],
        },
        "ru": {
            "summary": "Похожий на волка, неутомимый и яростно преданный стае. Чехословацкая волчья собака — редкая самостоятельная рабочая порода для опытных и активных владельцев.",
            "care": "Расчёсывайте раз в неделю, а в две сильные линьки в год каждый день. Планируйте два часа и больше ходьбы, бега или походов, на длинном поводке или в надёжно огороженном месте.\nСоциализируйте рано и широко, а потом продолжайте всю жизнь. Дрессировка строится на доверии, а не на силе.",
            "good_fit": [
                "Уже держали сильных самостоятельных собак",
                "Много бываете на природе, ходите в походы или бегаете",
                "Есть дом с участком и высокий надёжный забор",
                "Большую часть дня бываете дома",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Хотите собаку, которая сразу слушается и без поводка",
                "Живёте с кошками или мелкими животными",
                "Живёте в квартире в шумном городе",
            ],
            "daily": [
                "Два часа и больше, с настоящим километражем. Любит долгие походы и холод. Без поводка рискованно из-за сильного охотничьего инстинкта.",
                "Собака, сильно привязанная к стае, тяжело переживает одиночество. Долгое отсутствие ведёт к вою, подкопам и испорченной мебели.",
                "В доме спокойна после нагрузки, но нужны место и высокий надёжный забор. Умеет перелезать и подкапывать.",
                "Предана семье, включая знакомых детей, но это не порода для игр на весь день и рядом с малышами нужен присмотр.",
                "С незнакомыми собаками часто сдержанна. Мелкие животные, включая кошек, могут вызвать погоню.",
                "Ей подходят следовая работа, длинные походы, байкджоринг, каникросс и послушание. Быстро учится, но делает только то, в чём видит смысл.",
                "Активные утро и вечер и долгие периоды отдыха. Любит быть рядом с семьёй, дома и на улице.",
            ],
            "quirks": [
                "Она больше воет и пользуется языком тела, чем лает.",
                "Порода создана в 1950-х годах в Чехословакии скрещиванием немецких овчарок с карпатскими волками.",
                "Многие осторожны с чужими и не сразу решают, рады ли они гостю.",
            ],
        },
    },
    "dutch-shepherd-dog": {
        "prey": "moderate",
        "en": {
            "summary": "Active, alert and sturdy, with a brindle coat and a mind of its own. The Dutch Shepherd is a working all-rounder that thrives with an owner who keeps it busy.",
            "care": "Brush weekly for short and long coats, and two or three times a week for the rough coat, with occasional trimming. Plan for around two hours of exercise and training every day.\nStart training and socialisation early and stay calm and consistent: it learns fast and respects a fair leader.",
            "good_fit": [
                "Are active and enjoy outdoor time every day",
                "Like training and dog sports",
                "Have experience with working breeds",
                "Want a loyal, watchful family dog",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a calm dog for a quiet life",
                "Live in a small flat",
                "Are getting your first dog and are not ready to train",
            ],
            "daily": [
                "Around two hours a day with running, training and tasks. A short walk around the block is not enough.",
                "Can manage a few hours when used to it, but without a job it may become restless, noisy or destructive.",
                "Settles at home after exercise. A garden helps, but it needs company and a daily routine.",
                "Loyal and protective with its family. It plays well with respectful children but may herd them, so supervise small kids.",
                "Usually fine with dogs it grew up with. Cats and small animals need careful introductions.",
                "Obedience, agility, tracking, herding and protection sports are all good outlets. It is happiest working with you.",
                "Active mornings and evenings with regular training, then rest. Routine keeps it balanced.",
            ],
            "quirks": [
                "The brindle coat looks like a tiger's and is the breed's signature.",
                "The Dutch Shepherd was a farm all-rounder, herding sheep, pulling carts and guarding the yard.",
                "It is alert to every sound, and watches the street from the window.",
            ],
        },
        "ru": {
            "summary": "Активная, бдительная и крепкая, с тигровым окрасом и собственным мнением. Голландская овчарка — универсальная рабочая собака, которая расцветает у владельца, умеющего её занять.",
            "care": "Расчёсывайте раз в неделю у короткошёрстных и длинношёрстных, два–три раза в неделю у жёсткошёрстных, иногда с триммингом. Планируйте около двух часов нагрузки и занятий в день.\nНачинайте дрессировку и социализацию рано и действуйте спокойно и последовательно: она быстро учится и уважает справедливого лидера.",
            "good_fit": [
                "Активны и каждый день проводите время на улице",
                "Любите дрессировку и собачьи виды спорта",
                "Уже держали рабочих собак",
                "Хотите преданную бдительную семейную собаку",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите спокойную собаку для тихой жизни",
                "Живёте в маленькой квартире",
                "Берёте первую собаку и не готовы заниматься с ней",
            ],
            "daily": [
                "Около двух часов в день с бегом, занятиями и заданиями. Короткой прогулки вокруг дома недостаточно.",
                "Несколько часов выдержит, когда привыкнет, но без дела может стать беспокойной, шумной или разрушительной.",
                "Дома успокаивается после нагрузки. Участок помогает, но ей нужны компания и ежедневный распорядок.",
                "Предана и защищает семью. Хорошо играет с уважительными детьми, но может их пасти, поэтому за малышами нужен присмотр.",
                "Обычно ладит с собаками, с которыми выросла. С кошками и мелкими животными знакомьте осторожно.",
                "Послушание, аджилити, следовая работа, пастушьи и защитные виды спорта — всё это ей подходит. Счастлива, когда работает с вами.",
                "Активные утро и вечер с регулярными занятиями, затем отдых. Режим помогает ей быть уравновешенной.",
            ],
            "quirks": [
                "Тигровый окрас похож на шкуру тигра и считается визитной карточкой породы.",
                "Голландская овчарка была фермерским универсалом: пасла овец, возила тележки и охраняла двор.",
                "Она реагирует на каждый звук и наблюдает за улицей из окна.",
            ],
        },
    },
    "german-shepherd-dog": {
        "prey": "moderate",
        "en": {
            "summary": "Loyal, clever and eager to work. The German Shepherd is the classic all-round working dog, devoted to its family and watchful at home.",
            "care": "Brush two or three times a week, daily during the heavy twice-yearly shed. Plan for about two hours of exercise and training a day, ideally with a task.\nSocialise early and widely, and keep training fair and consistent. A bored or lonely shepherd quickly finds its own jobs.",
            "good_fit": [
                "Want a loyal dog that follows you around the house",
                "Enjoy training and daily outdoor time",
                "Are home for a good part of the day",
                "Do not mind a lot of dog hair",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Dislike shedding and daily vacuuming",
                "Have no time for early socialisation and training",
                "Want a dog that welcomes every visitor",
            ],
            "daily": [
                "Around two hours a day, including a run and some training. It enjoys structured walks with tasks.",
                "Does not do well alone for long. A bored shepherd may bark, dig or chew.",
                "Calm and attentive indoors once exercised, and happiest in the same room as its family. It is a natural watchdog.",
                "Devoted and protective with its own children, but a big, strong dog needs supervision around small kids.",
                "Often fine with other dogs when socialised. It may be reserved with strangers and can chase small animals.",
                "Obedience, tracking, agility, herding and protection sports suit it. It learns quickly and wants a purpose.",
                "Active mornings and evenings, with regular rest in between. It loves routine and being useful.",
            ],
            "quirks": [
                'Owners joke about the "German shedder": fur turns up on every surface, year round.',
                "It often leans against your legs or follows you from room to room.",
                "The ears stand up on their own at about four to six months, sometimes in odd positions first.",
            ],
        },
        "ru": {
            "summary": "Преданная, умная и стремящаяся работать. Немецкая овчарка — классическая универсальная рабочая собака, которая предана семье и бдительна дома.",
            "care": "Расчёсывайте два–три раза в неделю, а в сильную линьку дважды в год каждый день. Планируйте около двух часов нагрузки и занятий в день, лучше с заданием.\nСоциализируйте рано и широко, занимайтесь справедливо и последовательно. Заскучавшая или одинокая овчарка быстро находит себе занятия сама.",
            "good_fit": [
                "Хотите преданную собаку, которая ходит за вами по дому",
                "Любите дрессировку и ежедневное время на улице",
                "Значительную часть дня бываете дома",
                "Не против большого количества шерсти",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Не любите линьку и ежедневную уборку",
                "Нет времени на раннюю социализацию и занятия",
                "Хотите собаку, которая радуется каждому гостю",
            ],
            "daily": [
                "Около двух часов в день, включая бег и занятия. Любит организованные прогулки с заданиями.",
                "Плохо переносит долгое одиночество. Заскучавшая овчарка может лаять, рыть или грызть вещи.",
                "Дома спокойна и внимательна после нагрузки, больше всего любит быть в одной комнате с семьёй. Природный сторож.",
                "Предана и защищает своих детей, но большая сильная собака требует присмотра рядом с малышами.",
                "С социализацией часто ладит с другими собаками. С чужими людьми бывает сдержанной и может гнаться за мелкими животными.",
                "Ей подходят послушание, следовая работа, аджилити, пастушьи и защитные виды спорта. Быстро учится и хочет иметь цель.",
                "Активные утро и вечер, между ними регулярный отдых. Любит режим и быть полезной.",
            ],
            "quirks": [
                "Владельцы шутят про «немецкого линяльщика»: шерсть появляется на всех поверхностях круглый год.",
                "Она часто прислоняется к вашим ногам или ходит за вами из комнаты в комнату.",
                "Уши встают сами примерно к четырём–шести месяцам, иногда сначала в странных положениях.",
            ],
        },
    },
    "old-english-sheepdog": {
        "prey": "low",
        "en": {
            "summary": "Shaggy, cheerful and a little clownish. The Old English Sheepdog is a gentle family dog under a big coat, happiest in the middle of everything.",
            "care": "Brush the full coat thoroughly every two or three days, down to the skin, or keep it in a shorter trim. Plan for about an hour of walks and play, avoiding hard exercise in hot weather.\nBeard and feet get wet and muddy, so wipe them after walks.",
            "good_fit": [
                "Want a cheerful, goofy family dog",
                "Enjoy grooming and do not mind a messy beard",
                "Have a house with space, or a big flat and regular walks",
                "Are at home for much of the day",
            ],
            "think_twice": [
                "Dislike mud, drool and wet beards on the floor",
                "Live in a very warm climate",
                "Are away from home most of the day",
                "Do not have time for regular grooming",
            ],
            "daily": [
                "About an hour a day in total, with a free run when possible. It does not need sport, but it likes company on a walk.",
                "Does not like being alone for long. Without people it may bark or chew.",
                "Happy in the middle of the family, flopping down in the way. It needs space for its size and coat.",
                "Gentle, patient and playful with children. It may bump into or lean on small kids and may gently herd them.",
                "Usually friendly with dogs and other pets. It can try to herd family members and other animals.",
                "Enjoys walks, play, simple obedience and fetch. It does not need intense sport, but it does need regular activity.",
                "Relaxed routine of walks, play and long stretches lying close to people. Heat is its enemy.",
            ],
            "quirks": [
                'The "bear" walk with a rolling gait is typical of the breed.',
                "The fringe over the eyes looks thick, but the dog sees perfectly well. Many owners tie it back.",
                "Its bark is deep and resonant, almost like a bell.",
            ],
        },
        "ru": {
            "summary": "Лохматый, жизнерадостный и немного клоун. Бобтейл — мягкая семейная собака под большой шубой, счастливая в центре событий.",
            "care": "Тщательно расчёсывайте всю шерсть, до кожи, каждые два–три дня, или стригите её короче. Планируйте около часа прогулок и игр, избегая тяжёлой нагрузки в жару.\nБорода и лапы мокнут и пачкаются, поэтому вытирайте их после прогулки.",
            "good_fit": [
                "Хотите весёлую забавную семейную собаку",
                "Любите уход за шерстью и не боитесь неопрятной бороды",
                "Живёте в доме с местом или в большой квартире с регулярными прогулками",
                "Значительную часть дня бываете дома",
            ],
            "think_twice": [
                "Не любите грязь, слюни и мокрую бороду на полу",
                "Живёте в очень тёплом климате",
                "Большую часть дня не бываете дома",
                "Нет времени на регулярный груминг",
            ],
            "daily": [
                "Около часа в день в сумме, по возможности со свободным бегом. Спорт ей не нужен, но на прогулке нужна компания.",
                "Не любит долго оставаться одна. Без людей может лаять или грызть вещи.",
                "Счастлива в центре семьи и падает на пол там, где вы идёте. Ей нужно место из-за размера и шерсти.",
                "Нежна, терпелива и игрива с детьми. Может толкнуть или навалиться на малыша и мягко пасти детей.",
                "Обычно дружелюбна к собакам и другим животным. Может пытаться пасти членов семьи и других животных.",
                "Любит прогулки, игры, простое послушание и апорт. Интенсивный спорт не нужен, но нужна регулярная активность.",
                "Спокойный ритм: прогулки, игры и долгие периоды рядом с людьми. Жара — её враг.",
            ],
            "quirks": [
                "«Медвежья» перекатывающаяся походка типична для породы.",
                "Чёлка на глазах кажется густой, но собака прекрасно видит. Многие владельцы подвязывают её.",
                "Лай у неё глубокий и звучный, почти как колокол.",
            ],
        },
    },
    "pembroke-welsh-corgi": {
        "prey": "moderate",
        "en": {
            "summary": "Short-legged, bold and full of personality. The Pembroke Welsh Corgi is a herding dog in a small body, always ready to be the centre of the family.",
            "care": "Brush two or three times a week and daily during the heavy sheds, since the double coat sheds a lot. Plan for about an hour of walks and play a day.\nWatch the portions and treats: Corgis love food and gain weight easily. Keep jumping from heights to a minimum.",
            "good_fit": [
                "Want a lively, cheerful family dog",
                "Enjoy walks and simple games",
                "Do not mind a lot of fur",
                "Can keep the dog from gaining weight",
            ],
            "think_twice": [
                "Want a quiet dog that rarely barks",
                "Dislike dog hair on clothes and furniture",
                "Are away from home most of the day",
                "Cannot say no to a begging look",
            ],
            "daily": [
                "About an hour a day, split into two or three walks. It has plenty of energy and likes to cover ground despite the short legs.",
                "Manages a few hours when used to it. Bored Corgis bark, dig or make their own games.",
                "Suits a flat as long as walks are regular. It likes to be wherever you are and tends to be talkative.",
                "Friendly and playful with kids who treat it kindly. The herding habit of nipping at heels needs to be gently trained out.",
                "Usually gets on with dogs and cats it knows. It may try to herd them, and can bark at strangers.",
                "Enjoys fetch, agility, herding games, simple tricks and food puzzles. Training works well with treats.",
                "Active periods through the day with plenty of rest. It likes to stay close, from the kitchen to the sofa.",
            ],
            "quirks": [
                "Corgis love to lie flat like a frog, with the back legs stretched out behind them.",
                "They have a famous round rear end and a stub tail, or none at all.",
                "Many are expert beggars with a perfectly timed hopeful look.",
            ],
        },
        "ru": {
            "summary": "Коротконогий, смелый и полный характера. Вельш-корги пемброк — пастушья собака в маленьком теле, всегда готовая быть центром семьи.",
            "care": "Расчёсывайте два–три раза в неделю, а в сильную линьку каждый день: двойная шерсть сильно линяет. Планируйте около часа прогулок и игр в день.\nСледите за порциями и лакомствами: корги любят поесть и легко набирают вес. Прыжки с высоты сведите к минимуму.",
            "good_fit": [
                "Хотите живую весёлую семейную собаку",
                "Любите прогулки и простые игры",
                "Не против большого количества шерсти",
                "Сможете не давать собаке набирать вес",
            ],
            "think_twice": [
                "Хотите тихую собаку, которая редко лает",
                "Не любите шерсть на одежде и мебели",
                "Большую часть дня не бываете дома",
                "Не можете отказать просящему взгляду",
            ],
            "daily": [
                "Около часа в день, разделённого на две–три прогулки. Энергии много, и несмотря на короткие лапы, она любит пройти путь.",
                "Несколько часов выдержит, когда привыкнет. Заскучавшие корги лают, роют или придумывают игры сами.",
                "Подходит для квартиры при регулярных прогулках. Любит быть там, где вы, и обычно разговорчива.",
                "Дружелюбна и игрива с детьми, которые относятся к ней добро. Пастушью привычку хватать за пятки нужно мягко отучать.",
                "Обычно ладит с собаками и кошками, которых знает. Может пытаться их пасти и лаять на чужих.",
                "Любит апорт, аджилити, пастушьи игры, простые трюки и игрушки с лакомством. Дрессировка хорошо идёт на поощрении.",
                "Активные периоды в течение дня с достаточным отдыхом. Любит быть рядом, от кухни до дивана.",
            ],
            "quirks": [
                "Корги любят лежать «лягушкой»: плашмя, вытянув задние лапы назад.",
                "У них знаменитый круглый зад и куцый хвост или его отсутствие.",
                "Многие — мастера выпрашивания с идеально рассчитанным по времени взглядом.",
            ],
        },
    },
    "puli": {
        "prey": "moderate",
        "en": {
            "summary": "Springy, quick and unmistakable in its corded coat. The Puli is a Hungarian herding dog with a lot of energy, a loud voice and a clear opinion about everything.",
            "care": "The corded coat does not brush: cords are separated by hand every few weeks, and washing takes time and a full day to dry. Plan for about an hour and a half of exercise and play every day.\nTrain early and keep sessions varied: it is clever and gets bored with repetition.",
            "good_fit": [
                "Want a lively, alert dog with a unique look",
                "Enjoy active play and training",
                "Have time to maintain a corded coat",
                "Are around much of the day",
            ],
            "think_twice": [
                "Want a quiet dog that rarely barks",
                "Have no patience for coat care",
                "Are away from home most of the day",
                "Want a low-effort first dog",
            ],
            "daily": [
                "About an hour and a half a day, with play and training. It bounces and spins and loves to run.",
                "Not happy alone for long. A bored Puli will bark, dig and look for something to herd.",
                "Alert indoors and quick to announce visitors. It can live in a flat if walks are regular and the barking is trained.",
                "Playful with older children who respect it. It may herd small kids, and its energy can be a lot for toddlers.",
                "Usually fine with dogs it grew up with. It may try to herd other pets and can be wary of strangers.",
                "Enjoys agility, frisbee, herding games and trick training. It learns fast and needs variety.",
                "Active, busy days with rest breaks. It likes to be part of whatever happens in the house.",
            ],
            "quirks": [
                'Puli are famous for "popping": jumping straight up on the spot, even over a person\'s head.',
                "The cords can reach the ground and are sometimes mistaken for a mop.",
                "It barks loudly at anything new, so expect an announcement for every visitor.",
            ],
        },
        "ru": {
            "summary": "Пружинистый, быстрый и узнаваемый по шерсти-шнурам. Пули — венгерская пастушья собака с большим запасом энергии, громким голосом и собственным мнением обо всём.",
            "care": "Шерсть-шнуры не расчёсывают: шнуры разделяют руками раз в несколько недель, а мытьё требует времени, и сохнет она целый день. Планируйте около полутора часов нагрузки и игр в день.\nЗанимайтесь рано и разнообразно: пули умна и скучает от однообразия.",
            "good_fit": [
                "Хотите живую бдительную собаку с уникальной внешностью",
                "Любите активные игры и занятия",
                "Есть время поддерживать шнуры",
                "Большую часть дня бываете дома",
            ],
            "think_twice": [
                "Хотите тихую собаку, которая редко лает",
                "У вас нет терпения на уход за шерстью",
                "Большую часть дня не бываете дома",
                "Хотите первую собаку с минимумом усилий",
            ],
            "daily": [
                "Около полутора часов в день, с играми и занятиями. Подпрыгивает, вертится и любит бегать.",
                "Долго одной быть не любит. Заскучавшая пули лает, роет и ищет, кого бы попасти.",
                "Дома бдительна и быстро объявляет о гостях. В квартире жить может, если прогулки регулярны, а лай приучен.",
                "Игрива со старшими детьми, которые её уважают. Может пасти малышей, и её энергии для совсем маленьких детей бывает много.",
                "Обычно ладит с собаками, с которыми выросла. Может пытаться пасти других питомцев и настороженно относиться к чужим.",
                "Любит аджилити, фрисби, пастушьи игры и трюки. Быстро учится и нуждается в разнообразии.",
                "Активные насыщенные дни с перерывами на отдых. Хочет участвовать во всём, что происходит в доме.",
            ],
            "quirks": [
                "Пули знамениты «подскоками»: она прыгает вверх на месте, иногда выше головы человека.",
                "Шнуры могут достигать земли, и её иногда принимают за швабру.",
                "Она громко лает на всё новое, поэтому о каждом госте вас предупредят.",
            ],
        },
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, data in DOGS.items():
        values = {"prey_drive": data["prey"]}
        for lang in ("en", "ru"):
            block = data[lang]
            labels = LABELS[lang]
            texts = {
                "summary": block["summary"],
                "care": block["care"],
                "good_fit": "\n".join(block["good_fit"]),
                "think_twice": "\n".join(block["think_twice"]),
                "daily_life": "\n\n".join(
                    f"{l}: {t}" for l, t in zip(labels, block["daily"])
                ),
                "quirks": "\n".join(block["quirks"]),
            }
            for field, text in texts.items():
                values[f"{field}_{lang}"] = text
                if lang == "en":
                    values[field] = text
        for lang in ("de", "it", "es", "sr_latn"):
            for field in (
                "summary",
                "care",
                "good_fit",
                "think_twice",
                "daily_life",
                "quirks",
            ):
                values[f"{field}_{lang}"] = ""
        Dogs.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0061_dachshund_care_without_breeder")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
