from django.db import migrations

LABELS = {
    "en": ["Walks", "Being alone", "At home", "Children", "Other animals", "Play and activities", "Daily routine"],
    "ru": ["Прогулки", "Одиночество", "Дома", "Дети", "Другие животные", "Игры и занятия", "Распорядок дня"],
}

DAILY = {
    "australian-shepherd": {
        "en": [
            "Plan for around two hours a day in total. A stroll on a lead is not enough: the Aussie wants to run, fetch and work its brain. Where it is safe, give it off-lead time, and keep an eye on it near roads, since it likes to keep the family in sight and may try to round up passers-by.",
            "A few hours alone is possible once it is used to it, but a bored Aussie finds its own jobs. Digging, barking at the window and herding the furniture are common. Leave it with a chew or a puzzle toy and exercise it well beforehand.",
            "It is happiest in a house with a garden and a family that is around. In a flat it can cope if its exercise really is delivered every day, but it will follow you from room to room and will not accept being ignored.",
            "Devoted and playful with children who respect it. Like many herding dogs, it may nip at heels or try to round up running kids, so teach manners early and supervise games with younger children.",
            "Usually fine with dogs it grew up with and often fond of other pets at home. It may try to herd cats and small animals, and some are reserved or pushy with unfamiliar dogs, so introduce new ones calmly.",
            "Agility, obedience, frisbee, herding and trick training suit it well. It learns quickly and is at its best when it has a task: carrying things, finding toys, learning a new trick each week.",
            "An active morning and evening with rest in between. It does best when the day has a rhythm: a long outing, a training session, and then quiet time beside you at home.",
        ],
        "ru": [
            "Планируйте около двух часов в день в сумме. Прогулки на поводке мало: австралийская овчарка хочет бегать, приносить и работать головой. Где безопасно, давайте ей бегать без поводка, но у дороги присматривайте: она любит держать семью в поле зрения и может пытаться собрать прохожих.",
            "Несколько часов в одиночестве возможны, когда она привыкла, но заскучавшая овчарка находит себе занятия сама. Обычное дело: рытьё, лай в окно, «пастьба» мебели. Оставьте ей жвачку или игрушку-головоломку и заранее хорошо погуляйте.",
            "Счастливее всего в доме с участком и с семьёй, которая бывает дома. В квартире справится, если нагрузка действительно есть каждый день, но будет ходить за вами из комнаты в комнату и не примет, что её игнорируют.",
            "Предана и игрива с детьми, которые её уважают. Как многие пастушьи собаки, может хватать за пятки и пытаться собрать бегающих детей, поэтому манеры лучше воспитывать рано, а игры с малышами контролировать.",
            "Обычно ладит с собаками, с которыми выросла, и нередко привязывается к другим питомцам. Может пытаться пасти кошек и мелких животных, а с незнакомыми собаками бывает сдержанной или напористой, поэтому знакомьте спокойно.",
            "Ей подходят аджилити, послушание, фрисби, пастушьи тесты и трюки. Быстро учится и лучше всего чувствует себя, когда у неё есть задача: носить вещи, искать игрушки, раз в неделю осваивать новый трюк.",
            "Активные утро и вечер, между ними отдых. Лучше всего ей, когда у дня есть ритм: долгая прогулка, занятие и потом спокойное время рядом с вами дома.",
        ],
    },
    "belgian-shepherd-dog": {
        "en": [
            "Two hours or more, with real running and training. The Malinois needs the most, but all four varieties are tireless. A calm walk on a lead is only a warm-up: it needs room to run, a ball or a task, and a handler who stays interesting.",
            "It does not like long isolation. Left bored and alone, a Belgian Shepherd can become anxious, noisy or destructive, and the Malinois in particular needs work every day to stay balanced. Build up time alone gradually from puppyhood.",
            "Calm in the house only after its exercise is done. It likes a clear routine and a place close to the family, and it watches the home and the street. Expect it to follow you and to notice every change.",
            "Loyal and protective with its own children, and gentle with those it knows. Its speed, herding habits and strong reactions mean it needs supervision with small kids, and visiting children should be introduced calmly.",
            "Often fine with dogs and pets it grew up with. It can be intense with unfamiliar dogs and may chase running animals, so socialise it widely and keep it on a lead where cats or wildlife are around.",
            "Obedience, agility, tracking and protection sports are a good home for its brain. It learns fast and enjoys structured work, such as learning a sequence of commands or searching for a hidden toy.",
            "Active mornings and evenings with firm rest times in between. It does best with a regular routine and at least one real training session each day. Without it, the energy has to go somewhere.",
        ],
        "ru": [
            "Два часа и больше, с настоящим бегом и занятиями. Больше всех нужно малинуа, но все четыре разновидности неутомимы. Спокойная прогулка на поводке для неё лишь разминка: нужны место для бега, мяч или задание и хозяин, который остаётся интересным.",
            "Плохо переносит долгую изоляцию. Если оставить одну и без дела, бельгийская овчарка может тревожиться, шуметь или портить вещи, а малинуа особенно нужна работа каждый день, чтобы оставаться уравновешенной. Приучайте её к одиночеству постепенно, с щенячьего возраста.",
            "Дома спокойна только после нагрузки. Любит понятный распорядок и место рядом с семьёй, следит за домом и улицей. Будет ходить за вами и замечать любую перемену.",
            "Предана и защищает своих детей, мягка со знакомыми. Скорость, пастушьи привычки и сильные реакции означают, что рядом с малышами нужен присмотр, а приходящих детей лучше знакомить спокойно.",
            "Часто ладит с собаками и животными, с которыми выросла. С незнакомыми собаками бывает напористой и может гнаться за бегущими животными, поэтому социализируйте её широко и держите на поводке там, где есть кошки или дикие животные.",
            "Послушание, аджилити, следовая работа и защитные виды спорта дают её уму хорошее применение. Быстро учится и любит чёткую работу: выполнять цепочку команд или искать спрятанную игрушку.",
            "Активные утро и вечер, между ними чёткие периоды отдыха. Лучше всего с режимом и хотя бы одним настоящим занятием в день. Без этого энергия найдёт выход сама.",
        ],
    },
    "border-collie": {
        "en": [
            "Two hours or more, with running and a task. Short, repetitive walks are not enough for this brain. Add a ball, a frisbee or a bit of training on the way, and vary the route so it keeps finding things to figure out.",
            "It does not do well alone for long. A bored Border Collie may bark, dig or invent herding games with the sofa, the cat or the vacuum. If you must be away, give it exercise first and something to chew or solve.",
            "Needs to settle between activities, which usually has to be taught: practise a \"place\" or a mat from puppyhood. In a flat it can work if exercise is generous, but it will watch you and the window constantly.",
            "Gentle and playful with respectful children, and happy to run with them. It may try to herd running kids, nipping at heels, so teach it manners and teach children not to run screaming around it.",
            "Often fine with other dogs. It may fixate on cats, joggers, bikes and cars and try to control them by stalking and staring, so work on calm when something moves quickly.",
            "Agility, flyball, frisbee, obedience, scent work and trick training suit it well. It loves to solve problems and can learn the names of dozens of objects, so give it new challenges regularly.",
            "Active periods built around training, and rest only after a good workout. It thrives on routine and a clear job, and tends to get restless in unstructured days.",
        ],
        "ru": [
            "Два часа и больше, с бегом и заданием. Коротких однообразных прогулок такому уму мало. Добавляйте по пути мяч, фрисби или немного занятий и меняйте маршрут, чтобы ей было что разгадывать.",
            "Плохо переносит долгое одиночество. Заскучавший бордер-колли может лаять, рыть и придумывать пастушьи игры с диваном, кошкой или пылесосом. Если нужно уйти, сначала дайте нагрузку, потом оставьте что-то погрызть или решить.",
            "Ей нужно научиться успокаиваться между делами, и этому обычно приходится учить: отрабатывайте «место» или коврик с щенячьего возраста. В квартире получится, если нагрузка щедрая, но она будет постоянно следить за вами и за окном.",
            "Мягкий и игривый с уважительными детьми, охотно бегает с ними. Может пытаться пасти бегающих детей, хватая за пятки, поэтому учите манерам и собаку, и детей не носиться вокруг неё с криками.",
            "Часто ладит с другими собаками. Может зациклиться на кошках, бегунах, велосипедах и машинах и пытаться управлять ими, подкрадываясь и сверля взглядом, поэтому тренируйте спокойствие, когда рядом что-то быстро движется.",
            "Ему подходят аджилити, флайбол, фрисби, послушание, работа по запаху и трюки. Он любит решать задачи и способен выучить названия десятков предметов, поэтому регулярно придумывайте новые.",
            "Периоды активности строятся вокруг занятий, отдых только после хорошей нагрузки. Любит режим и понятное дело, а в дни без структуры становится беспокойным.",
        ],
    },
    "collie-rough": {
        "en": [
            "About an hour a day in total, with space to run. It enjoys long walks and moderate play more than intense training, and is happy to trot beside you through fields and woods. Keep it on a lead near roads, as it can chase moving things.",
            "It does not like being alone for long. Lonely Collies may bark or become withdrawn, and the voice is surprisingly big. If you are out for most of the day, this is not the dog for you.",
            "Peaceful in the house and happy to lie close to its people. It can live in a flat when walks are regular, though the coat and the bark need to be managed. It often picks a spot near the family and settles there.",
            "Gentle and patient with children, and often protective. It may nudge and herd running kids, and a loud household can upset a sensitive dog, so keep play calm.",
            "Usually friendly with other dogs and pets. Some are shy with strangers, so early socialisation helps. It is rarely pushy, and it reacts badly to harsh handling, loud voices and quarrels in the house.",
            "Enjoys walks, fetch, herding games, obedience and tricks. It learns quickly and responds to praise and gentle guidance. It is more of a thinker than an athlete, so offer activities that let it use its head.",
            "A steady rhythm of walks, play and long periods of rest close to the family suits it best. It likes predictability and calm company, and a quiet, regular day.",
        ],
        "ru": [
            "Около часа в день в сумме, с местом для бега. Любит долгие прогулки и умеренные игры больше, чем интенсивные тренировки, и охотно трусит рядом с вами по полям и лесу. Рядом с дорогой держите на поводке: она может погнаться за движущимся.",
            "Не любит долго оставаться одна. Одинокие колли могут лаять или замыкаться, а голос у неё неожиданно громкий. Если вас почти весь день нет дома, эта собака не для вас.",
            "Спокойна в доме и охотно лежит рядом с людьми. В квартире жить может при регулярных прогулках, но шерсть и лай придётся держать под контролем. Часто выбирает место рядом с семьёй и остаётся там.",
            "Нежна и терпелива с детьми, часто защищает их. Может подталкивать и пасти бегающих детей, а шумный дом расстраивает чуткую собаку, поэтому играйте спокойно.",
            "Обычно дружелюбна к другим собакам и животным. Некоторые застенчивы с чужими, поэтому полезна ранняя социализация. Редко напориста, а грубое обращение, громкие голоса и ссоры в доме переносит плохо.",
            "Любит прогулки, апорт, пастушьи игры, послушание и трюки. Быстро учится и отзывается на похвалу и мягкое руководство. Она скорее мыслитель, чем спортсмен, поэтому подбирайте занятия, где работает голова.",
            "Ей подходит ровный ритм: прогулки, игры и долгий отдых рядом с семьёй. Любит предсказуемость, спокойную компанию и тихий размеренный день.",
        ],
    },
    "czechoslovakian-wolfdog": {
        "en": [
            "Two hours or more, with real distance. It loves long hikes, cold weather and snow, and does well running beside a bike or on a long line. Off-lead is risky because of its strong prey drive and independent mind, so use a secure area or a long line.",
            "A strongly pack-minded dog that suffers when left alone. Long absences lead to howling, digging and destroyed furniture, and it can escape over or under fences. It is best for owners who are at home or can take it along.",
            "Calm indoors after exercise, but it needs space and a high, secure fence. It can climb and dig out, so check boundaries often. It prefers to be near the family, and often sleeps within reach of someone.",
            "Loyal to its family, including children it knows, but it is not a play-all-day breed. Its size, strength and wolf-like reactions mean it needs supervision around small kids and guests.",
            "Often reserved with unfamiliar dogs and may try to dominate them. Small animals, including cats, can trigger a chase, so living with them requires very careful introductions and early experience.",
            "Tracking, long hikes, bikejoring, canicross and obedience suit it. It learns quickly but only does what it sees a point in, so keep training varied and based on trust rather than repetition.",
            "Active mornings and evenings with long stretches of rest. It likes to stay close to the family, indoors and out, and does best with a routine that includes real outdoor time every day.",
        ],
        "ru": [
            "Два часа и больше, с настоящим километражем. Любит долгие походы, холод и снег, хорошо бегает рядом с велосипедом или на длинном поводке. Без поводка рискованно из-за сильного охотничьего инстинкта и самостоятельного ума, поэтому используйте огороженное место или длинный поводок.",
            "Собака, сильно привязанная к стае, тяжело переживает одиночество. Долгое отсутствие ведёт к вою, подкопам и испорченной мебели, а ещё она может уйти поверх или под забором. Лучше всего подходит тем, кто бывает дома или может брать её с собой.",
            "В доме спокойна после нагрузки, но ей нужны место и высокий надёжный забор. Умеет перелезать и подкапывать, поэтому почаще проверяйте границы. Предпочитает быть рядом с семьёй и часто спит в зоне досягаемости кого-то из людей.",
            "Предана семье, включая знакомых детей, но это не порода для игр на весь день. Размер, сила и волчьи реакции означают, что рядом с малышами и гостями нужен присмотр.",
            "С незнакомыми собаками часто сдержанна и может пытаться доминировать. Мелкие животные, включая кошек, могут вызвать погоню, поэтому совместная жизнь требует очень осторожного знакомства и раннего опыта.",
            "Ей подходят следовая работа, длинные походы, байкджоринг, каникросс и послушание. Быстро учится, но делает только то, в чём видит смысл, поэтому занятия лучше разнообразить и строить на доверии, а не на повторении.",
            "Активные утро и вечер и долгие периоды отдыха. Любит быть рядом с семьёй, дома и на улице, и лучше всего себя чувствует с распорядком, в котором каждый день есть настоящее время на природе.",
        ],
    },
    "dutch-shepherd-dog": {
        "en": [
            "Around two hours a day with running, training and tasks. A short walk around the block is not enough. It enjoys long outings in the countryside, and is happy to do a bit of work on the way, such as retrieving or searching.",
            "It can manage a few hours when used to it, but without a job it may become restless, noisy or destructive. Build up time alone gradually and give it a chew or a puzzle before you leave.",
            "It settles at home after exercise. A garden helps, but it needs company and a daily routine. It often lies where it can see the door and the family at once, and notices every sound outside.",
            "Loyal and protective with its family. It plays well with respectful children but may herd them, so supervise small kids. Teach it to stay calm when visitors arrive, and teach children to respect its space.",
            "Usually fine with dogs it grew up with. Cats and small animals need careful introductions, and a strong guarding instinct means unfamiliar dogs should be met on neutral ground.",
            "Obedience, agility, tracking, herding and protection sports are all good outlets. It is happiest working with you and picks up commands quickly, so a regular training session is a gift to it.",
            "Active mornings and evenings with regular training, then rest. A routine keeps it balanced, and an idle day tends to turn into mischief.",
        ],
        "ru": [
            "Около двух часов в день с бегом, занятиями и заданиями. Короткой прогулки вокруг дома недостаточно. Любит долгие выходы за город и охотно выполняет по пути небольшую работу: поиск, апорт.",
            "Несколько часов выдержит, когда привыкнет, но без дела может стать беспокойной, шумной или разрушительной. Приучайте к одиночеству постепенно и оставляйте жвачку или головоломку перед уходом.",
            "Дома успокаивается после нагрузки. Участок помогает, но ей нужны компания и ежедневный распорядок. Часто ложится так, чтобы видеть и дверь, и семью, и замечает каждый звук снаружи.",
            "Предана и защищает семью. Хорошо играет с уважительными детьми, но может их пасти, поэтому за малышами нужен присмотр. Учите её спокойно встречать гостей, а детей уважать её пространство.",
            "Обычно ладит с собаками, с которыми выросла. С кошками и мелкими животными знакомьте осторожно, а из-за сильного охранного инстинкта с незнакомыми собаками лучше встречаться на нейтральной территории.",
            "Послушание, аджилити, следовая работа, пастушьи и защитные виды спорта — всё это ей подходит. Счастлива, когда работает с вами, и быстро схватывает команды, так что регулярные занятия для неё подарок.",
            "Активные утро и вечер с регулярными занятиями, затем отдых. Режим помогает ей быть уравновешенной, а пустой день обычно превращается в шалости.",
        ],
    },
    "german-shepherd-dog": {
        "en": [
            "Around two hours a day, including a run and some training. It enjoys structured walks with tasks, such as retrieving, searching or practising commands. A shepherd that only gets a quick loop around the block usually finds its own entertainment.",
            "It does not do well alone for long. A bored shepherd may bark, dig or chew, and some become anxious when left. Build up time alone slowly and give it a routine to rely on.",
            "Calm and attentive indoors once exercised, and happiest in the same room as its family. It is a natural watchdog and will tell you about anything unusual, so expect it to be vocal at the door.",
            "Devoted and protective with its own children, and often a gentle companion. A big, strong dog still needs supervision around small kids, and visiting children should be introduced calmly.",
            "Often fine with other dogs when socialised. It may be reserved with strangers and can chase small animals, so early exposure to people, dogs and places matters a lot.",
            "Obedience, tracking, agility, herding and protection sports suit it. It learns quickly and wants a purpose, so a regular training routine keeps it content.",
            "Active mornings and evenings, with regular rest in between. It loves routine and being useful, and does best when it knows what comes next in the day.",
        ],
        "ru": [
            "Около двух часов в день, включая бег и занятия. Любит организованные прогулки с заданиями: апорт, поиск, отработка команд. Овчарка, которой достаётся только быстрый круг вокруг дома, обычно находит развлечения сама.",
            "Плохо переносит долгое одиночество. Заскучавшая овчарка может лаять, рыть или грызть вещи, а некоторые тревожатся, когда остаются одни. Приучайте к одиночеству медленно и дайте ей понятный распорядок.",
            "Дома спокойна и внимательна после нагрузки, больше всего любит быть в одной комнате с семьёй. Природный сторож: сообщит обо всём необычном, так что у двери она будет подавать голос.",
            "Предана и защищает своих детей, часто нежный компаньон. Большая сильная собака всё равно требует присмотра рядом с малышами, а приходящих детей лучше знакомить спокойно.",
            "С социализацией часто ладит с другими собаками. С чужими людьми бывает сдержанной и может гнаться за мелкими животными, поэтому раннее знакомство с людьми, собаками и местами очень важно.",
            "Ей подходят послушание, следовая работа, аджилити, пастушьи и защитные виды спорта. Быстро учится и хочет иметь цель, а регулярные занятия делают её довольной.",
            "Активные утро и вечер, между ними регулярный отдых. Любит режим и быть полезной, лучше всего себя чувствует, когда знает, что будет дальше в течение дня.",
        ],
    },
    "old-english-sheepdog": {
        "en": [
            "About an hour a day in total, with a free run when possible. It does not need sport, but it likes company on a walk and loves a romp in a field or a park. In summer, go out early or late, as the big coat makes heat hard work.",
            "It does not like being alone for long. Without people it may bark or chew, and its size means the damage is not small. It does best in a household where someone is usually around.",
            "Happy in the middle of the family, flopping down where you walk. It needs space for its size and coat, and it tends to leave water around the bowl and mud from its feet and beard.",
            "Gentle, patient and playful with children. It may bump into or lean on small kids, and may gently herd them, nudging them along. A big, clumsy dog needs room to play.",
            "Usually friendly with dogs and other pets. It can try to herd family members and other animals, but is rarely aggressive. Early introductions to cats and visitors make life easier.",
            "Enjoys walks, play, simple obedience and fetch. It does not need intense sport, but it does need regular activity and short training sessions. It is clever, with a sense of humour, and can get bored of repetition.",
            "A relaxed routine of walks, play and long stretches lying close to people. Heat is its enemy, so plan the day around cool hours and give it a cool place to rest.",
        ],
        "ru": [
            "Около часа в день в сумме, по возможности со свободным бегом. Спорт ей не нужен, но на прогулке нужна компания, и она любит порезвиться в поле или парке. Летом выходите рано или поздно: из-за большой шубы жара даётся ей тяжело.",
            "Не любит долго оставаться одна. Без людей может лаять или грызть вещи, а из-за размера ущерб будет немаленьким. Лучше всего чувствует себя в семье, где обычно кто-то дома.",
            "Счастлива в центре семьи и падает на пол там, где вы идёте. Ей нужно место из-за размера и шерсти, и вокруг миски обычно остаются вода, а на полу грязь с лап и бороды.",
            "Нежна, терпелива и игрива с детьми. Может толкнуть или навалиться на малыша и мягко пасти детей, подталкивая их. Большой неуклюжей собаке нужно место для игр.",
            "Обычно дружелюбна к собакам и другим животным. Может пытаться пасти членов семьи и других животных, но агрессивна редко. Ранее знакомство с кошками и гостями облегчает жизнь.",
            "Любит прогулки, игры, простое послушание и апорт. Интенсивный спорт не нужен, но нужны регулярная активность и короткие занятия. Умна, с чувством юмора, и от однообразия скучает.",
            "Спокойный ритм: прогулки, игры и долгие периоды рядом с людьми. Жара — её враг, поэтому планируйте день вокруг прохладных часов и дайте ей прохладное место для отдыха.",
        ],
    },
    "pembroke-welsh-corgi": {
        "en": [
            "About an hour a day, split into two or three walks. It has plenty of energy and likes to cover ground despite the short legs, and it enjoys exploring new places. Avoid asking for endless jumping or stair-climbing in its daily routine.",
            "It manages a few hours when used to it. Bored Corgis bark, dig or make their own games, and the voice is loud for the size. Leave it with a food puzzle and make sure it has had a proper walk before you go.",
            "It suits a flat as long as walks are regular. It likes to be wherever you are and tends to be talkative: barking at the door, at noises and sometimes at nothing in particular. Training a quiet command helps early.",
            "Friendly and playful with kids who treat it kindly. The herding habit of nipping at heels needs to be gently trained out, and children should learn not to chase or grab it.",
            "Usually gets on with dogs and cats it knows. It may try to herd them, and can bark at strangers or unfamiliar dogs. Early social experience helps it stay relaxed.",
            "Enjoys fetch, agility, herding games, simple tricks and food puzzles. Training works well with treats, but watch the quantity. It is clever and learns quickly, though it can be strong-willed.",
            "Active periods through the day with plenty of rest. It likes to stay close, from the kitchen to the sofa, and follows its family around. It knows exactly when mealtime is.",
        ],
        "ru": [
            "Около часа в день, разделённого на две–три прогулки. Энергии много, и несмотря на короткие лапы, она любит пройти путь и исследовать новые места. Не требуйте от неё в повседневной жизни бесконечных прыжков и подъёмов по лестнице.",
            "Несколько часов выдержит, когда привыкнет. Заскучавшие корги лают, роют или придумывают игры сами, а голос у них громкий для такого размера. Оставьте ей головоломку с лакомством и убедитесь, что до этого была настоящая прогулка.",
            "Подходит для квартиры при регулярных прогулках. Любит быть там, где вы, и обычно разговорчива: лает у двери, на шорохи и порой просто так. Команду «тихо» полезно отработать рано.",
            "Дружелюбна и игрива с детьми, которые относятся к ней добро. Пастушью привычку хватать за пятки нужно мягко отучать, а детей учить не гоняться за ней и не хватать её.",
            "Обычно ладит с собаками и кошками, которых знает. Может пытаться их пасти и лаять на чужих людей и незнакомых собак. Раннее знакомство с миром помогает ей оставаться спокойной.",
            "Любит апорт, аджилити, пастушьи игры, простые трюки и игрушки с лакомством. Дрессировка хорошо идёт на поощрении, но следите за количеством. Умна и быстро учится, хотя бывает упрямой.",
            "Активные периоды в течение дня с достаточным отдыхом. Любит быть рядом, от кухни до дивана, и ходит за семьёй. Точно знает, когда время кормления.",
        ],
    },
    "puli": {
        "en": [
            "About an hour and a half a day, with play and training. It bounces and spins and loves to run, and it loves a field or a big garden. Cords get wet and muddy, so plan for drying time after rainy walks.",
            "It is not happy alone for long. A bored Puli will bark, dig and look for something to herd, and the voice carries. It does best in a home where someone is around for most of the day.",
            "Alert indoors and quick to announce visitors and noises. It can live in a flat if walks are regular and the barking is trained, but it is an active, watchful dog that likes to know what is going on.",
            "Playful with older children who respect it. It may herd small kids, and its energy and bounce can be a lot for toddlers, so supervise and teach calm games.",
            "Usually fine with dogs it grew up with. It may try to herd other pets and can be wary of strangers, so socialise it with people and unfamiliar dogs from puppyhood.",
            "Enjoys agility, frisbee, herding games and trick training. It learns fast and needs variety, because repetition bores it. Short, lively sessions work better than long drills.",
            "Active, busy days with rest breaks. It wants to take part in whatever happens in the house and tends to follow its family from room to room. A tired Puli is a quiet Puli.",
        ],
        "ru": [
            "Около полутора часов в день, с играми и занятиями. Подпрыгивает, вертится и любит бегать, ей по душе поле или большой участок. Шнуры намокают и пачкаются, поэтому после дождливых прогулок закладывайте время на просушку.",
            "Долго одной быть не любит. Заскучавшая пули лает, роет и ищет, кого бы попасти, а голос у неё далеко слышен. Лучше всего ей в доме, где большую часть дня кто-то есть.",
            "Дома бдительна и быстро объявляет о гостях и шумах. В квартире жить может, если прогулки регулярны, а лай приучен, но это активная внимательная собака, которой нужно знать, что происходит.",
            "Игрива со старшими детьми, которые её уважают. Может пасти малышей, а её энергии и подскоков совсем маленьким детям бывает много, поэтому присматривайте и учите спокойным играм.",
            "Обычно ладит с собаками, с которыми выросла. Может пытаться пасти других питомцев и настороженно относиться к чужим, поэтому с щенячьего возраста знакомьте её с людьми и незнакомыми собаками.",
            "Любит аджилити, фрисби, пастушьи игры и трюки. Быстро учится и нуждается в разнообразии: однообразие её утомляет. Короткие живые занятия работают лучше долгих отработок.",
            "Активные насыщенные дни с перерывами на отдых. Хочет участвовать во всём, что происходит в доме, и ходит за семьёй из комнаты в комнату. Уставшая пули — тихая пули.",
        ],
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, data in DAILY.items():
        values = {}
        for lang in ("en", "ru"):
            text = "\n\n".join(f"{l}: {t}" for l, t in zip(LABELS[lang], data[lang]))
            values[f"daily_life_{lang}"] = text
            if lang == "en":
                values["daily_life"] = text
        Dogs.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0062_herding_breeds_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
