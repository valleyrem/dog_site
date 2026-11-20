from django.db import migrations

from woof.migrations._content import apply_content

DOGS = {
    "basset-hound": {
        "prey": "high",
        "en": {
            "summary": "Gentle, easygoing and endlessly curious. The Basset Hound is a low, long-eared scent hound that loves to follow its nose, and a relaxed, loving companion at home.",
            "care": [
                "Brush weekly with a rubber mitt and wipe the skin folds. Clean the long ears every week, because they trap moisture and dirt.",
                "Plan for about an hour of walks a day at a steady pace. Watch the weight closely, as extra kilos strain the long back.",
            ],
            "good_fit": [
                "Want a calm, friendly family dog",
                "Enjoy slow walks with plenty of sniffing",
                "Can be patient with training",
                "Are happy to clean ears and skin folds",
            ],
            "think_twice": [
                "Want a dog that comes back at once when called",
                "Have an unfenced garden",
                "Dislike drooling or a doggy smell",
                "Want a dog for jogging or active sports",
            ],
            "daily": [
                "About an hour a day at its own pace, with plenty of time to sniff. Keep it on a lead or in a fenced area, because it follows a scent and may not come back.",
                "It does not like long hours alone and may bay or howl. A routine and company help.",
                "A relaxed, sociable housemate that loves to nap close to the family. Low to the ground, it is not suited to many stairs.",
                "Patient and good-natured with children, and usually very tolerant. Teach children to be gentle with its back and ears.",
                "Usually friendly with other dogs, as it is used to the pack, and often fine with cats it knows.",
                "Scent games, tracking and slow, steady walks. Training takes patience and food rewards.",
                "A sniff-filled walk in the morning and evening and plenty of rest between.",
            ],
            "quirks": [
                "The long ears and loose skin sweep scent up from the ground towards the nose, which has hundreds of millions of scent receptors.",
                "Its deep bay carries through walls, so tell the neighbours if you have a puppy.",
                "The long ears need cleaning every week, and the folds under the eyes need a wipe.",
            ],
        },
        "ru": {
            "summary": "Мягкий, спокойный и бесконечно любопытный. Бассет-хаунд — низкая длинноухая гончая, которая любит идти по запаху, а дома — спокойный и ласковый компаньон.",
            "care": [
                "Раз в неделю расчёсывайте резиновой рукавицей и протирайте складки кожи. Каждую неделю чистите длинные уши: в них задерживаются влага и грязь.",
                "Рассчитывайте примерно на час прогулок в день в спокойном темпе. Следите за весом: лишние килограммы нагружают длинную спину.",
            ],
            "good_fit": [
                "Хотите спокойную дружелюбную семейную собаку",
                "Любите неспешные прогулки с обнюхиванием",
                "Готовы терпеливо дрессировать",
                "Не против чистить уши и складки",
            ],
            "think_twice": [
                "Хотите собаку, которая сразу возвращается по зову",
                "Двор не огорожен",
                "Не любите слюни и запах собаки",
                "Хотите собаку для бега или активного спорта",
            ],
            "daily": [
                "Около часа в день в собственном темпе, с большим запасом времени на обнюхивание. Держите на поводке или в огороженном месте: бассет идёт за запахом и может не вернуться.",
                "Долгое одиночество ему не нравится, он может лаять и выть. Помогают распорядок и компания.",
                "Спокойный общительный домашний друг, любит дремать рядом с семьёй. Он низкий, поэтому много лестниц ему не подходит.",
                "Терпелив и добродушен с детьми, обычно очень снисходителен. Научите детей бережно обращаться со спиной и ушами.",
                "Обычно дружелюбен с другими собаками, ведь привык к стае, и часто спокойно ладит со знакомыми кошками.",
                "Игры на поиск, работа по следу и неспешные прогулки. Дрессировка требует терпения и лакомств.",
                "Прогулка с обнюхиванием утром и вечером и много отдыха между ними.",
            ],
            "quirks": [
                "Длинные уши и свободная кожа поднимают запах от земли к носу, в котором сотни миллионов обонятельных рецепторов.",
                "Его низкий лай слышен через стены, поэтому предупредите соседей, если взяли щенка.",
                "Длинные уши нужно чистить каждую неделю, а складки под глазами протирать.",
            ],
        },
    },
    "beagle": {
        "prey": "high",
        "en": {
            "summary": "Merry, curious and friendly. The Beagle is a compact, sociable scent hound that loves people, loves food and loves to follow an interesting smell wherever it leads.",
            "care": [
                "The short coat needs a weekly brush. Check and clean the ears every week.",
                "Plan for an hour or more of walks a day. Beagles love food and gain weight easily, so measure meals.",
            ],
            "good_fit": [
                "Are active and enjoy daily walks",
                "Want a cheerful, sociable family dog",
                "Are home a lot or have company for the dog",
                "Have a secure, fenced garden",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a quiet dog",
                "Want a dog that always returns off lead",
                "Have unfenced outdoor space",
            ],
            "daily": [
                "An hour or more a day. Keep it on a lead or a long line in open spaces, because a good scent can make it forget the recall.",
                "Beagles do not like being alone, and when left they often bay or howl. They do best with company and a routine.",
                "A friendly, busy house dog that follows the family around. Keep food out of reach, because it will find it.",
                "Good-natured, playful and sturdy with children. It is a pack animal and loves family games.",
                "Usually friendly with other dogs, thanks to its pack background. Small pets such as rabbits may trigger the chase.",
                "Scent games, tracking, hiding treats and long walks. Training with food works well, though it can be distracted by smells.",
                "Active walks morning and evening, games between, and good sleep. Regular meals keep it calm.",
            ],
            "quirks": [
                'The Beagle\'s voice is a mix of bark and long howl called a bay, and it often "sings" when left alone.',
                "Its nose has around 220 million scent receptors, compared with about 5 million in a person.",
                "Food is its great love, so secure the bin, the cupboard and the table.",
            ],
        },
        "ru": {
            "summary": "Весёлый, любопытный и дружелюбный. Бигль — компактная общительная гончая, которая любит людей, еду и интересные запахи, куда бы они ни вели.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Каждую неделю проверяйте и чистите уши.",
                "Рассчитывайте на час и больше прогулок в день. Бигли любят поесть и легко полнеют, поэтому отмеряйте порции.",
            ],
            "good_fit": [
                "Активны и гуляете каждый день",
                "Хотите весёлую общительную семейную собаку",
                "Часто бываете дома или собаке есть с кем быть",
                "Есть огороженный двор",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите тихую собаку",
                "Хотите собаку, которая всегда возвращается без поводка",
                "Двор не огорожен",
            ],
            "daily": [
                "Час и больше в день. На открытых местах держите на поводке или длинной верёвке: интересный запах может заставить забыть команду.",
                "Бигли не любят быть одни и, оставшись, часто лают или воют. Им лучше с компанией и распорядком.",
                "Дружелюбный деятельный домашний пёс, который ходит за семьёй. Убирайте еду подальше: он её найдёт.",
                "Добродушен, игрив и вынослив с детьми. Это стайное животное, любит семейные игры.",
                "Обычно дружелюбен с другими собаками благодаря стайному прошлому. Мелкие питомцы, например кролики, могут вызвать погоню.",
                "Игры на поиск, работа по следу, поиск спрятанных лакомств и долгие прогулки. Дрессировка с лакомствами идёт хорошо, но запахи отвлекают.",
                "Активные прогулки утром и вечером, игры между ними и хороший сон. Регулярное кормление помогает ему быть спокойным.",
            ],
            "quirks": [
                "Голос бигля — смесь лая и протяжного воя, который называют «бей». Оставшись один, он часто «поёт».",
                "В носу бигля около 220 миллионов обонятельных рецепторов, у человека — около 5 миллионов.",
                "Еда — его большая любовь, поэтому прячьте мусорное ведро, шкафы и стол.",
            ],
        },
    },
    "black-and-tan-coonhound": {
        "prey": "high",
        "en": {
            "summary": "Friendly, relaxed and devoted. The Black and Tan Coonhound is a large, handsome scent hound with a deep voice, a loving nature and a strong need for outdoor time.",
            "care": [
                "The short coat needs a weekly brush. Clean the long ears weekly, and wipe the drooping lips.",
                "Plan for one and a half to two hours of walking and tracking a day.",
            ],
            "good_fit": [
                "Are active and enjoy long walks",
                "Have a secure garden and a tall fence",
                "Want a friendly, laid-back family dog",
                "Like scent games and tracking",
            ],
            "think_twice": [
                "Live in a flat or close to neighbours who dislike noise",
                "Want a dog that comes back every time",
                "Have cats or small pets",
                "Dislike drooling or a hound smell",
            ],
            "daily": [
                "One and a half to two hours a day, preferably in places where it can use its nose. Keep it on a lead or long line, as it follows a scent and does not hear its name.",
                "It does not like long hours alone and may bay or dig. Company and exercise before you leave help.",
                "Calm and relaxed once exercised, happy to lie by the family. It needs a comfortable, solid bed.",
                "Gentle and patient with children, though its size means younger kids should be supervised.",
                "Typically friendly with other dogs, thanks to its pack hunting background. Cats and small pets may trigger the chase.",
                "Scent tracking, long walks, and hiking. Training needs patience and rewards.",
                "A long walk morning and evening, quiet company in between.",
            ],
            "quirks": [
                "Its voice is a deep, musical bawl that carries for a long way.",
                "The long ears and loose lips help it to hold scents and follow a trail.",
                "It is a relaxed hound at home, often found asleep on the sofa after a good outing.",
            ],
        },
        "ru": {
            "summary": "Дружелюбный, спокойный и преданный. Чёрно-подпалый кунхаунд — крупная красивая гончая с низким голосом, ласковым характером и сильной потребностью быть на улице.",
            "care": [
                "Короткую шерсть расчёсывайте раз в неделю. Раз в неделю чистите длинные уши и протирайте отвисшие губы.",
                "Рассчитывайте на полтора–два часа ходьбы и работы по следу в день.",
            ],
            "good_fit": [
                "Активны и любите долгие прогулки",
                "Есть огороженный двор и высокий забор",
                "Хотите дружелюбную неторопливую семейную собаку",
                "Любите игры на поиск и работу по следу",
            ],
            "think_twice": [
                "Живёте в квартире или рядом с соседями, которым мешает шум",
                "Хотите собаку, которая каждый раз возвращается",
                "Дома кошки или мелкие животные",
                "Не любите слюни и запах гончей",
            ],
            "daily": [
                "Полтора–два часа в день, лучше там, где можно пользоваться носом. Держите на поводке или длинной верёвке: идя за запахом, она не слышит команд.",
                "Долгое одиночество ей не нравится, она может лаять и рыть землю. Помогают общение и нагрузка перед уходом.",
                "После прогулки спокойная и расслабленная, с удовольствием лежит рядом с семьёй. Ей нужна удобная крепкая лежанка.",
                "Мягкая и терпеливая с детьми, но из-за размера за маленькими детьми нужен присмотр.",
                "Обычно дружелюбна к другим собакам благодаря стайному прошлому. Кошки и мелкие питомцы могут вызвать погоню.",
                "Поиск по следу, долгие прогулки и походы. Дрессировка требует терпения и поощрения.",
                "Долгая прогулка утром и вечером, а между ними спокойная компания.",
            ],
            "quirks": [
                "Её голос — низкий мелодичный лай, который слышен далеко.",
                "Длинные уши и свободные губы помогают удерживать запахи и идти по следу.",
                "Дома это спокойная гончая: после хорошей прогулки её часто находят спящей на диване.",
            ],
        },
    },
    "bloodhound": {
        "prey": "high",
        "en": {
            "summary": "Gentle, patient and driven by its nose. The Bloodhound is a big, wrinkled scent hound with a kind nature that wants to follow every interesting smell and then rest close to its people.",
            "care": [
                "Wipe the face folds and wash the long ears every week, as dirt and moisture stay there. Brush the short coat weekly, and wipe drool.",
                "Plan for one and a half to two hours a day, with a chance to use its nose.",
            ],
            "good_fit": [
                "Are patient and tolerant of drool",
                "Enjoy long walks and scent games",
                "Have a secure fence",
                "Want a gentle, friendly big dog",
            ],
            "think_twice": [
                "Want a tidy house with no drool",
                "Want a dog that comes back immediately",
                "Live in a small flat",
                "Cannot give the dog company",
            ],
            "daily": [
                "One and a half to two hours a day, with time to sniff. Always keep it on a lead or in a secure area, because it follows a scent and is deaf to calls.",
                "It does not like being left alone and may bay, chew or dig. Company and exercise help.",
                "A calm, gentle housemate that loves to lie by the family. It drools and shakes, so keep towels near.",
                "Kind and patient with children, but its size and strength mean play with small kids should be watched.",
                "Usually friendly with other dogs. Cats and pets may trigger the chase, so introduce them carefully.",
                "Tracking, scent games and long sniffing walks are its favourite activity. Training is slow and needs patience and treats.",
                "Walks in the morning and evening, and a long rest between.",
            ],
            "quirks": [
                "The Bloodhound's skin folds and long ears are thought to help hold scent close to its nose.",
                "A trained Bloodhound can follow and identify the trail of a particular person, which is why it is used in search work.",
                "It needs a face wipe and ear wash after meals and drinks, as drool and food stay in the folds.",
            ],
        },
        "ru": {
            "summary": "Мягкий, терпеливый и ведомый носом. Бладхаунд — большая складчатая гончая с добрым характером, которая хочет идти за каждым интересным запахом, а потом отдыхать рядом с людьми.",
            "care": [
                "Раз в неделю протирайте складки на морде и мойте длинные уши: в них остаются грязь и влага. Короткую шерсть расчёсывайте раз в неделю, слюни вытирайте.",
                "Рассчитывайте на полтора–два часа в день с возможностью использовать нос.",
            ],
            "good_fit": [
                "Терпеливы и спокойно относитесь к слюням",
                "Любите долгие прогулки и игры на поиск",
                "Есть надёжный забор",
                "Хотите мягкую дружелюбную крупную собаку",
            ],
            "think_twice": [
                "Хотите чистый дом без слюней",
                "Хотите собаку, которая сразу возвращается",
                "Живёте в маленькой квартире",
                "Не можете обеспечить собаке компанию",
            ],
            "daily": [
                "Полтора–два часа в день с временем на обнюхивание. Всегда держите на поводке или в безопасном месте: идя за запахом, он не слышит зов.",
                "Он не любит оставаться один и может лаять, грызть вещи и рыть землю. Помогают общение и нагрузка.",
                "Спокойный мягкий домашний друг, любит лежать рядом с семьёй. Пускает слюни и отряхивается, поэтому держите под рукой полотенца.",
                "Добр и терпелив с детьми, но из-за размера и силы за играми с малышами нужно следить.",
                "Обычно дружелюбен с другими собаками. Кошки и мелкие питомцы могут вызвать погоню, знакомьте их осторожно.",
                "Больше всего любит работу по следу, игры на поиск и долгие прогулки с обнюхиванием. Обучение идёт медленно и требует терпения и лакомств.",
                "Прогулки утром и вечером и долгий отдых между ними.",
            ],
            "quirks": [
                "Считается, что складки кожи и длинные уши помогают удерживать запах рядом с носом бладхаунда.",
                "Обученный бладхаунд может идти по следу конкретного человека и узнавать его, поэтому породу используют в поиске.",
                "После еды и питья нужно протирать морду и мыть уши: слюни и еда задерживаются в складках.",
            ],
        },
    },
    "dalmatian": {
        "prey": "moderate",
        "en": {
            "summary": "Athletic, outgoing and full of stamina. The Dalmatian is a spotted runner that loves people and loves exercise, and does best with an active family.",
            "care": [
                "The short coat sheds all year and needs a brush two or three times a week, or a rubber mitt. It is clean and has little smell.",
                "Plan for two hours of running, playing and training a day. Hearing should be checked in puppies with a BAER test.",
            ],
            "good_fit": [
                "Are very active and enjoy running or cycling",
                "Want an outgoing, loyal dog",
                "Are happy to give daily training",
                "Do not mind short white hairs",
            ],
            "think_twice": [
                "Want a calm, low-energy dog",
                "Are away from home most of the day",
                "Dislike dog hair on furniture and clothes",
                "Are not ready for health checks and testing",
            ],
            "daily": [
                "Two hours a day of real activity: running, cycling or long hikes. It needs to burn energy, and a bored Dalmatian can become noisy and destructive.",
                "It needs its people and may bark or chew when left. Exercise and company before you leave help.",
                "Friendly and busy indoors, wanting to be near the family. It sheds, so expect hair on clothes and furniture.",
                "Playful and loyal with children, though its energy and size can knock over small ones. Teach calm greetings.",
                "Usually sociable with dogs, and with horses, as it was bred to run with carriages. Small pets may trigger chasing.",
                "Running, agility, canicross, tricks and games. Training needs consistency and short sessions with rewards.",
                "A long active walk or run in the morning, a play session in the evening, and rest between.",
            ],
            "quirks": [
                "Dalmatian puppies are born pure white, and the spots appear within the first weeks and keep developing for up to two years.",
                "A noticeable share of Dalmatians are born with some hearing loss, so puppies should have a hearing (BAER) test.",
                "It is a fast, steady runner, so a Dalmatian makes a good partner for jogging and cycling.",
            ],
        },
        "ru": {
            "summary": "Спортивный, общительный и очень выносливый. Далматин — пятнистый бегун, который любит людей и движение и лучше всего чувствует себя в активной семье.",
            "care": [
                "Короткая шерсть линяет круглый год, расчёсывайте два–три раза в неделю или резиновой рукавицей. Собака чистая и почти не пахнет.",
                "Рассчитывайте на два часа бега, игр и занятий в день. Слух у щенков нужно проверить тестом BAER.",
            ],
            "good_fit": [
                "Очень активны и любите бег или велосипед",
                "Хотите общительную преданную собаку",
                "Готовы ежедневно заниматься с собакой",
                "Не против коротких белых волос",
            ],
            "think_twice": [
                "Хотите спокойную собаку с небольшой энергией",
                "Большую часть дня не бываете дома",
                "Не любите собачью шерсть на мебели и одежде",
                "Не готовы к проверкам здоровья и тестам",
            ],
            "daily": [
                "Два часа в день настоящей нагрузки: бег, велосипед или долгие походы. Ей нужно тратить энергию, иначе скучающий далматин становится шумным и разрушительным.",
                "Ей нужны люди, оставшись одна, она может лаять и грызть вещи. Помогают нагрузка и общение перед уходом.",
                "Дома дружелюбная и деятельная, хочет быть рядом с семьёй. Она линяет, так что ожидайте шерсть на одежде и мебели.",
                "Игрива и предана детям, но из-за энергии и размеров может сбить малыша. Учите спокойному приветствию.",
                "Обычно общительна с собаками и лошадьми, ведь её вывели бегать рядом с каретами. Мелкие питомцы могут вызвать погоню.",
                "Бег, аджилити, каникросс, трюки и игры. Дрессировка требует последовательности и коротких занятий с поощрением.",
                "Долгая активная прогулка или бег утром, игры вечером и отдых между ними.",
            ],
            "quirks": [
                "Щенки далматина рождаются чисто белыми, пятна появляются в первые недели и продолжают проявляться до двух лет.",
                "Заметная часть далматинов рождается с нарушением слуха, поэтому щенков нужно проверять на слух (тест BAER).",
                "Это быстрый и выносливый бегун, поэтому далматин — хороший партнёр для пробежек и велопрогулок.",
            ],
        },
    },
    "drever": {
        "prey": "high",
        "en": {
            "summary": "Cheerful, sturdy and hardworking. The Drever is a small, long-bodied Swedish scent hound with a loud voice that loves tracking and being close to its family.",
            "care": [
                "The short dense coat needs a weekly brush. Check the ears and trim the nails regularly.",
                "Plan for an hour to an hour and a half of walks and scent games a day. Keep the weight lean to protect the back.",
            ],
            "good_fit": [
                "Enjoy outdoor walks and tracking games",
                "Want a friendly, medium-sized family dog",
                "Have a secure fence",
                "Can accept a dog that follows scent",
            ],
            "think_twice": [
                "Want a dog that comes back every time",
                "Live close to noise-sensitive neighbours",
                "Are away from home most of the day",
                "Have small pets",
            ],
            "daily": [
                "An hour to an hour and a half a day, with chances to sniff. Keep it on a lead, as it will follow a scent far.",
                "It likes company and can bark or howl when left alone. A routine and exercise help.",
                "Friendly and easygoing indoors once it has exercised, though it will bark to tell you about visitors.",
                "Playful and good-natured with children. Teach kids to be gentle with its long back.",
                "Usually fine with dogs it knows. A strong hunting instinct means small animals need care.",
                "Scent games, tracking and long walks. Training with rewards and patience works well.",
                "Active walks morning and evening with rest between.",
            ],
            "quirks": [
                "The Drever has a loud voice and tracks by scent, calling as it goes.",
                "The long, low body is sturdy, so it copes with rough ground and thick undergrowth.",
                "It is a friendly working hound that enjoys family life as much as the outdoors.",
            ],
        },
        "ru": {
            "summary": "Весёлая, крепкая и трудолюбивая собака. Древер — небольшая длиннотелая шведская гончая с громким голосом, которая любит работу по следу и быть рядом с семьёй.",
            "care": [
                "Короткую плотную шерсть расчёсывайте раз в неделю. Проверяйте уши и регулярно стригите когти.",
                "Рассчитывайте на час–полтора прогулок и игр на поиск в день. Не давайте набирать вес, чтобы беречь спину.",
            ],
            "good_fit": [
                "Любите прогулки на природе и игры на поиск",
                "Хотите дружелюбную собаку среднего размера для семьи",
                "Есть надёжный забор",
                "Готовы к собаке, которая идёт за запахом",
            ],
            "think_twice": [
                "Хотите собаку, которая каждый раз возвращается",
                "Живёте рядом с соседями, чувствительными к шуму",
                "Большую часть дня не бываете дома",
                "Дома есть мелкие животные",
            ],
            "daily": [
                "Час–полтора в день с возможностью обнюхивать. Держите на поводке: она может уйти далеко за запахом.",
                "Любит компанию и может лаять или выть, оставшись одна. Помогают распорядок и нагрузка.",
                "После прогулки дома дружелюбная и спокойная, но лаем сообщит о гостях.",
                "Игрива и добродушна с детьми. Научите ребёнка бережно обращаться с её длинной спиной.",
                "Обычно ладит со знакомыми собаками. Сильный охотничий инстинкт требует осторожности с мелкими животными.",
                "Игры на поиск, работа по следу и долгие прогулки. Хорошо работает дрессировка с поощрением и терпением.",
                "Активные прогулки утром и вечером и отдых между ними.",
            ],
            "quirks": [
                "У древера громкий голос: идя по следу, он подаёт голос.",
                "Длинное низкое тело крепкое, поэтому собака справляется с неровной местностью и густым подлеском.",
                "Это дружелюбная рабочая гончая, которой одинаково нравятся семейная жизнь и прогулки на природе.",
            ],
        },
    },
    "otterhound": {
        "prey": "high",
        "en": {
            "summary": "Big, shaggy and good-natured. The Otterhound is a rare, water-loving scent hound with a happy, easygoing nature that loves long walks and swims.",
            "care": [
                "The rough, oily double coat needs brushing two or three times a week to prevent knots, and a trim every few months. Wipe the beard after meals and wash the ears weekly.",
                "Plan for one and a half to two hours a day, ideally with some water.",
            ],
            "good_fit": [
                "Love long walks and water",
                "Have a large home and a secure garden",
                "Want a friendly, relaxed companion",
                "Can manage a big, shaggy dog",
            ],
            "think_twice": [
                "Want a tidy, low-shedding dog",
                "Live in a small flat",
                "Want a dog that always returns off lead",
                "Are away from home most of the day",
            ],
            "daily": [
                "One and a half to two hours a day, with scent trails, hills and water. Keep it on a lead near water or wildlife, as it follows a scent.",
                "It does not like long hours alone and can bay or dig. Company and exercise help.",
                "A friendly, big housemate that likes to lie close to the family. It is messy after drinking, so keep towels ready.",
                "Gentle, patient and playful with children. Its size means supervision with small kids.",
                "Often friendly with dogs, as it comes from a pack. Small pets may trigger its hunting instinct.",
                "Swimming, tracking, long walks and scent games. Training is slow and needs patience.",
                "Active morning and evening, relaxing between. Rough coat needs a regular brush.",
            ],
            "quirks": [
                "There are fewer than a thousand Otterhounds in the world, which makes it one of the rarest breeds.",
                "Its feet are webbed and its coat is oily and waterproof, so it loves to swim.",
                "The shaggy beard and moustache collect water and food, so a wipe after meals is part of the routine.",
            ],
        },
        "ru": {
            "summary": "Большая, лохматая и добродушная собака. Аутерхаунд — редкая гончая, любящая воду, с весёлым и спокойным характером, которая любит долгие прогулки и плавание.",
            "care": [
                "Жёсткую жирную шерсть расчёсывайте два–три раза в неделю, чтобы не было колтунов, и подстригайте раз в несколько месяцев. После еды протирайте бороду, раз в неделю мойте уши.",
                "Рассчитывайте на полтора–два часа в день, лучше с водой.",
            ],
            "good_fit": [
                "Любите долгие прогулки и воду",
                "Есть большой дом и надёжный двор",
                "Хотите дружелюбного спокойного компаньона",
                "Справитесь с большой лохматой собакой",
            ],
            "think_twice": [
                "Хотите аккуратную собаку, почти не линяющую",
                "Живёте в маленькой квартире",
                "Хотите собаку, которая всегда возвращается без поводка",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Полтора–два часа в день, со следами, холмами и водой. Рядом с водой и дикими животными держите на поводке: она идёт за запахом.",
                "Долгое одиночество ей не нравится, она может лаять и рыть землю. Помогают общение и нагрузка.",
                "Дружелюбная крупная домашняя собака, любит лежать рядом с семьёй. После питья оставляет лужи, поэтому держите полотенца под рукой.",
                "Мягкая, терпеливая и игривая с детьми. Из-за размера за малышами нужен присмотр.",
                "Часто дружелюбна с собаками, ведь происходит из своры. Мелкие питомцы могут пробудить охотничий инстинкт.",
                "Плавание, работа по следу, долгие прогулки и игры на поиск. Обучение идёт медленно и требует терпения.",
                "Активные утро и вечер и отдых между ними. Жёсткая шерсть требует регулярной расчёски.",
            ],
            "quirks": [
                "В мире меньше тысячи аутерхаундов, поэтому это одна из самых редких пород.",
                "У неё перепончатые лапы и жирная водонепроницаемая шерсть, поэтому она любит плавать.",
                "Лохматые борода и усы собирают воду и еду, поэтому протирание после еды входит в распорядок.",
            ],
        },
    },
    "rhodesian-ridgeback": {
        "prey": "high",
        "en": {
            "summary": "Dignified, loyal and strong. The Rhodesian Ridgeback is an athletic hound with a calm, reserved nature at home and plenty of stamina outdoors.",
            "care": [
                "The short sleek coat needs a weekly brush. Check the ears and nails, and give a warm coat in cold weather.",
                "Plan for one and a half to two hours of running and training a day.",
            ],
            "good_fit": [
                "Are active and enjoy running, hiking or cycling",
                "Can give firm, calm, consistent training from puppyhood",
                "Have a secure fence",
                "Want a devoted family guardian",
            ],
            "think_twice": [
                "Are a first-time dog owner",
                "Want a dog that welcomes every visitor",
                "Have small pets or cats that are not used to it",
                "Cannot give daily exercise",
            ],
            "daily": [
                "One and a half to two hours a day, with room to run. Keep it on a lead in public, as it has a strong chase instinct.",
                "It bonds closely with its family and does not like long hours alone. Bored, it may chew or dig.",
                "Calm and clean indoors once exercised, a quiet presence that stays close to the family. It is wary of strangers.",
                "Loyal and gentle with its own children. Because it is strong, always supervise play with small kids.",
                "Often reserved with unfamiliar dogs, particularly of the same sex. Early socialisation is important, and small animals can trigger a chase.",
                "Running, hiking, cycling, lure coursing and obedience. Training should be firm, fair and rewarding.",
                "Active outings morning and evening, with long rest in between.",
            ],
            "quirks": [
                "The ridge is a strip of hair along the back that grows in the opposite direction to the rest of the coat.",
                "A health point for puppy buyers: reputable breeders check for dermoid sinus, a skin tube near the ridge area.",
                "It is a clean dog with a short coat that sheds little and has hardly any smell.",
            ],
        },
        "ru": {
            "summary": "Достойный, преданный и сильный. Родезийский риджбек — атлетичная собака, спокойная и сдержанная дома и очень выносливая на улице.",
            "care": [
                "Короткую гладкую шерсть расчёсывайте раз в неделю. Проверяйте уши и когти, а в холод надевайте тёплую одежду.",
                "Рассчитывайте на полтора–два часа бега и занятий в день.",
            ],
            "good_fit": [
                "Активны и любите бег, походы или велосипед",
                "Можете с щенячьего возраста заниматься твёрдо, спокойно и последовательно",
                "Есть надёжный забор",
                "Хотите преданного защитника семьи",
            ],
            "think_twice": [
                "Это ваша первая собака",
                "Хотите собаку, которая рада каждому гостю",
                "Дома мелкие животные или кошки, не знакомые с собакой",
                "Не можете обеспечить ежедневную нагрузку",
            ],
            "daily": [
                "Полтора–два часа в день с местом для бега. В людных местах держите на поводке: у риджбека сильный инстинкт погони.",
                "Он тесно привязан к семье и не любит долгого одиночества. От скуки может грызть вещи и рыть землю.",
                "После нагрузки дома спокойный и чистоплотный, тихо держится рядом с семьёй. К чужим относится настороженно.",
                "Предан и мягок с детьми своей семьи. Из-за силы всегда наблюдайте за играми с малышами.",
                "К незнакомым собакам, особенно своего пола, часто относится сдержанно. Важна ранняя социализация, а мелкие животные могут вызвать погоню.",
                "Бег, походы, велосипед, курсинг и послушание. Дрессировка должна быть твёрдой, справедливой и с поощрением.",
                "Активные прогулки утром и вечером и долгий отдых между ними.",
            ],
            "quirks": [
                "Риджбек — это полоска шерсти вдоль спины, которая растёт в обратную сторону по сравнению с остальной шерстью.",
                "Важно при покупке щенка: добросовестные заводчики проверяют на дермоидный синус — кожный канал около гребня.",
                "Это чистоплотная собака с короткой шерстью, которая мало линяет и почти не пахнет.",
            ],
        },
    },
    "slovakian-hound": {
        "prey": "high",
        "en": {
            "summary": "Hardy, loyal and alert. The Slovakian Hound is a rare black-and-tan scent hound with a strong voice and good stamina that is devoted to its family and to the outdoors.",
            "care": [
                "The short dense coat needs a weekly brush. Check the ears and nails regularly.",
                "Plan for one and a half to two hours a day of walking, hiking and scent work.",
            ],
            "good_fit": [
                "Are active and enjoy long outdoor days",
                "Have a secure garden",
                "Want a loyal, hardy hound",
                "Like scent work and tracking",
            ],
            "think_twice": [
                "Live in a small flat",
                "Want a dog that always returns when called",
                "Have cats or small pets",
                "Are away from home most of the day",
            ],
            "daily": [
                "One and a half to two hours a day on varied terrain. Keep it on a lead or long line, as it follows scents.",
                "It likes company and may bay or dig when bored. Exercise before you leave helps.",
                "Calm indoors after exercise, but alert and ready to bark at a sound.",
                "Loyal and patient with family children. Supervise play with very small kids.",
                "Usually good with dogs it knows. Small animals can trigger its hunting instinct.",
                "Tracking, scent work, hiking and long walks. Training is easiest with patience and rewards.",
                "Active outings morning and evening and rest between.",
            ],
            "quirks": [
                "The black-and-tan coat is dense and weatherproof, so it stays comfortable in rain and cold.",
                "It has a clear, loud voice, and it uses it to follow a trail.",
                "It is a rare breed, so expect to wait for a puppy and to have to travel.",
            ],
        },
        "ru": {
            "summary": "Выносливая, преданная и бдительная собака. Словацкий копов — редкая чёрно-подпалая гончая с сильным голосом и хорошей выносливостью, преданная своей семье и прогулкам на природе.",
            "care": [
                "Короткую плотную шерсть расчёсывайте раз в неделю. Регулярно проверяйте уши и когти.",
                "Рассчитывайте на полтора–два часа ходьбы, походов и поиска в день.",
            ],
            "good_fit": [
                "Активны и любите долгие дни на природе",
                "Есть надёжный двор",
                "Хотите преданную выносливую гончую",
                "Нравится работа по запаху и следу",
            ],
            "think_twice": [
                "Живёте в маленькой квартире",
                "Хотите собаку, которая всегда возвращается по зову",
                "Дома кошки или мелкие животные",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Полтора–два часа в день на разной местности. Держите на поводке или длинной верёвке: она идёт за запахом.",
                "Любит компанию, от скуки может лаять и рыть землю. Нагрузка перед уходом помогает.",
                "После нагрузки спокойна дома, но бдительна и готова залаять на звук.",
                "Предана и терпелива с детьми семьи. Игры с совсем маленькими детьми контролируйте.",
                "Обычно хорошо ладит со знакомыми собаками. Мелкие животные могут пробудить охотничий инстинкт.",
                "Работа по следу, поиск, походы и долгие прогулки. Проще всего обучать с терпением и поощрением.",
                "Активные прогулки утром и вечером и отдых между ними.",
            ],
            "quirks": [
                "Чёрно-подпалая шерсть плотная и защищает от погоды, поэтому собаке комфортно в дождь и холод.",
                "У неё чёткий громкий голос, и она использует его, идя по следу.",
                "Порода редкая, поэтому щенка придётся подождать и, возможно, поехать за ним.",
            ],
        },
    },
}


def forwards(apps, schema_editor):
    apply_content(apps, DOGS)


class Migration(migrations.Migration):
    dependencies = [("woof", "0073_group5_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
