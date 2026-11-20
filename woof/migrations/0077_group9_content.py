from django.db import migrations

from woof.migrations._content import apply_content

DOGS = {
    "bichon-frise": {
        "prey": "low",
        "en": {
            "summary": "Cheerful, playful and affectionate. The Bichon Frise is a small white powder-puff of a dog that loves people, loves attention and brings energy to the home.",
            "care": [
                "The curly white coat sheds little but mats easily: brush it several times a week and groom it every four to six weeks. Wipe the tear stains daily.",
                "Plan for about 45 minutes of walks and play a day.",
            ],
            "good_fit": [
                "Want a cheerful, social small dog",
                "Do not mind regular grooming",
                "Are home often",
                "Like a dog that sheds little",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Do not want regular grooming costs",
                "Want a dog that is quiet alone",
                "Have very young children who may handle it roughly",
            ],
            "daily": [
                "About 45 minutes a day, split into two walks, with lively play. It enjoys short bursts of racing around.",
                "It dislikes being left alone for long and can bark or fret. Short, gradual absences from puppyhood help.",
                "A playful, affectionate lap dog that follows the family. House-training can take patience.",
                "Friendly and playful with gentle children. Small kids should be taught how to hold and play with it.",
                "Usually sociable with dogs, cats and other pets.",
                "Short walks, tricks, games and agility. It enjoys performing for praise and treats.",
                "Two walks, play and plenty of company, with naps between. Regular grooming sessions are part of the week.",
            ],
            "quirks": [
                'The Bichon has a habit of racing around the room in short, excited sprints, often called the "Bichon blast".',
                "The coat sheds little, but it needs brushing and trimming to stay free of mats.",
                "White fur under the eyes stains easily, so a daily wipe keeps the face clean.",
            ],
        },
        "ru": {
            "summary": "Весёлый, игривый и ласковый. Бишон-фризе — небольшой белоснежный пушистый комочек, который любит людей и внимание и приносит в дом энергию.",
            "care": [
                "Кудрявая белая шерсть мало линяет, но легко сваливается: расчёсывайте несколько раз в неделю и стригите каждые четыре–шесть недель. Каждый день протирайте дорожки от слёз.",
                "Рассчитывайте примерно на 45 минут прогулок и игр в день.",
            ],
            "good_fit": [
                "Хотите весёлую общительную маленькую собаку",
                "Не против регулярного ухода за шерстью",
                "Часто бываете дома",
                "Хотите собаку, которая мало линяет",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Не хотите тратить деньги на груминг",
                "Хотите собаку, которая спокойно остаётся одна",
                "Есть совсем маленькие дети, которые могут грубо обращаться с собакой",
            ],
            "daily": [
                "Около 45 минут в день в две прогулки, с активными играми. Любит короткие забеги.",
                "Долго оставаться одна не любит, может лаять и тревожиться. Помогают короткие постепенные отлучки с щенячьего возраста.",
                "Игривая ласковая комнатная собака, ходит за семьёй. Приучение к туалету может потребовать терпения.",
                "Дружелюбна и игрива с бережными детьми. Малышам нужно объяснить, как её брать и играть с ней.",
                "Обычно общительна с собаками, кошками и другими питомцами.",
                "Короткие прогулки, трюки, игры и аджилити. Ей нравится выступать за похвалу и лакомства.",
                "Две прогулки, игры и много компании, между ними сон. Регулярный груминг входит в неделю.",
            ],
            "quirks": [
                "Бишон любит носиться по комнате короткими восторженными забегами, их часто называют «взрывом бишона».",
                "Шерсть мало линяет, но её нужно расчёсывать и подстригать, чтобы не было колтунов.",
                "Белая шерсть под глазами легко пачкается, поэтому ежедневное протирание сохраняет мордочку чистой.",
            ],
        },
    },
    "bolognese": {
        "prey": "low",
        "en": {
            "summary": "Calm, affectionate and devoted. The Bolognese is a small white companion that loves to be close to its person and is happiest in the middle of family life.",
            "care": [
                "The fluffy white coat sheds little and needs brushing three or four times a week to avoid mats, plus a trim every few months. Wipe the face and eyes daily.",
                "Plan for about 40 minutes of walks and play a day.",
            ],
            "good_fit": [
                "Want a gentle, calm lap companion",
                "Are home often",
                "Do not mind regular brushing",
                "Prefer a small dog that sheds little",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a very active dog for sports",
                "Have rough young children",
                "Dislike grooming",
            ],
            "daily": [
                "About 40 minutes a day in two short walks, plus gentle play indoors. It enjoys exploring on a lead.",
                "It bonds closely and dislikes being left alone for long. Practise short absences early.",
                "Quiet, gentle and happy to sit on a lap or sofa. It is a devoted shadow.",
                "Gentle with calm children. Small kids should be taught to hold it carefully.",
                "Generally friendly with dogs and cats.",
                "Short walks, simple tricks and indoor games. It learns well with praise and treats.",
                "Two short walks, company and long naps. A regular brushing time is helpful.",
            ],
            "quirks": [
                "The Bolognese is always white, with a fluffy single-layer coat that doesn't have a dense undercoat.",
                "It is a calm, quiet small dog that tends to bark less than many companion breeds.",
                "It forms a very close bond and follows its person from room to room.",
            ],
        },
        "ru": {
            "summary": "Спокойная, ласковая и преданная собака. Болонка — небольшой белоснежный компаньон, который любит быть рядом с хозяином и счастлив в центре семейной жизни.",
            "care": [
                "Пушистая белая шерсть мало линяет и требует расчёски три–четыре раза в неделю, чтобы не было колтунов, и стрижки раз в несколько месяцев. Каждый день протирайте мордочку и глаза.",
                "Рассчитывайте примерно на 40 минут прогулок и игр в день.",
            ],
            "good_fit": [
                "Хотите мягкого спокойного компаньона для коленей",
                "Часто бываете дома",
                "Не против регулярной расчёски",
                "Предпочитаете маленькую собаку, которая мало линяет",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите очень активную собаку для спорта",
                "Есть шумные маленькие дети",
                "Не любите заниматься шерстью",
            ],
            "daily": [
                "Около 40 минут в день в две короткие прогулки и мягкие игры дома. Любит исследовать на поводке.",
                "Она тесно привязана и не любит долго оставаться одна. Приучайте к коротким отлучкам рано.",
                "Тихая, мягкая, любит сидеть на коленях или диване. Преданная тень хозяина.",
                "Мягка со спокойными детьми. Малышей нужно научить бережно её держать.",
                "Обычно дружелюбна с собаками и кошками.",
                "Короткие прогулки, простые трюки и игры дома. Она хорошо учится на похвале и лакомствах.",
                "Две короткие прогулки, компания и долгий сон. Удобно выделить постоянное время для расчёски.",
            ],
            "quirks": [
                "Болонка всегда белая, с пушистой шерстью без плотного подшёрстка.",
                "Это спокойная тихая маленькая собака, которая обычно лает меньше многих комнатных пород.",
                "Она очень крепко привязывается и ходит за хозяином из комнаты в комнату.",
            ],
        },
    },
    "brussels-griffon": {
        "prey": "low",
        "en": {
            "summary": "Expressive, affectionate and full of character. The Brussels Griffon is a small, human-faced companion that bonds closely with its person and has a big personality.",
            "care": [
                "The rough coat needs brushing weekly and hand-stripping a few times a year, while the smooth coat needs a weekly brush. Wipe the face and eyes daily.",
                "Plan for about 40 minutes of walks and play a day. It has a flat face, so avoid hot weather and use a harness.",
            ],
            "good_fit": [
                "Want a small, devoted, expressive companion",
                "Are home often",
                "Enjoy training with gentle methods",
                "Live in a flat or small home",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Have rough young children",
                "Live in a hot climate without cooling",
                "Want a quiet, undemanding dog",
            ],
            "daily": [
                "About 40 minutes a day, in short walks at cool times of day. Use a harness and stop if breathing becomes noisy or laboured.",
                "It bonds closely to its person and dislikes being left alone. It can become anxious and noisy without company.",
                "Lively and affectionate at home, following the family and wanting attention. It likes a warm spot on the sofa.",
                "Best with calm, considerate older children. It is small and sensitive, so young kids need guidance.",
                "Often bold with other dogs and gets on with cats it knows.",
                "Short walks, tricks and games. It is sensitive, so train with praise and rewards.",
                "Short walks, lots of company and naps between. Avoid heat.",
            ],
            "quirks": [
                "The Brussels Griffon's expressive face, with a short nose and big eyes, is often described as almost human.",
                "It is a flat-faced breed, so it overheats easily, and walks should stay short in warm weather.",
                "It comes in rough and smooth coats, and the rough coat is usually tidied by hand-stripping.",
            ],
        },
        "ru": {
            "summary": "Выразительный, ласковый и с ярким характером. Брюссельский гриффон — небольшой компаньон с почти человеческим выражением мордочки, который тесно привязывается к хозяину и обладает сильной личностью.",
            "care": [
                "Жёсткую шерсть расчёсывайте раз в неделю и несколько раз в год тримминговать, гладкую расчёсывайте раз в неделю. Каждый день протирайте мордочку и глаза.",
                "Рассчитывайте примерно на 40 минут прогулок и игр в день. Мордочка плоская, поэтому избегайте жары и используйте шлейку.",
            ],
            "good_fit": [
                "Хотите маленького преданного выразительного компаньона",
                "Часто бываете дома",
                "Любите мягкие методы дрессировки",
                "Живёте в квартире или небольшом доме",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Есть шумные маленькие дети",
                "Живёте в жарком климате без охлаждения",
                "Хотите тихую нетребовательную собаку",
            ],
            "daily": [
                "Около 40 минут в день короткими прогулками в прохладное время суток. Используйте шлейку и остановитесь, если дыхание стало шумным или тяжёлым.",
                "Она тесно привязана к хозяину и не любит оставаться одна. Без компании может тревожиться и шуметь.",
                "Дома живая и ласковая, ходит за семьёй и требует внимания. Любит тёплое место на диване.",
                "Лучше всего с спокойными внимательными детьми постарше. Она маленькая и чувствительная, поэтому малышам нужны подсказки.",
                "Часто смела с другими собаками и ладит со знакомыми кошками.",
                "Короткие прогулки, трюки и игры. Она чувствительна, поэтому дрессируйте с похвалой и поощрением.",
                "Короткие прогулки, много компании и сон между ними. Избегайте жары.",
            ],
            "quirks": [
                "Выразительную мордочку гриффона с коротким носом и большими глазами часто называют почти человеческой.",
                "Порода плосконосая, поэтому легко перегревается, и в тёплую погоду прогулки должны быть короткими.",
                "Бывает жёсткошёрстным и гладкошёрстным, жёсткую шерсть обычно приводят в порядок тримингом.",
            ],
        },
    },
    "cavalier-king-charles-spaniel": {
        "prey": "moderate",
        "en": {
            "summary": "Gentle, loving and eager to please. The Cavalier King Charles Spaniel is a sweet-natured companion that gets on with almost everyone and loves to be close.",
            "care": [
                "The silky coat needs brushing three or four times a week, and the long ears should be checked and cleaned weekly. Watch the weight.",
                "Plan for about an hour of walks and play a day. Heart checks by the vet are important from middle age.",
            ],
            "good_fit": [
                "Want a gentle, sociable family dog",
                "Are home often",
                "Enjoy walks and cuddles",
                "Do not mind regular brushing",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Are not ready for possible heart and health costs",
                "Want a guard dog",
                "Want a dog that needs little contact",
            ],
            "daily": [
                "About an hour a day with gentle walks and games. It enjoys running and sniffing, but needs a lead near roads, as a bird or bunny may tempt it.",
                "It needs company and can become anxious when left alone for long.",
                "A loving lap dog that wants to be on the sofa or in the bed. It follows the family from room to room.",
                "Gentle, patient and friendly with children. A good family dog when handled kindly.",
                "Typically friendly with dogs, cats and visitors.",
                "Walks, fetch, trick training and scent games. It is eager to please and learns with praise.",
                "Two walks, play and plenty of company with naps between.",
            ],
            "quirks": [
                "Cavaliers are prone to a leaking heart valve, so have the vet listen to the heart at every check-up, as a murmur is often the first sign.",
                "Its silky, feathered ears act like a magnet for food and water, so a quick wipe after meals helps.",
                'It is known as a "comforter" breed and has a talent for snuggling up to anyone who needs it.',
            ],
        },
        "ru": {
            "summary": "Мягкий, любящий и старательный. Кавалер-кинг-чарльз-спаниель — ласковый компаньон, который ладит почти со всеми и любит быть рядом.",
            "care": [
                "Шелковистую шерсть расчёсывайте три–четыре раза в неделю, а длинные уши проверяйте и чистите раз в неделю. Следите за весом.",
                "Рассчитывайте примерно на час прогулок и игр в день. С среднего возраста важна проверка сердца у ветеринара.",
            ],
            "good_fit": [
                "Хотите мягкую общительную семейную собаку",
                "Часто бываете дома",
                "Любите прогулки и обнимашки",
                "Не против регулярной расчёски",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Не готовы к возможным расходам на сердце и здоровье",
                "Хотите охранника",
                "Хотите собаку, которой нужно мало общения",
            ],
            "daily": [
                "Около часа в день спокойных прогулок и игр. Любит бегать и нюхать, но рядом с дорогами нужен поводок: птица или кролик могут её увлечь.",
                "Ей нужна компания, при долгом одиночестве она может тревожиться.",
                "Ласковая комнатная собака, хочет быть на диване или в кровати. Ходит за семьёй из комнаты в комнату.",
                "Мягкая, терпеливая и дружелюбная с детьми. Хорошая семейная собака при добром обращении.",
                "Обычно дружелюбна с собаками, кошками и гостями.",
                "Прогулки, апорт, трюки и игры на поиск. Она старательна и учится на похвале.",
                "Две прогулки, игры и много компании со сном между ними.",
            ],
            "quirks": [
                "Кавалеры склонны к недостаточности сердечного клапана, поэтому просите ветеринара слушать сердце на каждом осмотре: шум часто бывает первым признаком.",
                "Шелковистые ушки притягивают еду и воду, как магнит, поэтому после еды их полезно протирать.",
                "Породу называют «компаньоном-утешителем»: она умеет прижаться к каждому, кому это нужно.",
            ],
        },
    },
    "chihuahua": {
        "prey": "low",
        "en": {
            "summary": "Bold, loyal and quick. The Chihuahua is the smallest breed in the world, with a big personality that bonds closely to one person and watches over its home.",
            "care": [
                "Short-coated dogs need a weekly brush and long-coated ones three times a week. Brush the teeth daily, as small dogs have many dental problems.",
                "Plan for about 30 to 40 minutes of walks and play a day. It feels the cold, so give it a coat in winter.",
            ],
            "good_fit": [
                "Want a tiny, devoted companion",
                "Are home often",
                "Can handle a small dog gently",
                "Live in a flat or small home",
            ],
            "think_twice": [
                "Have young children who may handle it roughly",
                "Are away from home most of the day",
                "Want a dog that welcomes every stranger",
                "Do not want to do daily dental care",
            ],
            "daily": [
                "About 30 to 40 minutes a day in short walks, plus indoor play. It needs a coat or sweater in cold weather.",
                "It bonds closely and dislikes long hours alone. Teach short absences gradually.",
                "Alert and affectionate at home, often choosing one favourite person. It loves warm blankets and laps.",
                "Best with calm, careful older children. It is tiny and fragile, so young kids must be taught to hold it safely.",
                "Often bold with big dogs, so keep it from picking fights. It can get on with cats and pets it knows.",
                "Short walks, tricks and indoor games. Training works with short sessions and treats.",
                "Short walks, naps and warm cuddles, with a regular routine.",
            ],
            "quirks": [
                "Chihuahuas love warmth and often burrow under blankets and cushions to keep cosy.",
                "The skull of some puppies has a soft spot, called a molera, so handle a young Chihuahua gently.",
                "Small dogs have crowded teeth, so brushing every day helps avoid dental problems.",
            ],
        },
        "ru": {
            "summary": "Смелая, преданная и проворная собака. Чихуахуа — самая маленькая порода в мире с большим характером, которая тесно привязывается к одному человеку и охраняет свой дом.",
            "care": [
                "Короткошёрстных расчёсывайте раз в неделю, длинношёрстных — три раза в неделю. Чистите зубы каждый день: у мелких собак много проблем с зубами.",
                "Рассчитывайте примерно на 30–40 минут прогулок и игр в день. Она мёрзнет, поэтому зимой надевайте одежду.",
            ],
            "good_fit": [
                "Хотите крошечного преданного компаньона",
                "Часто бываете дома",
                "Умеете бережно обращаться с маленькой собакой",
                "Живёте в квартире или небольшом доме",
            ],
            "think_twice": [
                "Есть маленькие дети, которые могут грубо обращаться с собакой",
                "Большую часть дня не бываете дома",
                "Хотите собаку, которая рада каждому чужому",
                "Не хотите ежедневно ухаживать за зубами",
            ],
            "daily": [
                "Около 30–40 минут в день короткими прогулками и игры дома. В холод нужны одежда или свитер.",
                "Она тесно привязана и не любит долго оставаться одна. Приучайте к отлучкам постепенно.",
                "Дома внимательна и ласкова, часто выбирает одного любимого человека. Любит тёплые одеяла и колени.",
                "Лучше всего с спокойными внимательными детьми постарше. Она крошечная и хрупкая, поэтому малышей нужно учить безопасно её держать.",
                "Часто смела с крупными собаками, поэтому не позволяйте ей лезть в драку. Может ладить с кошками и знакомыми питомцами.",
                "Короткие прогулки, трюки и игры дома. Дрессировка идёт на коротких занятиях с лакомствами.",
                "Короткие прогулки, сон и тёплые объятия, с постоянным распорядком.",
            ],
            "quirks": [
                "Чихуахуа любят тепло и часто зарываются в одеяла и подушки.",
                "У некоторых щенков на черепе есть мягкое место — молера, поэтому молодого чихуахуа держите бережно.",
                "У мелких собак зубы стоят тесно, поэтому ежедневная чистка помогает избежать проблем.",
            ],
        },
    },
    "french-bulldog": {
        "prey": "low",
        "en": {
            "summary": "Playful, affectionate and easygoing. The French Bulldog is a compact, flat-faced companion that loves people and is happy in a flat with short, relaxed walks.",
            "care": [
                "The short coat needs a weekly brush. Clean the face folds daily and dry them well, and check the ears.",
                "Plan for about 40 minutes of gentle walks and play a day. It overheats easily, so keep exercise short in hot weather.",
            ],
            "good_fit": [
                "Want a small, friendly flat companion",
                "Are home often",
                "Prefer short, relaxed walks",
                "Can keep it cool and manage its weight",
            ],
            "think_twice": [
                "Live in a hot climate without cooling",
                "Want a dog for running or hiking",
                "Are not ready for possible vet costs for breathing and skin",
                "Are away from home most of the day",
            ],
            "daily": [
                "About 40 minutes a day in short, easy walks at cool times. Use a harness, not a collar, and stop if its breathing becomes noisy or laboured.",
                "It bonds closely and dislikes long hours alone. It may whine or chew without company.",
                "A cheerful, calm indoor companion that loves the sofa and company. It snores and snuffles.",
                "Playful, patient and sturdy with children. Supervise play with small kids.",
                "Usually friendly with dogs and cats, though some are bossy.",
                "Short walks, indoor games and gentle tricks. It is easily distracted, so keep training short and fun.",
                "Short walks, plenty of company and naps. Keep the home cool in summer.",
            ],
            "quirks": [
                "As a flat-faced breed, the French Bulldog overheats easily, so walks in hot weather should be early or late, with shade and water.",
                'Its upright "bat ears" are one of the breed\'s best-known features and move with its mood.',
                "It snores, snuffles and snorts, which most owners find endearing.",
            ],
        },
        "ru": {
            "summary": "Игривый, ласковый и добродушный компаньон. Французский бульдог — компактная плосконосая собака, которая любит людей и счастлива в квартире с короткими спокойными прогулками.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Каждый день чистите и хорошо просушивайте складки на морде, проверяйте уши.",
                "Рассчитывайте примерно на 40 минут спокойных прогулок и игр в день. Бульдог легко перегревается, поэтому в жару нагрузка должна быть короткой.",
            ],
            "good_fit": [
                "Хотите маленького дружелюбного компаньона для квартиры",
                "Часто бываете дома",
                "Предпочитаете короткие неспешные прогулки",
                "Сможете следить за прохладой и весом",
            ],
            "think_twice": [
                "Живёте в жарком климате без охлаждения",
                "Хотите собаку для бега или походов",
                "Не готовы к возможным расходам на лечение дыхания и кожи",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Около 40 минут в день короткими лёгкими прогулками в прохладное время. Используйте шлейку, а не ошейник, и остановитесь, если дыхание стало шумным или тяжёлым.",
                "Он тесно привязан и не любит долго оставаться один. Без компании может скулить и грызть вещи.",
                "Весёлый спокойный домашний компаньон, любит диван и общество. Сопит и храпит.",
                "Игрив, терпелив и вынослив с детьми. За играми с малышами присматривайте.",
                "Обычно дружелюбен с собаками и кошками, хотя некоторые любят командовать.",
                "Короткие прогулки, игры дома и мягкие трюки. Он легко отвлекается, поэтому занятия делайте короткими и весёлыми.",
                "Короткие прогулки, много компании и сон. Летом держите в доме прохладу.",
            ],
            "quirks": [
                "Французский бульдог плосконосый и легко перегревается, поэтому в жару гуляйте рано утром или поздно вечером, с тенью и водой.",
                "Стоячие «летучие» уши — одна из самых известных примет породы, они двигаются вместе с настроением.",
                "Он храпит, сопит и фыркает, что большинству хозяев кажется трогательным.",
            ],
        },
    },
    "pekingese": {
        "prey": "low",
        "en": {
            "summary": "Dignified, loyal and independent. The Pekingese is a small, lion-like companion with a calm, proud nature that is devoted to its own family.",
            "care": [
                "The long double coat needs brushing three or four times a week, with attention to the feathering, and the face folds need wiping daily. Check the eyes.",
                "Plan for about 30 minutes of gentle walks a day. It overheats easily, so keep it cool.",
            ],
            "good_fit": [
                "Want a calm, devoted small companion",
                "Are home often",
                "Do not mind regular grooming",
                "Prefer a dog with a quiet routine",
            ],
            "think_twice": [
                "Have young children who may handle it roughly",
                "Live in a hot climate without cooling",
                "Want an active sports dog",
                "Are away from home most of the day",
            ],
            "daily": [
                "About 30 minutes a day in short, slow walks at cool times. Use a harness and avoid heat.",
                "It likes to be near its people but tolerates short periods alone better than many toy breeds.",
                "Calm, dignified and affectionate at home, often choosing a favourite spot on the sofa.",
                "Best with calm, careful older children. It does not like rough handling.",
                "Usually fine with other pets it knows, but may be bossy.",
                "Gentle walks and quiet games. It is independent, so keep training short and rewarding.",
                "Short walks and plenty of calm rest. Daily face care is part of the routine.",
            ],
            "quirks": [
                "The Pekingese is one of the most flat-faced breeds, so keep walks short and cool and watch its breathing.",
                "The mane-like coat gives it a lion look, and it needs regular brushing to stay free of mats.",
                "It has a calm and dignified manner, and many Pekingese like to choose their favourite spot in the home.",
            ],
        },
        "ru": {
            "summary": "Достойная, преданная и самостоятельная собака. Пекинес — небольшой компаньон, похожий на льва, со спокойным гордым характером, преданный своей семье.",
            "care": [
                "Длинную шерсть с подшёрстком расчёсывайте три–четыре раза в неделю, особенно оперение, а складки на морде протирайте каждый день. Проверяйте глаза.",
                "Рассчитывайте примерно на 30 минут спокойных прогулок в день. Пекинес легко перегревается, поэтому держите его в прохладе.",
            ],
            "good_fit": [
                "Хотите спокойного преданного небольшого компаньона",
                "Часто бываете дома",
                "Не против регулярного ухода за шерстью",
                "Предпочитаете собаку со спокойным распорядком",
            ],
            "think_twice": [
                "Есть маленькие дети, которые могут грубо обращаться с собакой",
                "Живёте в жарком климате без охлаждения",
                "Хотите активную собаку для спорта",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Около 30 минут в день короткими неспешными прогулками в прохладное время. Используйте шлейку и избегайте жары.",
                "Он любит быть рядом с людьми, но коротких отлучек переносит лучше многих комнатных пород.",
                "Дома спокойный, достойный и ласковый, часто выбирает любимое место на диване.",
                "Лучше всего с спокойными внимательными детьми постарше. Грубого обращения он не любит.",
                "Обычно ладит со знакомыми питомцами, но может командовать.",
                "Неспешные прогулки и тихие игры. Он самостоятелен, поэтому занятия делайте короткими и с поощрением.",
                "Короткие прогулки и много спокойного отдыха. Ежедневный уход за мордой входит в распорядок.",
            ],
            "quirks": [
                "Пекинес — одна из самых плосконосых пород, поэтому гуляйте коротко и в прохладе и следите за дыханием.",
                "Шерсть, похожая на гриву, придаёт ему сходство со львом и требует регулярной расчёски, чтобы не было колтунов.",
                "У него спокойные достойные манеры, и многие пекинесы выбирают любимое место в доме.",
            ],
        },
    },
    "poodle": {
        "prey": "low",
        "en": {
            "summary": "Clever, graceful and eager to learn. The Poodle is a highly trainable, active dog that comes in four sizes and adapts to nearly any family that gives it attention and activity.",
            "care": [
                "The curly coat sheds very little but needs brushing several times a week and a trim every four to eight weeks. Clean the ears and the tear stains.",
                "Plan for one to two hours of walks, games and training a day, depending on size.",
            ],
            "good_fit": [
                "Enjoy training and teaching tricks",
                "Want a clever dog that sheds little",
                "Do not mind regular grooming",
                "Are active and home often",
            ],
            "think_twice": [
                "Dislike grooming costs",
                "Are away from home most of the day",
                "Want a low-effort dog",
                "Cannot give daily mental stimulation",
            ],
            "daily": [
                "One to two hours a day depending on size. Standard Poodles enjoy running and swimming, and smaller ones are happy with shorter walks and play.",
                "It bonds closely and dislikes long hours alone. Bored, it may bark or invent its own games.",
                "Affectionate and clever indoors, happy to stay close to the family. Its coat sheds little.",
                "Playful and good-natured with children. Smaller sizes are better with calm, careful kids.",
                "Usually friendly with dogs and pets, especially when socialised early.",
                "Tricks, agility, obedience, swimming and scent games. It learns fast and loves a challenge.",
                "Active morning and evening with training and games between.",
            ],
            "quirks": [
                "Poodles come in four sizes: Standard, Medium, Miniature and Toy, all with the same curly coat and clever mind.",
                "The curly coat sheds very little, so loose hair stays in the coat until it is brushed, and mats form if brushing is skipped.",
                "Many Poodles love water and are strong swimmers.",
            ],
        },
        "ru": {
            "summary": "Умная, грациозная и любознательная собака. Пудель — очень обучаемая активная порода четырёх размеров, которая подходит почти любой семье, готовой дать ей внимание и нагрузку.",
            "care": [
                "Кудрявая шерсть почти не линяет, но её нужно расчёсывать несколько раз в неделю и стричь раз в четыре–восемь недель. Чистите уши и убирайте дорожки от слёз.",
                "Рассчитывайте на один–два часа прогулок, игр и занятий в день в зависимости от размера.",
            ],
            "good_fit": [
                "Любите дрессировку и обучение трюкам",
                "Хотите умную собаку, которая мало линяет",
                "Не против регулярного груминга",
                "Активны и часто бываете дома",
            ],
            "think_twice": [
                "Не хотите тратить на груминг",
                "Большую часть дня не бываете дома",
                "Хотите собаку без особых усилий",
                "Не можете ежедневно давать умственные нагрузки",
            ],
            "daily": [
                "Один–два часа в день в зависимости от размера. Большие пудели любят бегать и плавать, а маленьким хватает коротких прогулок и игр.",
                "Он тесно привязан и не любит долгого одиночества. От скуки может лаять и придумывать свои игры.",
                "Дома ласковый и сообразительный, охотно остаётся рядом с семьёй. Шерсть почти не линяет.",
                "Игрив и добродушен с детьми. Маленькие размеры лучше подходят спокойным внимательным детям.",
                "Обычно дружелюбен с собаками и питомцами, особенно при ранней социализации.",
                "Трюки, аджилити, послушание, плавание и игры на поиск. Он быстро учится и любит задачи.",
                "Активные утро и вечер, между ними занятия и игры.",
            ],
            "quirks": [
                "Пудели бывают четырёх размеров: большой, средний, миниатюрный и той, и у всех одна кудрявая шерсть и острый ум.",
                "Кудрявая шерсть почти не линяет: выпавшие волоски остаются в ней до расчёски, а без расчёсывания появляются колтуны.",
                "Многие пудели любят воду и отлично плавают.",
            ],
        },
    },
    "pug": {
        "prey": "low",
        "en": {
            "summary": "Charming, affectionate and easygoing. The Pug is a small, flat-faced companion with a big personality that loves company and a comfortable place to rest.",
            "care": [
                "The short coat sheds a lot and needs brushing a few times a week. Clean the face wrinkles daily and dry them well.",
                "Plan for about 30 to 40 minutes of gentle walks a day. Watch the weight closely, since Pugs gain weight easily and their breathing suffers.",
            ],
            "good_fit": [
                "Want a small, sociable and affectionate companion",
                "Are home often",
                "Prefer short relaxed walks",
                "Do not mind snoring and shedding",
            ],
            "think_twice": [
                "Live in a hot climate without cooling",
                "Want a dog for running or hiking",
                "Are not ready for possible vet costs for breathing and skin",
                "Are away from home most of the day",
            ],
            "daily": [
                "About 30 to 40 minutes a day in short, easy walks at cool times. Use a harness, and stop if its breathing becomes noisy or laboured.",
                "It bonds closely and dislikes long hours alone. It may whine or chew without company.",
                "A cheerful, affectionate companion that loves lap time and the sofa. It snores, snorts and snuffles.",
                "Playful, patient and sturdy with children. Supervise play with small kids.",
                "Usually friendly with dogs, cats and visitors.",
                "Short walks, indoor games and gentle tricks. Food rewards work well, but keep an eye on calories.",
                "Short walks, lots of company and long naps. Keep the home cool in summer.",
            ],
            "quirks": [
                "Pugs have trouble cooling down in hot weather, so walks should be early or late, with shade and water.",
                "They love food and gain weight easily, which makes breathing harder, so measure meals.",
                "The wrinkled face and curled tail are the breed's trademarks, and the wrinkles need a daily wipe.",
            ],
        },
        "ru": {
            "summary": "Обаятельный, ласковый и добродушный компаньон. Мопс — небольшая плосконосая собака с большим характером, которая любит компанию и удобное место для отдыха.",
            "care": [
                "Короткая шерсть сильно линяет, расчёсывайте несколько раз в неделю. Каждый день чистите и просушивайте складки на морде.",
                "Рассчитывайте примерно на 30–40 минут спокойных прогулок в день. Следите за весом: мопсы легко полнеют, и от этого ухудшается дыхание.",
            ],
            "good_fit": [
                "Хотите небольшого общительного ласкового компаньона",
                "Часто бываете дома",
                "Предпочитаете короткие неспешные прогулки",
                "Не против храпа и шерсти",
            ],
            "think_twice": [
                "Живёте в жарком климате без охлаждения",
                "Хотите собаку для бега или походов",
                "Не готовы к возможным расходам на лечение дыхания и кожи",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Около 30–40 минут в день короткими лёгкими прогулками в прохладное время. Используйте шлейку и остановитесь, если дыхание стало шумным или тяжёлым.",
                "Он тесно привязан и не любит долго оставаться один. Без компании может скулить и грызть вещи.",
                "Весёлый ласковый компаньон, любит колени и диван. Храпит, фыркает и сопит.",
                "Игрив, терпелив и вынослив с детьми. За играми с малышами присматривайте.",
                "Обычно дружелюбен с собаками, кошками и гостями.",
                "Короткие прогулки, игры дома и мягкие трюки. Лакомства работают хорошо, но следите за калориями.",
                "Короткие прогулки, много компании и долгий сон. Летом держите дом прохладным.",
            ],
            "quirks": [
                "Мопсам трудно остывать в жару, поэтому гуляйте рано утром или поздно вечером, с тенью и водой.",
                "Они любят поесть и легко набирают вес, от чего дыхание становится тяжелее, поэтому отмеряйте порции.",
                "Морщинистая мордочка и закрученный хвост — визитные карточки породы, а морщинки нужно протирать каждый день.",
            ],
        },
    },
    "shih-tzu": {
        "prey": "low",
        "en": {
            "summary": "Friendly, affectionate and outgoing. The Shih Tzu is a small, long-coated companion that loves people, loves company and is happy in a flat or house.",
            "care": [
                "The long silky coat needs daily brushing or a short puppy clip every six to eight weeks. Wipe the face and eyes daily, and clean the ears.",
                "Plan for about 40 minutes of gentle walks and play a day, avoiding heat.",
            ],
            "good_fit": [
                "Want a small, friendly, sociable companion",
                "Are home often",
                "Do not mind daily brushing or a short clip",
                "Live in a flat or small home",
            ],
            "think_twice": [
                "Dislike grooming or grooming costs",
                "Are away from home most of the day",
                "Live in a hot climate without cooling",
                "Want a sporty dog",
            ],
            "daily": [
                "About 40 minutes a day in short, gentle walks at cool times. Use a harness and avoid heat.",
                "It bonds closely and dislikes being left alone for long. Practise short absences.",
                "A cheerful, affectionate companion that wants to be on the sofa or lap. Quiet, with a gentle bark for visitors.",
                "Friendly and playful with gentle children. Small kids must be taught to hold it carefully.",
                "Usually friendly with dogs, cats and other pets.",
                "Short walks, games and simple tricks. Training works with patience, praise and treats.",
                "Short walks, plenty of company and naps. Regular brushing is part of the routine.",
            ],
            "quirks": [
                "The Shih Tzu is a flat-faced breed that can overheat, so shorten walks in warm weather.",
                'Many owners choose a short "puppy clip" because the long coat needs daily brushing.',
                "It is a friendly dog that tends to greet everyone as a friend.",
            ],
        },
        "ru": {
            "summary": "Дружелюбный, ласковый и общительный компаньон. Ши-тцу — небольшая длинношёрстная собака, которая любит людей и компанию и счастлива и в квартире, и в доме.",
            "care": [
                "Длинную шелковистую шерсть расчёсывайте каждый день или делайте короткую «щенячью» стрижку раз в шесть–восемь недель. Каждый день протирайте мордочку и глаза, чистите уши.",
                "Рассчитывайте примерно на 40 минут спокойных прогулок и игр в день, избегая жары.",
            ],
            "good_fit": [
                "Хотите небольшого дружелюбного общительного компаньона",
                "Часто бываете дома",
                "Не против ежедневной расчёски или короткой стрижки",
                "Живёте в квартире или небольшом доме",
            ],
            "think_twice": [
                "Не любите уход за шерстью или расходы на груминг",
                "Большую часть дня не бываете дома",
                "Живёте в жарком климате без охлаждения",
                "Хотите спортивную собаку",
            ],
            "daily": [
                "Около 40 минут в день короткими спокойными прогулками в прохладное время. Используйте шлейку и избегайте жары.",
                "Он тесно привязан и не любит надолго оставаться один. Приучайте к коротким отлучкам.",
                "Весёлый ласковый компаньон, хочет быть на диване или на коленях. Тихий, гостям сообщает мягким лаем.",
                "Дружелюбен и игрив с бережными детьми. Малышей нужно научить бережно его держать.",
                "Обычно дружелюбен с собаками, кошками и другими питомцами.",
                "Короткие прогулки, игры и простые трюки. Дрессировка идёт на терпении, похвале и лакомствах.",
                "Короткие прогулки, много компании и сон. Регулярная расчёска входит в распорядок.",
            ],
            "quirks": [
                "Ши-тцу плосконосая порода, которая может перегреваться, поэтому в жару сокращайте прогулки.",
                "Многие хозяева выбирают короткую «щенячью» стрижку, потому что длинная шерсть требует ежедневной расчёски.",
                "Это дружелюбная собака, которая обычно здоровается со всеми, как с друзьями.",
            ],
        },
    },
    "tibetan-terrier": {
        "prey": "low",
        "en": {
            "summary": "Gentle, loyal and sensitive. The Tibetan Terrier is a medium-sized shaggy companion with a warm, devoted nature and plenty of stamina for family walks.",
            "care": [
                "The long double coat needs thorough brushing down to the skin several times a week to prevent mats, and a trim every few months. Check the eyes and ears.",
                "Plan for about an hour and a half of walks and play a day.",
            ],
            "good_fit": [
                "Want a loyal, sensitive family dog",
                "Are active and enjoy walks",
                "Do not mind regular brushing",
                "Are home often",
            ],
            "think_twice": [
                "Dislike grooming",
                "Are away from home most of the day",
                "Want a dog that does not bark at visitors",
                "Use harsh training",
            ],
            "daily": [
                "About an hour and a half a day, with walks and play. It has good stamina and is happy on long country walks.",
                "It bonds closely to its family and does not like being alone for long.",
                "Affectionate and calm indoors after exercise, with a sensitive nature that notices mood.",
                "Gentle and playful with children, usually patient.",
                "Typically friendly with dogs and pets, though it may be reserved with strangers.",
                "Walks, agility, tricks and games. It is sensitive, so use positive training.",
                "Active outings morning and evening and company in between.",
            ],
            "quirks": [
                "Despite its name, the Tibetan Terrier is not a true terrier.",
                "Its large, flat, round feet with hair between the toes act like snowshoes for walking on snow.",
                "The long coat needs brushing right down to the skin, as the thick undercoat mats easily.",
            ],
        },
        "ru": {
            "summary": "Мягкая, преданная и чуткая собака. Тибетский терьер — лохматый компаньон среднего размера с тёплым преданным характером и хорошей выносливостью для семейных прогулок.",
            "care": [
                "Длинную шерсть с подшёрстком тщательно расчёсывайте до кожи несколько раз в неделю, чтобы не было колтунов, и подстригайте раз в несколько месяцев. Проверяйте глаза и уши.",
                "Рассчитывайте примерно на полтора часа прогулок и игр в день.",
            ],
            "good_fit": [
                "Хотите преданную чуткую семейную собаку",
                "Активны и любите прогулки",
                "Не против регулярной расчёски",
                "Часто бываете дома",
            ],
            "think_twice": [
                "Не любите уход за шерстью",
                "Большую часть дня не бываете дома",
                "Хотите собаку, которая не лает на гостей",
                "Используете жёсткую дрессировку",
            ],
            "daily": [
                "Около полутора часов в день: прогулки и игры. У неё хорошая выносливость, и она рада долгим загородным прогулкам.",
                "Она тесно привязана к семье и не любит долго оставаться одна.",
                "Дома ласковая и спокойная после нагрузки, чуткая, замечает настроение.",
                "Мягкая и игривая с детьми, обычно терпелива.",
                "Обычно дружелюбна с собаками и питомцами, но с чужими может быть сдержанна.",
                "Прогулки, аджилити, трюки и игры. Она чувствительна, поэтому дрессируйте на поощрении.",
                "Активные прогулки утром и вечером и компания между ними.",
            ],
            "quirks": [
                "Несмотря на название, тибетский терьер — не настоящий терьер.",
                "Большие плоские круглые лапы с шерстью между пальцами работают как снегоступы для ходьбы по снегу.",
                "Длинную шерсть нужно расчёсывать до самой кожи, ведь густой подшёрсток легко сбивается в колтуны.",
            ],
        },
    },
}


def forwards(apps, schema_editor):
    apply_content(apps, DOGS)


class Migration(migrations.Migration):
    dependencies = [("woof", "0076_group8_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
