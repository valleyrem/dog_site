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
    "boxer": {
        "prey": "moderate",
        "en": {
            "summary": "Cheerful, athletic and endlessly playful. The Boxer is a loyal family dog that stays young at heart for years and loves to be in the middle of everything.",
            "care": "The short coat needs a quick brush once a week and a wipe after muddy walks. Plan for about one and a half hours of walks and play every day.\nBoxers dislike extreme heat and cold, so keep walks short in hot weather and give it a warm coat in winter.",
            "good_fit": [
                "Are active and enjoy daily walks and games",
                "Want a loyal, cheerful family dog",
                "Are at home for much of the day",
                "Can be patient with a slowly maturing, bouncy puppy",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Want a quiet, calm dog",
                "Dislike a bit of drool and snoring",
                "Are not ready for a strong dog that jumps up in greeting",
            ],
            "daily": [
                "About one and a half hours a day, with a good run or a game of fetch. Boxers have plenty of stamina and enjoy new routes. Keep walks short in hot weather.",
                "A Boxer wants to be with its people and does not like long hours alone. Left bored, it may chew, dig or bark.",
                "Happy to live in a house or a flat if exercise is regular. It follows the family from room to room and often sleeps close to someone, snoring a little.",
                "Patient and playful with children, and famous for loving them. Because it is strong and bouncy, play with small kids should be supervised.",
                "Usually friendly with dogs and often with the household cat. Some Boxers are pushy with unfamiliar dogs, so start socialising early.",
                "Fetch, tug, running alongside a bike, obedience and agility all suit it. It learns well when training is short, cheerful and rewarded.",
                "Active mornings and evenings with a nap in between. Boxers keep a puppy's energy for two or three years, then settle into a calmer adult.",
            ],
            "quirks": [
                "Boxers use their front paws in play, like little boxers, and this may be where the name comes from.",
                'When happy, a Boxer wiggles its whole body into a "kidney bean" shape and may jump with joy.',
                "It matures slowly and keeps a playful, puppy-like character well into adulthood.",
            ],
        },
        "ru": {
            "summary": "Весёлый, спортивный и неутомимый в играх. Боксёр — преданная семейная собака, которая долго остаётся молодой душой и любит быть в центре событий.",
            "care": "Короткую шерсть достаточно быстро расчёсывать раз в неделю и протирать после грязных прогулок. Рассчитывайте примерно на полтора часа прогулок и игр в день.\nБоксёры плохо переносят сильную жару и холод: в жару гуляйте недолго, а зимой надевайте тёплую одежду.",
            "good_fit": [
                "Активны и любите ежедневные прогулки и игры",
                "Хотите преданную весёлую семейную собаку",
                "Значительную часть дня бываете дома",
                "Готовы терпеливо растить энергичного щенка, который взрослеет медленно",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Хотите тихую спокойную собаку",
                "Не любите слюни и храп",
                "Не готовы к сильной собаке, которая прыгает на вас при встрече",
            ],
            "daily": [
                "Около полутора часов в день, с хорошим бегом или игрой в апорт. Выносливости у боксёров много, и им нравятся новые маршруты. В жару гуляйте недолго.",
                "Боксёр хочет быть рядом с людьми и не любит долго оставаться один. От скуки может грызть вещи, рыть и лаять.",
                "Хорошо живёт и в доме, и в квартире, если прогулки регулярные. Ходит за семьёй из комнаты в комнату, часто спит рядом с кем-то из людей и немного похрапывает.",
                "Терпелив и игрив с детьми, известен тем, что их обожает. Но он сильный и энергичный, поэтому игры с малышами нужно контролировать.",
                "Обычно дружелюбен к собакам и часто к домашней кошке. Некоторые боксёры напористы с незнакомыми собаками, поэтому социализируйте его с раннего возраста.",
                "Ему подходят апорт, перетягивание, бег рядом с велосипедом, послушание и аджилити. Он хорошо учится, если занятия короткие, весёлые и с поощрением.",
                "Активные утро и вечер, днём сон. Боксёры сохраняют щенячью энергию два–три года, а потом становятся спокойнее.",
            ],
            "quirks": [
                "В играх боксёры работают передними лапами, как настоящие боксёры, и, возможно, отсюда и название.",
                "Когда боксёр рад, он извивается всем телом, изгибаясь «бобом», и может подпрыгивать от радости.",
                "Он взрослеет медленно и надолго сохраняет игривый, почти щенячий характер.",
            ],
        },
    },
    "bulldog": {
        "prey": "low",
        "en": {
            "summary": "Calm, friendly and surprisingly gentle. The Bulldog is a sturdy companion that loves its family, its naps and a short, relaxed walk.",
            "care": "Wipe the facial folds and the wrinkles over the nose with a damp cloth every day and dry them well. Brush the short coat once a week.\nKeep walks short and slow in warm weather, and always give it shade and fresh water. Watch its weight, as it enjoys food.",
            "good_fit": [
                "Want a calm, affectionate indoor companion",
                "Enjoy short, relaxed walks",
                "Live in a flat or small house",
                "Are at home for much of the day",
            ],
            "think_twice": [
                "Want a dog for running, hiking or long outings",
                "Live in a very hot climate",
                "Dislike snoring, drool and snorting",
                "Are away from home most of the day",
            ],
            "daily": [
                "Two or three short walks, about 30 to 45 minutes in total. A Bulldog enjoys a slow stroll and sniffing around more than a run. In hot weather go out early or late.",
                "It can manage a few hours alone, but it prefers to be with people. Without company it may become bored and sulk.",
                "A true homebody. It likes a cool spot on the floor, a soft bed or the sofa next to you. Expect snoring, snorting and a calm presence.",
                "Patient and gentle with children, and sturdy enough to put up with some noise. Still, supervise toddlers, as the Bulldog is heavy and dislikes rough handling.",
                "Usually friendly with other dogs and pets. Some males can be pushy with other dogs, so socialise early.",
                "Short games, gentle fetch and sniffing walks suit it. Training is best kept short and rewarded with treats, since it is easy-going but not eager to work hard.",
                "A calm rhythm of short outings, meals and long naps. Plan for the cool parts of the day and give it a comfortable place to rest.",
            ],
            "quirks": [
                "The Bulldog is a national symbol of Britain, used in cartoons and posters for its determined look.",
                "Its rolling, waddling gait is unmistakable.",
                "Despite the grumpy face, a Bulldog is one of the sweetest and most affectionate breeds.",
            ],
        },
        "ru": {
            "summary": "Спокойный, дружелюбный и удивительно мягкий. Бульдог — крепкий компаньон, который любит свою семью, дневной сон и короткую неспешную прогулку.",
            "care": "Каждый день протирайте влажной тканью складки на морде и над носом и хорошо вытирайте насухо. Короткую шерсть расчёсывайте раз в неделю.\nВ тёплую погоду гуляйте недолго и медленно, всегда обеспечивайте тень и свежую воду. Следите за весом: он любит поесть.",
            "good_fit": [
                "Хотите спокойного ласкового домашнего компаньона",
                "Любите короткие неспешные прогулки",
                "Живёте в квартире или небольшом доме",
                "Значительную часть дня бываете дома",
            ],
            "think_twice": [
                "Хотите собаку для бега, походов или долгих выходов",
                "Живёте в очень жарком климате",
                "Не любите храп, слюни и сопение",
                "Большую часть дня не бываете дома",
            ],
            "daily": [
                "Две–три короткие прогулки, около 30–45 минут в сумме. Бульдог больше любит неспешно идти и обнюхивать всё вокруг, чем бегать. В жару выходите рано утром или поздно вечером.",
                "Несколько часов один выдержит, но предпочитает быть с людьми. Без компании может заскучать и обидеться.",
                "Настоящий домосед. Любит прохладное место на полу, мягкую лежанку или диван рядом с вами. Приготовьтесь к храпу, сопению и спокойному присутствию.",
                "Терпелив и мягок с детьми и достаточно крепок, чтобы перенести шум. Но малышей лучше не оставлять без присмотра: бульдог тяжёлый и не любит грубого обращения.",
                "Обычно дружелюбен к собакам и другим животным. Некоторые кобели напористы с другими собаками, поэтому социализируйте его с раннего возраста.",
                "Ему подходят короткие игры, лёгкий апорт и прогулки с обнюхиванием. Занятия лучше проводить короткие и поощрять лакомством: он уживчивый, но не любит напрягаться.",
                "Спокойный ритм: короткие прогулки, еда и долгий сон. Планируйте день на прохладные часы и обеспечьте ему удобное место для отдыха.",
            ],
            "quirks": [
                "Бульдог — национальный символ Великобритании: его изображают в карикатурах и на плакатах за решительный вид.",
                "Его вразвалку, перекатывающаяся походка узнаётся сразу.",
                "Несмотря на угрюмый вид, бульдог — одна из самых добрых и ласковых пород.",
            ],
        },
    },
    "dobermann": {
        "prey": "moderate",
        "en": {
            "summary": "Elegant, fast and deeply devoted. The Dobermann is a smart, sensitive companion that wants to be close to its person and works best with calm, fair training.",
            "care": "The short, smooth coat needs a quick brush once a week. Plan for about two hours of walks, runs and training a day.\nIt has no thick undercoat, so it feels the cold: give it a jacket in winter and a warm place to sleep.",
            "good_fit": [
                "Are active and want a partner for runs and training",
                "Want a loyal dog that stays close",
                "Have experience with large, energetic dogs",
                "Can give it daily attention and a warm place indoors",
            ],
            "think_twice": [
                "Are away from home most of the day",
                "Live in a very cold climate and cannot dress the dog warmly",
                "Do not have time for daily exercise and training",
                "Want a dog that welcomes every stranger",
            ],
            "daily": [
                "About two hours a day, including a run. It loves speed and does well beside a bike or on a long line. Walks in the cold need a jacket.",
                "A Dobermann is deeply attached to its people and does not like to be alone for long. Without company it may become anxious or destructive.",
                "Calm and affectionate indoors after exercise. It likes to lie close to you or lean against your legs, and it watches the home and the door.",
                "Loyal and protective with its family, and gentle with children it knows. Its size and strength mean that games with small children should be supervised.",
                "Often friendly with dogs it grew up with, but can be wary of unfamiliar ones. Socialise early and meet new animals calmly.",
                "Obedience, agility, tracking and running sports suit it. It learns very quickly and responds best to calm, consistent training and plenty of praise.",
                "An active morning, a rest, and an evening outing. It does best with a stable routine and regular time with its person.",
            ],
            "quirks": [
                'Dobermanns are often called "Velcro dogs" because they stick close to their person.',
                "The breed is named after Louis Dobermann, from the town of Apolda in Germany, who created it in the 1890s.",
                "A short coat with little undercoat means many Dobermanns love sunny spots and wear a coat in winter.",
            ],
        },
        "ru": {
            "summary": "Изящный, быстрый и глубоко преданный. Доберман — умный чуткий компаньон, который хочет быть рядом со своим человеком и лучше всего учится на спокойных и справедливых занятиях.",
            "care": "Короткую гладкую шерсть достаточно быстро расчёсывать раз в неделю. Рассчитывайте примерно на два часа прогулок, бега и занятий в день.\nПодшёрстка у него почти нет, поэтому он мёрзнет: зимой надевайте попону и обеспечьте тёплое место для сна.",
            "good_fit": [
                "Активны и хотите партнёра для бега и занятий",
                "Хотите преданную собаку, которая держится рядом",
                "Уже держали крупных энергичных собак",
                "Готовы каждый день уделять ей внимание и держать в тёплом доме",
            ],
            "think_twice": [
                "Большую часть дня не бываете дома",
                "Живёте в очень холодном климате и не сможете тепло одевать собаку",
                "Нет времени на ежедневные прогулки и занятия",
                "Хотите собаку, которая радуется любому чужому человеку",
            ],
            "daily": [
                "Около двух часов в день, включая бег. Любит скорость и хорошо бегает рядом с велосипедом или на длинном поводке. В холод нужна попона.",
                "Доберман очень привязан к своим людям и не любит долго оставаться один. Без компании может тревожиться и портить вещи.",
                "Дома спокоен и ласков после нагрузки. Любит лежать рядом с вами или прислоняться к ногам и присматривает за домом и дверью.",
                "Предан семье, защищает её и мягок со знакомыми детьми. Из-за размера и силы игры с малышами нужно контролировать.",
                "Часто дружелюбен к собакам, с которыми вырос, но с незнакомыми бывает настороженным. Социализируйте рано и знакомьте с новыми животными спокойно.",
                "Ему подходят послушание, аджилити, следовая работа и бег. Он очень быстро учится и лучше всего реагирует на спокойные последовательные занятия и щедрую похвалу.",
                "Активное утро, отдых и вечерняя прогулка. Ему лучше всего при постоянном распорядке и регулярном времени с хозяином.",
            ],
            "quirks": [
                "Доберманов часто называют «собаками-липучками»: они держатся рядом со своим человеком.",
                "Порода названа в честь Луи Добермана из немецкого города Апольда, который вывел её в 1890-х годах.",
                "Короткая шерсть почти без подшёрстка: многие доберманы любят солнечные места, а зимой носят попону.",
            ],
        },
    },
    "great-dane": {
        "prey": "low",
        "en": {
            "summary": "A gentle giant with a big heart. The Great Dane is calm, friendly and loving, and thinks it is a lap dog despite its size.",
            "care": "The short coat needs a brush once a week. Plan for about an hour and a half of walks a day, with a free stroll rather than hard running.\nA Great Dane needs a big bed, a sturdy lead, plenty of room and a food budget to match its size. Do not push it into hard exercise while young.",
            "good_fit": [
                "Have a spacious home and a large car",
                "Want a calm, friendly giant",
                "Are at home for much of the day",
                "Can afford the food and equipment of a very large dog",
            ],
            "think_twice": [
                "Live in a very small flat",
                "Are away from home most of the day",
                "Dislike drool and a big dog on the sofa",
                "Cannot lift or handle a strong 60 kg dog",
            ],
            "daily": [
                "About an hour and a half a day in total, in two or three walks. A Great Dane enjoys long, easy strolls more than fast running. Young dogs should not be pushed to run a lot.",
                "A few hours are fine for an adult that is used to it, but it is a people dog. Left alone for long, it may become bored and destroy things, and a bored giant can do real damage.",
                "Calm indoors, often lying on the floor or the sofa. It needs space to turn around and a bed of its own, and its tail can clear a coffee table.",
                "Very gentle and patient with children. Because of its size it can knock small kids over by accident, so supervise play.",
                "Usually friendly with other dogs and sometimes with cats if raised with them. Early socialisation helps it stay relaxed around smaller animals.",
                "Easy walks, gentle fetch and short training sessions suit it. It is eager to please and responds best to a soft, patient approach.",
                "Walks, meals and long naps. Many Great Danes sleep up to 16 hours a day and take their time getting up.",
            ],
            "quirks": [
                "A Great Dane called Zeus held the record as the world's tallest dog, at about 112 cm at the shoulder.",
                "Despite the name, the breed is German, where it is called the Deutsche Dogge.",
                "The cartoon dog Scooby-Doo is a Great Dane.",
            ],
        },
        "ru": {
            "summary": "Добрый великан с большим сердцем. Немецкий дог спокоен, дружелюбен и ласков и считает себя комнатной собачкой, несмотря на размер.",
            "care": "Короткую шерсть расчёсывайте раз в неделю. Рассчитывайте примерно на полтора часа прогулок в день: лучше неспешная ходьба, чем быстрый бег.\nДогу нужны большая лежанка, прочный поводок, много места и бюджет на корм под стать размеру. Не давайте щенку тяжёлую нагрузку, пока он растёт.",
            "good_fit": [
                "Живёте в просторном доме и есть большая машина",
                "Хотите спокойного дружелюбного великана",
                "Значительную часть дня бываете дома",
                "Можете позволить себе корм и снаряжение для очень крупной собаки",
            ],
            "think_twice": [
                "Живёте в очень маленькой квартире",
                "Большую часть дня не бываете дома",
                "Не любите слюни и огромную собаку на диване",
                "Не справитесь с сильной собакой весом 60 кг",
            ],
            "daily": [
                "Около полутора часов в день в сумме, в две–три прогулки. Дог любит долгие спокойные прогулки больше, чем быстрый бег. Молодых собак не заставляйте много бегать.",
                "Взрослая собака, привыкшая к этому, выдержит несколько часов, но дог любит быть с людьми. Если оставлять надолго, может заскучать и испортить вещи, а у скучающего великана это выходит основательно.",
                "Дома спокоен, часто лежит на полу или диване. Ему нужно место, чтобы развернуться, и своя лежанка, а хвостом он легко сметает вещи со столика.",
                "Очень мягок и терпелив с детьми. Из-за размера может случайно сбить малыша с ног, поэтому игры нужно контролировать.",
                "Обычно дружелюбен к другим собакам, а с кошками ладит, если вырос с ними. Ранняя социализация помогает ему спокойно относиться к мелким животным.",
                "Ему подходят неспешные прогулки, мягкий апорт и короткие занятия. Он стремится угодить и лучше всего отзывается на мягкий терпеливый подход.",
                "Прогулки, еда и долгий сон. Многие доги спят до 16 часов в сутки и встают не торопясь.",
            ],
            "quirks": [
                "Дог по кличке Зевс считался самой высокой собакой в мире: около 112 см в холке.",
                "Несмотря на название, порода немецкая: по-немецки она называется Deutsche Dogge.",
                "Мультяшный пёс Скуби-Ду — немецкий дог.",
            ],
        },
    },
    "hovawart": {
        "prey": "moderate",
        "en": {
            "summary": "Loyal, steady and watchful. The Hovawart is an old German farm dog that keeps a close eye on home and family, and bonds deeply with its people.",
            "care": "The long, slightly wavy coat needs brushing two or three times a week and daily during the shed. Plan for about two hours of walks and activity a day.\nThe Hovawart matures slowly, so start training and socialisation early and keep going into the third year.",
            "good_fit": [
                "Have a house with a garden and time for long walks",
                "Want a loyal, watchful family dog",
                "Are patient with a slowly maturing dog",
                "Are at home for much of the day",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Live in a small flat",
                "Are away from home most of the day",
                "Want a dog that welcomes every visitor",
            ],
            "daily": [
                "About two hours a day, including long walks and some off-lead time where it is safe. It enjoys hiking, swimming and being outdoors in any weather.",
                "A Hovawart bonds closely with its family and does not like to be alone for long. Without enough company, it may bark or dig.",
                "Calm in the house after exercise. A garden and a view of the street keep it content, and it likes to know who is coming and going.",
                "Gentle and protective with the family's children. It is big and strong, so supervise play with smaller kids.",
                "Often reserved with strangers and with unfamiliar dogs. It generally gets on with household pets if introduced early.",
                "Tracking, search games, obedience, hiking and swimming suit it. It likes to have a job and learns best from patient training.",
                "Active outings in the morning and evening and a calm day in between. It thrives on routine and time with its family.",
            ],
            "quirks": [
                'The name Hovawart means "yard keeper": the dog watches over the farm.',
                "It comes in three colours: black, black and gold, and blond.",
                "It is slow to mature and may keep a puppy's playfulness until about three years old.",
            ],
        },
        "ru": {
            "summary": "Преданный, уравновешенный и бдительный. Ховаварт — старая немецкая фермерская собака, которая следит за домом и семьёй и глубоко привязывается к людям.",
            "care": "Длинную слегка волнистую шерсть расчёсывайте два–три раза в неделю, а в линьку каждый день. Рассчитывайте примерно на два часа прогулок и занятий в день.\nХоваварт взрослеет медленно, поэтому начинайте занятия и социализацию рано и продолжайте их до трёх лет.",
            "good_fit": [
                "Живёте в доме с участком и есть время на долгие прогулки",
                "Хотите преданную бдительную семейную собаку",
                "Готовы терпеливо растить медленно взрослеющую собаку",
                "Значительную часть дня бываете дома",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Живёте в маленькой квартире",
                "Большую часть дня не бываете дома",
                "Хотите собаку, которая радуется каждому гостю",
            ],
            "daily": [
                "Около двух часов в день, включая долгие прогулки и свободный бег там, где это безопасно. Любит походы, плавание и улицу в любую погоду.",
                "Ховаварт тесно привязан к семье и не любит долго оставаться один. Без достаточного общения может лаять или рыть.",
                "Дома спокоен после нагрузки. Участок и вид на улицу делают его довольным: ему нравится знать, кто приходит и уходит.",
                "Мягок и защищает детей семьи. Он большой и сильный, поэтому игры с малышами нужно контролировать.",
                "С незнакомыми людьми и собаками часто сдержан. С домашними животными обычно ладит, если познакомить их рано.",
                "Ему подходят следовая работа, игры на поиск, послушание, походы и плавание. Он любит, когда у него есть дело, и лучше всего учится на терпеливых занятиях.",
                "Прогулки утром и вечером и спокойный день между ними. Ему хорошо при распорядке и времени, проведённом с семьёй.",
            ],
            "quirks": [
                "Название «ховаварт» означает «хранитель двора»: собака следит за хозяйством.",
                "Бывает трёх окрасов: чёрный, чёрно-подпалый и блонд.",
                "Он взрослеет медленно и может сохранять щенячью игривость до трёх лет.",
            ],
        },
    },
    "cane-corso": {
        "prey": "moderate",
        "en": {
            "summary": "Noble, powerful and devoted. The Italian Cane Corso is a calm, watchful guardian that is gentle with its own family and needs an owner who is steady and confident.",
            "care": "The short coat needs a brush once or twice a week, more during the shed. Plan for around an hour and a half of walks and activity a day.\nTrain and socialise from the first weeks. A strong dog needs a calm, consistent owner who sets clear rules.",
            "good_fit": [
                "Have experience with large, strong breeds",
                "Have a house with a secure garden",
                "Are calm, consistent and confident with training",
                "Want a loyal guardian that stays close to the family",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Live in a small flat",
                "Want a dog that welcomes every visitor",
                "Do not have time for early socialisation and training",
            ],
            "daily": [
                "About an hour and a half a day, in two walks, with a place to run. It is happiest with purposeful walks and a good sniff. Keep it on a lead in public.",
                "A Cane Corso is devoted to its family and does not like long isolation. Alone for hours, it may become bored, noisy or destructive.",
                "Calm indoors and watchful. It likes to lie where it can see the door and the family, and takes its role as guardian seriously.",
                "Affectionate and patient with the children of the family. Its size and strength call for supervision with small kids and visitors.",
                "Often wary of unfamiliar dogs and people. It can live with other pets if they are introduced early, but may chase small animals.",
                "Obedience, tracking and weight-pull sports suit it. It learns well from a calm, confident handler and short, varied sessions.",
                "Two active outings with long periods of calm rest. It prefers a stable routine and a clearly defined place in the home.",
            ],
            "quirks": [
                "The breed almost disappeared in the twentieth century, and enthusiasts saved it from the 1970s.",
                "It was recognised by the international federation (FCI) in 1996.",
                "It comes in black, grey, fawn and red, often with a dark mask on the face.",
            ],
        },
        "ru": {
            "summary": "Благородный, мощный и преданный. Итальянский кане-корсо — спокойный бдительный страж, мягкий со своей семьёй, которому нужен уверенный и уравновешенный владелец.",
            "care": "Короткую шерсть расчёсывайте раз–два в неделю, а в линьку чаще. Рассчитывайте примерно на полтора часа прогулок и занятий в день.\nЗанимайтесь и социализируйте с первых недель. Сильной собаке нужен спокойный последовательный хозяин, который устанавливает чёткие правила.",
            "good_fit": [
                "Уже держали крупных сильных собак",
                "Живёте в доме с огороженным участком",
                "Спокойны, последовательны и уверены в дрессировке",
                "Хотите преданного стража, который держится рядом с семьёй",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Живёте в маленькой квартире",
                "Хотите собаку, которая радуется каждому гостю",
                "Нет времени на раннюю социализацию и занятия",
            ],
            "daily": [
                "Около полутора часов в день, в две прогулки, и нужно место для бега. Ему нравятся целенаправленные прогулки и возможность всё обнюхать. В общественных местах держите на поводке.",
                "Кане-корсо предан семье и не любит долгой изоляции. Если оставлять на много часов, может заскучать, шуметь или портить вещи.",
                "Дома спокоен и бдителен. Любит лежать там, откуда видно дверь и семью, и серьёзно относится к своей роли сторожа.",
                "Ласков и терпелив с детьми семьи. Из-за размера и силы за малышами и приходящими детьми нужен присмотр.",
                "К незнакомым собакам и людям часто настороженный. С другими животными может жить, если познакомить их рано, но способен погнаться за мелкими.",
                "Ему подходят послушание, следовая работа и спортивное перетаскивание грузов. Он хорошо учится у спокойного уверенного хозяина на коротких разнообразных занятиях.",
                "Две активные прогулки и долгий спокойный отдых между ними. Предпочитает постоянный режим и чётко определённое место в доме.",
            ],
            "quirks": [
                "Порода почти исчезла в XX веке, а с 1970-х годов её спасли энтузиасты.",
                "Международная кинологическая федерация (FCI) признала её в 1996 году.",
                "Бывает чёрного, серого, рыжего и красного окраса, часто с тёмной маской на морде.",
            ],
        },
    },
    "miniature-pinscher": {
        "prey": "high",
        "en": {
            "summary": "Bold, quick and full of energy in a small body. The Miniature Pinscher is a lively companion that walks with its head high and thinks it is much bigger than it is.",
            "care": "The short, shiny coat needs only a quick brush or wipe once a week. Plan for about an hour of walks and play a day.\nIt feels the cold, so give it a coat in winter and keep it away from drafts.",
            "good_fit": [
                "Want a lively, alert small dog",
                "Live in a flat and enjoy several short walks",
                "Are at home for a good part of the day",
                "Enjoy training short tricks and games",
            ],
            "think_twice": [
                "Want a quiet, calm lap dog",
                "Share a home with hamsters, rabbits or other small pets",
                "Have a garden with low fencing",
                "Have very noise-sensitive neighbours",
            ],
            "daily": [
                "About an hour a day, in two or three walks, with time to run on a lead or in a safe area. It is quick and loves to dash, but it needs a secure place, because it will chase anything small.",
                "A Min Pin that is bored will bark or find its own entertainment. It can manage a few hours alone if it has had exercise and has toys.",
                "Suits a flat as long as there are daily walks. It is alert, quick to bark at sounds and likes to look out of the window.",
                "Playful with older children who treat it kindly. Small children can hurt it by accident, so teach them to be gentle.",
                "Usually fine with dogs it grew up with, and sometimes bold with much larger ones, so keep an eye on it. Small pets can trigger its chase instinct.",
                "Short games, agility, trick training and puzzle toys suit it. It learns quickly but is independent, so keep sessions short and rewarding.",
                "Bursts of activity through the day with rests on a warm cushion between. It likes to be wherever you are, ideally under a blanket.",
            ],
            "quirks": [
                'Its nickname is the "King of Toys", for its confident, proud attitude.',
                "It has a high-stepping gait, like a little trotting horse.",
                "Many Min Pins like to climb on furniture, and some find their way onto the highest shelf.",
            ],
        },
        "ru": {
            "summary": "Смелый, быстрый и полный энергии в маленьком теле. Цвергпинчер — живой компаньон, который ходит с высоко поднятой головой и уверен, что намного больше, чем есть на самом деле.",
            "care": "Короткую блестящую шерсть достаточно быстро расчесать или протереть раз в неделю. Рассчитывайте примерно на час прогулок и игр в день.\nОн мёрзнет, поэтому зимой надевайте одежду и оберегайте от сквозняков.",
            "good_fit": [
                "Хотите живую бдительную маленькую собаку",
                "Живёте в квартире и любите несколько коротких прогулок",
                "Значительную часть дня бываете дома",
                "Любите учить короткие трюки и играть",
            ],
            "think_twice": [
                "Хотите тихую спокойную диванную собачку",
                "Живёте с хомяками, кроликами и другими мелкими животными",
                "У вас участок с низким забором",
                "У вас очень чувствительные к шуму соседи",
            ],
            "daily": [
                "Около часа в день, в две–три прогулки, с возможностью побегать на поводке или в безопасном месте. Он быстрый и любит нестись, но место должно быть огорожено: он погонится за всем мелким.",
                "Заскучавший цвергпинчер лает или находит себе развлечения сам. Несколько часов один выдержит, если до этого погулял и у него есть игрушки.",
                "Подходит для квартиры, если ежедневно есть прогулки. Он бдителен, быстро лает на звуки и любит смотреть в окно.",
                "Игрив со старшими детьми, которые относятся к нему бережно. Маленькие дети могут случайно его ушибить, поэтому учите их быть нежными.",
                "Обычно ладит с собаками, с которыми вырос, а с намного более крупными бывает дерзким, поэтому присматривайте. Мелкие животные могут вызвать у него желание погнаться.",
                "Ему подходят короткие игры, аджилити, трюки и игрушки-головоломки. Он быстро учится, но самостоятелен, поэтому занятия делайте короткими и с наградой.",
                "Всплески активности в течение дня и отдых на тёплой подушке между ними. Любит быть там, где вы, лучше всего под одеялом.",
            ],
            "quirks": [
                "Его называют «королём игрушечных пород» за уверенный гордый вид.",
                "У него высокая «лошадиная» походка с поднятыми лапами, как у маленького рысака.",
                "Многие цвергпинчеры любят забираться на мебель, а некоторые находят путь на самую высокую полку.",
            ],
        },
    },
    "rottweiler": {
        "prey": "moderate",
        "en": {
            "summary": "Strong, calm and devoted. The Rottweiler is a confident guardian that is deeply attached to its family and happiest when it has a role and clear, fair leadership.",
            "care": "The short coat needs a brush once or twice a week, more during the shed. Plan for about an hour and a half of walks and activity a day.\nBegin training and socialisation in the first weeks. A strong dog needs a calm owner with clear rules.",
            "good_fit": [
                "Have experience with large, strong breeds",
                "Are calm, firm and fair with training",
                "Have a house with a secure garden",
                "Want a loyal dog that stays close to the family",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Live in a small flat",
                "Want a dog that welcomes every visitor",
                "Do not have time for early socialisation and training",
            ],
            "daily": [
                "About an hour and a half a day, in two walks, with some training mixed in. It likes purposeful walks and a game of fetch. In hot weather go out early or late.",
                "A Rottweiler prefers to be near its people. Left alone for long, it may become bored and noisy or destructive.",
                "Calm and watchful indoors. It lies where it can see the family, often on your feet, and takes its role as guardian seriously.",
                "Affectionate and patient with children of the family, and a good playmate. Because of its size, supervise games with small children.",
                "Can be wary of unfamiliar dogs, and some males are dominant. It lives well with household pets raised with it.",
                "Obedience, tracking, carting and weight-pull sports suit it. It learns well from fair, consistent handling and short sessions.",
                "Regular outings and plenty of rest. A steady routine and a clear place in the family keep it balanced.",
            ],
            "quirks": [
                "Many Rottweilers lean against your legs, and may try to sit on your lap despite their size.",
                'Rottweilers "talk": a low, rumbling sound that owners compare to purring.',
                "The breed is named after the German town of Rottweil, where butchers' dogs drove cattle to market.",
            ],
        },
        "ru": {
            "summary": "Сильный, спокойный и преданный. Ротвейлер — уверенный страж, глубоко привязанный к семье, который счастливее всего, когда у него есть роль и чёткое справедливое руководство.",
            "care": "Короткую шерсть расчёсывайте раз–два в неделю, в линьку чаще. Рассчитывайте примерно на полтора часа прогулок и занятий в день.\nНачинайте занятия и социализацию с первых недель. Сильной собаке нужен спокойный хозяин с чёткими правилами.",
            "good_fit": [
                "Уже держали крупных сильных собак",
                "Спокойны, тверды и справедливы в дрессировке",
                "Живёте в доме с огороженным участком",
                "Хотите преданную собаку, которая держится рядом с семьёй",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Живёте в маленькой квартире",
                "Хотите собаку, которая радуется каждому гостю",
                "Нет времени на раннюю социализацию и занятия",
            ],
            "daily": [
                "Около полутора часов в день, в две прогулки, с элементами занятий. Любит прогулки с целью и игру в апорт. В жару выходите рано или поздно.",
                "Ротвейлер предпочитает быть рядом с людьми. Если надолго оставлять одного, может заскучать, шуметь или портить вещи.",
                "Дома спокоен и бдителен. Лежит там, где видит семью, нередко на ваших ногах, и серьёзно относится к роли сторожа.",
                "Ласков и терпелив с детьми семьи, хороший товарищ по играм. Из-за размера игры с малышами нужно контролировать.",
                "К незнакомым собакам бывает настороженным, а некоторые кобели доминируют. С домашними животными, с которыми вырос, уживается хорошо.",
                "Ему подходят послушание, следовая работа, возка груза и спортивное перетаскивание. Он хорошо учится на справедливом последовательном подходе и коротких занятиях.",
                "Регулярные прогулки и много отдыха. Постоянный распорядок и чёткое место в семье помогают ему быть уравновешенным.",
            ],
            "quirks": [
                "Многие ротвейлеры прислоняются к ногам и пытаются сесть на колени, несмотря на размер.",
                "Ротвейлеры «разговаривают»: издают низкий рокочущий звук, который владельцы сравнивают с мурлыканьем.",
                "Порода названа по немецкому городу Ротвайль, где собаки мясников гоняли скот на рынок.",
            ],
        },
    },
    "saint-bernard": {
        "prey": "low",
        "en": {
            "summary": "Gentle, patient and warm-hearted. The Saint Bernard is a big, calm family dog that loves company, cool weather and a quiet place on the floor beside you.",
            "care": "Brush the coat two or three times a week, and daily during the shed, especially in the long-haired variety. Wipe the mouth and face after meals, as drooling is part of life.\nPlan for about an hour of walks a day. Avoid heat, and give it a cool place to rest.",
            "good_fit": [
                "Have a spacious home and a large car",
                "Want a calm, patient family dog",
                "Enjoy cool weather and relaxed walks",
                "Do not mind drool",
            ],
            "think_twice": [
                "Live in a warm climate or a small flat",
                "Dislike drool and fur",
                "Are away from home most of the day",
                "Cannot handle a very large, heavy dog",
            ],
            "daily": [
                "About an hour a day in total, in a couple of easy walks. It prefers a steady stroll to running, and loves cold weather and snow. In summer go out early or late.",
                "It does not like long hours alone. Left bored, it may whine, dig or chew, and with a dog this big the damage is not small.",
                "Calm in the house, mostly lying on a cool floor. It needs space for its size and a place away from heat. Be ready for drool on furniture and floors.",
                "Very patient and gentle with children. Its size can knock small kids over by accident, so supervise play.",
                "Usually friendly with other dogs and pets. Early socialisation keeps it relaxed with everyone, including cats.",
                "Easy walks, simple obedience and gentle games suit it. Training should be patient, as it learns at its own pace and responds to kindness.",
                "Calm days with short outings and long rests. It enjoys routine and company, and likes to sleep near its family.",
            ],
            "quirks": [
                "The most famous Saint Bernard, Barry, lived at the Alpine hospice in the early 1800s and is said to have helped to save dozens of travellers.",
                "The little brandy barrel under its chin is a myth, popularised by a painting from 1820.",
                "The Swiss national breed standard for the Saint Bernard was written in 1887.",
            ],
        },
        "ru": {
            "summary": "Добрый, терпеливый и сердечный. Сенбернар — большая спокойная семейная собака, которая любит компанию, прохладную погоду и тихое место на полу рядом с вами.",
            "care": "Расчёсывайте шерсть два–три раза в неделю, а в линьку каждый день, особенно у длинношёрстных. После еды вытирайте морду и пасть: слюни тут часть жизни.\nРассчитывайте примерно на час прогулок в день. Избегайте жары и обеспечьте прохладное место для отдыха.",
            "good_fit": [
                "Живёте в просторном доме и есть большая машина",
                "Хотите спокойную терпеливую семейную собаку",
                "Любите прохладную погоду и неспешные прогулки",
                "Не боитесь слюней",
            ],
            "think_twice": [
                "Живёте в тёплом климате или в маленькой квартире",
                "Не любите слюни и шерсть",
                "Большую часть дня не бываете дома",
                "Не справитесь с очень крупной тяжёлой собакой",
            ],
            "daily": [
                "Около часа в день в сумме, в пару неспешных прогулок. Предпочитает ровный шаг бегу и обожает холод и снег. Летом выходите рано или поздно.",
                "Не любит долго оставаться один. От скуки может выть, рыть или грызть вещи, а у такой огромной собаки это не мелочи.",
                "Дома спокоен, чаще всего лежит на прохладном полу. Ему нужно место по размеру и уголок подальше от жары. Будьте готовы к слюням на мебели и полу.",
                "Очень терпелив и мягок с детьми. Из-за размера может случайно сбить малыша с ног, поэтому игры нужно контролировать.",
                "Обычно дружелюбен к собакам и другим животным. Ранняя социализация помогает ему спокойно относиться ко всем, включая кошек.",
                "Ему подходят неспешные прогулки, простое послушание и мягкие игры. Заниматься нужно терпеливо: он учится в своём темпе и отзывается на доброту.",
                "Спокойные дни с короткими прогулками и долгим отдыхом. Он любит порядок и компанию и спит рядом с семьёй.",
            ],
            "quirks": [
                "Самый известный сенбернар, Барри, жил в альпийском приюте в начале 1800-х годов и, как говорят, помог спасти десятки путников.",
                "Бочонок с бренди на шее — выдумка, которую распространила картина 1820 года.",
                "Швейцарский национальный стандарт сенбернара был написан в 1887 году.",
            ],
        },
    },
    "shar-pei": {
        "prey": "moderate",
        "en": {
            "summary": "Dignified, loyal and quietly independent. The Shar Pei is a calm, clean dog with a wrinkled face and a deep bond with its family.",
            "care": "The short, bristly coat needs a weekly brush. Wipe the skin folds on the face and body and dry them well, especially after rain or a bath.\nPlan for about an hour of walks a day. Avoid heat, and begin socialisation early, since it is reserved with strangers.",
            "good_fit": [
                "Want a calm, loyal, clean dog",
                "Are patient and consistent with training",
                "Enjoy relaxed walks",
                "Are at home for a good part of the day",
            ],
            "think_twice": [
                "Want a dog that welcomes every stranger",
                "Live in a very hot climate",
                "Are away from home most of the day",
                "Do not have time to care for the skin folds",
            ],
            "daily": [
                "About an hour a day, in two walks. It likes a steady pace and sniffing around, and dislikes heat and rain. Keep it on a lead around unfamiliar dogs.",
                "It can manage a few hours alone when used to it, but is a family dog. Boredom shows up as chewing or digging.",
                "Quiet and tidy in the house. It likes a favourite spot near the family and does not bark much, though it watches everything.",
                "Loyal and calm with children it knows. Teach small kids to treat it gently, since it dislikes rough handling.",
                "Often reserved with unfamiliar dogs, and some are dominant. It can live with other pets if raised together.",
                "Short walks, simple games and puzzle toys suit it. Training should be consistent and rewarding, as it is independent and does not like repetition.",
                "A quiet, regular routine: two walks, meals and long rests. It likes a calm household and a predictable day.",
            ],
            "quirks": [
                'The name Shar Pei means "sand skin", for its rough, bristly coat.',
                "In 1978 the Guinness Book of Records listed it as the rarest dog breed in the world.",
                "A puppy is the most wrinkled, and the folds are deepest on the head and neck.",
            ],
        },
        "ru": {
            "summary": "Достойный, преданный и спокойно независимый. Шарпей — тихая чистоплотная собака с морщинистой мордой и глубокой привязанностью к семье.",
            "care": "Короткую жёсткую шерсть расчёсывайте раз в неделю. Протирайте складки кожи на морде и теле и хорошо вытирайте насухо, особенно после дождя или купания.\nРассчитывайте примерно на час прогулок в день. Избегайте жары и начинайте социализацию рано: с чужими он сдержан.",
            "good_fit": [
                "Хотите спокойную преданную чистоплотную собаку",
                "Терпеливы и последовательны в занятиях",
                "Любите неспешные прогулки",
                "Значительную часть дня бываете дома",
            ],
            "think_twice": [
                "Хотите собаку, которая радуется каждому чужому",
                "Живёте в очень жарком климате",
                "Большую часть дня не бываете дома",
                "Нет времени ухаживать за складками кожи",
            ],
            "daily": [
                "Около часа в день, в две прогулки. Любит ровный шаг и обнюхивать всё вокруг, не любит жару и дождь. Рядом с незнакомыми собаками держите на поводке.",
                "Несколько часов один выдержит, когда привыкнет, но это семейная собака. Скука проявляется в том, что она грызёт вещи или роет.",
                "Дома тихий и аккуратный. У него есть любимое место рядом с семьёй, он мало лает, но внимательно следит за всем.",
                "Предан и спокоен со знакомыми детьми. Учите малышей обращаться с ним мягко: грубого обращения он не терпит.",
                "К незнакомым собакам часто сдержан, а некоторые доминируют. С другими животными может жить, если вырос вместе с ними.",
                "Ему подходят короткие прогулки, простые игры и игрушки-головоломки. Занятия должны быть последовательными и с наградой: он независим и не любит повторений.",
                "Тихий регулярный распорядок: две прогулки, еда и долгий отдых. Любит спокойный дом и предсказуемый день.",
            ],
            "quirks": [
                "Название «шарпей» означает «песчаная кожа»: так назвали за жёсткую щетинистую шерсть.",
                "В 1978 году Книга рекордов Гиннесса назвала шарпея самой редкой породой в мире.",
                "Больше всего морщин у щенка, а самые глубокие складки остаются на голове и шее.",
            ],
        },
    },
    "tibetan-mastiff": {
        "prey": "low",
        "en": {
            "summary": "Majestic, watchful and independent. The Tibetan Mastiff is an ancient guardian with a lion-like mane, calm with its family and serious about its territory.",
            "care": "The thick double coat needs brushing two or three times a week, and daily during the heavy annual shed. Plan for about an hour of walks a day.\nIt needs a large, securely fenced garden and a cool place to rest. Socialise early, and train with patience, as it thinks for itself.",
            "good_fit": [
                "Have a house with a large, high-fenced garden",
                "Have experience with independent guardian breeds",
                "Live in a cool climate",
                "Want a calm, dignified guard dog",
            ],
            "think_twice": [
                "Are getting your first dog",
                "Live in a flat or a hot climate",
                "Have close neighbours who dislike night barking",
                "Want a dog that obeys at once",
            ],
            "daily": [
                "About an hour a day, with a slow, steady pace. It is not a runner, and it should not be let off the lead in an open place, as it may wander. Walks in cool weather suit it best.",
                "It is calm alone for a few hours but needs a securely fenced garden. Unsupervised, it may dig or bark at night.",
                "Calm and dignified in the house, usually lying in a cool spot where it can watch the door. It does best with a large home and garden.",
                "Gentle and protective with the family's children. It is large and strong, so supervise small kids and visitors.",
                "Often wary of strangers and unfamiliar dogs. It gets on with other pets in the family if raised with them.",
                "Long walks and calm outdoor time suit it. It learns slowly and does what it sees fit, so train patiently and keep sessions short.",
                "A quiet day and an active night: many Tibetan Mastiffs are most alert in the evening and at night, and rest in the cool of the day.",
            ],
            "quirks": [
                "The thick mane around its neck gives it a lion-like look.",
                "It is traditionally a night guard: it rests by day and stays alert after dark.",
                "It sheds the thick undercoat once a year, usually in spring, and the coat comes out in large clumps.",
            ],
        },
        "ru": {
            "summary": "Величественный, бдительный и независимый. Тибетский мастиф — древний страж с гривой, как у льва, спокойный с семьёй и серьёзный в охране территории.",
            "care": "Густую двойную шерсть расчёсывайте два–три раза в неделю, а в сильную ежегодную линьку каждый день. Рассчитывайте примерно на час прогулок в день.\nЕму нужен большой надёжно огороженный участок и прохладное место для отдыха. Социализируйте рано и занимайтесь терпеливо: он привык думать сам.",
            "good_fit": [
                "Живёте в доме с большим участком и высоким забором",
                "Уже держали самостоятельных охранных собак",
                "Живёте в прохладном климате",
                "Хотите спокойного достойного сторожа",
            ],
            "think_twice": [
                "Берёте первую собаку",
                "Живёте в квартире или в жарком климате",
                "У вас близкие соседи, которым мешает ночной лай",
                "Хотите собаку, которая сразу выполняет команды",
            ],
            "daily": [
                "Около часа в день, медленным ровным шагом. Он не бегун, и в открытых местах его нельзя спускать с поводка: он может уйти. Лучше всего ему подходят прогулки в прохладную погоду.",
                "Несколько часов один проводит спокойно, но нужен надёжно огороженный участок. Без присмотра может рыть и лаять ночью.",
                "Дома спокоен и величав, обычно лежит в прохладном месте, откуда видна дверь. Лучше всего ему в большом доме с участком.",
                "Мягок и защищает детей семьи. Он большой и сильный, поэтому за малышами и гостями нужен присмотр.",
                "К чужим людям и незнакомым собакам часто настороженный. С другими животными в семье ладит, если вырос с ними.",
                "Ему подходят долгие прогулки и спокойное время на улице. Он учится медленно и делает то, что считает нужным, поэтому занимайтесь терпеливо и недолго.",
                "Тихий день и активная ночь: многие тибетские мастифы наиболее бдительны вечером и ночью, а днём отдыхают в прохладе.",
            ],
            "quirks": [
                "Густая грива вокруг шеи придаёт ему сходство со львом.",
                "Традиционно это ночной сторож: днём он отдыхает, а после наступления темноты остаётся настороже.",
                "Раз в год, обычно весной, он сбрасывает густой подшёрсток, и шерсть выходит крупными клочьями.",
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
    dependencies = [("woof", "0067_kinder_wording")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
