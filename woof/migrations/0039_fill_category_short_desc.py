from django.db import migrations

# One sentence per group for the cards on the Groups page. Only empty fields
# are filled, so anything edited in the admin is left alone.
SHORT = {
    "sheepdogs-cattledogs": {
        "en": "Herding dogs bred to gather, drive and guard livestock. Intelligent, responsive and eager to work with people.",
        "ru": "Пастушьи собаки, выведенные для сбора, выгона и охраны скота. Умные, отзывчивые и охотно работают рядом с человеком.",
        "de": "Hütehunde, die zum Hüten, Treiben und Bewachen von Vieh gezüchtet wurden. Intelligent, aufmerksam und gern mit Menschen bei der Arbeit.",
        "it": "Cani da pastore allevati per radunare, condurre e proteggere il bestiame. Intelligenti, reattivi e felici di lavorare con le persone.",
        "es": "Perros pastores criados para reunir, conducir y proteger el ganado. Inteligentes, receptivos y deseosos de trabajar con las personas.",
        "sr_latn": "Pastirski psi uzgajani da okupljaju, teraju i čuvaju stoku. Inteligentni, odzivni i vole da rade uz čoveka.",
    },
    "pinscher-schnauzer-molossoid": {
        "en": "Powerful guardian and working breeds, from pinschers and schnauzers to mastiffs and mountain dogs. Loyal and steady, with a confident presence.",
        "ru": "Сильные охранные и рабочие породы: от пинчеров и шнауцеров до догов и горных собак. Преданные, уравновешенные, с уверенным характером.",
        "de": "Kräftige Wach- und Arbeitshunde, von Pinschern und Schnauzern bis zu Doggen und Sennenhunden. Treu und ausgeglichen, mit selbstbewusstem Auftreten.",
        "it": "Razze robuste da guardia e da lavoro, dai pinscher e schnauzer ai molossoidi e ai bovari svizzeri. Fedeli ed equilibrati, con una presenza sicura.",
        "es": "Razas fuertes de guarda y trabajo, desde pinschers y schnauzers hasta molosos y perros de montaña. Leales y estables, con una presencia segura.",
        "sr_latn": "Snažne čuvarske i radne rase, od pinčera i šnaucera do molosa i planinskih pasa. Odani i staloženi, sa samouverenim držanjem.",
    },
    "terriers": {
        "en": "Spirited, determined dogs bred to hunt vermin and burrowing game. Courageous and energetic, with plenty of personality.",
        "ru": "Бойкие и упорные собаки, выведенные для охоты на грызунов и норных зверей. Смелые, энергичные и с ярким характером.",
        "de": "Temperamentvolle, entschlossene Hunde, die zur Jagd auf Schädlinge und Bauwild gezüchtet wurden. Mutig und energiegeladen, mit viel Persönlichkeit.",
        "it": "Cani vivaci e determinati, allevati per cacciare i parassiti e la selvaggina di tana. Coraggiosi ed energici, con tanta personalità.",
        "es": "Perros vivaces y decididos, criados para cazar alimañas y presas de madriguera. Valientes y enérgicos, con mucha personalidad.",
        "sr_latn": "Živahni i uporni psi uzgajani za lov na štetočine i divljač iz jazbina. Hrabri i puni energije, sa jakim karakterom.",
    },
    "dachshunds": {
        "en": "Long-bodied, brave hunting dogs bred to track game underground. Bold and persistent despite their small size.",
        "ru": "Длинные смелые охотничьи собаки, выведенные для работы под землёй. Отважные и настойчивые, несмотря на небольшой размер.",
        "de": "Langgestreckte, mutige Jagdhunde, die zur Arbeit unter der Erde gezüchtet wurden. Mutig und beharrlich, trotz ihrer geringen Größe.",
        "it": "Cani da caccia dal corpo lungo e coraggiosi, allevati per lavorare sotto terra. Audaci e tenaci nonostante le piccole dimensioni.",
        "es": "Perros de caza valientes y de cuerpo alargado, criados para rastrear presas bajo tierra. Audaces y tenaces a pesar de su tamaño.",
        "sr_latn": "Dugi i hrabri lovački psi uzgajani za rad pod zemljom. Odvažni i uporni uprkos malom rastu.",
    },
    "spitz-primitive": {
        "en": "Ancient, hardy breeds with thick coats, pointed ears and curled tails. Independent thinkers with strong natural instincts.",
        "ru": "Древние выносливые породы с густой шерстью, острыми ушами и хвостом-бубликом. Самостоятельные, с сильными природными инстинктами.",
        "de": "Uralte, robuste Rassen mit dichtem Fell, Stehohren und geringelter Rute. Eigenständig, mit starken natürlichen Instinkten.",
        "it": "Razze antiche e resistenti con pelo folto, orecchie erette e coda arricciata. Indipendenti, con forti istinti naturali.",
        "es": "Razas antiguas y resistentes, de pelaje denso, orejas erguidas y cola enroscada. Independientes, con fuertes instintos naturales.",
        "sr_latn": "Drevne i izdržljive rase sa gustom dlakom, šiljatim ušima i uvijenim repom. Samostalni, sa jakim prirodnim instinktima.",
    },
    "scent-hounds": {
        "en": "Tireless trackers that follow a scent trail over long distances. Patient, determined and driven by their nose.",
        "ru": "Неутомимые следопыты, идущие по запаховому следу на большие расстояния. Терпеливые, упорные, ведомые носом.",
        "de": "Ausdauernde Spurenfolger, die einer Fährte über weite Strecken folgen. Geduldig, zielstrebig und von ihrer Nase geleitet.",
        "it": "Segugi instancabili che seguono una pista odorosa per lunghe distanze. Pazienti, determinati e guidati dal naso.",
        "es": "Rastreadores incansables que siguen un rastro de olor a lo largo de grandes distancias. Pacientes, decididos y guiados por su olfato.",
        "sr_latn": "Neumorni tragači koji slede miris na velikim udaljenostima. Strpljivi, uporni i vođeni njuhom.",
    },
    "pointing-dogs": {
        "en": "Gundogs that find game and freeze in a pointing stance. Energetic, focused and eager to please.",
        "ru": "Охотничьи собаки, которые находят дичь и замирают в стойке. Энергичные, сосредоточенные и стремятся угодить.",
        "de": "Vorstehhunde, die Wild aufspüren und in der Vorstehhaltung verharren. Energiegeladen, konzentriert und gefallsüchtig.",
        "it": "Cani da ferma che trovano la selvaggina e si immobilizzano in ferma. Energici, concentrati e desiderosi di compiacere.",
        "es": "Perros de muestra que encuentran la caza y se quedan inmóviles en punta. Enérgicos, concentrados y deseosos de agradar.",
        "sr_latn": "Ptičari koji pronalaze divljač i ukočeno zastaju u stavu. Energični, skoncentrisani i željni da ugode.",
    },
    "retrievers-flushing-water-dogs": {
        "en": "Friendly gundogs bred to retrieve game, flush it from cover and work in water. Gentle, social and keen to work with people.",
        "ru": "Дружелюбные охотничьи собаки: приносят дичь, поднимают её из укрытия и работают в воде. Мягкие, общительные и любят работать с человеком.",
        "de": "Freundliche Jagdhunde, die Wild apportieren, aufstöbern und im Wasser arbeiten. Sanft, gesellig und gern mit Menschen bei der Arbeit.",
        "it": "Cani da caccia socievoli, allevati per riportare la selvaggina, stanarla e lavorare in acqua. Docili, socievoli e felici di lavorare con le persone.",
        "es": "Perros de caza amistosos criados para cobrar piezas, levantarlas de la maleza y trabajar en el agua. Dóciles, sociables y deseosos de trabajar con las personas.",
        "sr_latn": "Prijateljski lovački psi koji donose divljač, isteruju je iz zaklona i rade u vodi. Blagi, društveni i vole da rade sa ljudima.",
    },
    "companion-toy-dogs": {
        "en": "Small, affectionate dogs bred mainly for human company. Charming, social and devoted to their owners.",
        "ru": "Небольшие ласковые собаки, выведенные в первую очередь для общения с человеком. Обаятельные, общительные и преданные хозяевам.",
        "de": "Kleine, anhängliche Hunde, die vor allem als Gefährten des Menschen gezüchtet wurden. Charmant, gesellig und ihren Besitzern ergeben.",
        "it": "Cani piccoli e affettuosi, allevati soprattutto per fare compagnia all'uomo. Simpatici, socievoli e devoti ai proprietari.",
        "es": "Perros pequeños y cariñosos, criados sobre todo para hacer compañía a las personas. Encantadores, sociables y devotos de sus dueños.",
        "sr_latn": "Mali i nežni psi uzgajani pre svega za društvo ljudima. Šarmantni, društveni i privrženi vlasnicima.",
    },
    "sighthounds": {
        "en": "Elegant, fast dogs that hunt by sight. Calm and gentle at home, explosive outdoors.",
        "ru": "Изящные быстрые собаки, охотящиеся по зрению. Дома спокойные и мягкие, на улице стремительные.",
        "de": "Elegante, schnelle Hunde, die nach Sicht jagen. Zu Hause ruhig und sanft, draußen explosiv schnell.",
        "it": "Cani eleganti e velocissimi che cacciano a vista. Calmi e dolci in casa, esplosivi all'aperto.",
        "es": "Perros elegantes y veloces que cazan a la vista. Tranquilos y dulces en casa, explosivos al aire libre.",
        "sr_latn": "Elegantni i brzi psi koji love na oko. Mirni i nežni kod kuće, eksplozivni napolju.",
    },
    "breeds-outside-fci-classification": {
        "en": "Breeds not recognised by the FCI but accepted by other kennel clubs such as the AKC or UKC. We keep them in a separate category so they are easy to browse.",
        "ru": "Породы, не признанные FCI, но принятые другими кинологическими клубами, например AKC и UKC. Мы собрали их в отдельной категории, чтобы их было удобно смотреть.",
        "de": "Rassen, die von der FCI nicht anerkannt, aber von anderen Zuchtverbänden wie AKC oder UKC akzeptiert werden. Wir führen sie in einer eigenen Kategorie, damit sie leicht zu finden sind.",
        "it": "Razze non riconosciute dalla FCI ma accettate da altri club cinofili, come AKC e UKC. Le raccogliamo in una categoria separata per sfogliarle facilmente.",
        "es": "Razas no reconocidas por la FCI pero aceptadas por otros clubes caninos, como el AKC o el UKC. Las reunimos en una categoría aparte para consultarlas con facilidad.",
        "sr_latn": "Rase koje FCI ne priznaje, ali ih prihvataju drugi kinološki klubovi, poput AKC i UKC. Držimo ih u zasebnoj kategoriji da bi se lakše pregledale.",
    },
}


def fill(apps, schema_editor):
    Category = apps.get_model("woof", "Category")
    for slug, texts in SHORT.items():
        cat = Category.objects.filter(slug=slug).first()
        if not cat:
            continue
        for lang, text in texts.items():
            field = f"short_desc_{lang}"
            if not getattr(cat, field):
                setattr(cat, field, text)
        if not cat.short_desc:
            cat.short_desc = texts["en"]
        cat.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0038_category_short_desc")]
    operations = [migrations.RunPython(fill, migrations.RunPython.noop)]
