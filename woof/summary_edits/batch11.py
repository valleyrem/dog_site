"""Batch 11 (last): treeing-walker, weimaraner, whippet, wire-fox-terrier, xolo,
yakutian-laika, yorkshire-terrier."""

EDITS = {
    "en": {
        "weimaraner": [
            (
                'The Weimaraner, often called the "Gray Ghost" due to its striking silver-gray coat, is a highly versatile and energetic hunting dog.',
                'The Weimaraner, often called the "Gray Ghost" due to its striking silver-gray coat, is an energetic and deeply loyal gundog.',
            )
        ],
        "whippet": [
            (
                "Originally bred for hunting by sight, Whippets are capable of incredible bursts of speed",
                "Whippets are capable of incredible bursts of speed",
            )
        ],
        "wire-fox-terrier": [
            (
                "Historically bred for hunting, these dogs were originally used to hunt small game, especially foxes, which is reflected in their high energy and strong prey drive.",
                "Their high energy and strong prey drive are reflected in everything they do.",
            )
        ],
        "xoloitzcuintli": [
            (
                "The Xoloitzcuintli is one of the oldest and most distinctive dog breeds, originating in Mexico over 3,000 years ago and deeply connected to ancient Aztec culture. ",
                "",
            )
        ],
        "yakutian-laika": [
            (
                "The Yakutian Laika is an ancient Siberian working breed developed for sled pulling, hunting, and survival in extreme Arctic climates. ",
                "",
            )
        ],
        "yorkshire-terrier": [
            (
                "Originally bred in the 19th century to catch rats in mills, Yorkies were highly prized for their intelligence and agility.",
                "Yorkies are highly prized for their intelligence and agility.",
            ),
            (
                "Over time, they became popular as companion dogs due to their affectionate nature and loyalty.",
                "They are affectionate, loyal companion dogs.",
            ),
        ],
    },
    "ru": {
        "weimaraner": [
            (
                "Веймаранер, часто называемый «серым призраком» из-за эффектной серебристо-серой шерсти, — очень универсальная и энергичная охотничья собака.",
                "Веймаранер, часто называемый «серым призраком» из-за эффектной серебристо-серой шерсти, — энергичная и глубоко преданная подружейная собака.",
            )
        ],
        "whippet": [
            (
                "Выведенный изначально для охоты по зрению, уиппет способен на невероятные всплески скорости",
                "Уиппет способен на невероятные всплески скорости",
            ),
            (" Сложение и темперамент делают их уникальными среди собачьих групп.", ""),
        ],
        "wire-fox-terrier": [
            (
                "Исторически выведенная для охоты, порода использовалась для охоты на мелкую дичь, особенно лис, что отражается в высокой энергии и сильном охотничьем инстинкте.",
                "Высокая энергия и сильный охотничий инстинкт отражаются во всём, что она делает.",
            )
        ],
        "xoloitzcuintli": [
            (
                "Ксолоитцкуинтли — одна из самых древних и самобытных пород собак, происходящая из Мексики более 3000 лет назад и глубоко связанная с культурой древних ацтеков. ",
                "",
            ),
            (" У них часто густая шерсть, остроконечные уши и закрученный хвост.", ""),
        ],
        "yakutian-laika": [
            (
                "Якутская лайка — древняя сибирская рабочая порода, выведенная для ездовой работы, охоты и выживания в экстремальном арктическом климате. ",
                "",
            ),
            (
                " Многие из этих пород сохраняют сильные инстинкты и независимое мышление. Они, как правило, внимательны, жизнестойки и хорошо приспособлены к суровому климату.",
                "",
            ),
        ],
        "yorkshire-terrier": [
            (
                "Выведенный в XIX веке для ловли крыс на мельницах, йорк высоко ценён за ум и ловкость.",
                "Йорк высоко ценён за ум и ловкость.",
            ),
            (
                "Со временем он стал популярной собакой-компаньоном благодаря ласковому нраву и преданности.",
                "Это ласковая и преданная собака-компаньон.",
            ),
        ],
    },
    "de": {
        "weimaraner": [
            (
                "ist ein höchst vielseitiger und energiegeladener Jagdhund.",
                "ist ein energiegeladener und tief loyaler Jagdhund.",
            )
        ],
        "whippet": [
            (
                "Ursprünglich zur Sichtjagd gezüchtet, ist der Whippet zu beeindruckenden Geschwindigkeitssprints fähig",
                "Der Whippet ist zu beeindruckenden Geschwindigkeitssprints fähig",
            ),
            (
                " Ihr Körperbau und ihr Temperament machen sie einzigartig unter den Hundegruppen.",
                "",
            ),
        ],
        "wire-fox-terrier": [
            (
                "Historisch für die Jagd gezüchtet, wurde er ursprünglich zur Jagd auf Kleinwild, besonders Füchse, eingesetzt — reflektiert durch hohe Energie und starken Jagdtrieb.",
                "Hohe Energie und starker Jagdtrieb prägen alles, was er tut.",
            )
        ],
        "xoloitzcuintli": [
            (
                "Der Xoloitzcuintli ist eine der ältesten und unverwechselbarsten Hunderassen, vor über 3000 Jahren in Mexiko entstanden und tief mit der aztekischen Kultur verbunden. ",
                "",
            ),
            (
                " Sie haben oft dichtes Fell, aufgestellte Ohren und eine eingerollte Rute.",
                "",
            ),
        ],
        "yakutian-laika": [
            (
                "Der Jakutische Laika ist eine uralte sibirische Arbeitsrasse, entwickelt für Schlittenziehen, Jagd und Überleben in extremen arktischen Klimazonen. ",
                "",
            ),
            (" Viele dieser Rassen haben starke Instinkte und denken unabhängig.", ""),
        ],
        "yorkshire-terrier": [
            (
                "Jahrhundert gezüchtet, um in Mühlen Ratten zu fangen, wurde der Yorkie für Intelligenz und Wendigkeit geschätzt.",
                "Der Yorkie wird für seine Intelligenz und Wendigkeit geschätzt.",
            ),
            (
                "Mit der Zeit wurde er wegen seiner anhänglichen Art und Loyalität als Begleithund beliebt.",
                "Er ist ein anhänglicher und loyaler Begleithund.",
            ),
        ],
    },
    "it": {
        "treeing-walker-coonhound": [
            (
                "Il Treeing Walker Coonhound è una razza americana di taglia media-grande, specializzata nella caccia tramite 'treeing': insegue la preda e la tiene praticamente su un albero.",
                "Il Treeing Walker Coonhound è una razza di taglia media-grande, dal mantello tricolore e dalle lunghe orecchie.",
            )
        ],
        "weimaraner": [
            (
                "Il Weimaraner, soprannominato 'il fantasma grigio' per il mantello argenteo, è una razza tedesca di taglia grande, versatile e atletica.",
                "Il Weimaraner, soprannominato 'il fantasma grigio' per il mantello argenteo, è una razza di taglia grande, versatile e atletica.",
            ),
            (
                "È un cane da caccia eccellente, usato per la cerca della selvaggina e per il riporto.",
                "È un cane da caccia eccellente e instancabile.",
            ),
        ],
        "whippet": [
            (
                "Il Whippet è un levriero elegante e slanciato, originario dell'Inghilterra, dove veniva usato per la corsa e la caccia alla piccola selvaggina.",
                "Il Whippet è un levriero elegante e slanciato, con un mantello corto e fine.",
            )
        ],
        "wire-fox-terrier": [
            (
                " Originario dell'Inghilterra, era usato per cacciare le volpi nelle tane.",
                "",
            ),
        ],
        "xoloitzcuintli": [
            (
                "Lo Xoloitzcuintle, chiamato anche 'cane nudo messicano' o semplicemente 'Xolo', è una delle razze più antiche del mondo, presente in Messico da oltre tremila anni e legata alla cultura azteca.",
                "Lo Xoloitzcuintle, chiamato anche 'cane nudo messicano' o semplicemente 'Xolo', è una delle razze più particolari al mondo.",
            )
        ],
        "yakutian-laika": [
            (
                "Nonostante l'origine da lavoro, è affettuoso, socievole e molto legato alla famiglia.",
                None,
            )
        ],
        "yorkshire-terrier": [
            (
                "Originario dell'Inghilterra, dove veniva usato per cacciare i topi, oggi è un compagno elegante e fedele",
                "Oggi è un compagno elegante e fedele, molto legato al suo proprietario.",
            )
        ],
    },
    "sr_latn": {
        "weimaraner": [
            (
                "veoma je svestran i energičan lovački pas.",
                "energičan je i veoma odan lovački pas.",
            )
        ],
        "whippet": [
            (
                "Prvobitno uzgajan za lov vizuelnim praćenjem, vipet je sposoban za neverovatne izlive brzine",
                "Vipet je sposoban za neverovatne izlive brzine",
            )
        ],
        "wire-fox-terrier": [
            (
                "Istorijski uzgajan za lov, prvobitno je korišćen za lov na sitnu divljač, posebno lisice, što se ogleda u visokoj energiji i snažnom lovačkom nagonu.",
                "Visoka energija i snažan lovački nagon ogledaju se u svemu što radi.",
            )
        ],
        "xoloitzcuintli": [
            (
                "Ksolockuintli je jedna od najstarijih i najprepoznatljivijih rasa pasa, poreklom iz Meksika pre više od 3.000 godina i duboko povezana sa drevnom astečkom kulturom.",
                "Ksolockuintli je jedna od najprepoznatljivijih rasa pasa.",
            )
        ],
        "yakutian-laika": [
            (
                "Jakutska lajka je drevna sibirska radna rasa razvijena za vuču saonica, lov i preživljavanje u ekstremnoj arktičkoj klimi. ",
                "",
            )
        ],
        "yorkshire-terrier": [
            (
                "veku za hvatanje pacova u mlinovima, jorki je bio visoko cenjen zbog inteligencije i spretnosti.",
                "Jorki je bio visoko cenjen zbog inteligencije i spretnosti.",
            ),
            (
                "Vremenom je postao popularan kao pas saputnik zbog privržene prirode i odanosti.",
                "To je privržen i odan pas saputnik.",
            ),
            (
                " Prvobitno uzgajani za lov i suzbijanje štetočina, poznati su po hrabrosti i istrajnosti.",
                "",
            ),
        ],
    },
}
