"""Translated names of every dictionary the site shows: FCI groups, sections,
countries, coat types, coat lengths, temperaments.

Keyed by the English name (categories by their slug), then by language;
applied by `manage.py fill_content` (empty fields only)."""

VOCABULARY = {
 'categories': {
  'sheepdogs-cattledogs': {
   'en': {
    'name': 'Sheepdogs and Cattledogs (except Swiss Cattledogs)',
    'desc': 'Sheepdogs and Cattledogs are intelligent working breeds developed to manage livestock with precision and control. They are known for their strong instincts, responsiveness, and ability to work closely with humans. These dogs often show high levels of focus, making them excellent partners for both work and training. Many breeds in this group are energetic and require regular mental and physical stimulation. Their loyalty and attentiveness make them well-suited for active households. They tend to form deep bonds with their owners and thrive when given a clear role. While highly capable, they need guidance and engagement to stay balanced. Without enough activity, they may become restless or overly alert.',
   },
   'ru': {
    'name': 'Пастушьи и скотогонные собаки (кроме швейцарских скотогонных)',
    'desc': 'Овчарки и скотогонные собаки — умные рабочие породы, выведенные для управления домашним скотом с точностью и контролем. Они известны сильными инстинктами, отзывчивостью и способностью тесно работать с человеком. Эти собаки часто проявляют высокую сосредоточенность, что делает их отличными партнёрами и в работе, и в дрессировке. Многие породы этой группы энергичны и требуют регулярной умственной и физической стимуляции. Преданность и внимательность делают их подходящими для активных семей. Они склонны образовывать глубокие связи с владельцами и процветают, когда им дают чёткую роль. Будучи весьма способными, они нуждаются в руководстве и вовлечённости для сохранения баланса. Без достаточной активности они могут становиться беспокойными или чрезмерно настороженными.',
   },
   'de': {
    'name': 'Hüte- und Treibhunde (außer Schweizer Sennenhunde)',
    'desc': 'Schäfer- und Treibhunde sind intelligente Arbeitshunde, die gezüchtet wurden, um Vieh mit Präzision und Kontrolle zu hüten. Sie sind bekannt für ihre starken Instinkte, ihre Reaktionsfähigkeit und ihre Fähigkeit, eng mit Menschen zusammenzuarbeiten. Diese Hunde zeigen oft ein hohes Maß an Konzentration und sind hervorragende Partner für Arbeit und Training. Viele Rassen dieser Gruppe sind energiegeladen und brauchen regelmäßige geistige und körperliche Auslastung. Ihre Loyalität und Aufmerksamkeit machen sie ideal für aktive Haushalte. Sie gehen tiefe Bindungen mit ihren Besitzern ein und brauchen eine klare Aufgabe. Ohne genügend Aktivität werden sie unruhig oder übermäßig wachsam.',
   },
   'it': {
    'name': 'Cani da pastore e bovari (eccetto bovari svizzeri)',
    'desc': "I cani da pastore e bovari sono razze da lavoro intelligenti, sviluppate per gestire il bestiame con precisione e controllo. Sono noti per i forti istinti, la reattività e la capacità di lavorare a stretto contatto con l'uomo. Questi cani richiedono una guida coerente e buona attività.",
   },
   'es': {
    'name': 'Perros pastores y de ganado (excepto los suizos)',
    'desc': 'Los pastores y los perros de ganado son razas de trabajo inteligentes, desarrolladas para gestionar el ganado con precisión y control. Son conocidos por sus fuertes instintos, su receptividad y su capacidad para trabajar en estrecha colaboración con las personas. Estos perros suelen mostrar altos niveles de concentración, por lo que son excelentes compañeros tanto para el trabajo como para el adiestramiento. Muchas razas de este grupo son enérgicas y requieren estimulación mental y física regular. Su lealtad y su atención los hacen adecuados para hogares activos. Tienen tendencia a formar lazos profundos con sus dueños y prosperan cuando se les da un papel claro. Aunque muy capaces, necesitan orientación y participación para mantenerse equilibrados. Sin actividad suficiente, pueden volverse inquietos o demasiado vigilantes.',
   },
   'sr_latn': {
    'name': 'Ovčarski i stočarski psi (osim švajcarskih stočarskih pasa)',
    'desc': 'Ovčarski i stočarski psi su inteligentne radne rase razvijene za upravljanje stokom sa preciznošću i kontrolom. Poznati su po snažnim instinktima, oštroj reakciji i sposobnosti da rade u bliskoj saradnji sa čovekom. Ovim psima je potrebno dosledno vođenje i dovoljno aktivnosti.',
   },
  },
  'pinscher-schnauzer-molossoid': {
   'en': {
    'name': 'Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs',
    'desc': 'This group includes powerful and versatile breeds with strong guarding instincts and a confident presence. Many of these dogs were originally bred for protection, farm work, and companionship. They tend to be loyal, steady, and naturally alert to their surroundings. Some breeds are large and imposing, while others are more compact but equally self-assured. Early socialization and consistent training are important to shape their behavior. These dogs often form strong attachments to their families and can be very protective. They usually require experienced handling and clear boundaries. With the right structure, they are calm, reliable, and deeply devoted companions.',
   },
   'ru': {
    'name': 'Пинчеры и шнауцеры — молоссоиды, швейцарские горные и скотогонные собаки',
    'desc': 'Эта группа включает мощные и универсальные породы с сильными охранными инстинктами и уверенным присутствием. Многие из этих собак изначально выводились для охраны, фермерской работы и общения с человеком. Они, как правило, преданы, стабильны и природно внимательны к окружению. Одни породы крупные и внушительные, другие более компактные, но одинаково уверенные в себе. Ранняя социализация и последовательная дрессировка важны для формирования поведения. Эти собаки часто образуют крепкие привязанности к семьям и могут быть очень защитными. Обычно они требуют опытного обращения и чётких границ. При правильной структуре это спокойные, надёжные и глубоко преданные компаньоны.',
   },
   'de': {
    'name': 'Pinscher und Schnauzer – Molosser – Schweizer Sennenhunde und Treibhunde',
    'desc': 'Zu dieser Gruppe gehören kräftige und vielseitige Rassen mit ausgeprägtem Schutzinstinkt und selbstbewusster Präsenz. Viele dieser Hunde wurden ursprünglich für Schutz, Hofarbeit und Gesellschaft gezüchtet. Sie sind loyal, ausgeglichen und von Natur aus aufmerksam. Manche sind groß und imposant, andere kompakter, aber ebenso selbstsicher. Frühe Sozialisierung und konsequentes Training sind wichtig für ausgewogenes Verhalten. Diese Hunde binden sich stark an ihre Familie und können sehr schützend sein. Sie brauchen erfahrene Führung und klare Grenzen. Mit der richtigen Struktur sind sie ruhige, zuverlässige und hingebungsvolle Begleiter.',
   },
   'it': {
    'name': 'Pinscher e Schnauzer - Molossoidi e cani svizzeri da montagna e bovari',
    'desc': 'Questo gruppo comprende razze potenti e versatili con forti istinti di guardia e una presenza sicura. Molti di questi cani sono stati allevati originariamente per la protezione, il lavoro agricolo e la compagnia. Tendono a essere leali, stabili e devoti alla famiglia.',
   },
   'es': {
    'name': 'Pinscher y Schnauzer - Molosoide, montañés suizo y de ganado',
    'desc': 'Este grupo incluye razas potentes y versátiles con fuertes instintos de guardia y una presencia segura. Muchos de estos perros se criaron originalmente para la protección, el trabajo en la granja y la compañía. Tienen tendencia a ser leales, estables y naturalmente vigilantes con su entorno. Algunas razas son grandes e imponentes, otras son más compactas pero igual de seguras de sí mismas. La socialización temprana y el adiestramiento coherente son importantes para moldear su comportamiento. Estos perros suelen formar fuertes lazos con sus familias y pueden ser muy protectores. Normalmente requieren un manejo experimentado y límites claros. Con la estructura adecuada, son compañeros tranquilos, fiables y profundamente dedicados.',
   },
   'sr_latn': {
    'name': 'Pinčer i šnaucer — molosoidni, švajcarski planinski i stočarski psi',
    'desc': 'Ova grupa obuhvata moćne i svestrane rase sa snažnim zaštitničkim instinktima i samouverenim prisustvom. Mnogi od ovih pasa su prvobitno uzgajani za zaštitu, poljoprivredne poslove i društvo. Skloni su odanosti, stabilnosti i posvećenosti porodici.',
   },
  },
  'terriers': {
   'en': {
    'name': 'Terriers',
    'desc': 'Terriers are lively, determined, and full of personality. Originally bred to hunt and control vermin, they are known for their courage and persistence. These dogs are often energetic and curious, with a strong independent streak. Many terriers enjoy digging, exploring, and staying busy. Their bold nature makes them confident, sometimes even stubborn, companions. They benefit from consistent training and mental stimulation. Despite their small to medium size, they often have big attitudes. With the right balance, they are playful, loyal, and endlessly entertaining.',
   },
   'ru': {
    'name': 'Терьеры',
    'desc': 'Терьеры — живые, решительные и полные характера собаки. Выведенные изначально для охоты и борьбы с грызунами, они известны отвагой и настойчивостью. Эти собаки часто энергичны и любопытны, с сильной независимой жилкой. Многие терьеры любят копать, исследовать и оставаться занятыми. Смелая натура делает их уверенными, иногда даже упрямыми компаньонами. Им полезны последовательная дрессировка и умственная стимуляция. Несмотря на малый или средний размер, у них часто большие амбиции. При правильном балансе это игривые, преданные и бесконечно увлекательные собаки.',
   },
   'de': {
    'name': 'Terrier',
    'desc': 'Terrier sind lebhaft, entschlossen und voller Persönlichkeit. Ursprünglich zur Jagd auf Schädlinge gezüchtet, sind sie für ihren Mut und ihre Beharrlichkeit bekannt. Diese Hunde sind oft energiegeladen und neugierig, mit einem starken Hang zur Unabhängigkeit. Viele Terrier graben gern, erkunden und sind ständig beschäftigt. Ihre wagemutige Art macht sie zu selbstbewussten, manchmal auch sturen Begleitern. Sie profitieren von konsequentem Training und geistiger Auslastung. Trotz ihrer kleinen bis mittleren Größe haben sie oft ein großes Auftreten. Mit der richtigen Balance sind sie verspielt, loyal und unendlich unterhaltsam.',
   },
   'it': {
    'name': 'Terrier',
    'desc': 'I Terrier sono vivaci, determinati e pieni di personalità. Allevati originariamente per cacciare e tenere sotto controllo i parassiti, sono noti per il coraggio e la tenacia. Questi cani sono spesso energici e curiosi, con una forte indipendenza e grande spirito.',
   },
   'es': {
    'name': 'Terriers',
    'desc': 'Los terriers son vivaces, decididos y llenos de personalidad. Criados originalmente para cazar y controlar plagas, son conocidos por su coraje y su persistencia. Estos perros suelen ser enérgicos y curiosos, con un fuerte matiz de independencia. A muchos terriers les gusta cavar, explorar y mantenerse ocupados. Su naturaleza audaz los hace compañeros seguros de sí mismos, incluso testarudos. Se benefician del adiestramiento coherente y de la estimulación mental. A pesar de su tamaño pequeño o mediano, a menudo tienen un carácter grande. Con el equilibrio adecuado, son juguetones, leales y entretenidos sin fin.',
   },
   'sr_latn': {
    'name': 'Terijeri',
    'desc': 'Terijeri su živahni, odlučni i puni ličnosti. Prvobitno uzgajani za lov i suzbijanje štetočina, poznati su po hrabrosti i istrajnosti. Ovi psi su često energični i radoznali, sa snažnom nezavisnošću i velikim duhom.',
   },
  },
  'dachshunds': {
   'en': {
    'name': 'Dachshunds',
    'desc': 'Dachshunds are a distinct group known for their long bodies and strong hunting heritage. Originally bred to track and flush out burrowing animals, they are brave and determined. Despite their size, they often show surprising confidence and independence. They can be playful and affectionate, forming close bonds with their owners. Dachshunds tend to be curious and enjoy exploring their environment. Training may require patience due to their stubborn streak. They adapt well to different living situations, including apartments. With proper care, they are charming and loyal companions. It is the only group in the FCI system that contains a single breed. The Dachshund hunts both above and below ground: short legs, a long body and a narrow chest let it follow a badger or a fox into the burrow, and that build fits neither the scenthounds nor the terriers. Its three coat types and three sizes stay together here instead of being spread across several groups.',
   },
   'ru': {
    'name': 'Таксы',
    'desc': 'Таксы — самобытная группа, известная удлинённым телом и сильным охотничьим наследием. Выведенные изначально для выслеживания и выгона норных животных, они отважны и целеустремлённы. Несмотря на размер, таксы часто проявляют удивительную уверенность и независимость. Они могут быть игривыми и ласковыми, образуя тесные связи с владельцами. Таксы любопытны и любят исследовать окружение. Дрессировка может требовать терпения из-за упрямства. Они хорошо адаптируются к разным условиям жизни, включая квартиры. При правильном уходе это обаятельные и преданные компаньоны. Это единственная группа в системе FCI, где всего одна порода. Такса охотится и над землёй, и под землёй: короткие лапы, длинное тело и узкая грудь позволяют ей идти за барсуком или лисой прямо в нору, и такое сложение не подходит ни гончим, ни терьерам. Три типа шерсти и три размера остаются в одной группе, а не разбросаны по нескольким.',
   },
   'de': {
    'name': 'Dackel',
    'desc': 'Dackel sind eine eigenständige Gruppe, bekannt für ihre langen Körper und ihr starkes Jagderbe. Ursprünglich gezüchtet, um Bodentiere aufzuspüren und zu treiben, sind sie mutig und entschlossen. Trotz ihrer Größe zeigen sie oft überraschendes Selbstvertrauen und Unabhängigkeit. Sie können verspielt und anhänglich sein und enge Bindungen zu ihren Besitzern aufbauen. Dackel sind neugierig und erkunden gern ihre Umgebung. Beim Training braucht man Geduld wegen ihrer Sturheit. Sie passen sich verschiedenen Lebenssituationen an, auch Wohnungen. Mit der richtigen Pflege sind sie charmante und treue Begleiter. Sie ist die einzige Gruppe im FCI-System mit nur einer Rasse. Der Dackel jagt über und unter der Erde: kurze Läufe, ein langer Körper und eine schmale Brust lassen ihn dem Dachs oder Fuchs in den Bau folgen, und dieser Körperbau passt weder zu den Laufhunden noch zu den Terriern. Seine drei Fellarten und drei Größen bleiben hier zusammen, statt auf mehrere Gruppen verteilt zu werden.',
   },
   'it': {
    'name': 'Bassotti',
    'desc': "I Bassotti sono un gruppo distinto, noto per il corpo allungato e la forte tradizione da caccia. Allevati originariamente per tracciare e stanare gli animali scavatori, sono coraggiosi e determinati. Nonostante la taglia, mostrano spesso una sorprendente fiducia in sé. È l'unico gruppo del sistema FCI con una sola razza. Il bassotto caccia sopra e sotto terra: zampe corte, corpo lungo e torace stretto gli permettono di seguire un tasso o una volpe nella tana, e questa struttura non si adatta né ai segugi né ai terrier. I suoi tre tipi di pelo e le tre taglie restano qui, invece di essere distribuiti su più gruppi.",
   },
   'es': {
    'name': 'Teckels',
    'desc': 'Los teckels son un grupo distintivo conocido por sus cuerpos largos y su fuerte herencia cinegética. Criados originalmente para rastrear y sacar de sus madrigueras a los animales excavadores, son valientes y decididos. A pesar de su tamaño, a menudo muestran una confianza y una independencia sorprendentes. Pueden ser juguetones y afectuosos, formando lazos estrechos con sus dueños. Los teckels suelen ser curiosos y disfrutan explorando su entorno. El adiestramiento puede requerir paciencia por su testarudez. Se adaptan bien a diferentes situaciones de vida, incluidos los apartamentos. Con los cuidados adecuados, son compañeros encantadores y leales. Es el único grupo del sistema FCI con una sola raza. El teckel caza sobre y bajo tierra: patas cortas, cuerpo largo y pecho estrecho le permiten seguir a un tejón o a un zorro dentro de la madriguera, y esa constitución no encaja ni con los sabuesos ni con los terriers. Sus tres tipos de pelo y sus tres tamaños se quedan juntos aquí, en lugar de repartirse por varios grupos.',
   },
   'sr_latn': {
    'name': 'Jazavičari',
    'desc': 'Jazavičari su posebna grupa poznata po izduženom telu i snažnoj lovačkoj tradiciji. Prvobitno uzgajani za praćenje i izgon životinja iz jazbina, hrabri su i odlučni. Uprkos svojoj veličini, često pokazuju iznenađujuće samopouzdanje. To je jedina grupa u FCI sistemu sa samo jednom rasom. Jazavičar lovi i na zemlji i pod zemljom: kratke noge, dugačko telo i uska prsa omogućavaju mu da prati jazavca ili lisicu u jazbinu, a takva građa ne odgovara ni goničima ni terijerima. Njegova tri tipa dlake i tri veličine ostaju ovde zajedno, umesto da budu razbacane po više grupa.',
   },
  },
  'spitz-primitive': {
   'en': {
    'name': 'Spitz and primitive types',
    'desc': 'Spitz and primitive type dogs are among the oldest and most natural breed groups. They often have thick coats, pointed ears, and curled tails. Many of these breeds retain strong instincts and independent thinking. They are typically alert, resilient, and well-adapted to harsh climates. Some are highly social, while others are more reserved and self-reliant. These dogs often require understanding and respectful training approaches. Their behavior can feel more instinct-driven compared to other groups. With the right environment, they are loyal, fascinating, and deeply expressive companions.',
   },
   'ru': {
    'name': 'Шпицы и породы примитивного типа',
    'desc': 'Шпицы и породы примитивного типа — одни из самых древних и естественных групп пород. У них часто густая шерсть, остроконечные уши и закрученный хвост. Многие из этих пород сохраняют сильные инстинкты и независимое мышление. Они, как правило, внимательны, жизнестойки и хорошо приспособлены к суровому климату. Одни очень общительны, другие более сдержанны и самодостаточны. Эти собаки часто требуют понимающего и уважительного подхода к дрессировке. Их поведение может ощущаться более инстинктивным по сравнению с другими группами. При правильной среде это преданные, увлекательные и глубоко выразительные компаньоны.',
   },
   'de': {
    'name': 'Spitze und Urtyp-Rassen',
    'desc': 'Spitze und Hunde vom Urtyp gehören zu den ältesten und natürlichsten Rassegruppen. Sie haben oft dichtes Fell, aufgestellte Ohren und eine eingerollte Rute. Viele dieser Rassen haben starke Instinkte und denken unabhängig. Sie sind meist aufmerksam, widerstandsfähig und gut an raue Klimata angepasst. Manche sind sehr sozial, andere zurückhaltender und eigenständig. Diese Hunde brauchen verständnisvolle und respektvolle Trainingsmethoden. Ihr Verhalten wirkt im Vergleich zu anderen Gruppen instinktiv geprägt. Mit der richtigen Umgebung sind sie treue, faszinierende und ausdrucksstarke Begleiter.',
   },
   'it': {
    'name': 'Spitz e tipi primitivi',
    'desc': 'Gli Spitz e i cani di tipo primitivo sono tra i gruppi più antichi e naturali di razze. Hanno spesso mantelli folti, orecchie erette e coda arrotolata. Molte di queste razze conservano istinti forti e un pensiero indipendente. Sono energici, fedeli e richiedono una guida chiara e costante.',
   },
   'es': {
    'name': 'Spitz y tipos primitivos',
    'desc': 'Los perros de tipo spitz y primitivo se encuentran entre los grupos de razas más antiguos y naturales. Suelen tener pelajes gruesos, orejas puntiagudas y colas enrolladas. Muchas de estas razas conservan fuertes instintos y un pensamiento independiente. Normalmente son vigilantes, resilientes y bien adaptados a climas duros. Algunos son muy sociables, otros más reservados y autosuficientes. Estos perros a menudo requieren enfoques de adiestramiento comprensivos y respetuosos. Su comportamiento puede sentirse más impulsado por el instinto en comparación con otros grupos. Con el entorno adecuado, son compañeros leales, fascinantes y profundamente expresivos.',
   },
   'sr_latn': {
    'name': 'Špic i primitivni tipovi',
    'desc': 'Špic rase i psi primitivnog tipa spadaju među najstarije i najprirodnije grupe rasa. Često imaju gustu dlaku, uspravne uši i zavijen rep. Mnoge od ovih rasa zadržale su snažne instinkte i nezavisno razmišljanje. Energični su, odani i zahtevaju jasno i dosledno vođenje.',
   },
  },
  'scent-hounds': {
   'en': {
    'name': 'Scent hounds and related breeds',
    'desc': 'Scent hounds are driven by their powerful sense of smell and natural tracking ability. They were developed to follow trails over long distances with focus and endurance. These dogs are often patient, determined, and independent in their work. Many have a calm and friendly temperament at home. Their strong scent instincts can make recall and off-leash control more challenging. Regular exercise and enrichment are important to keep them satisfied. They usually get along well with people and other dogs. With proper guidance, they are gentle, loyal, and steady companions.',
   },
   'ru': {
    'name': 'Гончие и родственные породы',
    'desc': 'Гончие по запаху движимы мощным обонянием и природной способностью к выслеживанию. Они были выведены для следования по тропе на дальние расстояния с сосредоточенностью и выносливостью. Эти собаки часто терпеливы, целеустремлённы и независимы в работе. Многие имеют спокойный и дружелюбный темперамент дома. Сильные нюхательные инстинкты могут делать подзыв и контроль без поводка более сложными. Регулярные нагрузки и обогащение среды важны для их удовлетворённости. Обычно они хорошо ладят с людьми и другими собаками. При правильном руководстве это нежные, преданные и стабильные компаньоны.',
   },
   'de': {
    'name': 'Laufhunde und verwandte Rassen',
    'desc': 'Laufhunde werden von ihrem ausgeprägten Geruchssinn und ihrem natürlichen Spürvermögen angetrieben. Sie wurden gezüchtet, um Spuren über lange Strecken mit Fokus und Ausdauer zu verfolgen. Diese Hunde sind in ihrer Arbeit oft geduldig, entschlossen und unabhängig. Zu Hause haben viele ein ruhiges und freundliches Temperament. Ihr starker Geruchsinstinkt kann den Rückruf und die Freilaufführung erschweren. Regelmäßige Bewegung und Auslastung sind wichtig für ihre Zufriedenheit. Sie verstehen sich meist gut mit Menschen und anderen Hunden. Mit der richtigen Führung sind sie sanfte, treue und ausgeglichene Begleiter.',
   },
   'it': {
    'name': 'Segugi e razze affini',
    'desc': "I segugi da fiuto sono guidati dal potente senso dell'olfatto e dalla naturale capacità di seguire tracce. Sono stati sviluppati per seguire piste su lunghe distanze con concentrazione e resistenza. Questi cani sono spesso pazienti, determinati e indipendenti.",
   },
   'es': {
    'name': 'Sabuesos y razas relacionadas',
    'desc': 'Los sabuesos se mueven por su potente sentido del olfato y su capacidad natural de rastreo. Fueron desarrollados para seguir rastros a largas distancias con concentración y resistencia. Estos perros suelen ser pacientes, decididos e independientes en su trabajo. Muchos tienen un temperamento tranquilo y amigable en casa. Sus fuertes instintos olfativos pueden hacer que el regreso y el control sin correa sean más difíciles. El ejercicio regular y el enriquecimiento son importantes para mantenerlos satisfechos. Normalmente se llevan bien con las personas y con otros perros. Con la orientación adecuada, son compañeros amables, leales y estables.',
   },
   'sr_latn': {
    'name': 'Goniči po mirisu i srodne rase',
    'desc': 'Goniči po mirisu vode se snažnim čulom mirisa i prirodnom sposobnošću praćenja tragova. Razvijeni su da prate tragove na velikim udaljenostima sa koncentracijom i izdržljivošću. Ovi psi su često strpljivi, odlučni i nezavisni.',
   },
  },
  'pointing-dogs': {
   'en': {
    'name': 'Pointing Dogs',
    'desc': 'Pointing dogs are skilled hunting companions known for their precision and focus. They are trained to locate game and signal its presence with a characteristic stance. These breeds are typically energetic, responsive, and eager to work. They thrive on activity and close cooperation with their handler. Many pointing dogs are affectionate and balanced in the home environment. They require regular exercise and mental engagement to stay content. Training is usually effective due to their willingness to learn. With the right lifestyle, they are graceful, attentive, and loyal partners.',
   },
   'ru': {
    'name': 'Легавые',
    'desc': 'Легавые — умелые охотничьи компаньоны, известные точностью и сосредоточенностью. Их обучают находить дичь и сигнализировать о её присутствии характерной стойкой. Эти породы, как правило, энергичны, отзывчивы и стремятся работать. Они процветают от активности и тесного сотрудничества с проводником. Многие легавые ласковы и уравновешенны дома. Для довольства им нужны регулярные нагрузки и умственная вовлечённость. Дрессировка обычно эффективна благодаря желанию учиться. При правильном образе жизни это грациозные, внимательные и преданные партнёры.',
   },
   'de': {
    'name': 'Vorstehhunde',
    'desc': 'Vorstehhunde sind geschickte Jagdbegleiter, bekannt für ihre Präzision und Konzentration. Sie sind darauf trainiert, Wild zu finden und durch eine typische Haltung zu signalisieren. Diese Rassen sind meist energisch, aufmerksam und engagiert. Sie brauchen Aktivität und enge Zusammenarbeit mit ihrem Führer. Viele Vorstehhunde sind zu Hause anhänglich und ausgeglichen. Sie benötigen regelmäßige Bewegung und geistige Beschäftigung. Das Training gelingt meist leicht wegen ihrer Lernbereitschaft. Mit dem richtigen Lebensstil sind sie elegante, aufmerksame und treue Partner.',
   },
   'it': {
    'name': 'Cani da ferma',
    'desc': 'I cani da ferma sono abili compagni di caccia, noti per precisione e concentrazione. Sono addestrati a individuare la selvaggina e a segnalarne la presenza con una postura caratteristica. Queste razze sono in genere energiche, reattive e desiderose di lavorare.',
   },
   'es': {
    'name': 'Perros de muestra',
    'desc': 'Los perros de muestra son hábiles compañeros de caza conocidos por su precisión y su concentración. Se entrenan para localizar la caza y señalar su presencia con una postura característica. Estas razas suelen ser enérgicas, receptivas y con ganas de trabajar. Prosperan con la actividad y la estrecha cooperación con su guía. Muchos perros de muestra son afectuosos y equilibrados en el hogar. Requieren ejercicio regular y estimulación mental para estar contentos. El adiestramiento suele ser eficaz gracias a su disposición a aprender. Con el estilo de vida adecuado, son partners elegantes, atentos y leales.',
   },
   'sr_latn': {
    'name': 'Ptičari',
    'desc': 'Ptičari su vešti lovački pratioci, poznati po preciznosti i koncentraciji. Obučeni su da pronađu divljač i ukažu na njeno prisustvo karakterističnim stavom. Ove rase su obično energične, prisebne i željne rada.',
   },
  },
  'retrievers-flushing-water-dogs': {
   'en': {
    'name': 'Retrievers - Flushing Dogs - Water Dogs',
    'desc': 'This group includes friendly and versatile sporting dogs with a strong instinct to retrieve and assist. They are often known for their gentle mouths and cooperative nature. Many breeds here are highly social and enjoy working closely with people. They typically have balanced temperaments and adapt well to family life. Regular activity and engagement are important for their well-being. These dogs often excel in training and various dog sports. Their affectionate nature makes them especially popular companions. With enough stimulation, they are reliable, kind, and easy to live with.',
   },
   'ru': {
    'name': 'Ретриверы — спаниели — водяные собаки',
    'desc': 'Эта группа включает дружелюбных и универсальных спортивных собак с сильным инстинктом апортировки и помощи. Они часто известны мягкой хваткой и кооперативным нравом. Многие породы здесь очень общительны и любят тесную работу с людьми. У них, как правило, уравновешенный темперамент, и они хорошо адаптируются к семейной жизни. Регулярная активность и вовлечённость важны для благополучия. Эти собаки часто преуспевают в дрессировке и разных собачьих видах спорта. Ласковый нрав делает их особенно популярными компаньонами. При достаточной стимуляции они надёжны, добры и легки в совместной жизни.',
   },
   'de': {
    'name': 'Retriever – Stöberhunde – Wasserhunde',
    'desc': 'Zu dieser Gruppe gehören freundliche und vielseitige Sport- und Jagdhunde mit einem starken Apportier- und Helferinstinkt. Sie sind oft für ihr sanftes Maul und ihre kooperative Art bekannt. Viele Rassen hier sind sehr sozial und arbeiten gern eng mit Menschen. Sie haben meist ein ausgeglichenes Temperament und passen gut in Familien. Regelmäßige Aktivität und Beschäftigung sind wichtig für ihr Wohlbefinden. Diese Hunde eignen sich oft hervorragend für Training und Hundesport. Ihr liebevolles Wesen macht sie besonders beliebte Begleiter. Mit genügend Auslastung sind sie zuverlässig, freundlich und leicht zu halten.',
   },
   'it': {
    'name': 'Cani da riporto - Cani da cerca - Cani da acqua',
    'desc': "Questo gruppo comprende cani sportivi amichevoli e versatili con un forte istinto di riporto e assistenza. Sono spesso noti per la bocca morbida e la natura cooperativa. Molte razze qui sono molto socievoli e amano lavorare a stretto contatto con l'uomo.",
   },
   'es': {
    'name': 'Retrievers - Perros de agua',
    'desc': 'Este grupo incluye perros deportivos amigables y versátiles, con un fuerte instinto de traer y asistir. Son conocidos por su boca suave y su naturaleza cooperativa. Muchas razas de este grupo son muy sociosas y disfrutan trabajando en estrecha colaboración con las personas. Suelen tener temperamentos equilibrados y se adaptan bien a la vida familiar. La actividad y la participación regulares son importantes para su bienestar. Estos perros a menudo destacan en el adiestramiento y en varios deportes caninos. Su naturaleza afectuosa los convierte en compañeros especialmente populares. Con estimulación suficiente, son fiables, amables y fáciles de convivir.',
   },
   'sr_latn': {
    'name': 'Retriveri — španijeli i vodeni psi',
    'desc': 'Ova grupa obuhvata druželjubive i svestrane lovne pse sa snažnim instinktom donošenja i pomaganja. Često su poznati po mekom ustima i saradljivoj prirodi. Mnoge rase ovde su veoma društvene i vole rad u bliskoj saradnji sa čovekom.',
   },
  },
  'companion-toy-dogs': {
   'en': {
    'name': 'Companion and Toy Dogs',
    'desc': 'Companion and toy dogs are bred primarily for human company and emotional connection. They are often small in size but rich in personality and charm. Many breeds in this group are affectionate, social, and attentive to their owners. They typically adapt well to indoor living and smaller spaces. Despite their size, they still benefit from regular activity and interaction. Some may be more sensitive or expressive in behavior. They often form strong emotional bonds and enjoy being close to people. With proper care, they are devoted, lively, and comforting companions.',
   },
   'ru': {
    'name': 'Компаньоны и декоративные собаки',
    'desc': 'Компаньоны и декоративные собаки выведены прежде всего для общения с человеком и эмоциональной связи. Они часто малы по размеру, но богаты характером и обаянием. Многие породы этой группы ласковы, общительны и внимательны к владельцам. Они обычно хорошо адаптируются к жизни в помещении и небольшим пространствам. Несмотря на размер, им всё же полезна регулярная активность и взаимодействие. Некоторые могут быть более чувствительными или выразительными в поведении. Они часто образуют крепкие эмоциональные связи и любят находиться рядом с людьми. При правильном уходе это преданные, живые и успокаивающие компаньоны.',
   },
   'de': {
    'name': 'Begleit- und Toy-Hunde',
    'desc': 'Begleit- und Toy-Hunde sind in erster Linie für Gesellschaft und emotionale Nähe zum Menschen gezüchtet. Sie sind oft klein, aber reich an Persönlichkeit und Charme. Viele Rassen dieser Gruppe sind anhänglich, sozial und aufmerksam gegenüber ihren Besitzern. Sie passen sich meist gut an das Leben in Innenräumen und kleinere Wohnungen an. Trotz ihrer Größe profitieren sie von regelmäßiger Bewegung und Interaktion. Manche sind sensibler oder ausdrucksstärker im Verhalten. Sie gehen oft enge emotionale Bindungen ein und sind gern in der Nähe von Menschen. Mit der richtigen Pflege sind sie hingebungsvolle, lebhafte und tröstende Begleiter.',
   },
   'it': {
    'name': 'Cani da compagnia e da salotto',
    'desc': 'I cani da compagnia e da salotto sono allevati soprattutto per la compagnia umana e il legame emotivo. Sono spesso di piccola taglia ma ricchi di personalità e fascino. Molte razze di questo gruppo sono affettuose, socievoli e attente al proprietario.',
   },
   'es': {
    'name': 'Perros de compañía y juguete',
    'desc': 'Los perros de compañía y juguete se criaron principalmente para la compañía humana y la conexión emocional. Suelen ser pequeños de tamaño pero ricos en personalidad y encanto. Muchas razas de este grupo son afectuosas, socias y atentas con sus dueños. Normalmente se adaptan bien a la vida en interiores y a espacios pequeños. A pesar de su tamaño, se benefician de actividad e interacción regulares. Algunas pueden ser más sensibles o expresivas en su comportamiento. Suelen formar fuertes lazos emocionales y disfrutan estando cerca de las personas. Con los cuidados adecuados, son compañeros dedicados, vivaces y reconfortantes.',
   },
   'sr_latn': {
    'name': 'Psi za društvo i patuljasti psi',
    'desc': 'Psi za društvo i patuljasti psi uzgajani su pre svega radi ljudskog društva i emotivne povezanosti. Često su male veličine, ali bogati ličnošću i šarmom. Mnoge rase iz ove grupe su privržene, druželjubive i pažljive prema vlasniku.',
   },
  },
  'sighthounds': {
   'en': {
    'name': 'Sighthounds',
    'desc': 'Sighthounds are elegant and athletic dogs bred for speed and visual tracking. They rely on sight rather than scent to pursue moving targets. These breeds are often calm and gentle at home, despite their incredible speed outdoors. They tend to be independent but quietly affectionate. Many enjoy short bursts of intense activity followed by long periods of rest. Their build and temperament make them unique among dog groups. Training requires patience and understanding of their instincts. With the right balance, they are graceful, peaceful, and deeply loyal companions.',
   },
   'ru': {
    'name': 'Борзые',
    'desc': 'Борзые — элегантные и атлетичные собаки, выведенные для скорости и визуального выслеживания. Они полагаются на зрение, а не на запах, при преследовании движущихся целей. Эти породы часто спокойны и мягки дома, несмотря на невероятную скорость на улице. Они склонны быть независимыми, но тихо ласковыми. Многие любят короткие всплески интенсивной активности с последующим долгим отдыхом. Сложение и темперамент делают их уникальными среди собачьих групп. Дрессировка требует терпения и понимания их инстинктов. При правильном балансе это грациозные, мирные и глубоко преданные компаньоны.',
   },
   'de': {
    'name': 'Windhunde',
    'desc': 'Windhunde sind elegante und athletische Hunde, gezüchtet für Geschwindigkeit und Sichtjagd. Sie verlassen sich beim Verfolgen beweglicher Ziele auf den Blick statt auf den Geruch. Diese Rassen sind zu Hause oft ruhig und sanft — trotz ihrer unglaublichen Geschwindigkeit im Freien. Sie sind unabhängig, aber auf ihre Weise still anhänglich. Viele genießen kurze, intensive Aktivitätsphasen und danach lange Ruhezeiten. Ihr Körperbau und ihr Temperament machen sie einzigartig unter den Hundegruppen. Training erfordert Geduld und Verständnis für ihre Instinkte. Mit der richtigen Balance sind sie anmutige, friedliche und tief loyale Begleiter.',
   },
   'it': {
    'name': 'Levrieri',
    'desc': "I Levrieri sono cani eleganti e atletici, allevati per la velocità e il tracciamento visivo. Si affidano alla vista, più che all'olfatto, per inseguire bersagli in movimento. Queste razze sono spesso calme e gentili in casa, nonostante la loro incredibile velocità.",
   },
   'es': {
    'name': 'Galgos',
    'desc': 'Los galgos son perros elegantes y atléticos, criados para la velocidad y el rastreo visual. Confían en la vista más que en el olfato para perseguir objetivos en movimiento. Estas razas suelen ser tranquilas y amables en casa, a pesar de su increíble velocidad al aire libre. Tienen tendencia a ser independientes pero afectuosos de forma callada. A muchos les gustan los estallidos breves de actividad intensa seguidos de largos períodos de descanso. Su constitución y temperamento los hacen únicos entre los grupos de perros. El adiestramiento requiere paciencia y comprensión de sus instintos. Con el equilibrio adecuado, son compañeros elegantes, pacíficos y profundamente leales.',
   },
   'sr_latn': {
    'name': 'Hrtovi',
    'desc': 'Hrtovi su elegantni i atletski psi uzgajani za brzinu i vizuelno praćenje. Oslanjaju se na vid, više nego na miris, kada jure pokretne mete. Ove rase su često smirene i nežne kod kuće, uprkos neverovatnoj brzini.',
   },
  },
  'breeds-outside-fci-classification': {
   'en': {
    'name': 'Breeds outside FCI classification',
    'desc': 'This category includes dog breeds that are not recognized by the Fédération Cynologique Internationale (FCI), but are officially registered or widely accepted by other kennel clubs such as the AKC or UKC. These breeds often come from regions outside Europe and may have different or less standardized classification systems. Despite not being part of the FCI system, they are well-established, actively bred, and valued for their working abilities and companionship.',
   },
   'ru': {
    'name': 'Породы вне классификации FCI',
    'desc': 'Эта категория включает породы собак, не признанные Fédération Cynologique Internationale (FCI), но официально зарегистрированные или широко принятые другими кинологическими клубами, такими как AKC или UKC. Эти породы часто происходят из регионов за пределами Европы и могут иметь иные или менее стандартизированные системы классификации. Несмотря на то, что они не входят в систему FCI, они хорошо устоялись, активно разводятся и ценятся за рабочие качества и общение с человеком.',
   },
   'de': {
    'name': 'Rassen außerhalb der FCI-Klassifikation',
    'desc': 'Diese Kategorie umfasst Hunderassen, die nicht von der Fédération Cynologique Internationale (FCI) anerkannt sind, aber offiziell registriert oder von anderen Zuchtvereinen wie dem AKC oder UKC allgemein akzeptiert werden. Diese Rassen stammen oft aus Regionen außerhalb Europas und haben möglicherweise unterschiedliche oder weniger standardisierte Klassifikationssysteme. Obwohl sie nicht Teil des FCI-Systems sind, sind sie etabliert, werden aktiv gezüchtet und sind für ihre Arbeitsfähigkeit und Begleitung geschätzt.',
   },
   'it': {
    'name': 'Razze fuori dalla classificazione FCI',
    'desc': 'Questa categoria comprende razze canine non riconosciute dalla Fédération Cynologique Internationale (FCI), ma registrate ufficialmente o ampiamente accettate da altri club cinofili come AKC o UKC. Queste razze hanno spesso origini e storie uniche e sono apprezzate in tutto il mondo per le loro qualità specifiche.',
   },
   'es': {
    'name': 'Razas fuera de la clasificación FCI',
    'desc': 'Esta categoría incluye razas de perros que no están reconocidas por la Fédération Cynologique Internationale (FCI), pero que están oficialmente registradas o ampliamente aceptadas por otros clubes cinófilos como el AKC o el UKC. Estas razas suelen proceder de regiones fuera de Europa y pueden tener sistemas de clasificación diferentes o menos estandarizados. A pesar de no formar parte del sistema de la FCI, están bien establecidas, se crían activamente y se valoran por sus capacidades de trabajo y por su compañía.',
   },
   'sr_latn': {
    'name': 'Rase izvan FCI klasifikacije',
    'desc': 'Ova kategorija obuhvata rase pasa koje ne priznaje Fédération Cynologique Internationale (FCI), ali su zvanično registrovane ili široko prihvaćene od strane drugih kinoloških saveza poput AKC ili UKC. Ove rase često imaju jedinstveno poreklo i istoriju i cenjene su širom sveta zbog svojih specifičnih kvaliteta.',
   },
  },
 },
 'sections': {
  'sheepdogs-cattledogs': {
   'Cattledogs (except Swiss Cattledogs)': {
    'en': {
     'name': 'Cattledogs (except Swiss Cattledogs)',
    },
    'ru': {
     'name': 'Скотогонные собаки (кроме швейцарских скотогонных)',
    },
    'de': {
     'name': 'Treibhunde (außer Schweizer Sennenhunde)',
    },
    'it': {
     'name': 'Cani bovari (eccetto bovari svizzeri)',
    },
    'es': {
     'name': 'Perros de ganado (excepto los suizos)',
    },
    'sr_latn': {
     'name': 'Stočarski psi (osim švajcarskih stočarskih pasa)',
    },
   },
   'Sheepdogs': {
    'en': {
     'name': 'Sheepdogs',
    },
    'ru': {
     'name': 'Овчарки',
    },
    'de': {
     'name': 'Hütehunde',
    },
    'it': {
     'name': 'Cani da pastore',
    },
    'es': {
     'name': 'Perros pastores',
    },
    'sr_latn': {
     'name': 'Ovčarski psi',
    },
   },
  },
  'pinscher-schnauzer-molossoid': {
   'Molossian type': {
    'en': {
     'name': 'Molossian type',
    },
    'ru': {
     'name': 'Молоссы',
    },
    'de': {
     'name': 'Molosser',
    },
    'it': {
     'name': 'Tipo molossoide',
    },
    'es': {
     'name': 'Tipo molosoide',
    },
    'sr_latn': {
     'name': 'Molosoidni tip',
    },
   },
   'Pinscher and Schnauzer type': {
    'en': {
     'name': 'Pinscher and Schnauzer type',
    },
    'ru': {
     'name': 'Пинчеры и шнауцеры',
    },
    'de': {
     'name': 'Pinscher und Schnauzer',
    },
    'it': {
     'name': 'Tipo Pinscher e Schnauzer',
    },
    'es': {
     'name': 'Tipo Pinscher y Schnauzer',
    },
    'sr_latn': {
     'name': 'Pinčeri i šnauceri',
    },
   },
   'Swiss Mountain and Cattledogs': {
    'en': {
     'name': 'Swiss Mountain and Cattledogs',
    },
    'ru': {
     'name': 'Швейцарские горные и скотогонные собаки',
    },
    'de': {
     'name': 'Schweizer Sennenhunde und Treibhunde',
    },
    'it': {
     'name': 'Cani svizzeri da montagna e bovari',
    },
    'es': {
     'name': 'Montañeses suizos y perros de ganado',
    },
    'sr_latn': {
     'name': 'Švajcarski planinski i stočarski psi',
    },
   },
  },
  'terriers': {
   'Bull type Terriers': {
    'en': {
     'name': 'Bull type Terriers',
    },
    'ru': {
     'name': 'Терьеры буль-типа',
    },
    'de': {
     'name': 'Bull-Terrier',
    },
    'it': {
     'name': 'Terrier di tipo Bull',
    },
    'es': {
     'name': 'Terriers tipo bull',
    },
    'sr_latn': {
     'name': 'Terijeri bul tipa',
    },
   },
   'Large and medium sized Terriers': {
    'en': {
     'name': 'Large and medium sized Terriers',
    },
    'ru': {
     'name': 'Крупные и средние терьеры',
    },
    'de': {
     'name': 'Große und mittelgroße Terrier',
    },
    'it': {
     'name': 'Terrier di taglia grande e media',
    },
    'es': {
     'name': 'Terriers grandes y medianos',
    },
    'sr_latn': {
     'name': 'Veliki i srednji terijeri',
    },
   },
   'Small sized Terriers': {
    'en': {
     'name': 'Small sized Terriers',
    },
    'ru': {
     'name': 'Мелкие терьеры',
    },
    'de': {
     'name': 'Kleine Terrier',
    },
    'it': {
     'name': 'Terrier di piccola taglia',
    },
    'es': {
     'name': 'Terriers de tamaño pequeño',
    },
    'sr_latn': {
     'name': 'Mali terijeri',
    },
   },
   'Toy Terriers': {
    'en': {
     'name': 'Toy Terriers',
    },
    'ru': {
     'name': 'Той-терьеры',
    },
    'de': {
     'name': 'Toy-Terrier',
    },
    'it': {
     'name': 'Terrier toy',
    },
    'es': {
     'name': 'Terriers de juguete',
    },
    'sr_latn': {
     'name': 'Patuljasti terijeri',
    },
   },
  },
  'dachshunds': {
   'Single breed group (no sections)': {
    'en': {
     'name': 'Single breed group (no sections)',
    },
    'ru': {
     'name': 'Группа из одной породы (без разделов)',
    },
    'de': {
     'name': 'Einzelrassengruppe (ohne Sektionen)',
    },
    'it': {
     'name': 'Gruppo di singola razza (senza sezioni)',
    },
    'es': {
     'name': 'Grupo de una sola raza (sin secciones)',
    },
    'sr_latn': {
     'name': 'Grupa sa jednom rasom (bez sekcija)',
    },
   },
  },
  'spitz-primitive': {
   'Asian Spitz and related breeds': {
    'en': {
     'name': 'Asian Spitz and related breeds',
    },
    'ru': {
     'name': 'Азиатские шпицы и родственные породы',
    },
    'de': {
     'name': 'Asiatische Spitze und verwandte Rassen',
    },
    'it': {
     'name': 'Spitz asiatici e razze affini',
    },
    'es': {
     'name': 'Spitz asiáticos y razas relacionadas',
    },
    'sr_latn': {
     'name': 'Azijski špic i srodne rase',
    },
   },
   'European Spitz': {
    'en': {
     'name': 'European Spitz',
    },
    'ru': {
     'name': 'Европейские шпицы',
    },
    'de': {
     'name': 'Europäische Spitze',
    },
    'it': {
     'name': 'Spitz europei',
    },
    'es': {
     'name': 'Spitz europeos',
    },
    'sr_latn': {
     'name': 'Evropski špic',
    },
   },
   'Nordic Hunting Dogs': {
    'en': {
     'name': 'Nordic Hunting Dogs',
    },
    'ru': {
     'name': 'Северные охотничьи собаки',
    },
    'de': {
     'name': 'Nordische Jagdhunde',
    },
    'it': {
     'name': 'Cani nordici da caccia',
    },
    'es': {
     'name': 'Perros de caza nórdicos',
    },
    'sr_latn': {
     'name': 'Nordijski lovački psi',
    },
   },
   'Nordic Sledge Dogs': {
    'en': {
     'name': 'Nordic Sledge Dogs',
    },
    'ru': {
     'name': 'Северные ездовые собаки',
    },
    'de': {
     'name': 'Nordische Schlittenhunde',
    },
    'it': {
     'name': 'Cani nordici da slitta',
    },
    'es': {
     'name': 'Perros de trineo nórdicos',
    },
    'sr_latn': {
     'name': 'Nordijski psi za saonice',
    },
   },
   'Nordic Watchdogs and Herders': {
    'en': {
     'name': 'Nordic Watchdogs and Herders',
    },
    'ru': {
     'name': 'Северные сторожевые и пастушьи собаки',
    },
    'de': {
     'name': 'Nordische Wach- und Hütehunde',
    },
    'it': {
     'name': 'Cani nordici da guardia e da pastore',
    },
    'es': {
     'name': 'Perros de guardia y pastores nórdicos',
    },
    'sr_latn': {
     'name': 'Nordijski psi čuvari i pastiri',
    },
   },
   'Primitive type': {
    'en': {
     'name': 'Primitive type',
    },
    'ru': {
     'name': 'Примитивный тип',
    },
    'de': {
     'name': 'Urtyp-Rassen',
    },
    'it': {
     'name': 'Tipo primitivo',
    },
    'es': {
     'name': 'Tipo primitivo',
    },
    'sr_latn': {
     'name': 'Primitivni tip',
    },
   },
   'Primitive type - Hunting Dogs': {
    'en': {
     'name': 'Primitive type - Hunting Dogs',
    },
    'ru': {
     'name': 'Примитивный тип — охотничьи собаки',
    },
    'de': {
     'name': 'Urtyp – Jagdhunde',
    },
    'it': {
     'name': 'Tipo primitivo - cani da caccia',
    },
    'es': {
     'name': 'Tipo primitivo - Perros de caza',
    },
    'sr_latn': {
     'name': 'Primitivni tip — lovački psi',
    },
   },
  },
  'scent-hounds': {
   'Leash (scent) Hounds': {
    'en': {
     'name': 'Leash (scent) Hounds',
    },
    'ru': {
     'name': 'Гончие по следу',
    },
    'de': {
     'name': 'Schweißhunde',
    },
    'it': {
     'name': 'Segugi da traccia (da fiuto)',
    },
    'es': {
     'name': 'Sabuesos en correa (por olfato)',
    },
    'sr_latn': {
     'name': 'Goniči na povocu (po mirisu)',
    },
   },
   'Related breeds': {
    'en': {
     'name': 'Related breeds',
    },
    'ru': {
     'name': 'Родственные породы',
    },
    'de': {
     'name': 'Verwandte Rassen',
    },
    'it': {
     'name': 'Razze affini',
    },
    'es': {
     'name': 'Razas relacionadas',
    },
    'sr_latn': {
     'name': 'Srodne rase',
    },
   },
   'Scent hounds': {
    'en': {
     'name': 'Scent hounds',
    },
    'ru': {
     'name': 'Гончие',
    },
    'de': {
     'name': 'Laufhunde',
    },
    'it': {
     'name': 'Segugi da fiuto',
    },
    'es': {
     'name': 'Sabuesos por olfato',
    },
    'sr_latn': {
     'name': 'Goniči po mirisu',
    },
   },
  },
  'pointing-dogs': {
   'British and Irish Pointers and Setters': {
    'en': {
     'name': 'British and Irish Pointers and Setters',
    },
    'ru': {
     'name': 'Британские и ирландские пойнтеры и сеттеры',
    },
    'de': {
     'name': 'Britische und irische Pointer und Setter',
    },
    'it': {
     'name': 'Cani da ferma britannici e irlandesi',
    },
    'es': {
     'name': 'Perros de muestra y setter británicos e irlandeses',
    },
    'sr_latn': {
     'name': 'Britanski i irski ptičari i seteri',
    },
   },
   'Continental Pointing Dogs': {
    'en': {
     'name': 'Continental Pointing Dogs',
    },
    'ru': {
     'name': 'Континентальные легавые',
    },
    'de': {
     'name': 'Kontinentale Vorstehhunde',
    },
    'it': {
     'name': 'Cani da ferma continentali',
    },
    'es': {
     'name': 'Perros de muestra continentales',
    },
    'sr_latn': {
     'name': 'Kontinentalni ptičari',
    },
   },
  },
  'retrievers-flushing-water-dogs': {
   'Flushing Dogs': {
    'en': {
     'name': 'Flushing Dogs',
    },
    'ru': {
     'name': 'Спаниели',
    },
    'de': {
     'name': 'Stöberhunde',
    },
    'it': {
     'name': 'Cani da cerca',
    },
    'es': {
     'name': 'Perros de levantamiento',
    },
    'sr_latn': {
     'name': 'Španijeli',
    },
   },
   'Retrievers': {
    'en': {
     'name': 'Retrievers',
    },
    'ru': {
     'name': 'Ретриверы',
    },
    'de': {
     'name': 'Retriever',
    },
    'it': {
     'name': 'Cani da riporto',
    },
    'es': {
     'name': 'Retrievers',
    },
    'sr_latn': {
     'name': 'Retriveri',
    },
   },
   'Water Dogs': {
    'en': {
     'name': 'Water Dogs',
    },
    'ru': {
     'name': 'Водяные собаки',
    },
    'de': {
     'name': 'Wasserhunde',
    },
    'it': {
     'name': 'Cani da acqua',
    },
    'es': {
     'name': 'Perros de agua',
    },
    'sr_latn': {
     'name': 'Vodeni psi',
    },
   },
  },
  'companion-toy-dogs': {
   'Bichons and related breeds': {
    'en': {
     'name': 'Bichons and related breeds',
    },
    'ru': {
     'name': 'Бишоны и родственные породы',
    },
    'de': {
     'name': 'Bichons und verwandte Rassen',
    },
    'it': {
     'name': 'Bichon e razze affini',
    },
    'es': {
     'name': 'Bichones y razas relacionadas',
    },
    'sr_latn': {
     'name': 'Bišoni i srodne rase',
    },
   },
   'Chihuahueno': {
    'en': {
     'name': 'Chihuahueno',
    },
    'ru': {
     'name': 'Чихуахуэно',
    },
    'de': {
     'name': 'Chihuahueño',
    },
    'it': {
     'name': 'Chihuahueño',
    },
    'es': {
     'name': 'Chihuahueño',
    },
    'sr_latn': {
     'name': 'Čivava',
    },
   },
   'Continental Toy Spaniel and others': {
    'en': {
     'name': 'Continental Toy Spaniel and others',
    },
    'ru': {
     'name': 'Континентальные декоративные спаниели и другие',
    },
    'de': {
     'name': 'Kontinentale Toy Spaniel und andere',
    },
    'it': {
     'name': 'Epagneul nani continentali e altri',
    },
    'es': {
     'name': 'Spaniel continental de juguete y otros',
    },
    'sr_latn': {
     'name': 'Kontinentalni patuljasti španijeli i ostali',
    },
   },
   'English Toy Spaniels': {
    'en': {
     'name': 'English Toy Spaniels',
    },
    'ru': {
     'name': 'Английские декоративные спаниели',
    },
    'de': {
     'name': 'Englische Toy Spaniel',
    },
    'it': {
     'name': 'Epagneul nani inglesi',
    },
    'es': {
     'name': 'Spaniels ingleses de juguete',
    },
    'sr_latn': {
     'name': 'Engleski patuljasti španijeli',
    },
   },
   'Hairless Dogs': {
    'en': {
     'name': 'Hairless Dogs',
    },
    'ru': {
     'name': 'Голые собаки',
    },
    'de': {
     'name': 'Nackthunde',
    },
    'it': {
     'name': 'Cani nudi',
    },
    'es': {
     'name': 'Perros sin pelo',
    },
    'sr_latn': {
     'name': 'Psi bez dlake',
    },
   },
   'Japan Chin and Pekingese': {
    'en': {
     'name': 'Japan Chin and Pekingese',
    },
    'ru': {
     'name': 'Японский хин и пекинес',
    },
    'de': {
     'name': 'Japan Chin und Pekingese',
    },
    'it': {
     'name': 'Chin giapponesi e Pechinesi',
    },
    'es': {
     'name': 'Japan Chin y Pekineses',
    },
    'sr_latn': {
     'name': 'Japanski čin i pekinezer',
    },
   },
   'Kromfohrländer': {
    'en': {
     'name': 'Kromfohrländer',
    },
    'ru': {
     'name': 'Кромфорлендер',
    },
    'de': {
     'name': 'Kromfohrländer',
    },
    'it': {
     'name': 'Kromfohrländer',
    },
    'es': {
     'name': 'Kromfohrländer',
    },
    'sr_latn': {
     'name': 'Kromforlender',
    },
   },
   'Poodle': {
    'en': {
     'name': 'Poodle',
    },
    'ru': {
     'name': 'Пудель',
    },
    'de': {
     'name': 'Pudel',
    },
    'it': {
     'name': 'Barbone',
    },
    'es': {
     'name': 'Caniches',
    },
    'sr_latn': {
     'name': 'Pudla',
    },
   },
   'Small Belgian Dogs': {
    'en': {
     'name': 'Small Belgian Dogs',
    },
    'ru': {
     'name': 'Мелкие бельгийские собаки',
    },
    'de': {
     'name': 'Kleine belgische Hunde',
    },
    'it': {
     'name': 'Piccoli cani belgi',
    },
    'es': {
     'name': 'Perros belgas pequeños',
    },
    'sr_latn': {
     'name': 'Mali belgijski psi',
    },
   },
   'Small Molossian type Dogs': {
    'en': {
     'name': 'Small Molossian type Dogs',
    },
    'ru': {
     'name': 'Мелкие молоссы',
    },
    'de': {
     'name': 'Kleine Molosser',
    },
    'it': {
     'name': 'Cani di tipo molossoide di piccola taglia',
    },
    'es': {
     'name': 'Perros pequeños de tipo molosoide',
    },
    'sr_latn': {
     'name': 'Mali psi molosoidnog tipa',
    },
   },
   'Tibetan breeds': {
    'en': {
     'name': 'Tibetan breeds',
    },
    'ru': {
     'name': 'Тибетские породы',
    },
    'de': {
     'name': 'Tibetische Rassen',
    },
    'it': {
     'name': 'Razze tibetane',
    },
    'es': {
     'name': 'Razas tibetanas',
    },
    'sr_latn': {
     'name': 'Tibetanske rase',
    },
   },
  },
  'sighthounds': {
   'Long-haired or fringed Sighthounds': {
    'en': {
     'name': 'Long-haired or fringed Sighthounds',
    },
    'ru': {
     'name': 'Длинношёрстные борзые',
    },
    'de': {
     'name': 'Langhaarige oder befranste Windhunde',
    },
    'it': {
     'name': 'Levrieri a pelo lungo o frangiato',
    },
    'es': {
     'name': 'Galgos de pelo largo o con flequillo',
    },
    'sr_latn': {
     'name': 'Dugodlaki ili resasti hrtovi',
    },
   },
   'Rough-haired Sighthounds': {
    'en': {
     'name': 'Rough-haired Sighthounds',
    },
    'ru': {
     'name': 'Жесткошёрстные борзые',
    },
    'de': {
     'name': 'Rauhaarige Windhunde',
    },
    'it': {
     'name': 'Levrieri a pelo duro',
    },
    'es': {
     'name': 'Galgos de pelo áspero',
    },
    'sr_latn': {
     'name': 'Grubodlaki hrtovi',
    },
   },
   'Short-haired Sighthounds': {
    'en': {
     'name': 'Short-haired Sighthounds',
    },
    'ru': {
     'name': 'Короткошёрстные борзые',
    },
    'de': {
     'name': 'Kurzhaarige Windhunde',
    },
    'it': {
     'name': 'Levrieri a pelo corto',
    },
    'es': {
     'name': 'Galgos de pelo corto',
    },
    'sr_latn': {
     'name': 'Kratkodlaki hrtovi',
    },
   },
  },
  'breeds-outside-fci-classification': {
   'Recognized by Other Kennel Clubs': {
    'en': {
     'name': 'Recognized by Other Kennel Clubs',
    },
    'ru': {
     'name': 'Признаны другими кинологическими клубами',
    },
    'de': {
     'name': 'Von anderen Zuchtvereinen anerkannt',
    },
    'it': {
     'name': 'Riconosciute da altri club cinofili',
    },
    'es': {
     'name': 'Reconocidos por otros clubes cinófilos',
    },
    'sr_latn': {
     'name': 'Priznate od strane drugih kinoloških saveza',
    },
   },
   'Unrecognized but Documented Breeds': {
    'en': {
     'name': 'Unrecognized but Documented Breeds',
    },
    'ru': {
     'name': 'Непризнанные, но документально подтверждённые породы',
    },
    'de': {
     'name': 'Nicht anerkannt, aber dokumentiert',
    },
    'it': {
     'name': 'Razze non riconosciute ma documentate',
    },
    'es': {
     'name': 'Razas no reconocidas pero documentadas',
    },
    'sr_latn': {
     'name': 'Nepriznate, ali dokumentovane rase',
    },
   },
  },
 },
 'countries': {
  'Afghanistan': {
   'en': {
    'name': 'Afghanistan',
   },
   'ru': {
    'name': 'Афганистан',
   },
   'de': {
    'name': 'Afghanistan',
   },
   'it': {
    'name': 'Afghanistan',
   },
   'es': {
    'name': 'Afganistán',
   },
   'sr_latn': {
    'name': 'Avganistan',
   },
  },
  'Australia': {
   'en': {
    'name': 'Australia',
   },
  },
  'Belgium': {
   'en': {
    'name': 'Belgium',
   },
   'ru': {
    'name': 'Бельгия',
   },
   'de': {
    'name': 'Belgien',
   },
   'it': {
    'name': 'Belgio',
   },
   'es': {
    'name': 'Bélgica',
   },
   'sr_latn': {
    'name': 'Belgija',
   },
  },
  'Belgium, France': {
   'en': {
    'name': 'Belgium, France',
   },
   'ru': {
    'name': 'Бельгия, Франция',
   },
   'de': {
    'name': 'Belgien, Frankreich',
   },
   'it': {
    'name': 'Belgio, Francia',
   },
   'es': {
    'name': 'Bélgica, Francia',
   },
   'sr_latn': {
    'name': 'Belgija, Francuska',
   },
  },
  'Canada': {
   'en': {
    'name': 'Canada',
   },
   'ru': {
    'name': 'Канада',
   },
   'de': {
    'name': 'Kanada',
   },
   'it': {
    'name': 'Canada',
   },
   'es': {
    'name': 'Canadá',
   },
   'sr_latn': {
    'name': 'Kanada',
   },
  },
  'China': {
   'en': {
    'name': 'China',
   },
   'ru': {
    'name': 'Китай',
   },
   'de': {
    'name': 'China',
   },
   'it': {
    'name': 'Cina',
   },
   'es': {
    'name': 'China',
   },
   'sr_latn': {
    'name': 'Kina',
   },
  },
  'Croatia': {
   'en': {
    'name': 'Croatia',
   },
   'ru': {
    'name': 'Хорватия',
   },
   'de': {
    'name': 'Kroatien',
   },
   'it': {
    'name': 'Croazia',
   },
   'es': {
    'name': 'Croacia',
   },
   'sr_latn': {
    'name': 'Hrvatska',
   },
  },
  'Czechoslovakia': {
   'en': {
    'name': 'Czechoslovakia',
   },
   'ru': {
    'name': 'Чехословакия',
   },
   'de': {
    'name': 'Tschechoslowakei',
   },
   'it': {
    'name': 'Cecoslovacchia',
   },
   'es': {
    'name': 'Checoslovaquia',
   },
   'sr_latn': {
    'name': 'Čehoslovačka',
   },
  },
  'France': {
   'en': {
    'name': 'France',
   },
   'ru': {
    'name': 'Франция',
   },
   'de': {
    'name': 'Frankreich',
   },
   'it': {
    'name': 'Francia',
   },
   'es': {
    'name': 'Francia',
   },
   'sr_latn': {
    'name': 'Francuska',
   },
  },
  'Germany': {
   'en': {
    'name': 'Germany',
   },
   'ru': {
    'name': 'Германия',
   },
   'de': {
    'name': 'Deutschland',
   },
   'it': {
    'name': 'Germania',
   },
   'es': {
    'name': 'Alemania',
   },
   'sr_latn': {
    'name': 'Nemačka',
   },
  },
  'Great Britain': {
   'en': {
    'name': 'Great Britain',
   },
   'ru': {
    'name': 'Великобритания',
   },
   'de': {
    'name': 'Großbritannien',
   },
   'it': {
    'name': 'Gran Bretagna',
   },
   'es': {
    'name': 'Gran Bretaña',
   },
   'sr_latn': {
    'name': 'Velika Britanija',
   },
  },
  'Hungary': {
   'en': {
    'name': 'Hungary',
   },
   'ru': {
    'name': 'Венгрия',
   },
   'de': {
    'name': 'Ungarn',
   },
   'it': {
    'name': 'Ungheria',
   },
   'es': {
    'name': 'Hungría',
   },
   'sr_latn': {
    'name': 'Mađarska',
   },
  },
  'Ireland': {
   'en': {
    'name': 'Ireland',
   },
   'ru': {
    'name': 'Ирландия',
   },
   'de': {
    'name': 'Irland',
   },
   'it': {
    'name': 'Irlanda',
   },
   'es': {
    'name': 'Irlanda',
   },
   'sr_latn': {
    'name': 'Irska',
   },
  },
  'Italy': {
   'en': {
    'name': 'Italy',
   },
   'ru': {
    'name': 'Италия',
   },
   'de': {
    'name': 'Italien',
   },
   'it': {
    'name': 'Italia',
   },
   'es': {
    'name': 'Italia',
   },
   'sr_latn': {
    'name': 'Italija',
   },
  },
  'Japan': {
   'en': {
    'name': 'Japan',
   },
   'ru': {
    'name': 'Япония',
   },
   'de': {
    'name': 'Japan',
   },
   'it': {
    'name': 'Giappone',
   },
   'es': {
    'name': 'Japón',
   },
   'sr_latn': {
    'name': 'Japan',
   },
  },
  'Mali': {
   'en': {
    'name': 'Mali',
   },
   'ru': {
    'name': 'Мали',
   },
   'de': {
    'name': 'Mali',
   },
   'it': {
    'name': 'Mali',
   },
   'es': {
    'name': 'Malí',
   },
   'sr_latn': {
    'name': 'Mali',
   },
  },
  'Mexico': {
   'en': {
    'name': 'Mexico',
   },
   'ru': {
    'name': 'Мексика',
   },
   'de': {
    'name': 'Mexiko',
   },
   'it': {
    'name': 'Messico',
   },
   'es': {
    'name': 'México',
   },
   'sr_latn': {
    'name': 'Meksiko',
   },
  },
  'Middle East': {
   'en': {
    'name': 'Middle East',
   },
   'ru': {
    'name': 'Ближний Восток',
   },
   'de': {
    'name': 'Naher Osten',
   },
   'it': {
    'name': 'Medio Oriente',
   },
   'es': {
    'name': 'Oriente Medio',
   },
   'sr_latn': {
    'name': 'Bliski istok',
   },
  },
  'Morocco': {
   'en': {
    'name': 'Morocco',
   },
   'ru': {
    'name': 'Марокко',
   },
   'de': {
    'name': 'Marokko',
   },
   'it': {
    'name': 'Marocco',
   },
   'es': {
    'name': 'Marruecos',
   },
   'sr_latn': {
    'name': 'Maroko',
   },
  },
  'Northern Russia, Siberia': {
   'en': {
    'name': 'Northern Russia, Siberia',
   },
   'ru': {
    'name': 'Северная Россия, Сибирь',
   },
   'de': {
    'name': 'Nordrussland, Sibirien',
   },
   'it': {
    'name': 'Russia settentrionale, Siberia',
   },
   'es': {
    'name': 'Rusia septentrional, Siberia',
   },
   'sr_latn': {
    'name': 'Severna Rusija, Sibir',
   },
  },
  'Norway': {
   'en': {
    'name': 'Norway',
   },
   'ru': {
    'name': 'Норвегия',
   },
   'de': {
    'name': 'Norwegen',
   },
   'it': {
    'name': 'Norvegia',
   },
   'es': {
    'name': 'Noruega',
   },
   'sr_latn': {
    'name': 'Norveška',
   },
  },
  'Portugal': {
   'en': {
    'name': 'Portugal',
   },
   'ru': {
    'name': 'Португалия',
   },
   'de': {
    'name': 'Portugal',
   },
   'it': {
    'name': 'Portogallo',
   },
   'es': {
    'name': 'Portugal',
   },
   'sr_latn': {
    'name': 'Portugal',
   },
  },
  'Russian Federation': {
   'en': {
    'name': 'Russian Federation',
   },
   'ru': {
    'name': 'Российская Федерация',
   },
   'de': {
    'name': 'Russische Föderation',
   },
   'it': {
    'name': 'Federazione Russa',
   },
   'es': {
    'name': 'Federación Rusa',
   },
   'sr_latn': {
    'name': 'Ruska Federacija',
   },
  },
  'Slovakia': {
   'en': {
    'name': 'Slovakia',
   },
   'ru': {
    'name': 'Словакия',
   },
  },
  'South Africa': {
   'en': {
    'name': 'South Africa',
   },
   'ru': {
    'name': 'Южная Африка',
   },
   'de': {
    'name': 'Südafrika',
   },
   'it': {
    'name': 'Sudafrica',
   },
   'es': {
    'name': 'Sudáfrica',
   },
   'sr_latn': {
    'name': 'Južna Afrika',
   },
  },
  'Spain': {
   'en': {
    'name': 'Spain',
   },
   'ru': {
    'name': 'Испания',
   },
   'de': {
    'name': 'Spanien',
   },
   'it': {
    'name': 'Spagna',
   },
   'es': {
    'name': 'España',
   },
   'sr_latn': {
    'name': 'Španija',
   },
  },
  'Sweden': {
   'en': {
    'name': 'Sweden',
   },
   'ru': {
    'name': 'Швеция',
   },
   'de': {
    'name': 'Schweden',
   },
   'it': {
    'name': 'Svezia',
   },
   'es': {
    'name': 'Suecia',
   },
   'sr_latn': {
    'name': 'Švedska',
   },
  },
  'Switzerland': {
   'en': {
    'name': 'Switzerland',
   },
   'ru': {
    'name': 'Швейцария',
   },
   'de': {
    'name': 'Schweiz',
   },
   'it': {
    'name': 'Svizzera',
   },
   'es': {
    'name': 'Suiza',
   },
   'sr_latn': {
    'name': 'Švajcarska',
   },
  },
  'The Netherlands': {
   'en': {
    'name': 'The Netherlands',
   },
   'ru': {
    'name': 'Нидерланды',
   },
   'de': {
    'name': 'Niederlande',
   },
   'it': {
    'name': 'Paesi Bassi',
   },
   'es': {
    'name': 'Países Bajos',
   },
   'sr_latn': {
    'name': 'Holandija',
   },
  },
  'Tibet (China)': {
   'en': {
    'name': 'Tibet (China)',
   },
   'ru': {
    'name': 'Тибет (Китай)',
   },
   'de': {
    'name': 'Tibet (China)',
   },
   'it': {
    'name': 'Tibet (Cina)',
   },
   'es': {
    'name': 'Tíbet (China)',
   },
   'sr_latn': {
    'name': 'Tibet (Kina)',
   },
  },
  'Turkey': {
   'en': {
    'name': 'Turkey',
   },
   'ru': {
    'name': 'Турция',
   },
   'de': {
    'name': 'Türkei',
   },
   'it': {
    'name': 'Turchia',
   },
   'es': {
    'name': 'Turquía',
   },
   'sr_latn': {
    'name': 'Turska',
   },
  },
  'USA': {
   'en': {
    'name': 'USA',
   },
   'ru': {
    'name': 'США',
   },
   'de': {
    'name': 'USA',
   },
   'it': {
    'name': 'Stati Uniti',
   },
   'es': {
    'name': 'EE. UU.',
   },
   'sr_latn': {
    'name': 'SAD',
   },
  },
 },
 'coat_types': {
  'Corded': {
   'en': {
    'name': 'Corded',
   },
   'ru': {
    'name': 'Шнуровая',
   },
   'de': {
    'name': 'Geschnürt',
   },
   'it': {
    'name': 'Cordonato',
   },
   'es': {
    'name': 'En cordones',
   },
   'sr_latn': {
    'name': 'Užadasta',
   },
  },
  'Curly': {
   'en': {
    'name': 'Curly',
   },
   'ru': {
    'name': 'Курчавая',
   },
   'de': {
    'name': 'Lockig',
   },
   'it': {
    'name': 'Riccio',
   },
   'es': {
    'name': 'Rizada',
   },
   'sr_latn': {
    'name': 'Kudrava',
   },
  },
  'Double coat': {
   'en': {
    'name': 'Double coat',
   },
   'ru': {
    'name': 'Двойная шерсть',
   },
   'de': {
    'name': 'Doppeltes Fell',
   },
   'it': {
    'name': 'Doppio mantello',
   },
   'es': {
    'name': 'Doble',
   },
   'sr_latn': {
    'name': 'Dvostruka dlaka',
   },
  },
  'Hairless': {
   'en': {
    'name': 'Hairless',
   },
   'ru': {
    'name': 'Голая',
   },
   'de': {
    'name': 'Nackt',
   },
   'it': {
    'name': 'Nudo',
   },
   'es': {
    'name': 'Sin pelo',
   },
   'sr_latn': {
    'name': 'Bez dlake',
   },
  },
  'Rough': {
   'en': {
    'name': 'Rough',
   },
   'ru': {
    'name': 'Жёсткая',
   },
   'de': {
    'name': 'Rauhaarig',
   },
   'it': {
    'name': 'Ruvido',
   },
   'es': {
    'name': 'Áspera',
   },
   'sr_latn': {
    'name': 'Gruba',
   },
  },
  'Silky': {
   'en': {
    'name': 'Silky',
   },
   'ru': {
    'name': 'Шёлковая',
   },
   'de': {
    'name': 'Seidig',
   },
   'it': {
    'name': 'Setoso',
   },
   'es': {
    'name': 'Sedosa',
   },
   'sr_latn': {
    'name': 'Svilenkasta',
   },
  },
  'Smooth': {
   'en': {
    'name': 'Smooth',
   },
   'ru': {
    'name': 'Гладкая',
   },
   'de': {
    'name': 'Kurzhaar',
   },
   'it': {
    'name': 'Liscio',
   },
   'es': {
    'name': 'Lisa',
   },
   'sr_latn': {
    'name': 'Glatka',
   },
  },
  'Wavy': {
   'en': {
    'name': 'Wavy',
   },
   'ru': {
    'name': 'Волнистая',
   },
   'de': {
    'name': 'Gewellt',
   },
   'it': {
    'name': 'Mosso',
   },
   'es': {
    'name': 'Ondulada',
   },
   'sr_latn': {
    'name': 'Talasaasta',
   },
  },
  'Wiry': {
   'en': {
    'name': 'Wiry',
   },
   'ru': {
    'name': 'Проволокообразная',
   },
   'de': {
    'name': 'Drahtig',
   },
   'it': {
    'name': 'Duro (fil di ferro)',
   },
   'es': {
    'name': 'Estíbar',
   },
   'sr_latn': {
    'name': 'Žičana',
   },
  },
 },
 'coat_lengths': {
  'Long': {
   'en': {
    'name': 'Long',
   },
   'ru': {
    'name': 'Длинная',
   },
   'de': {
    'name': 'Lang',
   },
   'it': {
    'name': 'Lungo',
   },
   'es': {
    'name': 'Larga',
   },
   'sr_latn': {
    'name': 'Duga',
   },
  },
  'Medium': {
   'en': {
    'name': 'Medium',
   },
   'ru': {
    'name': 'Средняя',
   },
   'de': {
    'name': 'Mittel',
   },
   'it': {
    'name': 'Medio',
   },
   'es': {
    'name': 'Media',
   },
   'sr_latn': {
    'name': 'Srednja',
   },
  },
  'Short': {
   'en': {
    'name': 'Short',
   },
   'ru': {
    'name': 'Короткая',
   },
   'de': {
    'name': 'Kurz',
   },
   'it': {
    'name': 'Corto',
   },
   'es': {
    'name': 'Corta',
   },
   'sr_latn': {
    'name': 'Kratka',
   },
  },
 },
 'temperaments': {
  'Active': {
   'en': {
    'name': 'Active',
   },
   'ru': {
    'name': 'Активный',
   },
   'de': {
    'name': 'Aktiv',
   },
   'it': {
    'name': 'Attivo',
   },
   'es': {
    'name': 'Activo',
   },
   'sr_latn': {
    'name': 'Aktivan',
   },
  },
  'Affectionate': {
   'en': {
    'name': 'Affectionate',
   },
   'ru': {
    'name': 'Ласковый',
   },
   'de': {
    'name': 'Zärtlich',
   },
   'it': {
    'name': 'Affettuoso',
   },
   'es': {
    'name': 'Afectuoso',
   },
   'sr_latn': {
    'name': 'Privržen',
   },
  },
  'Alert': {
   'en': {
    'name': 'Alert',
   },
   'ru': {
    'name': 'Живой',
   },
   'de': {
    'name': 'Aufmerksam',
   },
   'it': {
    'name': 'Vigile',
   },
   'es': {
    'name': 'Alerta',
   },
   'sr_latn': {
    'name': 'Budan',
   },
  },
  'Brave': {
   'en': {
    'name': 'Brave',
   },
   'ru': {
    'name': 'Храбрый',
   },
   'de': {
    'name': 'Tapfer',
   },
   'it': {
    'name': 'Audace',
   },
   'es': {
    'name': 'Valiente',
   },
   'sr_latn': {
    'name': 'Hrabar',
   },
  },
  'Calm': {
   'en': {
    'name': 'Calm',
   },
   'ru': {
    'name': 'Спокойный',
   },
   'de': {
    'name': 'Gelassen',
   },
   'it': {
    'name': 'Calmo',
   },
   'es': {
    'name': 'Tranquilo',
   },
   'sr_latn': {
    'name': 'Smiren',
   },
  },
  'Confident': {
   'en': {
    'name': 'Confident',
   },
   'ru': {
    'name': 'Уверенный',
   },
   'de': {
    'name': 'Selbstbewusst',
   },
   'it': {
    'name': 'Sicuro di sé',
   },
   'es': {
    'name': 'Seguro de sí mismo',
   },
   'sr_latn': {
    'name': 'Samouveren',
   },
  },
  'Courageous': {
   'en': {
    'name': 'Courageous',
   },
   'ru': {
    'name': 'Отважный',
   },
   'de': {
    'name': 'Mutig',
   },
   'it': {
    'name': 'Coraggioso',
   },
   'es': {
    'name': 'Corajudo',
   },
   'sr_latn': {
    'name': 'Odvažan',
   },
  },
  'Dignified': {
   'en': {
    'name': 'Dignified',
   },
   'ru': {
    'name': 'Достойный',
   },
   'de': {
    'name': 'Würdevoll',
   },
   'it': {
    'name': 'Dignitoso',
   },
   'es': {
    'name': 'Digno',
   },
   'sr_latn': {
    'name': 'Dostojanstven',
   },
  },
  'Eager': {
   'en': {
    'name': 'Eager',
   },
   'ru': {
    'name': 'Послушный',
   },
   'de': {
    'name': 'Eifrig',
   },
   'it': {
    'name': 'Desideroso',
   },
   'es': {
    'name': 'Con ganas',
   },
   'sr_latn': {
    'name': 'Revnostan',
   },
  },
  'Energetic': {
   'en': {
    'name': 'Energetic',
   },
   'ru': {
    'name': 'Энергичный',
   },
   'de': {
    'name': 'Energiegeladen',
   },
   'it': {
    'name': 'Energico',
   },
   'es': {
    'name': 'Enérgico',
   },
   'sr_latn': {
    'name': 'Energičan',
   },
  },
  'Even-tempered': {
   'en': {
    'name': 'Even-tempered',
   },
   'ru': {
    'name': 'Уравновешенный',
   },
   'de': {
    'name': 'Ausgeglichen',
   },
   'it': {
    'name': 'Equilibrato',
   },
   'es': {
    'name': 'De temperamento equilibrado',
   },
   'sr_latn': {
    'name': 'Staložen',
   },
  },
  'Friendly': {
   'en': {
    'name': 'Friendly',
   },
   'ru': {
    'name': 'Дружелюбный',
   },
   'de': {
    'name': 'Freundlich',
   },
   'it': {
    'name': 'Amichevole',
   },
   'es': {
    'name': 'Amigable',
   },
   'sr_latn': {
    'name': 'Prijazan',
   },
  },
  'Gentle': {
   'en': {
    'name': 'Gentle',
   },
   'ru': {
    'name': 'Нежный',
   },
   'de': {
    'name': 'Sanft',
   },
   'it': {
    'name': 'Gentile',
   },
   'es': {
    'name': 'Amable',
   },
   'sr_latn': {
    'name': 'Nežan',
   },
  },
  'Independent': {
   'en': {
    'name': 'Independent',
   },
   'ru': {
    'name': 'Независимый',
   },
   'de': {
    'name': 'Unabhängig',
   },
   'it': {
    'name': 'Indipendente',
   },
   'es': {
    'name': 'Independiente',
   },
   'sr_latn': {
    'name': 'Nezavisan',
   },
  },
  'Intelligent': {
   'en': {
    'name': 'Intelligent',
   },
   'ru': {
    'name': 'Умный',
   },
   'de': {
    'name': 'Intelligent',
   },
   'it': {
    'name': 'Intelligente',
   },
   'es': {
    'name': 'Inteligente',
   },
   'sr_latn': {
    'name': 'Inteligentan',
   },
  },
  'Loyal': {
   'en': {
    'name': 'Loyal',
   },
   'ru': {
    'name': 'Верный',
   },
   'de': {
    'name': 'Loyal',
   },
   'it': {
    'name': 'Leale',
   },
   'es': {
    'name': 'Leal',
   },
   'sr_latn': {
    'name': 'Veran',
   },
  },
  'Playful': {
   'en': {
    'name': 'Playful',
   },
   'ru': {
    'name': 'Игривый',
   },
   'de': {
    'name': 'Verspielt',
   },
   'it': {
    'name': 'Giocoso',
   },
   'es': {
    'name': 'Juguetón',
   },
   'sr_latn': {
    'name': 'Razigran',
   },
  },
  'Protective': {
   'en': {
    'name': 'Protective',
   },
   'ru': {
    'name': 'Защитный',
   },
   'de': {
    'name': 'Schützend',
   },
   'it': {
    'name': 'Protettivo',
   },
   'es': {
    'name': 'Protector',
   },
   'sr_latn': {
    'name': 'Zaštitnički',
   },
  },
 },
}
