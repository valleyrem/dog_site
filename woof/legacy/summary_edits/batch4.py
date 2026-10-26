"""Batch 4: borzoi, boxer, brussels-griffon, bulldog, bull-terrier, cane-corso."""

EDITS = {
    "en": {
        "borzoi": [
            (
                "The Borzoi, also known as the Russian Wolfhound (Russian Hunting Sighthound), is a majestic and elegant breed renowned for",
                "The Borzoi is a majestic and elegant breed renowned for",
            ),
            (
                "Originally bred in Russia for hunting wolves, Borzois have an elongated, slender build",
                "Borzois have an elongated, slender build",
            ),
        ],
        "boxer": [
            (
                "The Boxer is a medium-to-large working breed from Germany, known for its strength",
                "The Boxer is a medium-to-large working breed known for its strength",
            ),
            (
                "Originally developed for hunting and guarding, the breed later became widely used in military and service roles.",
                "They need plenty of exercise and mental work to stay calm and content.",
            ),
        ],
        "brussels-griffon": [
            (
                "The Brussels Griffon is a small companion breed originating from Belgium, historically developed from stable dogs used for hunting vermin.",
                "The Brussels Griffon is a small companion breed with a wiry or smooth coat and a lively, watchful expression.",
            ),
            (
                "Over time, the breed transitioned into a companion role and became especially valued for its expressive, almost human-like face and strong emotional attachment to its owners.",
                "It is especially valued for its expressive, almost human-like face.",
            ),
        ],
        "cane-corso": [
            (
                "The Cane Corso is a powerful and muscular Italian breed known for its protective instincts",
                "The Cane Corso is a powerful and muscular breed known for its protective instincts",
            ),
            (
                "Originally bred for guarding property, protecting livestock, and hunting large game, Cane Corsos are versatile working dogs.",
                "Cane Corsos are versatile working dogs that need a job, clear rules, and an experienced owner.",
            ),
        ],
    },
    "ru": {
        "borzoi": [
            (
                "Выведенная в России для охоты на волков, борзая обладает вытянутым стройным телосложением",
                "Борзая обладает вытянутым стройным телосложением",
            )
        ],
        "boxer": [
            (
                "Боксёр — рабочая порода среднего или крупного размера из Германии, известная",
                "Боксёр — рабочая порода среднего или крупного размера, известная",
            ),
            (
                "Изначально выведенный для охоты и охраны, боксёр позднее широко использовался в военных и служебных ролях.",
                "Ему нужны большие нагрузки и умственная работа, чтобы оставаться спокойным и довольным.",
            ),
            (
                " Многие из этих собак изначально выводились для охраны, фермерской работы и общения с человеком.",
                "",
            ),
        ],
        "brussels-griffon": [
            (
                "Брюссельский гриффон — маленькая порода-компаньон родом из Бельгии, исторически произошедшая от собачек, живших в конюшнях и охотeвших на грызунов.",
                "Брюссельский гриффон — маленькая порода-компаньон с жёсткой или гладкой шерстью и живым, внимательным выражением морды.",
            ),
            (
                "Со временем порода перешла в роль компаньона и особенно ценётся за выразительную, почти человеческую морду и сильную эмоциональную привязанность к владельцам.",
                "Особенно ценят её за выразительную, почти человеческую морду.",
            ),
        ],
        "cane-corso": [
            (
                "Кане-корсо — мощная и мускулистая итальянская порода, известная защитными инстинктами",
                "Кане-корсо — мощная и мускулистая порода, известная защитными инстинктами",
            ),
            (
                "Изначально выведенная для охраны имущества, защиты скота и охоты на крупную дичь, кане-корсо — универсальная рабочая собака.",
                "Кане-корсо — универсальная рабочая собака, которой нужны занятие, чёткие правила и опытный владелец.",
            ),
        ],
    },
    "de": {
        "borzoi": [
            (
                "Ursprünglich in Russland zur Wolfsjagd gezüchtet, haben Borzois einen länglichen, schlanken Körperbau",
                "Borzois haben einen länglichen, schlanken Körperbau",
            )
        ],
        "boxer": [
            (
                "Der Boxer ist eine mittelgroße bis große Arbeitshundrasse aus Deutschland, bekannt für Kraft",
                "Der Boxer ist eine mittelgroße bis große Arbeitshundrasse, bekannt für Kraft",
            ),
            (
                "Ursprünglich für Jagd und Wachdienst gezüchtet, wurde die Rasse später vielseitig im Militär- und Dienstwesen eingesetzt.",
                "Er braucht viel Bewegung und geistige Arbeit, um ruhig und zufrieden zu bleiben.",
            ),
            (
                " Viele dieser Hunde wurden ursprünglich für Schutz, Hofarbeit und Gesellschaft gezüchtet.",
                "",
            ),
        ],
        "brussels-griffon": [
            (
                "Der Brüsseler Griffon ist eine kleine Begleithunderasse aus Belgien, ursprünglich aus Stallhunden zur Schädlingsjagd entwickelt.",
                "Der Brüsseler Griffon ist eine kleine Begleithunderasse mit drahtigem oder glattem Fell und einem lebhaften, wachsamen Ausdruck.",
            ),
            (
                "Mit der Zeit wurde die Rasse zum Begleithund und vor allem für ihr ausdrucksstarkes, fast menschliches Gesicht und ihre starke emotionale Bindung an ihre Besitzer geschätzt.",
                "Vor allem ihr ausdrucksstarkes, fast menschliches Gesicht wird geschätzt.",
            ),
        ],
        "cane-corso": [
            (
                "Der Cane Corso ist eine kräftige und muskulöse italienische Rasse, bekannt für Schutzinstinkte",
                "Der Cane Corso ist eine kräftige und muskulöse Rasse, bekannt für Schutzinstinkte",
            ),
            (
                "Ursprünglich zum Bewachen von Eigentum, Schutz von Vieh und zur Jagd auf Großwild gezüchtet, ist der Cane Corso ein vielseitiger Arbeitshund.",
                "Der Cane Corso ist ein vielseitiger Arbeitshund, der eine Aufgabe, klare Regeln und einen erfahrenen Besitzer braucht.",
            ),
        ],
    },
    "it": {
        "borzoi": [
            (
                "Il Borzoi, noto anche come Levriero Russo, è una razza grande ed elegante, allevata in Russia per la caccia al lupo.",
                "Il Borzoi è una razza grande ed elegante, con un bisogno quotidiano di corsa libera.",
            )
        ],
        "boxer": [
            (
                "Il Boxer è una razza di taglia media-grande, muscolosa e piena di energia, originaria della Germania.",
                "Il Boxer è una razza di taglia media-grande, muscolosa e piena di energia.",
            )
        ],
        "brussels-griffon": [
            (
                "Il Grifone di Bruxelles è una piccola razza belga dal carattere deciso",
                "Il Grifone di Bruxelles è una piccola razza dal carattere deciso",
            )
        ],
        "bulldog": [
            (
                "Originario dell'Inghilterra, è un cane da compagnia dal cuore d'oro",
                "È un cane da compagnia dal cuore d'oro",
            )
        ],
        "bull-terrier": [
            (
                "Originario dell'Inghilterra, è un cane coraggioso, energico e dal carattere unico",
                "È un cane coraggioso, energico e dal carattere unico",
            )
        ],
        "cane-corso": [
            (
                "Il Cane Corso è una razza italiana grande e possente, discendente dei molossi romani, usata storicamente come cane da guardia, da guerra e per la caccia grossa.",
                "Il Cane Corso è una razza grande e possente, con una testa massiccia e uno sguardo vigile.",
            )
        ],
    },
    "sr_latn": {
        "borzoi": [
            (
                "Borzoj, poznat i kao ruski hrt, veličanstvena je i elegantna rasa",
                "Borzoj je veličanstvena i elegantna rasa",
            ),
            (
                "Prvobitno uzgajan u Rusiji za lov na vukove, borzoj ima izduženu, vitku građu",
                "Borzoj ima izduženu, vitku građu",
            ),
        ],
        "boxer": [
            (
                "Bokser je radna rasa srednje do velike veličine iz Nemačke, poznata",
                "Bokser je radna rasa srednje do velike veličine, poznata",
            ),
            (
                "Prvobitno razvijen za lov i čuvanje, rasa je kasnije postala široko korišćena u vojnim i službenim ulogama.",
                "Potrebne su mu velike količine vežbe i mentalnog rada da bi ostao smiren i zadovoljan.",
            ),
        ],
        "brussels-griffon": [
            (
                "Briselski grifon je mala rasa saputnika poreklom iz Belgije, istorijski razvijena od štalskih pasa korišćenih za lov na štetočine.",
                "Briselski grifon je mala rasa saputnika sa žičanom ili glatkom dlakom i živim, budnim izrazom lica.",
            ),
            (
                "Vremenom je rasa prešla u ulogu saputnika i postala posebno cenjena zbog izražajnog, gotovo ljudskog lica i snažne emotivne vezanosti za vlasnike.",
                "Posebno je cenjena zbog izražajnog, gotovo ljudskog lica.",
            ),
            ("klasifikaciji patuljasте rase", "klasifikaciji patuljaste rase"),
        ],
        "cane-corso": [
            (
                "Kane korso je moćna i mišićava italijanska rasa poznata po zaštitničkim instinktima",
                "Kane korso je moćna i mišićava rasa poznata po zaštitničkim instinktima",
            ),
            (
                "Prvobitno uzgajan za čuvanje imovine, zaštitu stoke i lov na krupnu divljač, kane korso je svestran radni pas.",
                "Kane korso je svestran radni pas kome su potrebni zadatak, jasna pravila i iskusan vlasnik.",
            ),
        ],
    },
}
