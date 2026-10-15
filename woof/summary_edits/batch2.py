"""Batch 2: azawakh … border-terrier — origin facts removed from the summaries."""

EDITS = {
    "en": {
        "azawakh": [
            (
                "The Azawakh is a unique and elegant breed originating from the Sahel region of West Africa.",
                "The Azawakh is a unique and elegant sighthound with an unusually lean, fine-boned build.",
            ),
            (
                "Known for its slender, athletic build, the Azawakh was traditionally used by the Tuareg people for hunting large game such as gazelles, antelopes, and even wild boar.",
                "Its short, fine coat needs very little care, but the breed feels the cold and appreciates a warm, soft bed.",
            ),
        ],
        "barbado-da-terceira": [
            (
                "The Barbado da Terceira is a rare Portuguese herding breed originating from the island of Terceira in the Azores.",
                "The Barbado da Terceira is a rare herding breed with a long, thick coat and a sturdy, agile build.",
            ),
            (
                "Historically used for managing and guarding cattle, it is an intelligent, agile, and versatile working dog.",
                "It is an intelligent and versatile working dog that needs a real job to stay happy.",
            ),
        ],
        "basset-hound": [
            (
                "Originally bred in France for tracking small game, Basset Hounds have one of the most powerful noses in the dog world",
                "Basset Hounds have one of the most powerful noses in the dog world",
            )
        ],
        "bedlington-terrier": [
            (
                "The Bedlington Terrier is a distinctive, lamb-like terrier breed originally developed in the mining regions of Northumberland, England.",
                "The Bedlington Terrier is a distinctive, lamb-like terrier breed with a soft curly coat and a pear-shaped head.",
            )
        ],
        "black-and-tan-coonhound": [
            (
                "The Black and Tan Coonhound is a powerful and determined scent hound originally developed in the United States for tracking and treeing game, particularly raccoons.",
                "The Black and Tan Coonhound is a powerful and determined scent hound with a short, glossy black-and-tan coat.",
            )
        ],
        "bolognese": [
            (
                "The Bolognese is a small companion breed that originated in Italy, known for its calm",
                "The Bolognese is a small companion breed known for its calm",
            )
        ],
        "border-collie": [
            (
                "originally developed for herding sheep along the border of Scotland and England.",
                "known for its intense gaze and its ability to learn an astonishing number of commands.",
            )
        ],
        "border-terrier": [
            (
                "The Border Terrier is a small, hardy working terrier originally developed along the border region between England and Scotland for fox hunting and vermin control.",
                "The Border Terrier is a small, hardy working terrier with a wiry coat, an otter-like head, and a compact, sturdy build.",
            )
        ],
    },
    "ru": {
        "azawakh": [
            (
                "Азавак — уникальная и элегантная порода родом из региона Сахель в Западной Африке.",
                "Азавак — уникальная и элегантная борзая с необычно сухим, тонкокостным телосложением.",
            ),
            (
                "Известный своим стройным, атлетичным телосложением, азавак традиционно использовался народом туарегов для охоты на крупную дичь: газелей, антилоп и даже диких кабанов.",
                "Короткая тонкая шерсть почти не требует ухода, но порода плохо переносит холод и любит тёплое мягкое место.",
            ),
        ],
        "barbado-da-terceira": [
            (
                "Барбадо да Терсейра — редкая португальская пастушья порода с острова Терсейра в архипелаге Азорские острова.",
                "Барбадо да Терсейра — редкая пастушья порода с длинной густой шерстью и крепким, ловким сложением.",
            ),
            (
                "Исторически использовавшаяся для выпаса и охраны крупного рогатого скота, это умная, ловкая и универсальная рабочая собака.",
                "Это умная и универсальная рабочая собака, которой нужна настоящая работа, чтобы быть счастливой.",
            ),
        ],
        "basset-hound": [
            (
                "Выведенная во Франции для охоты на мелкую дичь по следу, бассет-хаунд обладает одним из самых мощных носов в мире собак",
                "Бассет-хаунд обладает одним из самых мощных носов в мире собак",
            )
        ],
        "bedlington-terrier": [
            (
                "Бедлингтон-терьер — самобытная порода терьеров, внешне напоминающая овцу; выведена в шахтёрских районах Нортумберленда в Англии.",
                "Бедлингтон-терьер — самобытная порода терьеров, внешне напоминающая овцу, с мягкой вьющейся шерстью и грушевидной головой.",
            ),
            (
                " Выведенные изначально для охоты и борьбы с грызунами, они известны отвагой и настойчивостью.",
                "",
            ),
        ],
        "black-and-tan-coonhound": [
            (
                "Блэк-энд-тан кунхаунд — мощная и целеустремлённая гончая по запаху, выведенная в США для выслеживания и загона дичи на дерево, особенно енотов.",
                "Блэк-энд-тан кунхаунд — мощная и целеустремлённая гончая по запаху с короткой блестящей чёрно-подпалой шерстью.",
            ),
            (" Эти собаки часто терпеливы, целеустремлённы и независимы в работе.", ""),
        ],
        "bolognese": [
            (
                "Болоньез — маленькая порода-компаньон родом из Италии, известная",
                "Болоньез — маленькая порода-компаньон, известная",
            )
        ],
        "border-collie": [
            (
                "Бордер-колли считается одной из самых умных пород собак: она была выведена для пастьбы овец на границе Шотландии и Англии.",
                "Бордер-колли считается одной из самых умных пород собак: она известна пристальным взглядом и способностью выучить огромное число команд.",
            )
        ],
        "border-terrier": [
            (
                "Бордер-терьер — небольшая выносливая рабочая порода терьеров, выведенная в приграничном регионе между Англией и Шотландией для охоты на лис и борьбы с грызунами.",
                "Бордер-терьер — небольшая выносливая рабочая порода терьеров с жёсткой шерстью, головой «выдры» и компактным крепким сложением.",
            )
        ],
    },
    "de": {
        "azawakh": [
            (
                "Der Azawakh ist eine einzigartige und elegante Rasse aus der Sahel-Region Westafrikas.",
                "Der Azawakh ist ein einzigartiger, eleganter Windhund mit ungewöhnlich trockenem, feinknochigem Körperbau.",
            ),
            (
                "Bekannt für seinen schlanken, athletischen Körperbau, wurde der Azawakh traditionell von den Tuareg zur Jagd auf Großwild wie Gazellen, Antilopen und sogar Wildschweine eingesetzt.",
                "Sein kurzes, feines Fell braucht kaum Pflege, doch die Rasse ist kälteempfindlich und liebt einen warmen, weichen Platz.",
            ),
        ],
        "barbado-da-terceira": [
            (
                "Der Barbado da Terceira ist eine seltene portugiesische Hütehundrasse von der Insel Terceira auf den Azoren.",
                "Der Barbado da Terceira ist eine seltene Hütehundrasse mit langem, dichtem Fell und kräftigem, wendigem Körperbau.",
            ),
            (
                "Historisch für die Verwaltung und Bewachung von Rindern eingesetzt, ist er ein intelligenter, wendiger und vielseitiger Arbeitshund.",
                "Er ist ein intelligenter und vielseitiger Arbeitshund, der eine echte Aufgabe braucht, um zufrieden zu sein.",
            ),
        ],
        "basset-hound": [
            (
                "Ursprünglich in Frankreich zur Spurensuche nach Kleinwild gezüchtet, hat der Basset Hound eine der stärksten Nasen der Hundewelt",
                "Der Basset Hound hat eine der stärksten Nasen der Hundewelt",
            )
        ],
        "bedlington-terrier": [
            (
                "Der Bedlington Terrier ist eine unverwechselbare, lammähnliche Terrierrasse aus den Bergbauregionen von Northumberland, England.",
                "Der Bedlington Terrier ist eine unverwechselbare, lammähnliche Terrierrasse mit weichem Lockenfell und birnenförmigem Kopf.",
            )
        ],
        "black-and-tan-coonhound": [
            (
                "Der Black and Tan Coonhound ist ein kräftiger und entschlossener Laufhund, ursprünglich in den USA zur Spurensuche und zum Stellen von Wild, besonders Waschbären, gezüchtet.",
                "Der Black and Tan Coonhound ist ein kräftiger und entschlossener Laufhund mit kurzem, glänzendem schwarz-lohfarbenem Fell.",
            )
        ],
        "bolognese": [
            (
                "Der Bologneser ist eine kleine Begleithunderasse aus Italien, bekannt für sein ruhiges",
                "Der Bologneser ist eine kleine Begleithunderasse, bekannt für sein ruhiges",
            )
        ],
        "border-collie": [
            (
                "Der Border Collie gilt weithin als eine der intelligentesten Hunderassen und wurde ursprünglich zum Hüten von Schafen entlang der Grenze zwischen Schottland und England gezüchtet.",
                "Der Border Collie gilt weithin als eine der intelligentesten Hunderassen, bekannt für seinen intensiven Blick und die Fähigkeit, sehr viele Kommandos zu lernen.",
            )
        ],
        "border-terrier": [
            (
                "Der Border Terrier ist ein kleiner, robuster Arbeitsterrier, ursprünglich in der Grenzregion zwischen England und Schottland für Fuchsjagd und Schädlingsbekämpfung gezüchtet.",
                "Der Border Terrier ist ein kleiner, robuster Arbeitsterrier mit drahtigem Fell, otterähnlichem Kopf und kompaktem, zähem Körperbau.",
            )
        ],
    },
    "it": {
        "azawakh": [
            (
                "L'Azawakh è un levriero africano antico e elegante, originario della regione del Sahel.",
                None,
            ),
            (
                "Snello, alto e velocissimo, è un cane da caccia e da guardia per le popolazioni tuareg.",
                "Snello, alto e velocissimo, ha un pelo corto e sottile che richiede poca cura.",
            ),
        ],
        "barbado-da-terceira": [
            (
                "Il Barbado da Terceira è un'antica razza da lavoro dell'isola di Terceira, nelle Azzorre (Portogallo), usata per la conduzione del bestiame.",
                None,
            )
        ],
        "bedlington-terrier": [
            (
                "Originario dell'Inghilterra, era un cane da caccia e da corsa.",
                "Un tempo cane da caccia e da corsa, oggi è soprattutto un compagno di famiglia.",
            )
        ],
        "bichon-frise": [
            (
                "Originario della regione mediterranea, è stato per secoli cane da compagnia di corte e aristocratici.",
                "Ha un mantello che va spazzolato ogni giorno e ama stare al centro dell'attenzione.",
            )
        ],
        "black-and-tan-coonhound": [
            (
                "Il Black and Tan Coonhound è una razza americana di taglia grande, specializzata nella caccia al procione e ad altra selvaggina con il 'treeing'.",
                "Il Black and Tan Coonhound è una razza di taglia grande e dall'ossatura robusta.",
            )
        ],
        "bolognese": [
            (
                "Il Bolognese è una piccola razza italiana dal mantello bianco e soffice",
                "Il Bolognese è una piccola razza dal mantello bianco e soffice",
            )
        ],
        "border-collie": [
            (
                "Originario della zona di confine tra Inghilterra e Scozia, è stato allevato per la conduzione delle pecore e conserva un istinto pastorale straordinario.",
                "Ha un istinto pastorale straordinario e impara con una velocità sorprendente.",
            )
        ],
        "border-terrier": [
            (
                "Il Border Terrier è una razza piccola e robusta, originaria della zona di confine tra Inghilterra e Scozia, dove veniva usata per la caccia alle volpi.",
                "Il Border Terrier è una razza piccola e robusta, con un mantello ruvido e una testa simile a quella di una lontra.",
            )
        ],
    },
    "sr_latn": {
        "azawakh": [
            (
                "Azavak je jedinstvena i elegantna rasa poreklom iz regiona Sahel u Zapadnoj Africi.",
                "Azavak je jedinstvena i elegantna rasa, veoma vitka i suve građe.",
            ),
            (
                "Poznat po vitkoj, atletskoj građi, azavak su tradicionalno koristili narod Tuarega za lov na krupnu divljač poput gazela, antilopa, pa čak i divljih svinja.",
                "Kratka, tanka dlaka zahteva malo nege, ali rasa slabo podnosi hladnoću i voli toplo mesto za odmor.",
            ),
        ],
        "barbado-da-terceira": [
            (
                "Barbado da Terseira je retka portugalska pastirska rasa poreklom sa ostrva Terseira na Azorima.",
                "Barbado da Terseira je retka pastirska rasa sa dugom, gustom dlakom i čvrstom, okretnom građom.",
            ),
            (
                "Istorijski korišćena za upravljanje i čuvanje stoke, inteligentan je, okretan i svestran radni pas.",
                "Inteligentan je i svestran radni pas kome je potreban pravi zadatak da bi bio zadovoljan.",
            ),
        ],
        "basset-hound": [
            (
                "Prvobitno uzgajan u Francuskoj za praćenje sitne divljači, baset hound ima jedan od najmoćnijih noseva u psećem svetu",
                "Baset hound ima jedan od najmoćnijih noseva u psećem svetu",
            )
        ],
        "bedlington-terrier": [
            (
                "Bedlington terijer je prepoznatljiva rasa terijera nalik jagnjetu, prvobitno razvijena u rudarskim oblastima Nortamberlenda u Engleskoj.",
                "Bedlington terijer je prepoznatljiva rasa terijera nalik jagnjetu, sa mekom kovrdžavom dlakom i glavom u obliku kruške.",
            )
        ],
        "black-and-tan-coonhound": [
            (
                "Blek end ten kunhound je snažan i odlučan gonič po mirisu, prvobitno razvijen u Sjedinjenim Američkim Državama za praćenje i teranje divljači na drvo, posebno rakune.",
                "Blek end ten kunhound je snažan i odlučan gonič po mirisu sa kratkom, sjajnom crno-tan dlakom.",
            )
        ],
        "bloodhound": [
            (" Ovi psi su često strpljivi, odlučni i nezavisni.", ""),
        ],
        "bolognese": [
            (
                "Bolonjez je mala rasa saputnika poreklom iz Italije, poznata",
                "Bolonjez je mala rasa saputnika, poznata",
            )
        ],
        "border-collie": [
            (
                "Border koli se široko smatra jednom od najinteligentnijih rasa pasa, prvobitno razvijenom za čuvanje ovaca na granici Škotske i Engleske.",
                "Border koli se široko smatra jednom od najinteligentnijih rasa pasa, poznatom po upornom pogledu i sposobnosti da nauči ogroman broj komandi.",
            )
        ],
        "border-terrier": [
            (
                "Border terijer je mali, čvrst radni terijer, prvobitno razvijen na granici između Engleske i Škotske za lov na lisice i suzbijanje štetočina.",
                "Border terijer je mali, čvrst radni terijer sa žičanom dlakom, glavom nalik vidri i kompaktnom, izdržljivom građom.",
            )
        ],
    },
}
