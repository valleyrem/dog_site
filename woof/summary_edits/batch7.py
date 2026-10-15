"""Batch 7: golden-retriever, great-dane, hovawart, irish-wolfhound, italian-sighthound,
italian-spinone, kai, keeshond."""

EDITS = {
    "en": {
        "great-dane": [
            (
                'The Great Dane is often referred to as the "Apollo of dogs" due to its majestic stature and graceful appearance.',
                "The Great Dane is a majestic breed with a graceful appearance and a stately, unhurried stride.",
            )
        ],
        "hovawart": [
            (
                "The Hovawart is a large German working breed historically developed as a guard and estate dog, with a name that literally means \u201cyard watcher.\u201d",
                "The Hovawart is a large working breed with a thick, slightly wavy coat and a calm, watchful expression.",
            ),
            (
                "Originally used for guarding, tracking, and rescue work, the breed combines physical strength",
                "The breed combines physical strength",
            ),
        ],
        "irish-wolfhound": [
            (
                "The Irish Wolfhound is a majestic breed that embodies both strength and grace, originally bred for hunting large game like wolves and deer in Ireland.",
                "The Irish Wolfhound is a majestic breed that embodies both strength and grace, with a rough coat and a gentle, dignified manner.",
            )
        ],
        "italian-spinone": [
            (
                "The Spinone Italiano is a large, rugged hunting breed from Italy, developed for tracking, pointing, and retrieving in challenging terrain.",
                "The Spinone Italiano is a large, rugged gundog with a coarse, wiry coat and a long, shaggy beard.",
            )
        ],
        "kai": [
            (
                "is a rare and ancient Japanese breed, renowned for its striking brindle coat",
                "is a rare breed renowned for its striking brindle coat",
            ),
            (
                "Originally bred to hunt large game such as bears, wild boars, and deer, this medium-sized dog is agile, alert, and highly intelligent.",
                "This medium-sized dog is agile, alert, and highly intelligent, and it needs plenty of exercise and a job to do.",
            ),
        ],
        "keeshond-wolfspitz": [
            (
                "Originally developed in the Netherlands as a companion and watchdog on river barges, the breed is known for its expressive",
                "The breed is known for its expressive",
            )
        ],
    },
    "ru": {
        "golden-retriever": [
            (
                " При достаточной стимуляции они надёжны, добры и легки в совместной жизни.",
                "",
            ),
        ],
        "great-dane": [
            (
                "Немецкого дога часто называют «аполлоном собак» за величественный рост и грациозную внешность.",
                "Немецкий дог — величественная порода с грациозной внешностью и неторопливой, уверенной походкой.",
            )
        ],
        "hovawart": [
            (
                "Ховаварт — крупная немецкая рабочая порода, исторически выведенная как охранник усадьбы; само название буквально означает «сторож двора».",
                "Ховаварт — крупная рабочая порода с густой, слегка волнистой шерстью и спокойным, внимательным выражением.",
            ),
            (
                "Изначально использовавшиеся для охраны, работы по следу и спасательных работ, порода сочетает физическую силу",
                "Порода сочетает физическую силу",
            ),
            (
                " Эта группа включает мощные и универсальные породы с сильными охранными инстинктами и уверенным присутствием.",
                "",
            ),
        ],
        "irish-wolfhound": [
            (
                "Ирландский волкодав — величественная порода, воплощающая и силу, и грацию; выведена в Ирландии для охоты на крупную дичь: волков и оленей.",
                "Ирландский волкодав — величественная порода, воплощающая и силу, и грацию, с жёсткой шерстью и мягким, достойным поведением.",
            )
        ],
        "italian-sighthound": [
            (
                " Борзые — элегантные и атлетичные собаки, выведенные для скорости и визуального выслеживания.",
                "",
            ),
        ],
        "italian-spinone": [
            (
                "Итальянский спиноне — крупная, выносливая охотничья порода из Италии, выведенная для работы по следу, стойки и апортировки на сложной местности.",
                "Итальянский спиноне — крупная, выносливая подружейная порода с жёсткой шерстью и длинной лохматой бородой.",
            )
        ],
        "kai": [
            (
                "Каи, также известная как каи-кен, — редкая древняя японская порода, славящаяся",
                "Каи, также известная как каи-кен, — редкая порода, славящаяся",
            ),
            (
                "Выведенная изначально для охоты на крупную дичь — медведей, кабанов и оленей, эта собака среднего размера ловка, внимательна и очень умна.",
                "Эта собака среднего размера ловка, внимательна и очень умна, ей нужны большие нагрузки и занятие.",
            ),
        ],
        "keeshond-wolfspitz": [
            (
                "Выведенный в Нидерландах как компаньон и сторож речных барж, порода известна выразительными «очками»",
                "Порода известна выразительными «очками»",
            )
        ],
    },
    "de": {
        "golden-retriever": [
            (
                " Mit genügend Auslastung sind sie zuverlässig, freundlich und leicht zu halten.",
                "",
            ),
        ],
        "great-dane": [
            (
                "Die Deutsche Dogge wird oft als „Apollo der Hunde“ bezeichnet — wegen ihrer majestätischen Statur und eleganten Erscheinung.",
                "Die Deutsche Dogge ist eine majestätische Rasse mit eleganter Erscheinung und einem gemessenen, ruhigen Schritt.",
            )
        ],
        "hovawart": [
            (
                "Der Hovawart ist eine große deutsche Arbeitsrasse, historisch als Wach- und Gutshund entwickelt — der Name bedeutet wörtlich „Hofwächter“.",
                "Der Hovawart ist eine große Arbeitsrasse mit dichtem, leicht gewelltem Fell und einem ruhigen, wachsamen Ausdruck.",
            ),
            (
                "Ursprünglich für Schutz, Spurensuche und Rettung eingesetzt, verbindet die Rasse körperliche Stärke",
                "Die Rasse verbindet körperliche Stärke",
            ),
            (
                " Zu dieser Gruppe gehören kräftige und vielseitige Rassen mit ausgeprägtem Schutzinstinkt und selbstbewusster Präsenz.",
                "",
            ),
        ],
        "irish-wolfhound": [
            (
                "Der Irische Wolfshund ist eine majestätische Rasse, die Stärke und Anmut vereint; ursprünglich in Irland zur Jagd auf Großwild wie Wölfe und Hirsche gezüchtet.",
                "Der Irische Wolfshund ist eine majestätische Rasse, die Stärke und Anmut vereint, mit rauem Fell und sanftem, würdigem Wesen.",
            )
        ],
        "italian-sighthound": [
            (
                " Windhunde sind elegante und athletische Hunde, gezüchtet für Geschwindigkeit und Sichtjagd.",
                "",
            ),
        ],
        "italian-spinone": [
            (
                "Der Italienische Spinone ist ein großer, robuster Jagdhund aus Italien, entwickelt für Spurensuche, Vorstehen und Apportieren in schwierigem Gelände.",
                "Der Italienische Spinone ist ein großer, robuster Jagdhund mit rauem Fell und langem, zotteligem Bart.",
            ),
            (
                " Vorstehhunde sind geschickte Jagdbegleiter, bekannt für ihre Präzision und Konzentration.",
                "",
            ),
        ],
        "kai": [
            (
                "ist eine seltene und uralte japanische Rasse, berühmt für sein auffälliges gestromtes Fell",
                "ist eine seltene Rasse, berühmt für sein auffälliges gestromtes Fell",
            ),
            (
                "Ursprünglich zur Jagd auf Großwild wie Bären, Wildschweine und Hirsche gezüchtet, ist dieser mittelgroße Hund wendig, wachsam und hochintelligent.",
                "Dieser mittelgroße Hund ist wendig, wachsam und hochintelligent und braucht viel Bewegung und eine Aufgabe.",
            ),
        ],
        "keeshond-wolfspitz": [
            (
                "Ursprünglich in den Niederlanden als Begleiter und Wachhund auf Flussschiffen entwickelt, ist die Rasse für ihre ausdrucksstarken",
                "Die Rasse ist für ihre ausdrucksstarken",
            )
        ],
    },
    "it": {
        "golden-retriever": [
            (
                "Sviluppato in Gran Bretagna come cane da riporto, eccelle in molti ruoli: dalla caccia all'assistenza, fino alla terapia.",
                "Eccelle in molti ruoli: dall'assistenza alla terapia, fino allo sport.",
            )
        ],
        "great-dane": [
            (
                "L'Alano, conosciuto anche come Deutsches Dogge, è una razza gigante dalla presenza maestosa e dal carattere gentile.",
                "L'Alano è una razza gigante dalla presenza maestosa e dal carattere gentile.",
            ),
            (
                "Originariamente allevato per la caccia alla selvaggina grossa, oggi è un compagno dignitoso e leale",
                "È un compagno dignitoso e leale",
            ),
        ],
        "hovawart": [
            (
                "L'Hovawart è una razza tedesca grande e potente, il cui nome significa 'guardiano della tenuta'.",
                "L'Hovawart è una razza grande e potente, con un mantello folto e leggermente ondulato.",
            )
        ],
        "irish-wolfhound": [
            (
                "Il Levriero Irlandese è una delle razze più alte del mondo, originaria dell'Irlanda dove veniva usata per la caccia al lupo e al cervo.",
                "Il Levriero Irlandese è una delle razze più alte del mondo, con un mantello ruvido e un carattere dolce.",
            )
        ],
        "italian-sighthound": [
            (
                "Il Piccolo Levriero Italiano è una razza piccola ed elegante, originaria dell'Italia, dove era il cane preferito delle corti rinascimentali.",
                "Il Piccolo Levriero Italiano è una razza piccola ed elegante, dall'ossatura fine e dal pelo corto e liscio.",
            )
        ],
        "italian-spinone": [
            (
                "Lo Spinone Italiano è una razza italiana antica e versatile, usata come cane da caccia e da ferma in ogni tipo di terreno.",
                "Lo Spinone Italiano è una razza versatile e resistente, adatta a ogni tipo di terreno.",
            )
        ],
        "kai": [
            (
                "Il Kai, detto anche 'cane tigre giapponese', è una razza giapponese antica e rara, dal mantello tigrato brindle",
                "Il Kai, detto anche 'cane tigre', è una razza rara, dal mantello tigrato brindle",
            ),
            (
                "Originario del Giappone, è stato allevato per la caccia al cervo e al cinghiale.",
                "Ha un forte istinto venatorio e un carattere indipendente.",
            ),
        ],
        "keeshond-wolfspitz": [
            (
                "Originario dell'Olanda e della Germania, era il cane simbolo dei patrioti olandesi.",
                "Ha un mantello folto che richiede spazzolature regolari.",
            )
        ],
    },
    "sr_latn": {
        "golden-retriever": [
            (
                " Mnoge rase ovde su veoma društvene i vole rad u bliskoj saradnji sa čovekom.",
                "",
            ),
        ],
        "great-dane": [
            (
                "Nemačka doga se često naziva „Apolo pasa“ zbog svoje veličanstvene građe i gracioznog izgleda.",
                "Nemačka doga je veličanstvena rasa gracioznog izgleda i odmerenog, mirnog hoda.",
            )
        ],
        "hovawart": [
            (
                "Hovavart je velika nemačka radna rasa, istorijski razvijena kao pas čuvar i imanja, sa imenom koje doslovno znači „čuvar dvorišta”.",
                "Hovavart je velika radna rasa sa gustom, blago talasastom dlakom i smirenim, budnim izrazom.",
            ),
            (
                "Prvobitno korišćen za čuvanje, praćenje traga i spasavanje, rasa kombinuje fizičku snagu",
                "Rasa kombinuje fizičku snagu",
            ),
        ],
        "irish-wolfhound": [
            (
                "Irski vučji hrt je veličanstvena rasa koja oličava i snagu i gracioznost, prvobitno uzgajana za lov na krupnu divljač poput vukova i jelena u Irskoj.",
                "Irski vučji hrt je veličanstvena rasa koja oličava i snagu i gracioznost, sa oštrom dlakom i blagim, dostojanstvenim držanjem.",
            )
        ],
        "italian-sighthound": [
            (
                " Hrtovi su elegantni i atletski psi uzgajani za brzinu i vizuelno praćenje.",
                "",
            ),
        ],
        "italian-spinone": [
            (
                "Italijanski spinone je velika, čvrsta lovačka rasa iz Italije, razvijena za praćenje, pokazivanje i donošenje na izazovnom terenu.",
                "Italijanski spinone je velika, čvrsta lovačka rasa sa oštrom dlakom i dugom, čupavom bradom.",
            )
        ],
        "kai": [
            (
                "Kai ken, poznat i kao kai pas, retka je i drevna japanska rasa, poznata po upadljivoj tigrastoj dlaci",
                "Kai ken, poznat i kao kai pas, retka je rasa, poznata po upadljivoj tigrastoj dlaci",
            ),
            (
                "Prvobitno uzgajan za lov na krupnu divljač poput medveda, divljih svinja i jelena, ovaj pas srednje veličine je okretan, budan i veoma inteligentan.",
                "Ovaj pas srednje veličine je okretan, budan i veoma inteligentan, i potrebni su mu mnogo kretanja i zadatak.",
            ),
        ],
        "keeshond-wolfspitz": [
            (
                "Prvobitno razvijen u Holandiji kao saputnik i pas čuvar na rečnim baržama, rasa je poznata po izražajnim",
                "Rasa je poznata po izražajnim",
            )
        ],
    },
}
