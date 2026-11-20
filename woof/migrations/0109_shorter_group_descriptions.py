from django.db import migrations

# Card texts of the Groups page, about 110 characters each.
SHORT = {
    "sheepdogs-cattledogs": {
        "en": "Herding dogs bred to gather, drive and guard livestock. Intelligent, responsive and eager to work with people.",
        "ru": "Пастушьи собаки, выведенные для сбора, выгона и охраны скота. Умные, отзывчивые, охотно работают с человеком.",
        "de": "Hütehunde, die Vieh sammeln, treiben und bewachen. Intelligent, aufmerksam und gern mit Menschen bei der Arbeit.",
        "it": "Cani da pastore per radunare, condurre e proteggere il bestiame. Intelligenti, reattivi e pronti a collaborare.",
        "es": "Perros pastores para reunir, conducir y proteger el ganado. Inteligentes, receptivos y deseosos de trabajar.",
        "sr_latn": "Pastirski psi uzgajani da okupljaju, teraju i čuvaju stoku. Inteligentni, odzivni i vole da rade uz čoveka.",
    },
    "pinscher-schnauzer-molossoid": {
        "en": "Powerful guardian and working breeds, from pinschers to mastiffs. Loyal and steady, with a confident presence.",
        "ru": "Сильные охранные и рабочие породы, от пинчеров до догов. Преданные и уравновешенные, с уверенным характером.",
        "de": "Kräftige Wach- und Arbeitshunde, von Pinschern bis Doggen. Treu und ausgeglichen, selbstbewusst im Auftreten.",
        "it": "Razze robuste da guardia e da lavoro, dai pinscher ai molossoidi. Fedeli ed equilibrati, con una presenza sicura.",
        "es": "Razas fuertes de guarda y trabajo, de pinschers a molosos. Leales y estables, con una presencia segura.",
        "sr_latn": "Snažne čuvarske i radne rase, od pinčera do molosa. Odani i staloženi, sa samouverenim i sigurnim držanjem.",
    },
    "terriers": {
        "en": "Spirited, determined dogs bred to hunt vermin and burrowing game. Courageous, energetic, full of personality.",
        "ru": "Бойкие упорные собаки, выведенные для охоты на грызунов и норных зверей. Смелые, энергичные, с ярким характером.",
        "de": "Temperamentvolle Hunde für die Jagd auf Schädlinge und Bauwild. Mutig, energiegeladen, mit viel Persönlichkeit.",
        "it": "Cani vivaci e determinati, allevati per cacciare parassiti e selvaggina di tana. Coraggiosi, energici, di carattere.",
        "es": "Perros vivaces y decididos, criados para cazar alimañas y presas de madriguera. Valientes y enérgicos.",
        "sr_latn": "Živahni i uporni psi uzgajani za lov na štetočine i divljač iz jazbina. Hrabri i puni energije, sa jakim karakterom.",
    },
    "dachshunds": {
        "en": "Long-bodied, brave hunting dogs bred to track game underground. Bold and persistent despite their small size.",
        "ru": "Длинные смелые охотничьи собаки, выведенные для работы под землёй. Отважные и настойчивые, несмотря на размер.",
        "de": "Langgestreckte, mutige Jagdhunde für die Arbeit unter der Erde. Kühn und beharrlich trotz ihrer geringen Größe.",
        "it": "Cani da caccia dal corpo lungo, allevati per lavorare sotto terra. Audaci e tenaci nonostante le piccole dimensioni.",
        "es": "Perros de caza de cuerpo alargado, criados para trabajar bajo tierra. Audaces y tenaces a pesar de su tamaño.",
        "sr_latn": "Dugi i hrabri lovački psi uzgajani za praćenje divljači pod zemljom. Odvažni i uporni uprkos malom rastu.",
    },
    "spitz-primitive": {
        "en": "Ancient, hardy breeds with thick coats, pointed ears and curled tails. Independent, with strong instincts.",
        "ru": "Древние выносливые породы с густой шерстью, острыми ушами и хвостом-бубликом. Самостоятельные, с сильными инстинктами.",
        "de": "Uralte, robuste Rassen mit dichtem Fell, Stehohren und geringelter Rute. Eigenständig, mit starken Instinkten.",
        "it": "Razze antiche e resistenti con pelo folto, orecchie erette e coda arricciata. Indipendenti, con forti istinti.",
        "es": "Razas antiguas y resistentes, de pelaje denso, orejas erguidas y cola enroscada. Independientes, con instintos fuertes.",
        "sr_latn": "Drevne i izdržljive rase sa gustom dlakom, šiljatim ušima i uvijenim repom. Samostalni, sa jakim prirodnim instinktima.",
    },
    "scent-hounds": {
        "en": "Tireless trackers that follow a scent trail over long distances. Patient, determined and driven by their nose.",
        "ru": "Неутомимые следопыты, идущие по запаховому следу на большие расстояния. Терпеливые, упорные, ведомые носом.",
        "de": "Ausdauernde Spurenfolger, die einer Fährte über weite Strecken folgen. Geduldig, zielstrebig, nasengesteuert.",
        "it": "Segugi instancabili che seguono una pista odorosa per lunghe distanze. Pazienti, determinati e guidati dal naso.",
        "es": "Rastreadores incansables que siguen un rastro de olor a grandes distancias. Pacientes y guiados por su olfato.",
        "sr_latn": "Neumorni tragači koji slede trag mirisa na velikim udaljenostima. Strpljivi, uporni i vođeni njuhom.",
    },
    "pointing-dogs": {
        "en": "Gundogs that search for game and freeze in a pointing stance. Energetic, focused and eager to please.",
        "ru": "Легавые собаки, которые находят дичь и замирают в стойке. Энергичные, сосредоточенные, стремятся угодить.",
        "de": "Vorstehhunde, die Wild aufspüren und in der Vorstehhaltung verharren. Energiegeladen, konzentriert und folgsam.",
        "it": "Cani da ferma che trovano la selvaggina e si immobilizzano in ferma. Energici, attenti e desiderosi di compiacere.",
        "es": "Perros de muestra que encuentran la caza y se quedan inmóviles en punta. Enérgicos y deseosos de agradar.",
        "sr_latn": "Ptičari koji pronalaze divljač i ukočeno zastaju u stavu. Energični, skoncentrisani i željni da ugode.",
    },
    "retrievers-flushing-water-dogs": {
        "en": "Hunting dogs specializing in finding and retrieving game, including from water. Friendly and sociable.",
        "ru": "Охотничьи собаки, специализирующиеся на поиске и подаче дичи, в том числе из воды. Дружелюбные и общительные.",
        "de": "Jagdhunde, die auf das Aufspüren und Apportieren von Wild spezialisiert sind, auch aus dem Wasser. Freundlich.",
        "it": "Cani da caccia specializzati nel trovare e riportare la selvaggina, anche in acqua. Amichevoli e socievoli.",
        "es": "Perros de caza especializados en localizar y cobrar piezas, también en el agua. Amigables y sociables.",
        "sr_latn": "Lovački psi specijalizovani za pronalaženje i donošenje divljači, uključujući i iz vode. Prijateljski i druželjubivi.",
    },
    "companion-toy-dogs": {
        "en": "Small, affectionate dogs bred mainly for human company. Charming, social and devoted to their owners.",
        "ru": "Небольшие ласковые собаки, выведенные в первую очередь для общения с человеком. Обаятельные и преданные.",
        "de": "Kleine, anhängliche Hunde, die vor allem als Gefährten des Menschen gezüchtet wurden. Charmant und ergeben.",
        "it": "Cani piccoli e affettuosi, allevati soprattutto per fare compagnia all'uomo. Simpatici e devoti ai proprietari.",
        "es": "Perros pequeños y cariñosos, criados sobre todo para hacer compañía a las personas. Encantadores y devotos.",
        "sr_latn": "Mali i nežni psi uzgajani pre svega za društvo ljudima. Šarmantni, društveni i privrženi vlasnicima.",
    },
    "sighthounds": {
        "en": "Elegant, fast dogs that hunt by sight. Calm and gentle at home, explosive outdoors, built for speed.",
        "ru": "Изящные быстрые собаки, охотящиеся по зрению. Дома спокойные и мягкие, на улице стремительные и азартные.",
        "de": "Elegante, schnelle Hunde, die nach Sicht jagen. Zu Hause ruhig und sanft, draußen explosiv schnell.",
        "it": "Cani eleganti e veloci che cacciano a vista. Calmi e dolci in casa, esplosivi all'aperto, nati per la velocità.",
        "es": "Perros elegantes y veloces que cazan a la vista. Tranquilos y dulces en casa, explosivos al aire libre.",
        "sr_latn": "Elegantni i brzi psi koji love na oko. Mirni i nežni kod kuće, eksplozivni napolju, stvoreni za brzinu.",
    },
    "breeds-outside-fci-classification": {
        "en": "Breeds recognized by other kennel clubs (AKC, UKC, etc.) or with a documented history of their own.",
        "ru": "Породы, признанные другими кинологическими клубами (AKC, UKC и др.) или имеющие документированную историю.",
        "de": "Von anderen Kynologenverbänden (AKC, UKC usw.) anerkannte Rassen oder Rassen mit dokumentierter Geschichte.",
        "it": "Razze riconosciute da altre organizzazioni cinofile (AKC, UKC, ecc.) o con una storia documentata.",
        "es": "Razas reconocidas por otras organizaciones caninas (AKC, UKC, etc.) o con una historia documentada.",
        "sr_latn": "Rase koje priznaju druge kinološke organizacije (AKC, UKC i dr.) ili imaju dokumentovanu istoriju.",
    },
}


def update(apps, schema_editor):
    Category = apps.get_model("woof", "Category")
    for slug, texts in SHORT.items():
        cat = Category.objects.filter(slug=slug).first()
        if not cat:
            continue
        for lang, text in texts.items():
            setattr(cat, f"short_desc_{lang}", text)
        cat.short_desc = texts["en"]
        cat.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0108_restore_native_name")]
    operations = [migrations.RunPython(update, migrations.RunPython.noop)]
