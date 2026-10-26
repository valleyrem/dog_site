"""Batch 9: pembroke-welsh-corgi, pomeranian, poodle, portuguese-podengo, pug, puli,
rat-terrier, romagna-water-dog."""

EDITS = {
    "en": {
        "pembroke-welsh-corgi": [
            (
                "While they were originally bred for herding cattle, Corgis are now cherished family pets",
                "Corgis are cherished family pets",
            )
        ],
        "poodle": [
            (
                "The Poodle is an intelligent and highly versatile breed originally developed as a water retriever for hunting waterfowl.",
                "The Poodle is an intelligent and highly versatile breed with a dense, curly coat that sheds very little.",
            )
        ],
        "portuguese-podengo": [
            (
                "Originating from Portugal, this breed was developed to hunt rabbits in rocky terrain, which explains its agility, intelligence, and independence.",
                "It is agile, intelligent and independent, and it needs a job to stay happy.",
            )
        ],
        "pug": [
            (
                "Originally bred as companion dogs for royalty in ancient China, Pugs are known for their friendly",
                "Pugs are known for their friendly",
            )
        ],
        "puli": [
            (
                "Originally developed for herding sheep, it is agile, intelligent, and highly responsive",
                "It is agile, intelligent, and highly responsive",
            )
        ],
        "rat-terrier": [
            (
                "The Rat Terrier is a small but highly capable American working breed developed for farm and pest control tasks, especially hunting rodents.",
                "The Rat Terrier is a small but highly capable working breed with a short, smooth coat and a muscular, athletic build.",
            )
        ],
        "romagna-water-dog": [
            (
                "The Lagotto Romagnolo is an ancient Italian working breed originally used as a water retriever and later specialized in truffle hunting thanks to its exceptional sense of smell.",
                "The Lagotto Romagnolo is a working breed with a dense, curly, water-resistant coat and an exceptional sense of smell.",
            )
        ],
    },
    "ru": {
        "pembroke-welsh-corgi": [
            (
                "Хотя корги изначально выводились для пастьбы крупного рогатого скота, сегодня они — любимые семейные питомцы",
                "Сегодня корги — любимые семейные питомцы",
            )
        ],
        "poodle": [
            (
                "Пудель — умная и очень универсальная порода, изначально выведенная как водяной ретривер для охоты на водоплавающую дичь.",
                "Пудель — умная и очень универсальная порода с густой курчавой шерстью, которая почти не линяет.",
            ),
        ],
        "portuguese-podengo": [
            (
                "Родом из Португалии, порода была выведена для охоты на кроликов в каменистой местности, что объясняет её ловкость, ум и независимость.",
                "Порода ловка, умна и независима, и ей нужно занятие, чтобы быть счастливой.",
            ),
            (
                " Шпицы и породы примитивного типа — одни из самых древних и естественных групп пород.",
                "",
            ),
        ],
        "pug": [
            (
                "Выведенный изначально как собака-компаньон для знати в древнем Китае, мопс известен дружелюбной общительной натурой",
                "Мопс известен дружелюбной общительной натурой",
            )
        ],
        "puli": [
            (
                "Выведенный для пастьбы овец, пули ловок, умён и очень отзывчив",
                "Пули ловок, умён и очень отзывчив",
            ),
            (
                " Они склонны образовывать глубокие связи с владельцами и процветают, когда им дают чёткую роль.",
                "",
            ),
        ],
        "rat-terrier": [
            (
                "Рэт-терьер — маленькая, но очень способная американская рабочая порода, выведенная для фермерских и вредительских задач, особенно для охоты на грызунов.",
                "Рэт-терьер — маленькая, но очень способная рабочая порода с короткой гладкой шерстью и мускулистым атлетичным сложением.",
            )
        ],
        "romagna-water-dog": [
            (
                "Лаготто-романьоло — древняя итальянская рабочая порода, изначально использовавшаяся как водный ретривер, а позднее специализировавшаяся на поиске трюфелей благодаря исключительному обонянию.",
                "Лаготто-романьоло — рабочая порода с густой курчавой водостойкой шерстью и исключительным обонянием.",
            ),
            (
                " У них, как правило, уравновешенный темперамент, и они хорошо адаптируются к семейной жизни.",
                "",
            ),
        ],
    },
    "de": {
        "pembroke-welsh-corgi": [
            (
                "Ursprünglich zum Hüten von Rindern gezüchtet, sind Corgis heute beliebte Familienhunde",
                "Corgis sind heute beliebte Familienhunde",
            )
        ],
        "poodle": [
            (
                "Der Pudel ist eine intelligente und äußerst vielseitige Rasse, ursprünglich als Wasserapporteur für die Jagd auf Wassergeflügel gezüchtet.",
                "Der Pudel ist eine intelligente und äußerst vielseitige Rasse mit dichtem Lockenfell, das kaum haart.",
            )
        ],
        "portuguese-podengo": [
            (
                "Ursprünglich aus Portugal, wurde diese Rasse zur Kaninchenjagd in felsigem Gelände gezüchtet — daher ihre Wendigkeit, Intelligenz und Unabhängigkeit.",
                "Sie ist wendig, intelligent und unabhängig und braucht eine Aufgabe, um zufrieden zu sein.",
            ),
            (
                " Spitze und Hunde vom Urtyp gehören zu den ältesten und natürlichsten Rassegruppen.",
                "",
            ),
        ],
        "pug": [
            (
                "Ursprünglich als Begleithund für das Königshaus im alten China gezüchtet, ist der Mops für sein freundliches, geselliges Wesen",
                "Der Mops ist für sein freundliches, geselliges Wesen",
            )
        ],
        "puli": [
            (
                "Ursprünglich zum Hüten von Schafen entwickelt, ist er wendig, intelligent und hochreaktiv",
                "Er ist wendig, intelligent und hochreaktiv",
            ),
            (
                " Sie gehen tiefe Bindungen mit ihren Besitzern ein und brauchen eine klare Aufgabe.",
                "",
            ),
        ],
        "rat-terrier": [
            (
                "Der Rat Terrier ist eine kleine, aber hochfähige amerikanische Arbeitsrasse, entwickelt für Farm- und Schädlingsbekämpfung, besonders die Jagd auf Nagetiere.",
                "Der Rat Terrier ist eine kleine, aber hochfähige Arbeitsrasse mit kurzem, glattem Fell und muskulösem, athletischem Körperbau.",
            )
        ],
        "romagna-water-dog": [
            (
                "Der Lagotto Romagnolo ist eine uralte italienische Arbeitsrasse, ursprünglich als Wasserapporteur eingesetzt und später dank seines außergewöhnlichen Geruchssinns auf die Trüffelsuche spezialisiert.",
                "Der Lagotto Romagnolo ist eine Arbeitsrasse mit dichtem, lockigem, wasserabweisendem Fell und außergewöhnlichem Geruchssinn.",
            )
        ],
    },
    "it": {
        "pembroke-welsh-corgi": [
            (
                "Il Welsh Corgi Pembroke è una razza piccola e robusta dal corpo lungo e dalle zampe corte, originaria del Galles, dove conduceva il bestiame.",
                "Il Welsh Corgi Pembroke è una razza piccola e robusta dal corpo lungo e dalle zampe corte.",
            )
        ],
        "pomeranian": [
            (
                "Originario della regione della Pomerania e reso famoso dalla regina Vittoria, è intelligente, curioso e vigile",
                "È intelligente, curioso e vigile",
            )
        ],
        "portuguese-podengo": [
            (
                "Il Podengo Portoghese è una razza antica del Portogallo, disponibile in tre taglie",
                "Il Podengo Portoghese è una razza disponibile in tre taglie",
            ),
            (
                "È un cane da caccia versatile, usato per la caccia al coniglio in terreni difficili.",
                "È un cane da caccia versatile, resistente e adattabile.",
            ),
        ],
        "pug": [
            (
                "Originario della Cina e caro alle corti europee, è un compagno ideale per la vita di casa",
                "È un compagno ideale per la vita di casa",
            )
        ],
        "puli": [
            (
                "Originariamente usato per la conduzione delle pecore, è agile, intelligente e molto reattivo",
                "È agile, intelligente e molto reattivo",
            )
        ],
        "rat-terrier": [
            (
                "Il Rat Terrier è una razza americana di piccola-media taglia, sviluppata per il controllo dei roditori nelle fattorie.",
                "Il Rat Terrier è una razza di piccola-media taglia.",
            ),
        ],
        "romagna-water-dog": [
            (
                "Il Lagotto Romagnolo è un'antica razza italiana, originariamente cane da acqua e oggi specializzato nella ricerca del tartufo grazie al suo straordinario olfatto.",
                "Il Lagotto Romagnolo è una razza compatta e robusta, con un olfatto straordinario.",
            )
        ],
    },
    "sr_latn": {
        "pembroke-welsh-corgi": [
            (
                "Iako su prvobitno uzgajani za čuvanje stoke, korgiji su sada omiljeni porodični ljubimci",
                "Korgiji su sada omiljeni porodični ljubimci",
            )
        ],
        "poodle": [
            (
                "Pudlica je inteligentna i veoma svestrana rasa, prvobitno razvijena kao vodeni retriver za lov na vodene ptice.",
                "Pudlica je inteligentna i veoma svestrana rasa sa gustom kovrdžavom dlakom koja se skoro ne linja.",
            ),
            (
                " Mnoge rase iz ove grupe su privržene, druželjubive i pažljive prema vlasniku.",
                "",
            ),
        ],
        "portuguese-podengo": [
            (
                "Poreklom iz Portugala, ova rasa je razvijena za lov na zečeve u kamenitom terenu, što objašnjava njenu spretnost, inteligenciju i nezavisnost.",
                "Ova rasa je spretna, inteligentna i nezavisna, i potreban joj je zadatak da bi bila zadovoljna.",
            ),
            (" Često imaju gustu dlaku, uspravne uši i zavijen rep.", ""),
        ],
        "pug": [
            (
                "Prvobitno uzgajan kao pas u krilu za kraljevske porodice u staroj Kini, mops je poznat po prijateljskoj, društvenoj prirodi",
                "Mops je poznat po prijateljskoj, društvenoj prirodi",
            )
        ],
        "puli": [
            (
                "Prvobitno razvijen za čuvanje ovaca, okretan je, inteligentan i veoma odzivan",
                "Okretan je, inteligentan i veoma odzivan",
            )
        ],
        "rat-terrier": [
            (
                "Pacovski terijer je mala, ali veoma sposobna američka radna rasa razvijena za poslove na farmi i suzbijanje štetočina, posebno lov na glodare.",
                "Pacovski terijer je mala, ali veoma sposobna radna rasa sa kratkom, glatkom dlakom i mišićavom, atletskom građom.",
            )
        ],
        "romagna-water-dog": [
            (
                "Lagoto romanjolo je drevna italijanska radna rasa, prvobitno korišćena kao vodeni retriver, a kasnije specijalizovana za lov na tartufe zahvaljujući izuzetnom čulu mirisa.",
                "Lagoto romanjolo je radna rasa sa gustom, kovrdžavom, vodootpornom dlakom i izuzetnim čulom mirisa.",
            )
        ],
    },
}
