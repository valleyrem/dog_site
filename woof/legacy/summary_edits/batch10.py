"""Batch 10: rottweiler, saint-bernard, samoyed, scottish-terrier, shar-pei, shih-tzu,
siberian-husky, sloughi."""

EDITS = {
    "en": {
        "rottweiler": [
            (
                "Originally bred to drive cattle and protect property, Rottweilers are known for their excellent guarding instincts",
                "Rottweilers are known for their excellent guarding instincts",
            )
        ],
        "saint-bernard": [
            (
                "The Saint Bernard is a massive, affectionate breed that has earned its reputation as a rescue dog in the Swiss Alps.",
                "The Saint Bernard is a massive, affectionate breed with a dense coat and a heavy, powerful build.",
            )
        ],
        "samoyed": [
            (
                "Samoyeds are also known for their strength and stamina, originally bred by Siberian nomads to herd reindeer and pull sleds.",
                "Samoyeds are also known for their strength and stamina and need plenty of exercise every day.",
            )
        ],
        "scottish-terrier": [
            (
                "Historically bred for hunting, they retain a strong prey drive and are alert",
                "They retain a strong prey drive and are alert",
            )
        ],
        "shar-pei": [
            (
                "The Chinese Shar-Pei is an ancient dog breed originating from China, known for its loose, wrinkled skin",
                "The Chinese Shar-Pei is known for its loose, wrinkled skin",
            ),
            (
                "Historically used as a farm dog for guarding property and hunting, it is a strong, independent, and highly loyal breed.",
                "It is a strong, independent, and highly loyal breed.",
            ),
        ],
        "shih-tzu": [
            (
                "They have a royal history, originally bred as lap dogs for Chinese royalty, and their calm yet lively personality makes them excellent companions.",
                "Their calm yet lively personality makes them excellent companions.",
            )
        ],
        "siberian-husky": [
            (
                "Known for their endurance and strength, Huskies were originally bred to pull sleds in harsh Arctic conditions, making them naturally suited to outdoor activities and requiring a lot of physical activity.",
                "Known for their endurance and strength, Huskies need a lot of physical activity and are happiest outdoors.",
            )
        ],
        "sloughi": [
            (
                "The Sloughi is an ancient North African sighthound originally bred for hunting game across desert terrain.",
                "The Sloughi is a sighthound with a lean, dry build and a short, fine coat.",
            )
        ],
    },
    "ru": {
        "rottweiler": [
            (
                "Выведенный изначально для перегонки скота и охраны имущества, ротвейлер известен отличными охранными инстинктами",
                "Ротвейлер известен отличными охранными инстинктами",
            )
        ],
        "saint-bernard": [
            (
                "Сенбернар — массивная, ласковая порода, заслужившая репутацию спасателя в швейцарских Альпах.",
                "Сенбернар — массивная, ласковая порода с густой шерстью и тяжёлым, мощным сложением.",
            )
        ],
        "samoyed": [
            (
                "Самоеды также известны силой и выносливостью: их изначально выводили сибирские кочевники для пастьбы северных оленей и перевозки саней.",
                "Самоеды также известны силой и выносливостью и нуждаются в больших ежедневных нагрузках.",
            ),
            (
                " Их поведение может ощущаться более инстинктивным по сравнению с другими группами. При правильной среде это преданные, увлекательные и глубоко выразительные компаньоны.",
                "",
            ),
        ],
        "scottish-terrier": [
            (
                "Исторически выведенный для охоты, скоти сохраняет сильный охотничий инстинкт",
                "Скоти сохраняет сильный охотничий инстинкт",
            )
        ],
        "shar-pei": [
            (
                "Китайский шарпей — древняя порода родом из Китая, известная свободной морщинистой кожей",
                "Китайский шарпей известен свободной морщинистой кожей",
            ),
            (
                "Исторически использовавшийся как фермерская собака для охраны имущества и охоты, шарпей — сильная, независимая и очень преданная порода.",
                "Это сильная, независимая и очень преданная порода.",
            ),
        ],
        "shih-tzu": [
            (
                "У породы царственная история: изначально их выводили как коленных собачек китайской знати, а спокойный, но живой характер делает их отличными компаньонами.",
                "Спокойный, но живой характер делает их отличными компаньонами.",
            ),
            (
                " Многие породы этой группы ласковы, общительны и внимательны к владельцам.",
                "",
            ),
        ],
        "siberian-husky": [
            (
                "Хаски известны своей выносливостью и силой: изначально их выводили для перевозки саней в суровых условиях Арктики, поэтому они от природы приспособлены к активности на свежем воздухе и нуждаются в большом количестве физических нагрузок.",
                "Хаски известны выносливостью и силой, они нуждаются в больших физических нагрузках и лучше всего чувствуют себя на улице.",
            )
        ],
        "sloughi": [
            (
                "Слюги — древняя североафриканская борзая, изначально выведенная для охоты на дичь в пустынной местности.",
                "Слюги — борзая с сухим, лёгким телосложением и короткой тонкой шерстью.",
            )
        ],
    },
    "de": {
        "rottweiler": [
            (
                "Ursprünglich zum Treiben von Vieh und zum Schutz von Eigentum gezüchtet, ist der Rottweiler für seine hervorragenden Schutzinstinkte bekannt",
                "Der Rottweiler ist für seine hervorragenden Schutzinstinkte bekannt",
            )
        ],
        "saint-bernard": [
            (
                "Der Bernhardiner ist eine riesige, anhängliche Rasse, die sich ihren Ruf als Rettungshund in den Schweizer Alpen erworben hat.",
                "Der Bernhardiner ist eine riesige, anhängliche Rasse mit dichtem Fell und schwerem, kräftigem Körperbau.",
            )
        ],
        "samoyed": [
            (
                "Samojeden sind bekannt für Stärke und Ausdauer — ursprünglich von sibirischen Nomaden zum Hüten von Rentieren und Ziehen von Schlitten gezüchtet.",
                "Samojeden sind bekannt für Stärke und Ausdauer und brauchen jeden Tag viel Bewegung.",
            ),
            (
                " Mit der richtigen Umgebung sind sie treue, faszinierende und ausdrucksstarke Begleiter.",
                "",
            ),
        ],
        "scottish-terrier": [
            (
                "Historisch für die Jagd gezüchtet, behält er einen starken Jagdtrieb",
                "Er behält einen starken Jagdtrieb",
            )
        ],
        "shar-pei": [
            (
                "Der Chinesische Shar-Pei ist eine uralte Hunderasse aus China, bekannt für seine lockere, faltige Haut",
                "Der Chinesische Shar-Pei ist bekannt für seine lockere, faltige Haut",
            ),
            (
                "Historisch als Bauernhund zum Bewachen und Jagen eingesetzt, ist er eine starke, unabhängige und hochloyale Rasse.",
                "Er ist eine starke, unabhängige und hochloyale Rasse.",
            ),
        ],
        "shih-tzu": [
            (
                " Er hat eine königliche Geschichte: ursprünglich als Schoßhund für die chinesische Kaiserfamilie gezüchtet.",
                "",
            ),
            (" Sie sind oft klein, aber reich an Persönlichkeit und Charme.", ""),
        ],
        "siberian-husky": [
            (
                "Bekannt für Ausdauer und Kraft, wurde der Husky ursprünglich zum Ziehen von Schlitten in harten arktischen Bedingungen gezüchtet — natürlich für Outdoor-Aktivitäten geeignet, mit hohem Bewegungsbedarf.",
                "Bekannt für Ausdauer und Kraft, braucht der Husky viel Bewegung und ist am glücklichsten im Freien.",
            )
        ],
        "sloughi": [
            (
                "Der Sloughi ist ein uralter nordafrikanischer Windhund, ursprünglich zur Jagd in der Wüste gezüchtet.",
                "Der Sloughi ist ein Windhund mit trockenem, leichtem Körperbau und kurzem, feinem Fell.",
            ),
            (
                " Mit der richtigen Balance sind sie anmutige, friedliche und tief loyale Begleiter.",
                "",
            ),
        ],
    },
    "it": {
        "rottweiler": [
            (
                "Il Rottweiler è una razza grande, potente e sicura di sé, originaria della Germania, dove era usato come cane da guardia e da traino.",
                "Il Rottweiler è una razza grande, potente e sicura di sé, con una testa massiccia e un mantello corto e nero focato.",
            )
        ],
        "saint-bernard": [
            (
                "Il San Bernardo è una razza gigante e storica, resa celebre dai cani da soccorso delle Alpi svizzere.",
                "Il San Bernardo è una razza gigante, con un mantello folto e una corporatura massiccia.",
            )
        ],
        "samoyed": [
            (
                "Originario della Siberia, dove trainava le slitte e aiutava le popolazioni nomadi, è un cane da lavoro forte e resistente.",
                "È un cane da lavoro forte e resistente, che ha bisogno di molta attività fisica.",
            )
        ],
        "scottish-terrier": [
            (
                "Lo Scottish Terrier, soprannominato 'Scottie', è una razza piccola ma dal carattere forte e indipendente, originaria della Scozia.",
                "Lo Scottish Terrier, soprannominato 'Scottie', è una razza piccola ma dal carattere forte e indipendente.",
            )
        ],
        "shar-pei": [
            (
                "Lo Shar Pei è una razza antica cinese, inconfondibile per le pieghe della pelle e il muso particolare che ricorda un ippopotamo.",
                "Lo Shar Pei è inconfondibile per le pieghe della pelle e il muso particolare che ricorda un ippopotamo.",
            ),
            (
                "Era usato come cane da guardia e da combattimento; oggi è un compagno leale e dignitoso.",
                "Oggi è un compagno leale e dignitoso.",
            ),
        ],
        "shih-tzu": [
            (
                "Originario della Cina, dove era cani dei palazzi imperiali, è stato allevato esclusivamente come cane da compagnia.",
                None,
            )
        ],
        "siberian-husky": [
            (
                "L'Husky Siberiano è una razza di taglia media, elegante e atletica, originaria della Siberia dove veniva usata per trainare le slitte.",
                "L'Husky Siberiano è una razza di taglia media, elegante e atletica.",
            )
        ],
        "sloughi": [
            (
                "Lo Sloughi è un levriero antico originario del Nord Africa, allevato per la caccia nel deserto.",
                "Lo Sloughi è un levriero dal fisico asciutto e leggero, con un mantello corto e fine.",
            )
        ],
    },
    "sr_latn": {
        "rottweiler": [
            (
                "Prvobitno uzgajan za tjeranje stoke i čuvanje imovine, rotvajler je poznat po odličnim instinktima čuvara",
                "Rotvajler je poznat po odličnim instinktima čuvara",
            ),
            (
                "Svestrane su rase koje se ističu u različitim ulogama",
                "Svestran je pas koji se ističe u različitim ulogama",
            ),
        ],
        "saint-bernard": [
            (
                "Sveti Bernard je ogromna, privržena rasa koja je stekla reputaciju psa spasavaoca u švajcarskim Alpima.",
                "Sveti Bernard je ogromna, privržena rasa sa gustom dlakom i teškom, snažnom građom.",
            )
        ],
        "samoyed": [
            (
                "Samojedi su takođe poznati po snazi i izdržljivosti — prvobitno su ih sibirski nomadi uzgajali za čuvanje irvasa i vuču saonica.",
                "Samojedi su takođe poznati po snazi i izdržljivosti i potrebna im je svakodnevna velika aktivnost.",
            )
        ],
        "scottish-terrier": [
            (
                "Istorijski uzgajan za lov, zadržava snažan lovački nagon",
                "Zadržava snažan lovački nagon",
            )
        ],
        "shar-pei": [
            (
                "Kineski šar pei je drevna rasa poreklom iz Kine, poznata po labavoj, naboranoj koži",
                "Kineski šar pei je poznat po labavoj, naboranoj koži",
            ),
            (
                "Istorijski korišćen kao seoski pas za čuvanje imovine i lov, snažna je, nezavisna i veoma odana rasa.",
                "To je snažna, nezavisna i veoma odana rasa.",
            ),
        ],
        "shih-tzu": [
            (
                "Ima kraljevsku istoriju — prvobitno uzgajan kao pas u krilu za kineske plemiće — a njegova smirena, ali živahna ličnost čini ga odličnim saputnikom.",
                "Njegova smirena, ali živahna ličnost čini ga odličnim saputnikom.",
            )
        ],
        "siberian-husky": [
            (
                "Poznat po izdržljivosti i snazi, haski je prvobitno uzgajan za vuču saonica u surovim arktičkim uslovima, što ga čini prirodno prilagođenim aktivnostima na otvorenom i zahteva puno fizičke aktivnosti.",
                "Poznat po izdržljivosti i snazi, haski zahteva puno fizičke aktivnosti i najsrećniji je na otvorenom.",
            )
        ],
        "sloughi": [
            (
                "Slugi je drevni severnoafrički hrt, prvobitno uzgajan za lov na divljač u pustinjskom terenu.",
                "Slugi je hrt suve, lake građe i kratke, fine dlake.",
            )
        ],
    },
}
