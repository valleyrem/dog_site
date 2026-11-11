from django.db import migrations

LABELS = {
    "en": ["Walks", "Being alone", "At home", "Children", "Other animals", "Play and activities", "Daily routine"],
    "ru": ["Прогулки", "Одиночество", "Дома", "Дети", "Другие животные", "Игры и занятия", "Распорядок дня"],
}

DOGS = {
    "airedale-terrier": {
        "prey": "high",
        "en": {
            "summary": "Clever, brave and full of life. The Airedale is the largest of the terriers: a friendly, playful all-rounder that wants to be part of every family adventure.",
            "care": "The wiry coat sheds very little but needs brushing twice a week and a trim or hand-stripping every two to three months. Wipe the beard after meals and drinks.\nPlan for one and a half to two hours of walks, play and training every day.",
            "good_fit": ["Are active and enjoy long walks, hiking or swimming", "Want a clever, playful family dog", "Like training and giving a dog a job to do", "Have a secure garden or enough time outdoors"],
            "think_twice": ["Want a calm dog for a small flat", "Are away from home most of the day", "Have small pets such as rabbits or hamsters", "Do not want regular grooming costs"],
            "daily": [
                "One and a half to two hours a day with a good run, not just a stroll. An Airedale enjoys new routes, water and open spaces. Keep it on a lead near small animals, as the hunting instinct is strong.",
                "It likes to be with its people and does not do well with long hours alone. Bored and left by itself, it may dig, chew or bark.",
                "A good house dog when exercise is regular. It is happy to follow you around, join family life and then lie by your feet. A fenced garden is a real help.",
                "Playful and sturdy, and usually a great friend for older children who like to run and play. Young Airedales are bouncy, so supervise games with small kids.",
                "Often friendly with dogs it knows, though some are pushy with unfamiliar ones. Cats and small pets can trigger its chase instinct, so introduce them carefully from puppyhood.",
                "Fetch, swimming, hiking, tracking, agility and obedience all suit it. It learns quickly and enjoys training, but keep sessions short and varied or it loses interest.",
                "Active morning and evening, with play and training in between. It matures slowly, and stays playful until the age of two or three.",
            ],
            "quirks": ["The Airedale stays playful long into adulthood and matures only at two or three years old.", "Its wiry coat sheds very little, which makes it popular with owners who dislike dog hair around the house.", "A natural swimmer: the breed was developed in the Aire valley for hunting otters and rats along the river."],
        },
        "ru": {
            "summary": "Умный, смелый и полный жизни. Эрдельтерьер — самый крупный из терьеров: дружелюбный и игривый универсал, который хочет участвовать во всех семейных делах.",
            "care": "Жёсткая шерсть почти не линяет, но её нужно расчёсывать два раза в неделю и подстригать или тримминговать раз в два–три месяца. После еды и питья протирайте бороду.\nРассчитывайте на полтора–два часа прогулок, игр и занятий в день.",
            "good_fit": ["Активны и любите долгие прогулки, походы или плавание", "Хотите умную игривую семейную собаку", "Любите дрессировку и занятия с собакой", "Есть огороженный двор или много времени на улице"],
            "think_twice": ["Хотите спокойную собаку для маленькой квартиры", "Большую часть дня не бываете дома", "Дома живут мелкие животные: кролики или хомяки", "Не хотите регулярно платить за груминг"],
            "daily": [
                "Полтора–два часа в день с хорошим бегом, а не просто прогулкой. Эрдель любит новые маршруты, воду и открытые места. Рядом с мелкими животными держите его на поводке: охотничий инстинкт сильный.",
                "Он любит быть рядом с людьми и плохо переносит долгое одиночество. Оставшись один и заскучав, может рыть, грызть вещи и лаять.",
                "Хорошо живёт дома, если прогулки регулярные. Ходит за вами по комнатам, участвует в жизни семьи, а потом ложится у ног. Огороженный двор очень помогает.",
                "Игрив и вынослив, обычно отличный друг для детей постарше, которые любят бегать и играть. Молодые эрдели энергичны, поэтому игры с малышами нужно контролировать.",
                "Часто дружит с собаками, которых знает, но некоторые напористы с незнакомыми. Кошки и мелкие питомцы могут пробудить инстинкт погони, поэтому знакомьте их аккуратно, лучше с щенячьего возраста.",
                "Ему подходят апорт, плавание, походы, поиск по следу, аджилити и послушание. Он быстро учится и любит занятия, но делайте их короткими и разными, иначе ему станет скучно.",
                "Активные утро и вечер, а между ними игры и занятия. Взрослеет медленно и остаётся игривым до двух–трёх лет.",
            ],
            "quirks": ["Эрдельтерьер остаётся игривым и во взрослом возрасте и окончательно взрослеет только к двум–трём годам.", "Жёсткая шерсть почти не линяет, поэтому породу любят те, кому не нравится собачья шерсть в доме.", "Он прирождённый пловец: породу вывели в долине реки Эйр для охоты на выдр и крыс у воды."],
        },
    },
    "american-staffordshire-terrier": {
        "prey": "moderate",
        "en": {
            "summary": "Strong, loyal and very people-loving. The American Staffordshire Terrier is a muscular, athletic family dog that wants nothing more than to be close to its people.",
            "care": "The short coat needs a quick brush once a week and a wipe after muddy walks. Check the ears and nails regularly.\nPlan for about one and a half hours of exercise a day. It feels the cold, so give it a warm coat in winter.",
            "good_fit": ["Are active and enjoy daily exercise and games", "Want a loyal, affectionate companion", "Can give calm, consistent training and early socialisation", "Are at home for much of the day"],
            "think_twice": ["Are away from home most of the day", "Want a dog that gets along with every dog it meets", "Are new to dogs and want a very easy first dog", "Cannot give firm, regular training"],
            "daily": [
                "About one and a half hours a day, with a mix of brisk walking, running and games. It is strong, so a sturdy harness and training for walking on a loose lead are important.",
                "It bonds closely with its family and does not like long hours alone. Left bored, it may chew or become destructive.",
                "A real indoor companion that loves to be close. It will happily lean on you or try to sit on your lap, even though it is not a lap dog in size.",
                "Affectionate and often very patient with its own family's children. Because it is strong and enthusiastic, always supervise play with small kids.",
                "It can be friendly with other dogs, but many do not like dogs they do not know, especially of the same sex. Careful socialisation from puppyhood and a lead outdoors are a must.",
                "Weight pulling, agility, fetch with sturdy toys and tracking games are a good outlet. It learns well when training is positive, calm and consistent.",
                "Active morning and evening with a good rest in between. It is a keen companion for jogging or hiking once it has finished growing.",
            ],
            "quirks": ["Many Staffordshire Terriers lean their whole body against you, and some try to climb onto your lap.", "It is very athletic and enjoys dog sports such as weight pulling and agility.", "It has a short coat that sheds little, but it feels the cold and benefits from a coat in winter."],
        },
        "ru": {
            "summary": "Сильный, преданный и очень любит людей. Американский стаффордширский терьер — мускулистая спортивная семейная собака, которой важнее всего быть рядом со своими людьми.",
            "care": "Короткую шерсть достаточно быстро расчёсывать раз в неделю и протирать после грязных прогулок. Регулярно проверяйте уши и когти.\nРассчитывайте примерно на полтора часа нагрузки в день. Он мёрзнет, поэтому зимой надевайте тёплую одежду.",
            "good_fit": ["Активны и любите ежедневные нагрузки и игры", "Хотите преданную ласковую собаку-компаньона", "Можете спокойно и последовательно дрессировать и рано социализировать собаку", "Значительную часть дня бываете дома"],
            "think_twice": ["Большую часть дня не бываете дома", "Хотите собаку, которая ладит с любой встречной собакой", "Это ваша первая собака и вам нужна самая простая", "Не можете заниматься твёрдой регулярной дрессировкой"],
            "daily": [
                "Около полутора часов в день: быстрая ходьба, бег и игры. Он сильный, поэтому важны крепкая шлейка и обучение ходьбе на свободном поводке.",
                "Он сильно привязывается к семье и не любит долго оставаться один. От скуки может грызть вещи и портить мебель.",
                "Настоящий домашний компаньон, который любит быть рядом. С радостью прислонится к вам или попробует забраться на колени, хотя по размеру он не комнатная собачка.",
                "Ласков и часто очень терпелив с детьми своей семьи. Он сильный и увлекающийся, поэтому игры с малышами всегда нужно контролировать.",
                "Может дружить с другими собаками, но многие не любят незнакомых, особенно своего пола. Нужны аккуратная социализация с щенячьего возраста и поводок на улице.",
                "Хорошая отдушина: перетягивание тяжестей, аджилити, апорт с прочными игрушками и игры на поиск. Он хорошо учится, если дрессировка доброжелательная, спокойная и последовательная.",
                "Активные утро и вечер, а между ними хороший отдых. Когда вырастет, становится хорошим спутником для пробежек и походов.",
            ],
            "quirks": ["Многие стаффордширские терьеры прижимаются к человеку всем телом, а некоторые пытаются забраться на колени.", "Он очень спортивный и любит собачьи виды спорта, например перетягивание тяжестей и аджилити.", "Шерсть короткая и почти не линяет, но он мёрзнет, и зимой ему нужна одежда."],
        },
    },
    "bedlington-terrier": {
        "prey": "high",
        "en": {
            "summary": "Gentle at home, lively outdoors. The Bedlington looks like a little lamb, but it is a quick, athletic terrier that loves its family and enjoys a good run.",
            "care": "The soft, curly coat sheds very little but mats easily. Brush it several times a week and have it trimmed every six to eight weeks.\nPlan for about an hour of walks and play every day, with room to run safely.",
            "good_fit": ["Want a gentle, affectionate family dog", "Enjoy brisk walks and the chance to let a dog run", "Prefer a dog that sheds little", "Are happy to book regular grooming"],
            "think_twice": ["Have rabbits, hamsters or other small pets", "Are away from home most of the day", "Cannot let the dog off the lead in a safe place", "Do not want regular trimming"],
            "daily": [
                "About an hour a day with some off-lead running in a safe place. The Bedlington is fast and loves to chase, so a secure area matters. In between, it enjoys sniffing walks.",
                "It is attached to its family and prefers company. A few hours alone is fine once it is used to it, but long absences can lead to barking or chewing.",
                "Calm, soft-natured and happy to curl up beside you. Indoors it is quiet and affectionate, and it adapts well to a flat if it gets its outdoor time.",
                "Gentle and playful with children, and usually good with those who treat it kindly. Because it is not very big, small kids should be taught to handle it carefully.",
                "Often friendly with dogs it knows, though some stand their ground with others. The chase instinct is strong, so cats, rabbits and other small pets need careful introductions.",
                "Chasing a ball, running games, lure coursing, agility and tricks all suit it. It learns quickly and enjoys being close to you while it works.",
                "A lively walk in the morning and again later, with plenty of quiet time at home. Keep the grooming routine regular so the coat stays easy to manage.",
            ],
            "quirks": ["Bedlington puppies are born dark, and the coat lightens to blue, liver or sandy by about a year old.", "Behind the lamb-like look is a fast runner, so keep it on a lead where it could chase something.", "The curly coat sheds very little, but it grows quickly and needs a trim every six to eight weeks."],
        },
        "ru": {
            "summary": "Мягкий дома и живой на улице. Бедлингтон-терьер похож на ягнёнка, но на самом деле это быстрый спортивный терьер, который любит семью и хорошо побегать.",
            "care": "Мягкая кудрявая шерсть почти не линяет, но легко сваливается. Расчёсывайте её несколько раз в неделю и стригите каждые шесть–восемь недель.\nРассчитывайте примерно на час прогулок и игр в день, лучше с возможностью безопасно побегать.",
            "good_fit": ["Хотите мягкую ласковую семейную собаку", "Любите быстрые прогулки и можете дать собаке побегать", "Предпочитаете собаку, которая мало линяет", "Готовы регулярно ходить к грумеру"],
            "think_twice": ["Дома живут кролики, хомяки или другие мелкие питомцы", "Большую часть дня не бываете дома", "Не можете отпускать собаку с поводка в безопасном месте", "Не хотите регулярно стричь собаку"],
            "daily": [
                "Около часа в день, с бегом без поводка в безопасном месте. Бедлингтон быстрый и любит догонять, поэтому важна закрытая территория. В остальное время ему нравятся неспешные прогулки с обнюхиванием.",
                "Он привязан к семье и предпочитает быть с людьми. Несколько часов в одиночестве допустимы, когда он привык, но долгое отсутствие может привести к лаю и погрызенным вещам.",
                "Спокойный, мягкий по характеру, с удовольствием сворачивается рядом с вами. Дома тих и ласков, хорошо живёт в квартире, если получает свои прогулки.",
                "Мягок и игрив с детьми, обычно хорошо ладит с теми, кто относится к нему бережно. Он не очень крупный, поэтому малышей нужно научить аккуратному обращению.",
                "Часто дружит со знакомыми собаками, но некоторые умеют постоять за себя перед чужими. Инстинкт погони сильный, поэтому кошек, кроликов и других мелких питомцев знакомьте с ним осторожно.",
                "Ему подходят погоня за мячом, игры в беге, курсинг, аджилити и трюки. Он быстро учится и любит работать рядом с хозяином.",
                "Живая прогулка утром и ещё одна позже, а остальное время дома в покое. Следите за регулярным уходом, чтобы шерсть оставалась удобной.",
            ],
            "quirks": ["Щенки бедлингтона рождаются тёмными, а к году шерсть светлеет до голубого, печёночного или песочного цвета.", "За видом ягнёнка скрывается быстрый бегун, поэтому там, где он может за кем-то погнаться, держите его на поводке.", "Кудрявая шерсть почти не линяет, но быстро отрастает, и стричь её нужно каждые шесть–восемь недель."],
        },
    },
    "border-terrier": {
        "prey": "high",
        "en": {
            "summary": "Cheerful, hardy and affectionate. The Border Terrier is a small, friendly working terrier that is easy to live with and loves being part of the family.",
            "care": "The wiry coat sheds little. Brush it once or twice a week and have it hand-stripped two or three times a year to keep the texture.\nPlan for about an hour of walks and play every day. Check the garden fences, as it likes to dig and explore.",
            "good_fit": ["Are active and enjoy walks in all weather", "Want a cheerful, easy-going small dog", "Have children who like to play", "Can secure a garden against digging and escaping"],
            "think_twice": ["Want a dog that is happy to be alone for many hours", "Have rabbits, hamsters or other small pets", "Dislike digging and barking at passers-by", "Cannot let the dog run safely"],
            "daily": [
                "About an hour a day, and it will happily do more. The Border Terrier was bred to keep up with horses and hounds, so it has plenty of stamina for hikes. It follows scents, so keep it on a lead near wildlife.",
                "It likes company and does not do well with long hours alone. Bored, it may dig, chew or bark.",
                "A good house companion, calm indoors when it has had its exercise. It likes to be close to the family and curl up on a sofa or in a basket.",
                "Friendly, sturdy and tolerant, which makes it a good family dog. As with any dog, teach small children to be gentle.",
                "Usually easy-going with other dogs, but the hunting instinct is strong, so cats and small pets need careful introductions. Outdoors, it may chase anything that moves.",
                "Hiking, scent games, digging boxes, agility and obedience all suit it. It learns well and enjoys time with its people.",
                "Busy mornings and evenings, with plenty of rest in between. It adapts to the pace of the household if it gets enough activity.",
            ],
            "quirks": ["The name comes from the border between England and Scotland, where the breed worked, and its long legs let it keep up with horses.", "Its loose, thick skin protects it from bites and lets it squeeze into tight spaces.", "It loves to dig and can slip under a fence, so check the garden carefully."],
        },
        "ru": {
            "summary": "Весёлый, выносливый и ласковый. Бордер-терьер — небольшой дружелюбный рабочий терьер, с которым легко жить и который любит быть частью семьи.",
            "care": "Жёсткая шерсть мало линяет. Расчёсывайте её раз–два в неделю и делайте тримминг два–три раза в год, чтобы сохранить структуру.\nРассчитывайте примерно на час прогулок и игр в день. Проверяйте заборы в саду: он любит рыть и исследовать.",
            "good_fit": ["Активны и любите гулять в любую погоду", "Хотите весёлую неприхотливую небольшую собаку", "Есть дети, которые любят играть", "Можете защитить сад от подкопов и побегов"],
            "think_twice": ["Хотите собаку, которая спокойно остаётся одна на много часов", "Дома живут кролики, хомяки или другие мелкие питомцы", "Не любите, когда собака роет землю и лает на прохожих", "Не можете безопасно дать собаке побегать"],
            "daily": [
                "Около часа в день, и он с радостью выдержит больше. Бордер-терьера выводили, чтобы он поспевал за лошадьми и гончими, поэтому для походов у него много сил. Он идёт по запахам, поэтому рядом с дикими животными держите его на поводке.",
                "Он любит быть с людьми и плохо переносит долгое одиночество. От скуки может рыть, грызть вещи и лаять.",
                "Хороший домашний компаньон, дома спокоен, если погулял. Любит быть рядом с семьёй и сворачиваться на диване или в лежанке.",
                "Дружелюбен, вынослив и терпелив, поэтому хорошо подходит для семьи. Как и любую собаку, малышей нужно научить обращаться с ним бережно.",
                "Обычно спокойно относится к другим собакам, но охотничий инстинкт сильный, поэтому кошек и мелких питомцев знакомьте с ним осторожно. На улице он может погнаться за всем, что движется.",
                "Ему подходят походы, игры на поиск запаха, ящик с землёй для копания, аджилити и послушание. Он хорошо учится и любит заниматься вместе с хозяином.",
                "Занятые утро и вечер и много отдыха между ними. Он подстраивается под ритм семьи, если получает достаточно движения.",
            ],
            "quirks": ["Название связано с границей между Англией и Шотландией, где работала порода, а длинные ноги позволяли ей не отставать от лошадей.", "Свободная плотная кожа защищает его от укусов и помогает пролезать в узкие места.", "Он любит рыть землю и может подкопаться под забор, поэтому внимательно проверяйте сад."],
        },
    },
    "bull-terrier": {
        "prey": "moderate",
        "en": {
            "summary": "Playful, strong and devoted. The Bull Terrier is a one-of-a-kind dog with an egg-shaped head, a big heart and a sense of fun that lasts into old age.",
            "care": "The short coat needs a quick brush once a week. White dogs can sunburn, so use shade and pet-safe sun cream on bare skin in strong sun.\nPlan for about an hour and a half of walks and play every day. It does not like cold weather, so give it a coat in winter.",
            "good_fit": ["Want a playful, affectionate companion", "Are active and enjoy daily exercise and games", "Can give consistent, positive training from puppyhood", "Are at home for much of the day"],
            "think_twice": ["Are away from home most of the day", "Want a dog that is calm and easy for a first-time owner", "Have small pets", "Cannot give regular company and attention"],
            "daily": [
                "About an hour and a half a day, with brisk walking and games. A Bull Terrier is strong, so train it early to walk on a loose lead. Keep it on a lead around other dogs.",
                "It needs its people and does not like being left alone for long. Left bored, it may chew, dig or create its own entertainment.",
                "A true family companion that wants to be where you are, often on the sofa or on your feet. It is lively indoors when young, and calms down with age.",
                "Playful, affectionate and often devoted to children in its own family. Because it is strong and bouncy, always supervise play with small kids.",
                "It can get along with other dogs if it is socialised early, but some are pushy or dislike unfamiliar dogs. Introductions to cats and small pets should be careful.",
                "Fetch with sturdy toys, tug games, agility and tricks suit it. It learns best from short, fun, rewarded sessions, and it needs plenty of toys to keep its mind busy.",
                "Active morning and evening, with naps in between. Keep a regular routine, and give it jobs and games so it does not make its own fun.",
            ],
            "quirks": ["Its egg-shaped head is unique: no other breed has this long, downward-curved profile.", "The breed has starred in advertising, including Bullseye, the mascot of a large US store chain, and Spuds MacKenzie in the 1980s.", "White Bull Terriers have pale skin that can burn in strong sun, so shade and sun cream matter."],
        },
        "ru": {
            "summary": "Игривый, сильный и преданный. Бультерьер — собака ни на кого не похожая: с яйцевидной головой, большим сердцем и чувством юмора, которое остаётся до старости.",
            "care": "Короткую шерсть достаточно быстро расчёсывать раз в неделю. Белые собаки могут обгорать, поэтому в сильное солнце давайте тень и наносите безопасный для собак солнцезащитный крем на открытую кожу.\nРассчитывайте примерно на полтора часа прогулок и игр в день. Он не любит холод, поэтому зимой надевайте одежду.",
            "good_fit": ["Хотите игривую ласковую собаку-компаньона", "Активны и любите ежедневные нагрузки и игры", "Можете последовательно и доброжелательно дрессировать с щенячьего возраста", "Значительную часть дня бываете дома"],
            "think_twice": ["Большую часть дня не бываете дома", "Хотите спокойную собаку, с которой легко новичку", "Дома живут мелкие питомцы", "Не можете регулярно уделять внимание и общаться с собакой"],
            "daily": [
                "Около полутора часов в день: быстрая ходьба и игры. Бультерьер сильный, поэтому с раннего возраста учите его ходить на свободном поводке. Рядом с другими собаками держите его на поводке.",
                "Ему нужны люди, и он не любит надолго оставаться один. От скуки может грызть вещи, рыть и придумывать себе занятия.",
                "Настоящий семейный компаньон, который хочет быть там, где вы, часто на диване или у ваших ног. В молодости дома довольно активен, с возрастом становится спокойнее.",
                "Игрив, ласков и часто предан детям своей семьи. Он сильный и энергичный, поэтому игры с малышами всегда нужно контролировать.",
                "Может ладить с другими собаками, если его рано социализировать, но некоторые напористы или не любят незнакомых собак. Знакомить с кошками и мелкими питомцами нужно осторожно.",
                "Ему подходят апорт с прочными игрушками, перетягивание, аджилити и трюки. Лучше всего он учится на коротких весёлых занятиях с поощрением, и ему нужно много игрушек, чтобы занять ум.",
                "Активные утро и вечер, а между ними сон. Придерживайтесь распорядка и давайте ему задания и игры, чтобы он не придумывал развлечения сам.",
            ],
            "quirks": ["Яйцевидная голова бультерьера уникальна: такого длинного профиля с изгибом вниз нет ни у одной другой породы.", "Порода снималась в рекламе: например, бультерьер Буллзай стал талисманом большой американской сети магазинов, а Спадс Маккензи прославился в 1980-х.", "У белых бультерьеров светлая кожа, которая может обгореть на сильном солнце, поэтому важны тень и солнцезащитный крем."],
        },
    },
    "jack-russell-terrier": {
        "prey": "high",
        "en": {
            "summary": "Bright, brave and bursting with energy. The Jack Russell is a small terrier with a big personality that is always ready for the next game or adventure.",
            "care": "The coat is smooth, rough or broken, and needs only a weekly brush. Hand-strip the rough coat once or twice a year if you like.\nPlan for at least an hour and a half of walks, play and training every day. Secure the garden: it digs and jumps.",
            "good_fit": ["Are very active and enjoy long walks and games", "Want a bright, trainable small dog for activities", "Enjoy training and dog sports", "Have a securely fenced garden"],
            "think_twice": ["Want a calm lap dog", "Are away from home most of the day", "Have rabbits, hamsters or other small pets", "Dislike digging and barking"],
            "daily": [
                "At least an hour and a half a day, and the Jack Russell will happily take more. It needs real running, not just a stroll. Keep it on a lead where there is wildlife, as it will chase anything that moves.",
                "It does not enjoy long hours alone. Left bored, it can dig, chew and bark, so give it a toy to work on and some exercise before you leave.",
                "A busy little dog that likes to be in the middle of things. It can be calm indoors if it has had enough exercise, but it is always ready to play.",
                "Energetic and fun for active children who respect it. It does not always tolerate rough handling, so teach small kids to be gentle.",
                "Often friendly with dogs it knows, but it can be bold with strangers. The hunting instinct is strong, so small pets are not safe with it.",
                "Fetch, agility, flyball, tricks and scent games are perfect. It learns quickly and loves a challenge, so keep training short and varied.",
                "Active morning and evening, with several play sessions in between. A tired Jack Russell is a happy one, and a regular routine helps.",
            ],
            "quirks": ["A Jack Russell can jump about a metre high from a standing start, so fences need to be high and the garden secure.", "The breed is named after the English clergyman John Russell, who loved fox hunting and bred these dogs in the 19th century.", "With good care, many live to 14 to 16 years or even longer."],
        },
        "ru": {
            "summary": "Умный, смелый и полный энергии. Джек-рассел-терьер — небольшой терьер с большим характером, всегда готовый к новой игре и приключению.",
            "care": "Шерсть гладкая, жёсткая или промежуточная, и достаточно расчёсывать её раз в неделю. Жёсткую шерсть при желании тримминговать раз–два в год.\nРассчитывайте минимум на полтора часа прогулок, игр и занятий в день. Позаботьтесь о безопасном дворе: он роет землю и прыгает.",
            "good_fit": ["Очень активны и любите долгие прогулки и игры", "Хотите умную обучаемую небольшую собаку для занятий", "Любите дрессировку и собачьи виды спорта", "Есть надёжно огороженный двор"],
            "think_twice": ["Хотите спокойную комнатную собачку", "Большую часть дня не бываете дома", "Дома живут кролики, хомяки или другие мелкие питомцы", "Не любите, когда собака роет землю и лает"],
            "daily": [
                "Минимум полтора часа в день, и джек-рассел с радостью возьмёт больше. Ему нужен настоящий бег, а не просто прогулка. Там, где есть дикие животные, держите его на поводке: он погонится за всем, что движется.",
                "Он не любит долго оставаться один. Заскучав, может рыть, грызть вещи и лаять, поэтому дайте ему игрушку для занятий и погуляйте перед уходом.",
                "Деятельная маленькая собака, которая любит быть в центре событий. Дома может быть спокойным, если достаточно погулял, но всегда готов играть.",
                "Энергичен и интересен активным детям, которые его уважают. Грубого обращения терпит не всегда, поэтому малышей нужно научить быть аккуратными.",
                "Часто дружит со знакомыми собаками, но с чужими может вести себя смело. Охотничий инстинкт сильный, поэтому мелкие питомцы рядом с ним не в безопасности.",
                "Идеально подходят апорт, аджилити, флайбол, трюки и игры на поиск запаха. Он быстро учится и любит задачи, поэтому занятия делайте короткими и разными.",
                "Активные утро и вечер и несколько игр между ними. Уставший джек-рассел — счастливый джек-рассел, и режим дня ему помогает.",
            ],
            "quirks": ["Джек-рассел может подпрыгнуть примерно на метр с места, поэтому заборы должны быть высокими, а двор надёжно закрытым.", "Название породы связано с английским священником Джоном Расселом, который любил охоту на лис и в XIX веке вывел этих собак.", "При хорошем уходе многие живут 14–16 лет и больше."],
        },
    },
    "scottish-terrier": {
        "prey": "high",
        "en": {
            "summary": "Dignified, loyal and full of character. The Scottish Terrier is a compact, confident dog with a famous beard and eyebrows, devoted to its own family.",
            "care": "The wiry coat needs brushing two or three times a week and trimming or hand-stripping every two to three months. Wipe the beard after drinking and eating.\nPlan for about an hour of walks and play every day. Check the garden fences, as it likes to dig.",
            "good_fit": ["Want a loyal, independent small dog", "Enjoy moderate daily walks", "Are happy to book regular grooming", "Can give calm, patient training"],
            "think_twice": ["Want a dog that is friendly to every visitor", "Are away from home most of the day", "Have rabbits or other small pets", "Have very small children"],
            "daily": [
                "About an hour a day with a brisk walk and some time to sniff and explore. A Scottie is happy with a moderate amount of exercise, but it should not skip walks. Keep it on a lead near small animals.",
                "It is independent and can manage some hours alone, but it is still devoted to its family. Long absences may lead to barking or digging.",
                "A calm, dignified housemate that likes a regular routine. It may be reserved with visitors, and is often at its best with its own family in a quiet home.",
                "Better with older children who respect its space. It does not always like noisy or rough play, so supervise small kids.",
                "It can live with other dogs if socialised early, but it is not always friendly with strange dogs. Small pets are at risk because of its hunting instinct.",
                "Short walks with sniffing, scent games, simple tricks and training suit it. It is clever but independent, so keep training patient and rewarding.",
                "A steady rhythm of walks, meals, grooming and rest. It likes order and a calm household.",
            ],
            "quirks": ["The Scottie dog is one of the tokens in the board game Monopoly.", "It is often a one-family dog: loyal and affectionate with its people but reserved with strangers.", "Its beard and leg furnishings collect dirt and water, so wipe them after walks and drinking."],
        },
        "ru": {
            "summary": "Достойный, преданный и с характером. Скотч-терьер — компактная уверенная собака с известной бородой и бровями, преданная своей семье.",
            "care": "Жёсткую шерсть нужно расчёсывать два–три раза в неделю и стричь или тримминговать раз в два–три месяца. После еды и питья протирайте бороду.\nРассчитывайте примерно на час прогулок и игр в день. Проверяйте заборы в саду: он любит рыть.",
            "good_fit": ["Хотите преданную независимую небольшую собаку", "Любите умеренные ежедневные прогулки", "Готовы регулярно ходить к грумеру", "Можете спокойно и терпеливо дрессировать"],
            "think_twice": ["Хотите собаку, дружелюбную к любому гостю", "Большую часть дня не бываете дома", "Дома живут кролики или другие мелкие питомцы", "У вас совсем маленькие дети"],
            "daily": [
                "Около часа в день: быстрая прогулка и время, чтобы понюхать и исследовать. Скотч-терьеру хватает умеренной нагрузки, но пропускать прогулки не стоит. Рядом с мелкими животными держите его на поводке.",
                "Он независим и может провести несколько часов в одиночестве, но всё равно предан своей семье. Долгое отсутствие может привести к лаю и подкопам.",
                "Спокойный солидный сосед, который любит режим. С гостями может быть сдержан и лучше всего чувствует себя со своей семьёй в тихом доме.",
                "Лучше ладит с детьми постарше, которые уважают его личное пространство. Шумные и грубые игры нравятся ему не всегда, поэтому за малышами нужно следить.",
                "Может жить с другими собаками, если его рано социализировали, но с чужими собаками дружит не всегда. Мелкие питомцы рядом с ним в опасности из-за охотничьего инстинкта.",
                "Ему подходят короткие прогулки с обнюхиванием, игры на поиск, простые трюки и дрессировка. Он умён, но самостоятелен, поэтому занимайтесь терпеливо и с поощрением.",
                "Ровный ритм прогулок, кормлений, ухода и отдыха. Он любит порядок и спокойный дом.",
            ],
            "quirks": ["Собачка-скотч-терьер — одна из фишек в настольной игре «Монополия».", "Часто это собака одной семьи: преданная и ласковая со своими, но сдержанная с чужими.", "Борода и длинная шерсть на ногах собирают грязь и воду, поэтому после прогулок и питья их нужно протирать."],
        },
    },
    "welsh-terrier": {
        "prey": "high",
        "en": {
            "summary": "Friendly, spirited and sturdy. The Welsh Terrier is a handy-sized terrier with a cheerful nature that loves to play and to be part of the family.",
            "care": "The wiry coat sheds very little but needs brushing two or three times a week and trimming or hand-stripping every two to three months.\nPlan for about an hour and a half of walks and play every day. Check the garden fences, as it likes to dig and explore.",
            "good_fit": ["Want a cheerful, hardy small-to-medium dog", "Are active and enjoy daily walks and games", "Prefer a dog that sheds little", "Are happy to book regular grooming"],
            "think_twice": ["Are away from home most of the day", "Have rabbits or other small pets", "Want a quiet dog", "Do not want regular grooming costs"],
            "daily": [
                "About an hour and a half a day, with a brisk walk and time to play. The Welsh Terrier has good stamina and enjoys a long outing. Keep it on a lead where it might chase wildlife.",
                "It likes company and does not enjoy long hours alone. Bored, it may dig, chew or bark.",
                "Cheerful and affectionate indoors, it likes to be where its people are. It is generally easier to live with than many terriers, if it has had enough exercise.",
                "Playful and sturdy, and usually a good friend for children who like to play. Supervise young kids, as with any lively terrier.",
                "Often friendly with other dogs, but some are bold with unfamiliar ones. Cats and small pets need careful introductions because of its hunting instinct.",
                "Fetch, hiking, scent games, agility and obedience all suit it. It learns well and enjoys training that is short, varied and fun.",
                "Active morning and evening, with play and rest in between. It adapts to a regular family routine.",
            ],
            "quirks": ["Its black-and-tan coat looks like a smaller Airedale, but the Welsh Terrier is lighter, more compact and has a more easy-going nature.", "It sheds very little, but the wiry coat needs regular grooming to keep its sharp outline.", "It is an alert watchdog and will tell you when someone is at the door."],
        },
        "ru": {
            "summary": "Дружелюбный, бойкий и крепкий. Вельш-терьер — терьер удобного размера с весёлым характером, который любит играть и быть частью семьи.",
            "care": "Жёсткая шерсть почти не линяет, но её нужно расчёсывать два–три раза в неделю и стричь или тримминговать раз в два–три месяца.\nРассчитывайте примерно на полтора часа прогулок и игр в день. Проверяйте заборы в саду: он любит рыть и исследовать.",
            "good_fit": ["Хотите весёлую выносливую собаку небольшого или среднего размера", "Активны и любите ежедневные прогулки и игры", "Предпочитаете собаку, которая мало линяет", "Готовы регулярно ходить к грумеру"],
            "think_twice": ["Большую часть дня не бываете дома", "Дома живут кролики или другие мелкие питомцы", "Хотите тихую собаку", "Не хотите регулярно платить за груминг"],
            "daily": [
                "Около полутора часов в день: быстрая прогулка и время на игры. У вельш-терьера хорошая выносливость, и он любит долгие выходы. Там, где он может погнаться за дикими животными, держите его на поводке.",
                "Он любит быть с людьми и не любит долго оставаться один. От скуки может рыть, грызть вещи и лаять.",
                "Дома весёлый и ласковый, любит быть рядом со своими людьми. Обычно с ним проще жить, чем со многими другими терьерами, если он достаточно погулял.",
                "Игрив и вынослив, обычно хороший друг для детей, которые любят играть. За маленькими детьми нужно следить, как и при любом живом терьере.",
                "Часто дружелюбен к другим собакам, но некоторые смело ведут себя с незнакомыми. Кошек и мелких питомцев знакомьте с ним осторожно из-за охотничьего инстинкта.",
                "Ему подходят апорт, походы, игры на поиск запаха, аджилити и послушание. Он хорошо учится и любит занятия, если они короткие, разные и весёлые.",
                "Активные утро и вечер, а между ними игры и отдых. Он легко подстраивается под семейный распорядок.",
            ],
            "quirks": ["Чёрно-подпалый окрас делает его похожим на маленького эрдельтерьера, но вельш-терьер легче, компактнее и спокойнее по характеру.", "Он почти не линяет, но жёсткая шерсть требует регулярного ухода, чтобы сохранить чёткий силуэт.", "Он внимательный сторож и обязательно сообщит, что кто-то пришёл."],
        },
    },
    "wire-fox-terrier": {
        "prey": "high",
        "en": {
            "summary": "Alert, lively and endlessly curious. The Wire Fox Terrier is a smart, sociable small dog that loves games, adventure and being with its family.",
            "care": "The wiry coat needs brushing two or three times a week and trimming or hand-stripping every two to three months. It sheds very little.\nPlan for about an hour and a half of walks, play and training every day. Secure the garden, as it digs and jumps.",
            "good_fit": ["Are active and enjoy walks, games and training", "Want a lively, clever small dog", "Prefer a dog that sheds little", "Have a securely fenced garden"],
            "think_twice": ["Want a quiet, calm dog", "Are away from home most of the day", "Have rabbits, hamsters or other small pets", "Do not want regular grooming costs"],
            "daily": [
                "About an hour and a half a day, with plenty of games and a chance to run. The Wire Fox Terrier has a lot of energy and loves new smells. Keep it on a lead where it might chase wildlife.",
                "It likes company and does not enjoy long hours alone. Left bored, it can dig, chew and bark.",
                "Alert and busy indoors, it follows the family and watches the window. It will bark to tell you about visitors, so teach a calm quiet command early.",
                "Playful and full of energy, a good match for active, kind children. Supervise small kids, as it can be bouncy and does not always like to be handled roughly.",
                "Often friendly with dogs it knows, but it can be bold with strangers. Small pets are at risk because of its strong chase instinct.",
                "Fetch, agility, flyball, scent games and tricks all suit it. It learns quickly, and short, varied training keeps it interested.",
                "Active morning and evening, with several play and training moments in between. A tired Wire Fox Terrier is a calm one.",
            ],
            "quirks": ["The Wire Fox Terrier has won Best in Show at the Westminster Dog Show more times than any other breed.", "A Wire Fox Terrier named Asta played the pet in the classic film The Thin Man.", "It barks to announce visitors, so early training of a quiet command makes life easier."],
        },
        "ru": {
            "summary": "Внимательный, живой и бесконечно любопытный. Жесткошёрстный фокстерьер — умная общительная небольшая собака, которая любит игры, приключения и быть рядом с семьёй.",
            "care": "Жёсткую шерсть нужно расчёсывать два–три раза в неделю и стричь или тримминговать раз в два–три месяца. Линяет он очень мало.\nРассчитывайте примерно на полтора часа прогулок, игр и занятий в день. Позаботьтесь о безопасном дворе: он роет землю и прыгает.",
            "good_fit": ["Активны и любите прогулки, игры и дрессировку", "Хотите живую умную небольшую собаку", "Предпочитаете собаку, которая мало линяет", "Есть надёжно огороженный двор"],
            "think_twice": ["Хотите тихую спокойную собаку", "Большую часть дня не бываете дома", "Дома живут кролики, хомяки или другие мелкие питомцы", "Не хотите регулярно платить за груминг"],
            "daily": [
                "Около полутора часов в день, с множеством игр и возможностью побегать. У фокстерьера много энергии, и он любит новые запахи. Там, где он может погнаться за дикими животными, держите его на поводке.",
                "Он любит быть с людьми и не любит долго оставаться один. От скуки может рыть, грызть вещи и лаять.",
                "Дома внимателен и занят: ходит за семьёй и наблюдает из окна. Он лает, сообщая о гостях, поэтому рано научите его спокойной команде «тихо».",
                "Игрив и полон энергии, хорошо подходит активным добрым детям. Малышей нужно контролировать: он может быть слишком энергичным и не всегда любит грубое обращение.",
                "Часто дружит со знакомыми собаками, но с чужими может вести себя смело. Мелкие питомцы в опасности из-за сильного инстинкта погони.",
                "Ему подходят апорт, аджилити, флайбол, игры на поиск запаха и трюки. Он быстро учится, а короткие разнообразные занятия не дают ему заскучать.",
                "Активные утро и вечер и несколько игр и занятий между ними. Уставший фокстерьер — спокойный фокстерьер.",
            ],
            "quirks": ["Жесткошёрстный фокстерьер побеждал в «Лучшем в шоу» на выставке Вестминстер чаще любой другой породы.", "Жесткошёрстный фокстерьер по кличке Аста сыграл собаку в классическом фильме «Тонкий человек».", "Он лает, сообщая о гостях, поэтому ранняя дрессировка команды «тихо» облегчает жизнь."],
        },
    },
    "yorkshire-terrier": {
        "prey": "moderate",
        "en": {
            "summary": "Tiny, bold and affectionate. The Yorkshire Terrier is a lively companion with a big personality and a silky coat that wants to be close to its family.",
            "care": "The long, silky coat needs daily brushing to avoid tangles, or a short \"puppy cut\" that is easier to keep. Brush the teeth often, as small dogs are prone to dental problems.\nPlan for about 45 minutes of walks and play every day. Give a coat in cold weather.",
            "good_fit": ["Want a small, affectionate indoor companion", "Live in a flat or small house", "Can brush the coat daily or book regular grooming", "Are at home for much of the day"],
            "think_twice": ["Have very young children who may handle a tiny dog roughly", "Are away from home most of the day", "Want a dog that does not bark", "Cannot brush or groom regularly"],
            "daily": [
                "About 45 minutes a day, split into two or three short walks. A Yorkie is tiny but loves to explore. Use a harness instead of a collar, and keep it on a lead, as it is fearless around larger dogs.",
                "It bonds closely to its family and does not like being left alone for long. Separation can lead to barking, so teach it to be alone in small steps.",
                "A lap dog at heart, it loves a cosy place close to its people. It is alert and will bark at noises, so teach a quiet command early.",
                "Best with older, gentle children who can be taught to handle a tiny dog. Small kids can hurt it accidentally, so supervise and teach not to pick it up roughly.",
                "Often bold and friendly with other dogs, but it does not know its size. It may chase small animals, so keep it on a lead outdoors.",
                "Short games, simple tricks, scent games and training are enough for a Yorkie. It is clever and enjoys learning, especially for treats.",
                "Short walks, meals, grooming and long naps on a soft bed. Keep a regular routine, and make sure it cannot jump off high furniture.",
            ],
            "quirks": ["Yorkshire Terrier puppies are born black and tan, and the coat gradually turns steel-blue and tan with age.", "The coat is more like human hair than fur, so it grows continuously, sheds little and many owners choose a short \"puppy cut\".", "Despite weighing only a few kilos, a Yorkie acts as if it is a much bigger dog, so keep it on a lead around large dogs."],
        },
        "ru": {
            "summary": "Крошечный, смелый и ласковый. Йоркширский терьер — живой компаньон с большим характером и шелковистой шерстью, который хочет быть рядом с семьёй.",
            "care": "Длинную шелковистую шерсть нужно расчёсывать ежедневно, чтобы не было колтунов, или сделать короткую «щенячью» стрижку, за которой проще ухаживать. Часто чистите зубы: у мелких собак они часто болят.\nРассчитывайте примерно на 45 минут прогулок и игр в день. В холод надевайте одежду.",
            "good_fit": ["Хотите небольшую ласковую домашнюю собаку", "Живёте в квартире или небольшом доме", "Можете ежедневно расчёсывать шерсть или регулярно ходить к грумеру", "Значительную часть дня бываете дома"],
            "think_twice": ["У вас маленькие дети, которые могут грубо обращаться с крошечной собакой", "Большую часть дня не бываете дома", "Хотите собаку, которая не лает", "Не можете регулярно ухаживать за шерстью"],
            "daily": [
                "Около 45 минут в день, разделённых на две–три короткие прогулки. Йорк крошечный, но любит исследовать. Используйте шлейку вместо ошейника и держите его на поводке: рядом с крупными собаками он бесстрашен.",
                "Он сильно привязан к семье и не любит долго оставаться один. Из-за разлуки может лаять, поэтому приучайте его быть одному маленькими шагами.",
                "В душе комнатная собачка, любит уютное место рядом с хозяевами. Внимателен и лает на шум, поэтому рано научите его команде «тихо».",
                "Лучше всего ладит с детьми постарше, которых можно научить бережно обращаться с крошечной собакой. Малыши могут нечаянно сделать ему больно, поэтому следите и учите не брать его грубо на руки.",
                "Часто смело и дружелюбно относится к другим собакам, но не знает своих размеров. Может гнаться за мелкими животными, поэтому на улице держите его на поводке.",
                "Йорку хватает коротких игр, простых трюков, игр на поиск и занятий. Он умён и любит учиться, особенно за лакомство.",
                "Короткие прогулки, кормления, уход и долгий сон на мягкой лежанке. Придерживайтесь распорядка и следите, чтобы он не прыгал с высокой мебели.",
            ],
            "quirks": ["Щенки йоркширского терьера рождаются чёрными с рыжими отметинами, а с возрастом шерсть становится стально-голубой с рыжим.", "Шерсть больше похожа на человеческие волосы, чем на мех: она постоянно растёт, мало линяет, а многие хозяева выбирают короткую «щенячью» стрижку.", "Весит он всего несколько килограммов, но ведёт себя как гораздо более крупная собака, поэтому рядом с большими собаками держите его на поводке."],
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
                "daily_life": "\n\n".join(f"{l}: {t}" for l, t in zip(labels, block["daily"])),
                "quirks": "\n".join(block["quirks"]),
            }
            for field, text in texts.items():
                values[f"{field}_{lang}"] = text
                if lang == "en":
                    values[field] = text
        for lang in ("de", "it", "es", "sr_latn"):
            for field in ("summary", "care", "good_fit", "think_twice", "daily_life", "quirks"):
                values[f"{field}_{lang}"] = ""
        Dogs.objects.filter(slug=slug).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0069_fun_facts_review")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
