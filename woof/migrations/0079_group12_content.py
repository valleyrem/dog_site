from django.db import migrations

from woof.migrations._content import apply_content

DOGS = {
    "american-bulldog": {
        "prey": "moderate",
        "en": {
            "summary": "Strong, confident and devoted. The American Bulldog is a powerful, athletic farm dog that is loyal and playful with its family and needs firm, kind leadership.",
            "care": [
                "The short coat needs a weekly brush. Clean the face folds and ears, and keep the weight lean to protect the joints.",
                "Plan for about an hour and a half of walks, games and training a day.",
            ],
            "good_fit": [
                "Have experience with strong dogs",
                "Can give calm, consistent training and socialisation",
                "Have a secure garden and a high fence",
                "Want a loyal, protective family dog",
            ],
            "think_twice": [
                "Are a first-time dog owner",
                "Want a dog that welcomes every dog",
                "Live in a hot climate without cooling",
                "Are away from home most of the day",
            ],
            "daily": [
                "About an hour and a half a day of walks and games. It is strong, so teach loose-lead walking early and use a sturdy harness.",
                "It bonds closely with its family and dislikes long hours alone. Bored, it may chew or dig.",
                "Calm and affectionate indoors once exercised, and happy to stay close to the family. It may snore and drool a little.",
                "Loyal, patient and protective with its family's children, but its size and strength mean supervision with small kids.",
                "Can be dominant with unfamiliar dogs, especially of the same sex. Early socialisation and a lead outdoors are important.",
                "Fetch, tug with rules, walks and basic obedience. Training should be firm, fair and reward-based.",
                "Active morning and evening and long rest in between.",
            ],
            "quirks": [
                "The American Bulldog is a very athletic dog and many can jump surprisingly high, so a tall fence is a good idea.",
                "It loves to be near its family and is happy to follow people around the house.",
                "Some have a white coat with coloured patches, and the coat is short and easy to keep.",
            ],
        },
        "ru": {
            "summary": "Сильная, уверенная и преданная собака. Американский бульдог — мощная спортивная фермерская собака, преданная и игривая со своей семьёй, которой нужны твёрдое и доброе руководство.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Чистите складки на морде и уши, держите вес в норме, чтобы беречь суставы.",
                "Рассчитывайте примерно на полтора часа прогулок, игр и занятий в день.",
            ],
            "good_fit": [
                "Есть опыт с сильными собаками",
                "Можете спокойно и последовательно дрессировать и социализировать",
                "Есть огороженный двор и высокий забор",
                "Хотите преданную защищающую семейную собаку",
            ],
            "think_twice": [
                "Это ваша первая собака",
                "Хотите собаку, которая дружит со всеми собаками",
                "Живёте в жарком климате без охлаждения",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Около полутора часов в день прогулок и игр. Он сильный, поэтому рано учите ходить на ослабленном поводке и используйте прочную шлейку.",
                "Он тесно привязан к семье и не любит долгого одиночества. От скуки может грызть вещи и рыть землю.",
                "Дома после нагрузки спокойный и ласковый, охотно остаётся рядом с семьёй. Может храпеть и немного пускать слюни.",
                "Предан, терпелив и защищает детей своей семьи, но из-за размера и силы за малышами нужен присмотр.",
                "С незнакомыми собаками, особенно своего пола, может доминировать. Важны ранняя социализация и поводок на улице.",
                "Апорт, перетягивание с правилами, прогулки и базовое послушание. Дрессировка должна быть твёрдой, справедливой и на поощрении.",
                "Активные утро и вечер и долгий отдых между ними.",
            ],
            "quirks": [
                "Американский бульдог очень спортивен, и многие прыгают удивительно высоко, поэтому высокий забор не помешает.",
                "Он любит быть рядом с семьёй и охотно ходит за людьми по дому.",
                "У некоторых белая шерсть с цветными пятнами, а шерсть короткая и неприхотливая.",
            ],
        },
    },
    "american-eskimo-dog": {
        "prey": "low",
        "en": {
            "summary": "Bright, cheerful and eager to learn. The American Eskimo Dog is a fluffy white spitz that comes in three sizes and thrives on attention, training and family company.",
            "care": [
                "The thick white double coat needs brushing two or three times a week, and daily during the heavy shed twice a year. Never shave it.",
                "Plan for about an hour to an hour and a half of walks, play and training a day.",
            ],
            "good_fit": [
                "Want a clever, trainable, cheerful family dog",
                "Enjoy tricks, agility and training",
                "Are home often",
                "Do not mind brushing and white hair",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a quiet dog",
                "Dislike dog hair on clothes and furniture",
                "Cannot give daily mental activity",
            ],
            "daily": [
                "An hour to an hour and a half a day, with games and training. It enjoys exploring and playing outdoors.",
                "It bonds closely and dislikes long hours alone. It may bark or dig when bored.",
                "A cheerful, watchful house dog that follows the family and reports visitors. Teach a quiet command early.",
                "Playful and friendly with children, though the smaller ones are delicate. Teach kids to handle it gently.",
                "Usually friendly with dogs and cats, especially when socialised early.",
                "Tricks, agility, obedience and games. It learns fast and loves praise.",
                "Active walks morning and evening, training in between, and company.",
            ],
            "quirks": [
                "It comes in three sizes: toy, miniature and standard, all with the same fluffy white coat and fox-like face.",
                "Despite the name, the breed has no connection to Eskimos or the Arctic, but its coat sheds dirt well and brushes clean easily.",
                "It loves to learn tricks, and many Eskies perform in dog shows and agility.",
            ],
        },
        "ru": {
            "summary": "Умная, весёлая и любознательная собака. Американская эскимосская собака — пушистый белый шпиц трёх размеров, который расцветает от внимания, занятий и компании семьи.",
            "care": [
                "Густую белую шерсть расчёсывайте два–три раза в неделю, а во время сильной линьки два раза в год — каждый день. Никогда не стригите под машинку.",
                "Рассчитывайте примерно на час–полтора прогулок, игр и занятий в день.",
            ],
            "good_fit": [
                "Хотите умную обучаемую весёлую семейную собаку",
                "Любите трюки, аджилити и дрессировку",
                "Часто бываете дома",
                "Не против расчёски и белой шерсти",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите тихую собаку",
                "Не любите собачью шерсть на одежде и мебели",
                "Не можете ежедневно давать умственные занятия",
            ],
            "daily": [
                "Час–полтора в день с играми и занятиями. Любит исследовать и играть на улице.",
                "Она тесно привязана и не любит долгого одиночества. От скуки может лаять и рыть землю.",
                "Весёлая, внимательная домашняя собака, ходит за семьёй и сообщает о гостях. Рано научите команде «тихо».",
                "Игрива и дружелюбна с детьми, но маленькие разновидности хрупкие. Научите детей бережно обращаться с собакой.",
                "Обычно дружелюбна с собаками и кошками, особенно при ранней социализации.",
                "Трюки, аджилити, послушание и игры. Она быстро учится и любит похвалу.",
                "Активные прогулки утром и вечером, занятия между ними и компания.",
            ],
            "quirks": [
                "Бывает трёх размеров: той, миниатюрная и стандартная, и у всех одна пушистая белая шерсть и лисья мордочка.",
                "Несмотря на название, порода не связана с эскимосами и Арктикой, но шерсть хорошо отталкивает грязь и легко вычёсывается.",
                "Она любит разучивать трюки, и многие эски выступают на выставках и в аджилити.",
            ],
        },
    },
    "american-pit-bull-terrier": {
        "prey": "moderate",
        "en": {
            "summary": "Strong, affectionate and eager to please. The American Pit Bull Terrier is a muscular, athletic dog that loves its people, loves activity and needs an experienced, responsible owner.",
            "care": [
                "The short coat needs a quick weekly brush and a wipe after muddy walks. Check the ears, nails and skin.",
                "Plan for about two hours of exercise, games and training a day.",
            ],
            "good_fit": [
                "Have experience with strong dogs",
                "Are active and enjoy games and sports",
                "Can give calm, consistent training and early socialisation",
                "Have a secure garden and a high fence",
            ],
            "think_twice": [
                "Are a first-time owner",
                "Want a dog that gets along with all dogs",
                "Live where the breed is restricted by law",
                "Are away from home most of the day",
            ],
            "daily": [
                "About two hours a day, with running, fetch and tug games. It is strong, so teach loose-lead walking early and use a sturdy harness.",
                "It bonds closely and dislikes long hours alone. Bored, it may chew or dig.",
                "A cuddly, people-loving housemate that wants to be near its family. It may lean on you or try to sit on your lap.",
                "Affectionate, patient and playful with children in its family. Because it is strong, always supervise play with small kids.",
                "Many do not enjoy unfamiliar dogs, especially of the same sex. Careful early socialisation, a lead outdoors and controlled introductions are essential.",
                "Weight pulling, agility, fetch with sturdy toys and tracking games. It learns well with positive training.",
                "Active morning and evening, with rest and company between.",
            ],
            "quirks": [
                "The breed is restricted or banned in some countries and cities, so check local rules before you get one.",
                "It is very athletic and loves to run, jump and play tug games.",
                'Many Pit Bulls are affectionate "lap dogs" in their own mind and try to sit on whoever is on the sofa.',
            ],
        },
        "ru": {
            "summary": "Сильная, ласковая и старательная собака. Американский питбультерьер — мускулистая спортивная собака, которая любит людей и движение и нуждается в опытном ответственном хозяине.",
            "care": [
                "Короткую шерсть достаточно быстро расчёсывать раз в неделю и вытирать после грязных прогулок. Проверяйте уши, когти и кожу.",
                "Рассчитывайте примерно на два часа нагрузки, игр и занятий в день.",
            ],
            "good_fit": [
                "Есть опыт с сильными собаками",
                "Активны и любите игры и спорт",
                "Можете спокойно и последовательно дрессировать и рано социализировать",
                "Есть огороженный двор и высокий забор",
            ],
            "think_twice": [
                "Это ваша первая собака",
                "Хотите собаку, которая дружит со всеми собаками",
                "Живёте там, где порода ограничена законом",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Около двух часов в день с бегом, апортом и перетягиванием. Она сильная, поэтому рано учите ходить на ослабленном поводке и используйте прочную шлейку.",
                "Она тесно привязана и не любит долгого одиночества. От скуки может грызть вещи и рыть землю.",
                "Ласковый домашний друг, любящий людей, хочет быть рядом с семьёй. Может прислоняться к вам или пытаться сесть на колени.",
                "Ласкова, терпелива и игрива с детьми своей семьи. Из-за силы всегда наблюдайте за играми с малышами.",
                "Многие не любят незнакомых собак, особенно своего пола. Важны осторожная ранняя социализация, поводок на улице и контролируемые знакомства.",
                "Тяга груза, аджилити, апорт с прочными игрушками и игры на поиск. Она хорошо учится на положительной дрессировке.",
                "Активные утро и вечер, между ними отдых и компания.",
            ],
            "quirks": [
                "В некоторых странах и городах порода ограничена или запрещена, поэтому перед покупкой проверьте местные правила.",
                "Она очень спортивна и любит бегать, прыгать и играть в перетягивание.",
                "Многие питбули считают себя комнатными собачками и пытаются сесть на любого, кто сидит на диване.",
            ],
        },
    },
    "anatolian-shepherd-dog": {
        "prey": "moderate",
        "en": {
            "summary": "Independent, watchful and powerful. The Anatolian Shepherd is a livestock guardian that protects its territory and flock on its own and needs an experienced owner with space.",
            "care": [
                "The short or medium double coat needs brushing once or twice a week, and daily during the heavy shed. Check the ears and nails.",
                "Plan for an hour and a half of walking a day, plus a large, securely fenced space to patrol.",
            ],
            "good_fit": [
                "Have a large property and a very high fence",
                "Have experience with guardian breeds",
                "Want a calm, independent guardian",
                "Can give early socialisation",
            ],
            "think_twice": [
                "Live in a flat or close to neighbours",
                "Want a dog that welcomes visitors",
                "Are a first-time owner",
                "Dislike barking, especially at night",
            ],
            "daily": [
                "An hour and a half a day of steady walking, plus a large space to patrol. Keep it on a lead in public: it is strong and protective.",
                "It is independent and can be alone with a large, secure space, but needs company too. It often barks at night.",
                "Calm and watchful, often resting during the day and active at night. Expect barking when it senses something outside.",
                "Gentle with its own family's children, but reserved with visitors and other children. Supervise play with small kids.",
                "Often reserved or dominant with unfamiliar dogs. With animals it was raised with, it is a calm protector.",
                "Long walks and patrol of the property. Training is about respect and calm routines, not repetition.",
                "Rests in the day, active at dusk and night. Offer shade in the heat.",
            ],
            "quirks": [
                "Anatolians are bred to bark on purpose, to warn off predators, and many are most alert at night.",
                "A guardian dog needs early, careful socialisation, so it learns that visitors and neighbours are not threats.",
                "It patrols the edge of its territory rather than moving the flock, and it works on its own.",
            ],
        },
        "ru": {
            "summary": "Самостоятельная, бдительная и мощная собака. Анатолийская овчарка — сторож скота, который сам защищает свою территорию и стадо и нуждается в опытном хозяине с большим участком.",
            "care": [
                "Короткую или среднюю шерсть расчёсывайте один–два раза в неделю, а во время сильной линьки каждый день. Проверяйте уши и когти.",
                "Рассчитывайте на полтора часа ходьбы в день и большое надёжно огороженное пространство для обхода.",
            ],
            "good_fit": [
                "Есть большой участок и очень высокий забор",
                "Есть опыт со сторожевыми породами",
                "Хотите спокойного самостоятельного сторожа",
                "Можете заниматься ранней социализацией",
            ],
            "think_twice": [
                "Живёте в квартире или рядом с соседями",
                "Хотите собаку, которая рада гостям",
                "Это ваша первая собака",
                "Не любите лай, особенно ночью",
            ],
            "daily": [
                "Полтора часа в день ровной ходьбы и большое пространство для обхода. В людных местах держите на поводке: она сильная и защищает.",
                "Она самостоятельна и может быть одна на большом надёжном участке, но компания ей тоже нужна. Часто лает ночью.",
                "Спокойная и бдительная, днём часто отдыхает, а ночью активна. Лай ожидайте, когда она чувствует что-то снаружи.",
                "Мягка с детьми своей семьи, но сдержанна с гостями и чужими детьми. За играми с малышами присматривайте.",
                "К незнакомым собакам часто относится сдержанно или доминирует. С животными, с которыми выросла, спокойный защитник.",
                "Долгие прогулки и обход участка. Дрессировка строится на уважении и спокойных привычках, а не на повторении.",
                "Днём отдыхает, активна на закате и ночью. В жару обеспечьте тень.",
            ],
            "quirks": [
                "Анатолийских овчарок разводили лаять осознанно, чтобы отпугивать хищников, и многие особенно бдительны ночью.",
                "Сторожевой собаке нужна ранняя аккуратная социализация, чтобы она понимала, что гости и соседи не угроза.",
                "Она обходит границы территории, а не гоняет стадо, и работает самостоятельно.",
            ],
        },
    },
    "barbado-da-terceira": {
        "prey": "moderate",
        "en": {
            "summary": "Sturdy, alert and devoted. The Barbado da Terceira is a rare, medium-to-large Azorean farm dog, with a protective, loyal nature that does best with an active family.",
            "care": [
                "The thick coat needs brushing once or twice a week, and more during the shed. Check the ears and nails.",
                "Plan for an hour and a half to two hours of walks, work and play a day.",
            ],
            "good_fit": [
                "Are active and have a secure property",
                "Want a loyal, watchful dog",
                "Can give calm, consistent training",
                "Have time for early socialisation",
            ],
            "think_twice": [
                "Want a dog that welcomes every visitor",
                "Live in a small flat",
                "Want a breed that is easy to find",
                "Are a first-time owner",
            ],
            "daily": [
                "An hour and a half to two hours a day with walks and tasks. It enjoys having a job to do.",
                "It bonds closely to its family and dislikes long hours alone.",
                "Calm and watchful at home, protective of its territory, and reserved with strangers.",
                "Loyal and gentle with its own family's children. Supervise play with small ones.",
                "Can be reserved with unfamiliar dogs. Early socialisation is important.",
                "Walks, herding-style games, obedience and tracking. Train gently, with praise and rewards.",
                "Active outdoors morning and evening and calm company between.",
            ],
            "quirks": [
                "It is a very rare breed from the Azores, so finding a puppy takes patience and planning.",
                "Its thick coat protects it from wind and rain on the islands where it was developed.",
                "It is a farm dog by nature and enjoys tasks and time outdoors with its family.",
            ],
        },
        "ru": {
            "summary": "Крепкая, бдительная и преданная собака. Барбадо да Терсейра — редкая азорская фермерская собака среднего–крупного размера с защитным преданным характером, которой лучше всего в активной семье.",
            "care": [
                "Густую шерсть расчёсывайте один–два раза в неделю, а во время линьки чаще. Проверяйте уши и когти.",
                "Рассчитывайте на полтора–два часа прогулок, работы и игр в день.",
            ],
            "good_fit": [
                "Активны и есть надёжный участок",
                "Хотите преданную бдительную собаку",
                "Можете спокойно и последовательно дрессировать",
                "Есть время на раннюю социализацию",
            ],
            "think_twice": [
                "Хотите собаку, которая рада каждому гостю",
                "Живёте в маленькой квартире",
                "Хотите породу, которую легко найти",
                "Это ваша первая собака",
            ],
            "daily": [
                "Полтора–два часа в день: прогулки и задания. Ей нравится иметь дело.",
                "Она тесно привязана к семье и не любит долгого одиночества.",
                "Дома спокойная и бдительная, защищает территорию, с чужими сдержанна.",
                "Предана и мягка с детьми своей семьи. За играми с малышами присматривайте.",
                "К незнакомым собакам может быть сдержанна. Важна ранняя социализация.",
                "Прогулки, пастушьи игры, послушание и работа по следу. Дрессируйте мягко, с похвалой и поощрением.",
                "Активные утро и вечер на улице и спокойная компания между ними.",
            ],
            "quirks": [
                "Это очень редкая порода с Азорских островов, поэтому на поиск щенка нужны терпение и планирование.",
                "Густая шерсть защищает её от ветра и дождя на островах, где порода сложилась.",
                "По природе это фермерская собака, ей нравятся задания и время на улице с семьёй.",
            ],
        },
    },
    "bluetick-coonhound": {
        "prey": "high",
        "en": {
            "summary": "Friendly, energetic and devoted to its people. The Bluetick Coonhound is a handsome, blue-mottled scent hound with a deep voice and a great need for exercise.",
            "care": [
                "The short glossy coat needs a weekly brush. Clean the long ears weekly and check the nails.",
                "Plan for two hours or more of walking, running and scent work a day.",
            ],
            "good_fit": [
                "Are very active and love the outdoors",
                "Have a secure garden and a high fence",
                "Enjoy scent games and tracking",
                "Want a friendly, laid-back family dog",
            ],
            "think_twice": [
                "Live in a flat or near noise-sensitive neighbours",
                "Want a dog that comes back every time",
                "Have cats or small pets",
                "Are away from home most of the day",
            ],
            "daily": [
                "Two hours or more a day, with chances to use its nose. Keep it on a lead or long line, as it follows a scent far.",
                "It does not like long hours alone and may bay, dig or chew. Company and exercise help.",
                "Calm and affectionate indoors once exercised, happy to lie near the family.",
                "Gentle and patient with children, though its size and energy need supervision with small ones.",
                "Typically friendly with dogs, as it comes from a pack. Cats and small pets may trigger the chase.",
                "Scent tracking, long walks, hiking and swimming. Training takes patience and food rewards.",
                "A long outing morning and evening and quiet company between.",
            ],
            "quirks": [
                "The Bluetick is Tennessee's state dog, and it has been the University of Tennessee's mascot since 1953.",
                "Its deep, bawling voice carries for long distances, so tell the neighbours if you have a puppy.",
                "The blue-ticked coat looks like a dark blue marbled pattern, and each dog's markings are unique.",
            ],
        },
        "ru": {
            "summary": "Дружелюбная, энергичная и преданная людям собака. Блютик-кунхаунд — красивая гончая с голубовато-крапчатым окрасом, низким голосом и большой потребностью в нагрузке.",
            "care": [
                "Короткую блестящую шерсть расчёсывайте раз в неделю. Раз в неделю чистите длинные уши и проверяйте когти.",
                "Рассчитывайте на два часа и больше ходьбы, бега и работы по запаху в день.",
            ],
            "good_fit": [
                "Очень активны и любите природу",
                "Есть огороженный двор и высокий забор",
                "Любите игры на поиск и работу по следу",
                "Хотите дружелюбную неторопливую семейную собаку",
            ],
            "think_twice": [
                "Живёте в квартире или рядом с соседями, чувствительными к шуму",
                "Хотите собаку, которая каждый раз возвращается",
                "Дома кошки или мелкие животные",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Два часа и больше в день с возможностью пользоваться носом. Держите на поводке или длинной верёвке: она далеко идёт за запахом.",
                "Долгое одиночество ей не нравится, она может лаять, рыть землю и грызть вещи. Помогают компания и нагрузка.",
                "Дома после нагрузки спокойная и ласковая, охотно лежит рядом с семьёй.",
                "Мягка и терпелива с детьми, но из-за размера и энергии за малышами нужен присмотр.",
                "Обычно дружелюбна с собаками, ведь происходит из своры. Кошки и мелкие питомцы могут вызвать погоню.",
                "Работа по следу, долгие прогулки, походы и плавание. Дрессировка требует терпения и лакомств.",
                "Долгая прогулка утром и вечером и спокойная компания между ними.",
            ],
            "quirks": [
                "Блютик — собака штата Теннесси, и с 1953 года она талисман Университета Теннесси.",
                "Её низкий протяжный лай слышен далеко, поэтому предупредите соседей, если взяли щенка.",
                "Окрас с голубыми крапинками выглядит как тёмно-голубой мраморный узор, у каждой собаки он свой.",
            ],
        },
    },
    "boerboel": {
        "prey": "moderate",
        "en": {
            "summary": "Powerful, confident and protective. The Boerboel is a giant South African mastiff that is calm and loving with its family and needs an experienced, confident owner.",
            "care": [
                "The short coat needs a weekly brush. Clean the face folds and ears, and watch the weight to protect the joints.",
                "Plan for about an hour and a half of walks and training a day. Avoid hard exercise on hot days.",
            ],
            "good_fit": [
                "Have experience with giant, strong breeds",
                "Can give calm, firm and consistent training from puppyhood",
                "Have a large property and a very secure fence",
                "Want a calm, protective family guardian",
            ],
            "think_twice": [
                "Are a first-time owner",
                "Want a dog that welcomes every visitor",
                "Live in a flat",
                "Cannot afford the costs of a giant breed",
            ],
            "daily": [
                "About an hour and a half a day of walking and training. Teach loose-lead walking early, because an adult is very strong.",
                "It bonds closely with its family. It needs company, and bored, it may chew or dig.",
                "Calm and watchful at home, protective and reserved with strangers. It needs space.",
                "Gentle and patient with its own family's children, but its size means supervision with small kids and visitors.",
                "Can be dominant with unfamiliar dogs. Early socialisation and controlled introductions are essential.",
                "Long walks, basic obedience and calm routines. Training should be firm, fair and reward-based.",
                "Walks morning and evening and long rests in between. It does not tolerate heat well.",
            ],
            "quirks": [
                "It is one of the largest mastiff breeds, so food, vet bills and space need to be planned for.",
                "Early, careful socialisation is essential, because a Boerboel's size and protective instinct need a calm, well-mannered adult.",
                "Although powerful, it is typically a calm and affectionate family dog.",
            ],
        },
        "ru": {
            "summary": "Мощная, уверенная и защищающая собака. Бурбуль — гигантский южноафриканский мастиф, спокойный и ласковый со своей семьёй и нуждающийся в опытном уверенном хозяине.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Чистите складки на морде и уши, следите за весом, чтобы беречь суставы.",
                "Рассчитывайте примерно на полтора часа прогулок и занятий в день. В жару избегайте тяжёлой нагрузки.",
            ],
            "good_fit": [
                "Есть опыт с гигантскими сильными породами",
                "Можете спокойно, твёрдо и последовательно дрессировать с щенячьего возраста",
                "Есть большой участок и очень надёжный забор",
                "Хотите спокойного защищающего семейного охранника",
            ],
            "think_twice": [
                "Это ваша первая собака",
                "Хотите собаку, которая рада каждому гостю",
                "Живёте в квартире",
                "Не можете позволить расходы на гигантскую породу",
            ],
            "daily": [
                "Около полутора часов в день ходьбы и занятий. Рано учите ходить на ослабленном поводке: взрослая собака очень сильная.",
                "Он тесно привязан к семье. Ему нужна компания, от скуки он может грызть вещи и рыть землю.",
                "Дома спокойный и бдительный, защищает и сдержан с чужими. Ему нужно место.",
                "Мягок и терпелив с детьми своей семьи, но из-за размера за малышами и гостями нужен присмотр.",
                "С незнакомыми собаками может доминировать. Важны ранняя социализация и контролируемые знакомства.",
                "Долгие прогулки, базовое послушание и спокойные ритуалы. Дрессировка должна быть твёрдой, справедливой и на поощрении.",
                "Прогулки утром и вечером и долгий отдых между ними. Жару он переносит плохо.",
            ],
            "quirks": [
                "Это одна из самых крупных пород мастифов, поэтому заранее планируйте расходы на корм, ветеринара и место.",
                "Важна ранняя аккуратная социализация, ведь размер и защитный инстинкт бурбуля требуют спокойного воспитанного взрослого пса.",
                "При всей мощи он обычно спокойная и ласковая семейная собака.",
            ],
        },
    },
    "boykin-spaniel": {
        "prey": "moderate",
        "en": {
            "summary": "Friendly, cheerful and eager to please. The Boykin Spaniel is a small, brown, wavy-coated spaniel that is great in the field, at home and in a car or on a boat.",
            "care": [
                "The wavy coat needs brushing two or three times a week. Clean and dry the ears weekly, especially after swimming.",
                "Plan for about an hour and a half to two hours of walks, swimming and games a day.",
            ],
            "good_fit": [
                "Are active and enjoy water and outdoor games",
                "Want a cheerful, trainable medium-sized dog",
                "Are home often",
                "Enjoy training and hunting-style games",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a calm, low-energy dog",
                "Have small birds as pets",
                "Dislike ear care",
            ],
            "daily": [
                "An hour and a half to two hours a day, with swimming and fetch. It loves water and mud.",
                "It bonds closely and dislikes long hours alone. It may bark or chew.",
                "Friendly, eager and affectionate indoors, wanting to be near the family.",
                "Playful and gentle with children, a good family dog when exercised.",
                "Usually friendly with dogs and cats. Birds may trigger its hunting instinct.",
                "Fetch, swimming, retrieving, scent games and obedience. It learns quickly and loves praise.",
                "Active walks morning and evening and company between.",
            ],
            "quirks": [
                "The Boykin Spaniel is South Carolina's state dog, named in 1985.",
                "It is a compact spaniel, small enough to fit in a canoe or a boat, which is part of its charm.",
                "It has a liver-brown wavy coat, and a rinse after muddy swims keeps it fresh.",
            ],
        },
        "ru": {
            "summary": "Дружелюбный, весёлый и старательный спаниель. Бойкин-спаниель — небольшая коричневая волнистошёрстная собака, отлично работающая в поле, дома, в машине и на лодке.",
            "care": [
                "Волнистую шерсть расчёсывайте два–три раза в неделю. Раз в неделю чистите и просушивайте уши, особенно после плавания.",
                "Рассчитывайте примерно на полтора–два часа прогулок, плавания и игр в день.",
            ],
            "good_fit": [
                "Активны и любите воду и игры на улице",
                "Хотите весёлую обучаемую собаку среднего размера",
                "Часто бываете дома",
                "Любите дрессировку и охотничьи игры",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите спокойную собаку с небольшой энергией",
                "Дома мелкие птицы",
                "Не любите уход за ушами",
            ],
            "daily": [
                "Полтора–два часа в день с плаванием и апортом. Любит воду и грязь.",
                "Он тесно привязан и не любит долгого одиночества. Может лаять и грызть вещи.",
                "Дома дружелюбный, старательный и ласковый, хочет быть рядом с семьёй.",
                "Игрив и мягок с детьми, хорошая семейная собака при достаточной нагрузке.",
                "Обычно дружелюбен с собаками и кошками. Птицы могут пробудить охотничий инстинкт.",
                "Апорт, плавание, подача, игры на поиск и послушание. Он быстро учится и любит похвалу.",
                "Активные прогулки утром и вечером и компания между ними.",
            ],
            "quirks": [
                "Бойкин-спаниель — собака штата Южная Каролина, объявленная такой в 1985 году.",
                "Это компактный спаниель, достаточно маленький, чтобы поместиться в каноэ или лодке, и это часть его обаяния.",
                "У него коричневая волнистая шерсть, и ополаскивание после грязного плавания сохраняет её свежей.",
            ],
        },
    },
    "catahoula-leopard-dog": {
        "prey": "high",
        "en": {
            "summary": "Active, intelligent and independent. The Catahoula Leopard Dog is a spotted, athletic working dog that is loyal to its family and needs plenty of exercise and a job to do.",
            "care": [
                "The short coat needs a weekly brush. Check the ears and nails, and dry the webbed feet after wet walks.",
                "Plan for two hours or more of exercise, work and training a day.",
            ],
            "good_fit": [
                "Are very active and love outdoor work",
                "Have experience with strong, independent dogs",
                "Have a large secure property",
                "Can give firm, kind training",
            ],
            "think_twice": [
                "Are a first-time owner",
                "Want a calm, low-energy pet",
                "Are away from home most of the day",
                "Have small pets",
            ],
            "daily": [
                "Two hours or more a day, with running, work or sport. It needs a job to do.",
                "It dislikes long hours alone. Bored, it may dig, chew or escape.",
                "Alert and loyal indoors, protective of its home and reserved with strangers.",
                "Loyal and playful with children it knows, though its energy and strength need supervision.",
                "Can be dominant with other dogs, particularly of the same sex. Early socialisation is important.",
                "Herding-style games, running, agility, swimming and scent work. It needs mental tasks and firm, fair training.",
                "Active morning and evening, with tasks and rest between.",
            ],
            "quirks": [
                "The Catahoula is the state dog of Louisiana, named in 1979.",
                "Its feet are webbed, which helps it work in marshy areas, and its eyes can be blue, brown or two different colours.",
                "Every Catahoula's coat pattern is unique, with spots, merle or brindle.",
            ],
        },
        "ru": {
            "summary": "Активная, умная и самостоятельная собака. Леопардовая собака катахула — пятнистая спортивная рабочая собака, преданная семье и нуждающаяся в большой нагрузке и деле.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Проверяйте уши и когти, после мокрых прогулок просушивайте перепончатые лапы.",
                "Рассчитывайте на два часа и больше нагрузки, работы и занятий в день.",
            ],
            "good_fit": [
                "Очень активны и любите работу на улице",
                "Есть опыт с сильными самостоятельными собаками",
                "Есть большой надёжный участок",
                "Можете твёрдо и доброжелательно дрессировать",
            ],
            "think_twice": [
                "Это ваша первая собака",
                "Хотите спокойного питомца с небольшой энергией",
                "Большую часть дня не бываете дома",
                "Дома мелкие животные",
            ],
            "daily": [
                "Два часа и больше в день с бегом, работой или спортом. Ей нужно иметь дело.",
                "Долгого одиночества она не любит. От скуки может рыть землю, грызть вещи и убегать.",
                "Дома внимательна и предана, защищает дом и сдержанна с чужими.",
                "Предана и игрива со знакомыми детьми, но энергия и сила требуют присмотра.",
                "С другими собаками, особенно своего пола, может доминировать. Важна ранняя социализация.",
                "Пастушьи игры, бег, аджилити, плавание и работа по запаху. Ей нужны умственные задачи и твёрдая справедливая дрессировка.",
                "Активные утро и вечер, между ними задания и отдых.",
            ],
            "quirks": [
                "Катахула — собака штата Луизиана, объявленная таковой в 1979 году.",
                "У неё перепончатые лапы, помогающие работать в болотистых местах, а глаза могут быть голубыми, карими или разного цвета.",
                "Рисунок шерсти у каждой катахулы уникален: пятна, мрамор или тигровый окрас.",
            ],
        },
    },
    "rat-terrier": {
        "prey": "high",
        "en": {
            "summary": "Lively, friendly and quick. The Rat Terrier is a small to medium, short-coated terrier that is affectionate with its family and loves to run, dig and play.",
            "care": [
                "The short coat needs a weekly brush. Check the ears and nails, and brush the teeth regularly.",
                "Plan for an hour to an hour and a half of walks, games and training a day.",
            ],
            "good_fit": [
                "Are active and enjoy games and walks",
                "Want a lively, affectionate small to medium dog",
                "Enjoy training and tricks",
                "Have a secure fence",
            ],
            "think_twice": [
                "Have hamsters, mice or other small pets",
                "Are away from home most of the day",
                "Want a dog that never digs",
                "Want a calm, low-energy dog",
            ],
            "daily": [
                "An hour to an hour and a half a day, including running and play. Keep it on a lead in open places, as its chase instinct is strong.",
                "It bonds closely and dislikes long hours alone. Bored, it may dig or bark.",
                "Cheerful and affectionate indoors, happy to curl up with the family. It is clean and tidy.",
                "Playful and friendly with children, though small children should handle it gently.",
                "Usually friendly with dogs, but small animals such as rodents may trigger its hunting instinct.",
                "Fetch, agility, scent games and tricks. It learns quickly with praise and treats.",
                "Active walks morning and evening, play and training in between.",
            ],
            "quirks": [
                "Rat Terriers come in several sizes, from miniature to standard, but all share a short, sleek coat and quick feet.",
                "It loves to dig, so a corner of the garden for digging games saves the flower beds.",
                "It is lively, athletic and can jump surprisingly high for its size.",
            ],
        },
        "ru": {
            "summary": "Живой, дружелюбный и проворный терьер. Рэт-терьер — небольшой или средний короткошёрстный терьер, ласковый со своей семьёй, который любит бегать, копать и играть.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Проверяйте уши и когти, регулярно чистите зубы.",
                "Рассчитывайте на час–полтора прогулок, игр и занятий в день.",
            ],
            "good_fit": [
                "Активны и любите игры и прогулки",
                "Хотите живую ласковую собаку небольшого или среднего размера",
                "Любите дрессировку и трюки",
                "Есть надёжный забор",
            ],
            "think_twice": [
                "Дома хомяки, мыши или другие мелкие животные",
                "Большую часть дня не бываете дома",
                "Хотите собаку, которая никогда не роет землю",
                "Хотите спокойную собаку с небольшой энергией",
            ],
            "daily": [
                "Час–полтора в день, включая бег и игры. В открытых местах держите на поводке: инстинкт погони сильный.",
                "Он тесно привязан и не любит долгого одиночества. От скуки может рыть землю и лаять.",
                "Дома весёлый и ласковый, охотно сворачивается рядом с семьёй. Чистоплотен и аккуратен.",
                "Игрив и дружелюбен с детьми, но малыши должны обращаться с ним бережно.",
                "Обычно дружелюбен с собаками, но мелкие животные, например грызуны, могут пробудить охотничий инстинкт.",
                "Апорт, аджилити, игры на поиск и трюки. Он быстро учится на похвале и лакомствах.",
                "Активные прогулки утром и вечером, между ними игры и занятия.",
            ],
            "quirks": [
                "Рэт-терьеры бывают разных размеров, от миниатюрных до стандартных, но у всех короткая гладкая шерсть и проворные лапы.",
                "Он любит копать, поэтому уголок в саду для игры в «раскопки» спасает цветочные клумбы.",
                "Он живой, спортивный и для своего размера прыгает удивительно высоко.",
            ],
        },
    },
    "treeing-walker-coonhound": {
        "prey": "high",
        "en": {
            "summary": "Friendly, fast and tireless. The Treeing Walker Coonhound is a lean, tricolour scent hound with a loud voice, a sociable nature and a huge need for exercise.",
            "care": [
                "The short smooth coat needs a weekly brush. Clean the long ears weekly and check the nails.",
                "Plan for two hours or more of running and scent work a day.",
            ],
            "good_fit": [
                "Are very active and love running or hiking",
                "Have a secure garden and a very high fence",
                "Enjoy scent games and tracking",
                "Want a friendly, social dog",
            ],
            "think_twice": [
                "Live in a flat or near noise-sensitive neighbours",
                "Want a dog that comes back every time",
                "Have cats or small pets",
                "Are away from home most of the day",
            ],
            "daily": [
                "Two hours or more a day, including real running. Keep it on a lead or in a fully fenced area, as it follows scent at speed.",
                "It dislikes long hours alone and may bay, dig or chew. Company and exercise help.",
                "Friendly and affectionate indoors once exercised, happy to lie on the sofa.",
                "Gentle and playful with children, though its energy needs supervision with small ones.",
                "Typically friendly with dogs, as it comes from a pack. Cats and small pets may trigger the chase.",
                "Scent tracking, running, hiking and swimming. Training takes patience and food rewards.",
                "A long outing morning and evening and calm company between.",
            ],
            "quirks": [
                "It is one of the fastest and most energetic coonhounds, with a clear, ringing voice that carries over long distances.",
                "A tricolour coat of white, black and tan is typical, and it is easy to see in the field.",
                "It is a sociable pack dog, so it is happiest with company, human or canine.",
            ],
        },
        "ru": {
            "summary": "Дружелюбная, быстрая и неутомимая собака. Уокер-кунхаунд — поджарая трёхцветная гончая с громким голосом, общительным характером и огромной потребностью в нагрузке.",
            "care": [
                "Короткую гладкую шерсть расчёсывайте раз в неделю. Раз в неделю чистите длинные уши и проверяйте когти.",
                "Рассчитывайте на два часа и больше бега и работы по запаху в день.",
            ],
            "good_fit": [
                "Очень активны и любите бег или походы",
                "Есть огороженный двор и очень высокий забор",
                "Любите игры на поиск и работу по следу",
                "Хотите дружелюбную общительную собаку",
            ],
            "think_twice": [
                "Живёте в квартире или рядом с соседями, чувствительными к шуму",
                "Хотите собаку, которая каждый раз возвращается",
                "Дома кошки или мелкие животные",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Два часа и больше в день, включая настоящий бег. Держите на поводке или в полностью огороженном месте: она быстро идёт за запахом.",
                "Долгое одиночество ей не нравится, она может лаять, рыть землю и грызть вещи. Помогают компания и нагрузка.",
                "Дома после нагрузки дружелюбная и ласковая, охотно лежит на диване.",
                "Мягка и игрива с детьми, но её энергия требует присмотра рядом с малышами.",
                "Обычно дружелюбна с собаками, ведь происходит из своры. Кошки и мелкие питомцы могут вызвать погоню.",
                "Работа по следу, бег, походы и плавание. Дрессировка требует терпения и лакомств.",
                "Долгая прогулка утром и вечером и спокойная компания между ними.",
            ],
            "quirks": [
                "Это одна из самых быстрых и энергичных кунхаундов, с чётким звонким голосом, который слышен на большие расстояния.",
                "Типичен трёхцветный окрас: белый, чёрный и рыжий, его хорошо видно в поле.",
                "Это общительная стайная собака, поэтому ей лучше всего в компании — людей или собак.",
            ],
        },
    },
}


def forwards(apps, schema_editor):
    apply_content(apps, DOGS)


class Migration(migrations.Migration):
    dependencies = [("woof", "0078_group11_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
