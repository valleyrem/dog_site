"""Batch 8: kleiner-munsterlander, labrador, kooikerhondje, elkhound, toller,
old-english-sheepdog, otterhound, pekingese."""

EDITS = {
    "en": {
        "kleiner-munsterlander": [
            (
                "The Small Munsterlander is a versatile German hunting breed developed for pointing, tracking, and retrieving both on land and in water.",
                "The Small Munsterlander is a versatile gundog with a brown-and-white coat and a long, feathered tail.",
            )
        ],
        "nederlandse-kooikerhondje": [
            (
                "The Nederlandse Kooikerhondje is a small Dutch sporting breed originally developed as a duck decoy dog, known for its intelligence",
                "The Nederlandse Kooikerhondje is a small sporting breed with a white-and-orange coat and a feathered tail, known for its intelligence",
            )
        ],
        "norwegian-elkhound-grey": [
            (
                "The Norwegian Elkhound is a versatile and hardy breed with a rich history as a hunting dog.",
                "The Norwegian Elkhound is a versatile and hardy breed with a thick grey coat and a tightly curled tail.",
            ),
            (
                "Originally bred for hunting elk, they are known for their exceptional tracking abilities",
                "They are known for their exceptional tracking abilities",
            ),
        ],
        "nova-scotia-duck-tolling-retriever": [
            (
                "The Nova Scotia Duck Tolling Retriever is the smallest of the retriever breeds, originally developed in Canada for luring and retrieving waterfowl.",
                "The Nova Scotia Duck Tolling Retriever is the smallest of the retriever breeds, with a rich red coat and a white-tipped tail.",
            )
        ],
        "old-english-sheepdog": [
            (
                "Historically bred as a herding dog, they are highly skilled at working with livestock",
                "They are highly skilled at working with livestock",
            )
        ],
        "otterhound": [
            (
                "The Otterhound is a large British scent hound originally bred to hunt otters.",
                "The Otterhound is a large scent hound with a rough, water-resistant coat and webbed feet.",
            )
        ],
        "pekingese": [
            (
                "The Pekingese is a small toy breed with ancient origins in China, historically bred as a companion dog for Chinese royalty.",
                "The Pekingese is a small toy breed with a long, flowing coat and a flat, wrinkled face.",
            ),
            (
                "Despite its compact size, it carries a dignified, almost lion-like presence and was once considered sacred in imperial courts.",
                "Despite its compact size, it carries a dignified, almost lion-like presence.",
            ),
        ],
    },
    "ru": {
        "kleiner-munsterlander": [
            (
                "Малый мюнстерлендер — универсальная немецкая охотничья порода, выведенная для стойки, работы по следу и апортировки и на суше, и в воде.",
                "Малый мюнстерлендер — универсальная подружейная порода с коричнево-белой шерстью и длинным, пышным хвостом.",
            ),
            (
                " Они процветают от активности и тесного сотрудничества с проводником. Для довольства им нужны регулярные нагрузки и умственная вовлечённость.",
                "",
            ),
        ],
        "labrador-retriever": [
            (
                " Эти собаки часто преуспевают в дрессировке и разных собачьих видах спорта.",
                "",
            ),
        ],
        "nederlandse-kooikerhondje": [
            (
                "Нейдерландский койкерхондье — небольшая голландская спортивная собака, изначально выведенная как подсадная утиная собака; известна умом",
                "Нейдерландский койкерхондье — небольшая спортивная собака с бело-рыжей шерстью и пышным хвостом, известная умом",
            ),
            (
                " Эта группа включает дружелюбных и универсальных спортивных собак с сильным инстинктом апортировки и помощи.",
                "",
            ),
        ],
        "norwegian-elkhound-grey": [
            (
                "Норвежский элкхунд — универсальная и выносливая порода с богатой историей охотничьей собаки.",
                "Норвежский элкхунд — универсальная и выносливая порода с густой серой шерстью и туго закрученным хвостом.",
            ),
            (
                "Выведенный изначально для охоты на лося, элкхунд известен исключительными способностями",
                "Элкхунд известен исключительными способностями",
            ),
        ],
        "nova-scotia-duck-tolling-retriever": [
            (
                "Новошотландский ретривер (толлер) — самая маленькая ретриверная порода, выведенная в Канаде для подманивания и апортировки водоплавающей дичи.",
                "Новошотландский ретривер (толлер) — самая маленькая ретриверная порода с насыщенно-рыжей шерстью и белым кончиком хвоста.",
            )
        ],
        "old-english-sheepdog": [
            (
                "Исторически выведенная как пастушья собака, она очень искусна в работе со скотом",
                "Она очень искусна в работе со скотом",
            )
        ],
        "otterhound": [
            (
                "Оттерхаунд — крупная британская гончая, первоначально выведенная для охоты на выдр.",
                "Оттерхаунд — крупная гончая с жёсткой водостойкой шерстью и плавательными перепонками на лапах.",
            ),
            (
                " Гончие по запаху движимы мощным обонянием и природной способностью к выслеживанию. Они были выведены для следования по тропе на дальние расстояния с сосредоточенностью и выносливостью.",
                "",
            ),
        ],
        "pekingese": [
            (
                "Пекинес — маленькая декоративная порода с древними китайскими корнями, исторически выведенная как собака-компаньон китайской знати.",
                "Пекинес — маленькая декоративная порода с длинной ниспадающей шерстью и плоской мордой.",
            ),
            (
                "Несмотря на компактные размеры, он обладает достойным, почти львиным присутствием и некогда считался священным при императорском дворе.",
                "Несмотря на компактные размеры, он обладает достойным, почти львиным присутствием.",
            ),
        ],
    },
    "de": {
        "kleiner-munsterlander": [
            (
                "Der Kleine Münsterländer ist eine vielseitige deutsche Jagdhunderasse, entwickelt für Vorstehen, Spurensuche und Apportieren an Land und im Wasser.",
                "Der Kleine Münsterländer ist eine vielseitige Jagdhunderasse mit braun-weißem Fell und langer, gefiederter Rute.",
            ),
            (" Sie brauchen Aktivität und enge Zusammenarbeit mit ihrem Führer.", ""),
        ],
        "labrador-retriever": [
            (
                " Regelmäßige Aktivität und Beschäftigung sind wichtig für ihr Wohlbefinden. Diese Hunde eignen sich oft hervorragend für Training und Hundesport.",
                "",
            )
        ],
        "nederlandse-kooikerhondje": [
            (
                "Das Nederlandse Kooikerhondje ist eine kleine niederländische Sportrasse, ursprünglich als Entenlockhund entwickelt und bekannt für Intelligenz",
                "Das Nederlandse Kooikerhondje ist eine kleine Sportrasse mit weiß-orangenem Fell und gefiederter Rute, bekannt für Intelligenz",
            ),
            (
                " Zu dieser Gruppe gehören freundliche und vielseitige Sport- und Jagdhunde mit einem starken Apportier- und Helferinstinkt.",
                "",
            ),
        ],
        "norwegian-elkhound-grey": [
            (
                "Der Norwegische Elchhund ist eine vielseitige und robuste Rasse mit reicher Jagdgeschichte.",
                "Der Norwegische Elchhund ist eine vielseitige und robuste Rasse mit dichtem grauem Fell und fest gerollter Rute.",
            ),
            (
                "Ursprünglich zur Elchjagd gezüchtet, ist er für außergewöhnliche Spürfähigkeiten",
                "Er ist für außergewöhnliche Spürfähigkeiten",
            ),
        ],
        "nova-scotia-duck-tolling-retriever": [
            (
                "Der Nova Scotia Duck Tolling Retriever ist die kleinste Retrieverrasse, ursprünglich in Kanada zum Anlocken und Apportieren von Wassergeflügel entwickelt.",
                "Der Nova Scotia Duck Tolling Retriever ist die kleinste Retrieverrasse, mit satt rotem Fell und weißer Rutenspitze.",
            )
        ],
        "old-english-sheepdog": [
            (
                "Historisch als Hütehund gezüchtet, ist er hochqualifiziert in der Arbeit mit Vieh",
                "Er ist hochqualifiziert in der Arbeit mit Vieh",
            )
        ],
        "otterhound": [
            (
                "Der Otterhund ist ein großer britischer Laufhund, der ursprünglich für die Jagd auf Otter gezüchtet wurde.",
                "Der Otterhund ist ein großer, kräftiger Laufhund mit Schwimmhäuten zwischen den Zehen.",
            ),
            (
                " Laufhunde werden von ihrem ausgeprägten Geruchssinn und ihrem natürlichen Spürvermögen angetrieben. Sie wurden gezüchtet, um Spuren über lange Strecken mit Fokus und Ausdauer zu verfolgen.",
                "",
            ),
        ],
        "pekingese": [
            (
                "Der Pekingese ist eine kleine Toy-Rasse mit uralten Ursprüngen in China, historisch als Begleithund für das chinesische Kaiserhaus gezüchtet.",
                "Der Pekingese ist eine kleine Toy-Rasse mit langem, fließendem Fell und flachem Gesicht.",
            ),
            (
                "Trotz seiner kompakten Größe trägt er eine würdevolle, fast löwenartige Präsenz und galt einst als heilig an den Kaiserhöfen.",
                "Trotz seiner kompakten Größe trägt er eine würdevolle, fast löwenartige Präsenz.",
            ),
        ],
    },
    "it": {
        "kleiner-munsterlander": [
            (
                "Il Piccolo Münsterländer è una razza tedesca versatile da caccia, di taglia media",
                "Il Piccolo Münsterländer è una razza versatile da caccia, di taglia media",
            )
        ],
        "labrador-retriever": [
            (
                "Originariamente allevato come cane da riporto per la caccia, ha mantenuto un forte istinto per l'acqua",
                "Ha mantenuto un forte istinto per l'acqua",
            )
        ],
        "nederlandse-kooikerhondje": [
            (
                "Il Kooikerhondje è un'antica razza olandese di piccola-media taglia, nota per il mantello bianco e arancio",
                "Il Kooikerhondje è una razza di piccola-media taglia, nota per il mantello bianco e arancio",
            ),
            (
                "Originariamente usato per attirare le anatre nelle trappole (da cui il nome), è oggi un compagno vivace e intelligente.",
                "È un compagno vivace e intelligente, sempre pronto a lavorare con il suo umano.",
            ),
        ],
        "norwegian-elkhound-grey": [
            (
                "L'Elkhound norvegese grigio è un'antica razza scandinava di taglia media, allevata per la caccia all'alce e all'orso.",
                "L'Elkhound norvegese grigio è una razza di taglia media, dal carattere vivace e indipendente.",
            )
        ],
        "nova-scotia-duck-tolling-retriever": [
            (
                "Il Nova Scotia Duck Tolling Retriever è una razza canadese di taglia media, specializzata nella caccia tramite 'tolling': attira le anatre con giochi e movimenti sulla riva.",
                "Il Nova Scotia Duck Tolling Retriever è una razza di taglia media, la più piccola dei retriever.",
            )
        ],
        "old-english-sheepdog": [
            (
                " Originario dell'Inghilterra, era usato per la conduzione del bestiame.",
                "",
            ),
        ],
        "otterhound": [
            (
                "L'Otterhound è un grande segugio britannico originariamente allevato per la caccia alla lontra.",
                "L'Otterhound è un grande segugio con zampe palmate.",
            )
        ],
        "pekingese": [
            (
                "Il Pechinese è una razza antica e regale, originaria della Cina, dove era il cane preferito degli imperatori.",
                None,
            )
        ],
    },
    "sr_latn": {
        "kleiner-munsterlander": [
            (
                "Mali minsterlander je svestrana nemačka lovačka rasa razvijena za pokazivanje, praćenje traga i donošenje i na kopnu i u vodi.",
                "Mali minsterlander je svestrana lovačka rasa sa braon-belom dlakom i dugim, pernatim repom.",
            )
        ],
        "nederlandse-kooikerhondje": [
            (
                "Nederlandski kooikerhondje je mali holandski lovni pas, prvobitno razvijen kao pas mamac za patke, poznat po inteligenciji",
                "Nederlandski kooikerhondje je mali lovni pas sa belo-narandžastom dlakom i pernatim repom, poznat po inteligenciji",
            )
        ],
        "norwegian-elkhound-grey": [
            (
                "Norveški elkhund je svestrana i čvrsta rasa sa bogatom istorijom lovačkog psa.",
                "Norveški elkhund je svestrana i čvrsta rasa sa gustom sivom dlakom i čvrsto uvijenim repom.",
            ),
            (
                "Prvobitno uzgajan za lov na losove, poznat je po izuzetnim sposobnostima praćenja",
                "Poznat je po izuzetnim sposobnostima praćenja",
            ),
        ],
        "nova-scotia-duck-tolling-retriever": [
            (
                "Novoškotski retriver za patke je najmanji od retrivera, prvobitno razvijen u Kanadi za privlačenje i donošenje vodene peradi.",
                "Novoškotski retriver za patke je najmanji od retrivera, sa bogatom crvenom dlakom i belim vrhom repa.",
            ),
            (
                " Ova grupa obuhvata druželjubive i svestrane lovne pse sa snažnim instinktom donošenja i pomaganja.",
                "",
            ),
        ],
        "old-english-sheepdog": [
            (
                "Istorijski uzgajan kao pastirski pas, izuzetno je vešt u radu sa stokom",
                "Izuzetno je vešt u radu sa stokom",
            )
        ],
        "otterhound": [
            (
                "Vidraš je veliki britanski gonič koji je prvobitno uzgajan za lov na vidre.",
                "Vidraš je veliki gonič sa plivaćim kožicama između prstiju.",
            ),
            (
                " Razvijeni su da prate tragove na velikim udaljenostima sa koncentracijom i izdržljivošću. Razvijeni su da prate tragove na velikim udaljenostima sa koncentracijom i izdržljivošću.",
                "",
            ),
        ],
        "pekingese": [
            (
                "Pekinezer je mala patuljasta rasa drevnog porekla iz Kine, istorijski uzgajana kao pas saputnik kineskog plemstva.",
                "Pekinezer je mala patuljasta rasa sa dugom dlakom i ravnim licem.",
            ),
            (
                "Uprkos kompaktnoj veličini, nosi dostojanstveno, gotovo lavlje prisustvo i nekada se smatrao svetim na carskim dvorovima.",
                "Uprkos kompaktnoj veličini, nosi dostojanstveno, gotovo lavlje prisustvo.",
            ),
        ],
    },
}
