import importlib

from django.db import migrations

# The three health paragraphs are assembled from what the site already knows
# about each breed: size, coat, activity and the breed's health concerns
# (the table kept in migration 0042). Only empty fields are filled, so
# anything written by hand in the admin is left alone.
_seed = importlib.import_module("woof.migrations.0042_fill_health_conditions")
CONDITIONS = _seed.CONDITIONS
BREEDS = _seed.BREEDS

LANGS = ("en", "ru", "de", "it", "es", "sr_latn")


def T(*texts):
    return dict(zip(LANGS, texts))


BASE = {
    "small": T(
        "A small breed, generally sturdy for its size, that tends to age well when its teeth, weight and joints are looked after.",
        "Небольшая порода, как правило, крепкая для своего размера; она хорошо стареет, если следить за зубами, весом и суставами.",
        "Eine kleine Rasse, für ihre Größe meist robust, die gut altert, wenn man auf Zähne, Gewicht und Gelenke achtet.",
        "Una razza di piccola taglia, in genere robusta per le sue dimensioni, che invecchia bene se si curano denti, peso e articolazioni.",
        "Una raza pequeña, en general robusta para su tamaño, que envejece bien si se cuidan los dientes, el peso y las articulaciones.",
        "Mala rasa, uglavnom otporna za svoju veličinu, koja dobro stari ako se vodi računa o zubima, težini i zglobovima.",
    ),
    "medium": T(
        "A medium-sized breed that is generally healthy, provided it gets regular exercise, a balanced diet and routine veterinary care.",
        "Порода среднего размера, в целом здоровая при регулярных нагрузках, сбалансированном питании и плановых визитах к ветеринару.",
        "Eine mittelgroße Rasse, die bei regelmäßiger Bewegung, ausgewogener Ernährung und routinemäßiger tierärztlicher Betreuung in der Regel gesund bleibt.",
        "Una razza di taglia media, in generale sana se ha movimento regolare, alimentazione equilibrata e controlli veterinari di routine.",
        "Una raza de tamaño medio, en general sana si hace ejercicio con regularidad, come de forma equilibrada y recibe controles veterinarios de rutina.",
        "Rasa srednje veličine, uglavnom zdrava uz redovno kretanje, uravnoteženu ishranu i redovne veterinarske kontrole.",
    ),
    "large": T(
        "A large breed whose joints and heart carry more load, so steady growth in puppyhood and a lean body weight matter a great deal.",
        "Крупная порода: суставы и сердце несут повышенную нагрузку, поэтому очень важны равномерный рост в щенячестве и стройное телосложение.",
        "Eine große Rasse, bei der Gelenke und Herz stärker belastet sind; deshalb sind gleichmäßiges Wachstum im Welpenalter und ein schlankes Körpergewicht besonders wichtig.",
        "Una razza di taglia grande, in cui articolazioni e cuore sopportano un carico maggiore: per questo contano molto una crescita regolare da cucciolo e un peso snello.",
        "Una raza grande en la que las articulaciones y el corazón soportan más carga, por lo que importan mucho un crecimiento pausado de cachorro y un peso esbelto.",
        "Velika rasa čiji zglobovi i srce nose veće opterećenje, pa su ravnomeran rast u štenećem dobu i vitka telesna masa veoma važni.",
    ),
}

LIFE = T(
    "Typical lifespan is {life} years.",
    "Средняя продолжительность жизни — {life} лет.",
    "Die typische Lebenserwartung beträgt {life} Jahre.",
    "L'aspettativa di vita tipica è di {life} anni.",
    "La esperanza de vida habitual es de {life} años.",
    "Uobičajeni životni vek je {life} godina.",
)

EXTRA = {
    "brachy": T(
        "The short muzzle makes it sensitive to heat and heavy exertion, so walks are best in the cool hours.",
        "Короткая морда делает её чувствительной к жаре и тяжёлым нагрузкам, поэтому гулять лучше в прохладные часы.",
        "Die kurze Schnauze macht sie empfindlich gegen Hitze und starke Anstrengung, daher sind Spaziergänge in kühleren Stunden am besten.",
        "Il muso corto la rende sensibile al caldo e agli sforzi intensi, quindi le passeggiate sono meglio nelle ore fresche.",
        "El hocico corto la hace sensible al calor y al esfuerzo intenso, por lo que conviene pasear en las horas frescas.",
        "Kratka njuška čini je osetljivom na vrućinu i veliki napor, pa su šetnje najbolje u hladnijim satima.",
    ),
    "coat": T(
        "Regular brushing also helps you spot skin problems early.",
        "Регулярное расчёсывание заодно помогает вовремя заметить проблемы с кожей.",
        "Regelmäßiges Bürsten hilft außerdem, Hautprobleme früh zu erkennen.",
        "Spazzolare con regolarità aiuta anche a notare per tempo i problemi della pelle.",
        "Cepillar el pelaje con regularidad también ayuda a detectar a tiempo los problemas de la piel.",
        "Redovno četkanje pomaže i da se na vreme uoče problemi sa kožom.",
    ),
    "active": T(
        "Daily exercise keeps muscles and joints in good shape and helps prevent weight gain.",
        "Ежедневные нагрузки поддерживают мышцы и суставы в хорошей форме и помогают не набирать лишний вес.",
        "Tägliche Bewegung hält Muskeln und Gelenke fit und beugt Übergewicht vor.",
        "L'esercizio quotidiano mantiene in forma muscoli e articolazioni e aiuta a evitare il sovrappeso.",
        "El ejercicio diario mantiene en forma músculos y articulaciones y ayuda a evitar el sobrepeso.",
        "Svakodnevno kretanje održava mišiće i zglobove u dobroj formi i sprečava gojaznost.",
    ),
    "calm": T(
        "A calm temperament makes weight gain easy, so portions are worth watching.",
        "Спокойный нрав располагает к набору веса, поэтому порции стоит контролировать.",
        "Das ruhige Wesen begünstigt Gewichtszunahme, daher sollte man die Portionen im Blick behalten.",
        "Il carattere tranquillo favorisce l'aumento di peso, quindi conviene controllare le porzioni.",
        "El carácter tranquilo favorece que gane peso, así que conviene vigilar las raciones.",
        "Miran temperament olakšava debljanje, pa treba paziti na veličinu obroka.",
    ),
}

RISK_INTRO = T(
    "The concerns most often reported in this breed are {list}.",
    "Чаще всего у этой породы отмечают такие проблемы: {list}.",
    "Bei dieser Rasse werden am häufigsten genannt: {list}.",
    "I problemi più spesso segnalati in questa razza sono {list}.",
    "Los problemas que se citan con más frecuencia en esta raza son {list}.",
    "Kod ove rase se najčešće navode: {list}.",
)

RISK_EXTRA = {
    "bloat": T(
        "Bloat is an emergency: avoid heavy exercise around mealtimes and see a vet at once if the belly swells or the dog retches without vomiting.",
        "Заворот желудка — неотложное состояние: не нагружайте собаку до и после еды и сразу обращайтесь к ветеринару, если живот вздулся или собака давится без рвоты.",
        "Eine Magendrehung ist ein Notfall: Starke Anstrengung rund um die Mahlzeiten vermeiden und bei aufgeblähtem Bauch oder erfolglosem Würgen sofort zum Tierarzt.",
        "La torsione gastrica è un'emergenza: evita sforzi intensi attorno ai pasti e rivolgiti subito al veterinario se la pancia si gonfia o il cane ha conati senza vomitare.",
        "La torsión gástrica es una urgencia: evita el ejercicio intenso en torno a las comidas y acude enseguida al veterinario si el abdomen se hincha o el perro tiene arcadas sin vomitar.",
        "Torzija želuca je hitno stanje: izbegavajte jak napor oko obroka i odmah idite veterinaru ako se stomak naduje ili pas pokušava da povraća bez uspeha.",
    ),
    "anesthesia": T(
        "Tell the vet about the breed's sensitivity to anesthesia before any procedure.",
        "Перед любой процедурой предупредите ветеринара о чувствительности породы к наркозу.",
        "Weisen Sie vor jedem Eingriff die Tierärztin oder den Tierarzt auf die Narkoseempfindlichkeit der Rasse hin.",
        "Prima di qualsiasi intervento informa il veterinario della sensibilità della razza all'anestesia.",
        "Antes de cualquier intervención, avisa al veterinario de la sensibilidad de la raza a la anestesia.",
        "Pre svake intervencije upozorite veterinara na osetljivost rase na anesteziju.",
    ),
    "heat": T(
        "Avoid exertion in hot weather and never leave the dog in a warm car or room.",
        "В жару избегайте нагрузок и никогда не оставляйте собаку в тёплой машине или комнате.",
        "Bei Hitze keine Anstrengung und den Hund niemals in einem warmen Auto oder Raum lassen.",
        "Con il caldo evita gli sforzi e non lasciare mai il cane in un'auto o in una stanza calda.",
        "Con calor evita el esfuerzo y no dejes nunca al perro en un coche o una habitación calurosos.",
        "Po vrućini izbegavajte napor i nikada ne ostavljajte psa u zagrejanom automobilu ili prostoriji.",
    ),
    "hereditary": T(
        "Many of these conditions are partly hereditary, so the health of the parents matters when choosing a puppy.",
        "Многие из этих состояний отчасти наследственные, поэтому при выборе щенка важно здоровье родителей.",
        "Viele dieser Erkrankungen sind teilweise erblich, daher zählt bei der Wahl eines Welpen die Gesundheit der Elterntiere.",
        "Molte di queste condizioni sono in parte ereditarie, quindi nella scelta del cucciolo conta la salute dei genitori.",
        "Muchas de estas afecciones son en parte hereditarias, por lo que al elegir un cachorro importa la salud de los padres.",
        "Mnoga od ovih stanja su delimično nasledna, pa pri izboru štenceta zdravlje roditelja ima veliki značaj.",
    ),
    "care": T(
        "Much of the rest can be kept in check with preventive care: weight control, dental hygiene and regular checks of the ears and skin.",
        "Остальное во многом можно держать под контролем профилактикой: контролем веса, гигиеной зубов и регулярным осмотром ушей и кожи.",
        "Vieles lässt sich durch Vorsorge in Schach halten: Gewichtskontrolle, Zahnpflege und regelmäßige Kontrollen von Ohren und Haut.",
        "Gran parte del resto si tiene sotto controllo con la prevenzione: controllo del peso, igiene dentale e controlli regolari di orecchie e pelle.",
        "Buena parte del resto se controla con prevención: control del peso, higiene dental y revisiones regulares de oídos y piel.",
        "Veći deo ostalog može se držati pod kontrolom prevencijom: kontrolom težine, higijenom zuba i redovnim pregledom ušiju i kože.",
    ),
}

RISK_RARE = T(
    "This breed is uncommon, so documented health data is limited; ask the breeder about the parents' health and keep up with regular veterinary check-ups.",
    "Порода редкая, поэтому данных о её здоровье мало; расспросите заводчика о здоровье родителей и регулярно показывайте собаку ветеринару.",
    "Die Rasse ist selten, daher gibt es nur wenige dokumentierte Gesundheitsdaten; fragen Sie den Züchter nach der Gesundheit der Elterntiere und gehen Sie regelmäßig zur Kontrolle.",
    "La razza è poco diffusa e i dati sanitari documentati sono limitati; chiedi all'allevatore della salute dei genitori e fai controlli veterinari regolari.",
    "La raza es poco común y hay pocos datos de salud documentados; pregunta al criador por la salud de los padres y haz revisiones veterinarias periódicas.",
    "Rasa je retka, pa je zabeleženih zdravstvenih podataka malo; pitajte odgajivača o zdravlju roditelja i redovno vodite psa na veterinarske preglede.",
)

HEREDITARY = set(
    "hip elbow patella pra cataract glaucoma cea dcm mitral heart vwd deaf "
    "epilepsy dm mdr1 dermoid legg copper addison eyelid brachy ivdd dryeye "
    "kidney".split()
)
CARE = set("obesity dental ear allergy folds stones trachea thyroid sun cancer".split())

EXAM_INTRO = T(
    "Useful checks for this breed include {list}.",
    "Для этой породы полезны: {list}.",
    "Für diese Rasse sind sinnvoll: {list}.",
    "Per questa razza sono utili: {list}.",
    "Para esta raza son útiles: {list}.",
    "Za ovu rasu su korisni: {list}.",
)
EXAM_BREEDER = T(
    "Ask the breeder for the results of the parents' health tests before you decide on a puppy.",
    "Прежде чем выбрать щенка, попросите у заводчика результаты тестов здоровья родителей.",
    "Lassen Sie sich vom Züchter die Ergebnisse der Gesundheitstests der Elterntiere zeigen, bevor Sie sich für einen Welpen entscheiden.",
    "Prima di scegliere un cucciolo, chiedi all'allevatore i risultati dei test sanitari dei genitori.",
    "Antes de decidirte por un cachorro, pide al criador los resultados de las pruebas de salud de los padres.",
    "Pre nego što izaberete štene, tražite od odgajivača rezultate zdravstvenih testova roditelja.",
)
EXAM_ROUTINE = T(
    "In addition, an annual check-up, up-to-date vaccinations and regular parasite control keep an adult dog in good shape.",
    "Кроме того, ежегодный осмотр, актуальные прививки и регулярная обработка от паразитов помогают взрослой собаке оставаться в хорошей форме.",
    "Zusätzlich halten eine jährliche Untersuchung, aktuelle Impfungen und regelmäßige Parasitenvorsorge einen erwachsenen Hund fit.",
    "Inoltre una visita annuale, le vaccinazioni aggiornate e il controllo regolare dei parassiti mantengono in forma il cane adulto.",
    "Además, una revisión anual, las vacunas al día y el control regular de parásitos mantienen en forma al perro adulto.",
    "Pored toga, godišnji pregled, ažurne vakcine i redovna zaštita od parazita održavaju odraslog psa u dobroj formi.",
)

EXAM = {
    "hip": T(
        "hip X-rays with an official hip score",
        "рентген тазобедренных суставов с официальной оценкой",
        "Röntgen der Hüften mit offizieller Auswertung",
        "radiografie delle anche con valutazione ufficiale",
        "radiografías de cadera con valoración oficial",
        "rendgen kukova sa zvaničnom ocenom",
    ),
    "elbow": T(
        "elbow X-rays",
        "рентген локтевых суставов",
        "Röntgen der Ellbogen",
        "radiografie dei gomiti",
        "radiografías de codos",
        "rendgen laktova",
    ),
    "patella": T(
        "a vet's check of the kneecaps",
        "осмотр коленных чашечек у ветеринара",
        "eine tierärztliche Kontrolle der Kniescheiben",
        "un controllo veterinario delle rotule",
        "una revisión veterinaria de las rótulas",
        "veterinarski pregled kolenih čašica",
    ),
    "eye": T(
        "an eye exam by a veterinary ophthalmologist",
        "осмотр глаз у ветеринарного офтальмолога",
        "eine Augenuntersuchung beim tierärztlichen Augenspezialisten",
        "una visita oculistica veterinaria",
        "una revisión oftalmológica veterinaria",
        "pregled očiju kod veterinara oftalmologa",
    ),
    "heart": T(
        "a heart check, with an ultrasound when advised",
        "осмотр сердца, при необходимости с УЗИ",
        "eine Herzuntersuchung, bei Bedarf mit Ultraschall",
        "una visita cardiologica, con ecografia se consigliata",
        "una revisión cardíaca, con ecografía si se aconseja",
        "pregled srca, po potrebi sa ultrazvukom",
    ),
    "thyroid": T(
        "a thyroid blood test",
        "анализ крови на гормоны щитовидной железы",
        "ein Schilddrüsen-Bluttest",
        "un esame del sangue per la tiroide",
        "un análisis de sangre de la tiroides",
        "analiza krvi za štitnu žlezdu",
    ),
    "lab": T(
        "routine blood and urine tests",
        "плановые анализы крови и мочи",
        "regelmäßige Blut- und Urinuntersuchungen",
        "esami del sangue e delle urine di routine",
        "análisis de sangre y orina de rutina",
        "redovne analize krvi i mokraće",
    ),
    "hear": T(
        "a hearing test (BAER)",
        "тест слуха (BAER)",
        "ein Hörtest (BAER)",
        "un test dell'udito (BAER)",
        "una prueba de audición (BAER)",
        "test sluha (BAER)",
    ),
    "dna": T(
        "the DNA tests that are available for the breed",
        "доступные для породы ДНК-тесты",
        "die für die Rasse verfügbaren DNA-Tests",
        "i test del DNA disponibili per la razza",
        "las pruebas de ADN disponibles para la raza",
        "DNK testovi dostupni za rasu",
    ),
    "dermoid": T(
        "a check of the puppy's back for a dermoid sinus",
        "осмотр спины щенка на дермоидный синус",
        "eine Kontrolle des Welpenrückens auf einen Dermoidsinus",
        "un controllo della schiena del cucciolo per il seno dermoide",
        "una revisión del lomo del cachorro por si hay seno dermoide",
        "pregled leđa štenceta zbog dermoidnog sinusa",
    ),
    "neuro": T(
        "a neurological exam if there are signs of back pain, weakness or seizures",
        "неврологический осмотр при болях в спине, слабости или судорогах",
        "eine neurologische Untersuchung bei Rückenschmerzen, Schwäche oder Krampfanfällen",
        "una visita neurologica in caso di dolore alla schiena, debolezza o convulsioni",
        "una revisión neurológica si hay dolor de espalda, debilidad o convulsiones",
        "neurološki pregled kod bolova u leđima, slabosti ili napada",
    ),
    "dental": T(
        "regular dental checks",
        "регулярный осмотр зубов",
        "regelmäßige Zahnkontrollen",
        "controlli dentali regolari",
        "revisiones dentales regulares",
        "redovni pregledi zuba",
    ),
    "ear": T(
        "regular ear checks",
        "регулярный осмотр ушей",
        "regelmäßige Ohrenkontrollen",
        "controlli regolari delle orecchie",
        "revisiones regulares de los oídos",
        "redovni pregledi ušiju",
    ),
    "skin": T(
        "regular skin checks",
        "регулярный осмотр кожи",
        "regelmäßige Hautkontrollen",
        "controlli regolari della pelle",
        "revisiones regulares de la piel",
        "redovni pregledi kože",
    ),
    "airway": T(
        "an assessment of the nostrils and airways",
        "оценка носовых ходов и дыхательных путей",
        "eine Beurteilung von Nasenlöchern und Atemwegen",
        "una valutazione di narici e vie respiratorie",
        "una valoración de las fosas nasales y las vías respiratorias",
        "procena nozdrva i disajnih puteva",
    ),
    "weight": T(
        "regular weigh-ins and body condition checks",
        "регулярное взвешивание и оценка упитанности",
        "regelmäßiges Wiegen und Kontrolle des Ernährungszustands",
        "pesate regolari e valutazione della condizione fisica",
        "pesajes regulares y valoración de la condición corporal",
        "redovno merenje i procena telesne kondicije",
    ),
    "lump": T(
        "regular checks of the body for lumps",
        "регулярный осмотр тела на наличие уплотнений",
        "regelmäßiges Abtasten des Körpers auf Knoten",
        "controlli regolari del corpo alla ricerca di noduli",
        "revisiones regulares del cuerpo en busca de bultos",
        "redovno pregledanje tela zbog kvržica",
    ),
}

EXAM_OF = {
    "hip": "hip",
    "legg": "hip",
    "elbow": "elbow",
    "patella": "patella",
    "pra": "eye",
    "cataract": "eye",
    "glaucoma": "eye",
    "cea": "eye",
    "dryeye": "eye",
    "eyelid": "eye",
    "heart": "heart",
    "mitral": "heart",
    "dcm": "heart",
    "thyroid": "thyroid",
    "vwd": "lab",
    "copper": "lab",
    "kidney": "lab",
    "stones": "lab",
    "addison": "lab",
    "deaf": "hear",
    "dm": "dna",
    "mdr1": "dna",
    "dermoid": "dermoid",
    "ivdd": "neuro",
    "epilepsy": "neuro",
    "dental": "dental",
    "ear": "ear",
    "allergy": "skin",
    "folds": "skin",
    "sun": "skin",
    "brachy": "airway",
    "trachea": "airway",
    "obesity": "weight",
    "cancer": "lump",
}

# names that keep their capital letter inside a sentence in English
ENGLISH_PROPER = {"vwd", "addison", "legg", "cea"}


def inline_name(key, lang):
    name = CONDITIONS[key][LANGS.index(lang)]
    if lang == "de" or (lang == "en" and key in ENGLISH_PROPER):
        return name
    return name[0].lower() + name[1:]


def join(items, lang):
    if len(items) == 1:
        return items[0]
    word = {"en": "and", "ru": "и", "de": "und", "it": "e", "es": "y", "sr_latn": "i"}[
        lang
    ]
    if (
        lang == "es"
        and items[-1][:1].lower() == "i"
        or (
            lang == "es"
            and items[-1].lower().startswith("hi")
            and not items[-1].lower().startswith("hie")
        )
    ):
        word = "e"
    return ", ".join(items[:-1]) + f" {word} " + items[-1]


def sentences(parts):
    return " ".join(parts)


def build(dog, keys, lang):
    life = (dog.life_expectancy or "").strip()
    general = [BASE.get(dog.size, BASE["medium"])[lang]]
    if life:
        general.append(LIFE[lang].format(life=life))
    lengths = {c.name for c in dog.coat_length.all()}
    types = {c.name for c in dog.coat_type.all()}
    if "brachy" in keys:
        general.append(EXTRA["brachy"][lang])
    elif "Long" in lengths or "Double coat" in types:
        general.append(EXTRA["coat"][lang])
    elif dog.activity_level in ("high", "energetic"):
        general.append(EXTRA["active"][lang])
    elif dog.activity_level == "calm":
        general.append(EXTRA["calm"][lang])

    if keys:
        names = [inline_name(k, lang) for k in keys]
        risks = [RISK_INTRO[lang].format(list=join(names, lang))]
        extras = []
        if "bloat" in keys:
            extras.append("bloat")
        if "anesthesia" in keys:
            extras.append("anesthesia")
        if "heat" in keys or "brachy" in keys:
            extras.append("heat")
        if HEREDITARY & set(keys):
            extras.append("hereditary")
        if CARE & set(keys):
            extras.append("care")
        risks += [RISK_EXTRA[e][lang] for e in extras[:2]]
    else:
        risks = [RISK_RARE[lang]]

    exam_keys = []
    for k in keys:
        e = EXAM_OF.get(k)
        if e and e not in exam_keys:
            exam_keys.append(e)
    exams = []
    if exam_keys:
        exams.append(
            EXAM_INTRO[lang].format(list=join([EXAM[e][lang] for e in exam_keys], lang))
        )
    exams += [EXAM_BREEDER[lang], EXAM_ROUTINE[lang]]
    return sentences(general), sentences(risks), sentences(exams)


def fill(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for dog in Dogs.objects.all():
        keys = BREEDS.get(dog.slug, "").split()
        values = {}
        for lang in LANGS:
            # English lives in the plain column and in its own "_en" column
            suffixes = ("", "_en") if lang == "en" else (f"_{lang}",)
            general, risks, exams = build(dog, keys, lang)
            for name, text in (
                ("health_general", general),
                ("health_risks", risks),
                ("health_exams", exams),
            ):
                for suffix in suffixes:
                    field = name + suffix
                    if not getattr(dog, field, None):
                        values[field] = text
        # update() instead of save(): the "Last updated" date must not move
        if values:
            Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0046_dog_health_profile")]

    operations = [migrations.RunPython(fill, migrations.RunPython.noop)]
