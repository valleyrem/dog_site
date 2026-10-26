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
   'uk': {
    'name': 'Вівчарки та худобницькі собаки (крім швейцарських)',
    'desc': "Вівчарки та худобницькі собаки — розумні робочі породи, виведені для точного керування худобою. Вони відомі сильними інстинктами, чутливістю до команд і здатністю тісно працювати з людьми. Ці собаки часто демонструють високий рівень зосередженості, тож чудові партнери як для роботи, так і для дресирування. Багато порід у цій групі енергійні й потребують регулярної розумової та фізичної стимуляції. Їхня віданість та уважність роблять їх добре придатними для активних домогосподарств. Вони схильні формувати глибокий зв'язок із власником і процвітають, коли мають чітку роль. Хоча надзвичайно здатні, їм потрібне керівництво та залучення для балансу. Без достатньої активності вони можуть стати неспокійними чи надто пильними.",
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
   'uk': {
    'name': 'Пінчери та шнауцери – молосоїдні – швейцарські гірські та худобницькі собаки',
    'desc': "Ця група включає могутні та універсальні породи зі сильними охоронними інстинктами та впевненою присутністю. Багато з цих собак спочатку виводили для захисту, фермерської роботи та компанійності. Вони зазвичай відані, стабільні та природно пильні до оточення. Деякі породи великі й грізні, інші — компактніші, але однаково впевнені. Рання соціалізація та послідовне дресирування важливі для формування їхньої поведінки. Ці собаки часто формують міцну прив'язаність до родини й можуть бути дуже охоронними. Зазвичай їм потрібен досвідчений господар і чіткі межі. За правильної структури вони — спокійні, надійні й глибоко відані компаньйони.",
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
   'uk': {
    'name': "Тер'єри",
    'desc': "Тер'єри — жваві, рішучі й сповнені характеру. Спочатку виведені для полювання та контролю шкідників, вони відомі мужністю та наполегливістю. Ці собаки часто енергійні й допитливі, з сильною ноткою самостійності. Багато тер'єрів люблять копати, досліджувати й бути зайнятими. Смілива натура робить їх впевненими, іноді навіть впертими компаньйонами. Вони виграють від послідованого дресирування та розумової стимуляції. Попри малий до середнього розмір, у них часто великий характер. За правильного балансу вони грайливі, відані й нескінченно цікаві.",
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
    'desc': 'Dachshunds are a distinct group known for their long bodies and strong hunting heritage. Originally bred to track and flush out burrowing animals, they are brave and determined. Despite their size, they often show surprising confidence and independence. They can be playful and affectionate, forming close bonds with their owners. Dachshunds tend to be curious and enjoy exploring their environment. Training may require patience due to their stubborn streak. They adapt well to different living situations, including apartments. With proper care, they are charming and loyal companions.',
   },
   'ru': {
    'name': 'Таксы',
    'desc': 'Таксы — самобытная группа, известная удлинённым телом и сильным охотничьим наследием. Выведенные изначально для выслеживания и выгона норных животных, они отважны и целеустремлённы. Несмотря на размер, таксы часто проявляют удивительную уверенность и независимость. Они могут быть игривыми и ласковыми, образуя тесные связи с владельцами. Таксы любопытны и любят исследовать окружение. Дрессировка может требовать терпения из-за упрямства. Они хорошо адаптируются к разным условиям жизни, включая квартиры. При правильном уходе это обаятельные и преданные компаньоны.',
   },
   'uk': {
    'name': 'Дахсунди',
    'desc': "Дахсунди — характерна група, відома довгим тілом та сильним мисливським спадком. Спочатку виведені для відстеження та виганяння тварин із нір, вони хоробрі й рішучі. Попри розмір, часто демонструють дивовижну впевненість і самостійність. Вони можуть бути грайливими й ласкавими, формуючи міцний зв'язок із власником. Дахсунди зазвичай допитливі й люблять досліджувати оточення. Дресирування може потребувати терпіння через нотку впертості. Добре пристосовуються до різних умов життя, включно з квартирами. За належного догляду — чарійні та відані компаньйони.",
   },
   'de': {
    'name': 'Dackel',
    'desc': 'Dackel sind eine eigenständige Gruppe, bekannt für ihre langen Körper und ihr starkes Jagderbe. Ursprünglich gezüchtet, um Bodentiere aufzuspüren und zu treiben, sind sie mutig und entschlossen. Trotz ihrer Größe zeigen sie oft überraschendes Selbstvertrauen und Unabhängigkeit. Sie können verspielt und anhänglich sein und enge Bindungen zu ihren Besitzern aufbauen. Dackel sind neugierig und erkunden gern ihre Umgebung. Beim Training braucht man Geduld wegen ihrer Sturheit. Sie passen sich verschiedenen Lebenssituationen an, auch Wohnungen. Mit der richtigen Pflege sind sie charmante und treue Begleiter.',
   },
   'it': {
    'name': 'Bassotti',
    'desc': 'I Bassotti sono un gruppo distinto, noto per il corpo allungato e la forte tradizione da caccia. Allevati originariamente per tracciare e stanare gli animali scavatori, sono coraggiosi e determinati. Nonostante la taglia, mostrano spesso una sorprendente fiducia in sé.',
   },
   'es': {
    'name': 'Teckels',
    'desc': 'Los teckels son un grupo distintivo conocido por sus cuerpos largos y su fuerte herencia cinegética. Criados originalmente para rastrear y sacar de sus madrigueras a los animales excavadores, son valientes y decididos. A pesar de su tamaño, a menudo muestran una confianza y una independencia sorprendentes. Pueden ser juguetones y afectuosos, formando lazos estrechos con sus dueños. Los teckels suelen ser curiosos y disfrutan explorando su entorno. El adiestramiento puede requerir paciencia por su testarudez. Se adaptan bien a diferentes situaciones de vida, incluidos los apartamentos. Con los cuidados adecuados, son compañeros encantadores y leales.',
   },
   'sr_latn': {
    'name': 'Jazavičari',
    'desc': 'Jazavičari su posebna grupa poznata po izduženom telu i snažnoj lovačkoj tradiciji. Prvobitno uzgajani za praćenje i izgon životinja iz jazbina, hrabri su i odlučni. Uprkos svojoj veličini, često pokazuju iznenađujuće samopouzdanje.',
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
   'uk': {
    'name': 'Шпіци та примітивні типи',
    'desc': 'Шпіци та примітивні типи — одні з найдавніших і найприродніших груп порід. У них часто густа шерсть, гострі вуха та закручені хвости. Багато цих порід зберігають сильні інстинкти та самостійне мислення. Вони зазвичай пильні, витривалі й добре пристосовані до суворого клімату. Деякі надзвичайно соціальні, інші — стриманіші та самодостатні. Цим собакам часто потрібні розуміння та шановний підхід до дресирування. Їхня поведінка може здаватися більш інстинктивною порівняно з іншими групами. За правильного середовища — відані, захопливі й глибоко виразні компаньйони.',
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
   'uk': {
    'name': 'Гончаки за запахом і споріднені породи',
    'desc': 'Гончаки за запахом керуються потужним нюхом і природною здатністю до слідування. Їх виводили для йти слідом на великі відстані з концентрацією та витривалістю. Ці собаки часто терплячі, рішучі й самостійні в роботі. Багато хто має спокійну та дружню вдачу вдома. Сильні нюхові інстинкти можуть ускладнювати відгук і контроль без повідка. Регулярна активність і збагачення важливі для задоволення. Вони зазвичай добре ладнають із людьми та іншими собаками. За правильного керівництва — ніжні, відані й стабільні компаньйони.',
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
   'uk': {
    'name': 'Лягаві',
    'desc': 'Лягаві — вправні мисливські компаньйони, відомі точністю та зосередженістю. Їх тренують знаходити дичину та подавати сигнал про неї характерною стійкою. Ці породи зазвичай енергійні, чутливі до команд і охочі до роботи. Вони процвітають від активності та тісної співпраці з господарем. Багато лягавих ласкаві та збалансовані в домашньому середовищі. Їм потрібна регулярна активність і розумове залучення для задоволення. Дресирування зазвичай ефективне завдяки готовності вчитися. За правильного способу життя — граційні, уважні та відані партнери.',
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
   'uk': {
    'name': 'Ретривери – болотні – водяні собаки',
    'desc': "Ця група включає дружелюбних та універсальних спортивних собак зі сильним інстинктом апортування та допомоги. Вони відомі м'якою пащею та співпрацюючою вдачею. Багато порід тут надзвичайно соціальні й люблять працювати тісно з людьми. Вони зазвичай мають збалансований темперамент і добре пристосовуються до сімейного життя. Регулярна активність і залучення важливі для їхнього самопочуття. Ці собаки часто відзначаються в дресируванні та різноманітних собачих спортах. Ласкава вдача робить їх особливо популярними компаньйонами. За достатньої стимуляції — надійні, добрі й легкі в спілкуванні.",
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
   'uk': {
    'name': 'Компаньйонні та іграшкові собаки',
    'desc': "Компаньйонні та іграшкові собаки виводилися передусім для людської компанії та емоційного зв'язку. Вони часто малі за розміром, але багаті на характер і чарівність. Багато порід у цій групі ласкаві, соціальні та уважні до власників. Вони зазвичай добре пристосовуються до життя в приміщенні та малих просторів. Попри розмір, їм усе одно корисна регулярна активність і взаємодія. Деякі можуть бути чутливішими чи виразнішими в поведінці. Вони часто формують міцний емоційний зв'язок і люблять бути поруч із людьми. За належного догляду — відані, жваві та заспокійливі компаньйони.",
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
   'uk': {
    'name': 'Хорти',
    'desc': 'Хорти — елегантні атлетичні собаки, виведені для швидкості та візуального слідування. Вони покладаються на зір, а не на нюх, для переслідування рухомої здобичі. Ці породи часто спокійні та ніжні вдома, попри вражаючу швидкість надворі. Вони зазвичай самостійні, але тихо ласкаві. Багато хто любить короткі спалахи інтенсивної активності з тривалим відпочинком. Їхня статура та темперамент роблять їх унікальними серед собачих груп. Дресирування потребує терпіння та розуміння їхніх інстинктів. За правильного балансу — граційні, миролюбні й глибоко відані компаньйони.',
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
   'uk': {
    'name': 'Породи поза класифікацією FCI',
    'desc': 'Ця категорія включає породи собак, які не визнані Міжнародною кінологічною федерацією (FCI), але офіційно зареєстровані або широко прийняті іншими кінологічними клубами — наприклад AKC чи UKC. Ці породи часто походять із регіонів поза Європою та можуть мати інші або менш стандартизовані системи класифікації. Попри те, що вони не є частиною системи FCI, відомі й активно розводяться та цінуються за робочі якості та компанійність.',
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
    'uk': {
     'name': 'Худобницькі собаки (крім швейцарських)',
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
    'uk': {
     'name': 'Вівчарки',
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
    'uk': {
     'name': 'Молосоїдний тип',
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
    'uk': {
     'name': 'Пінчери та шнауцери',
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
    'uk': {
     'name': 'Швейцарські гірські та худобницькі собаки',
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
    'uk': {
     'name': "Бультер'єри",
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
    'uk': {
     'name': "Великі та середні тер'єри",
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
    'uk': {
     'name': "Малі тер'єри",
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
    'uk': {
     'name': "Іграшкові тер'єри",
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
    'uk': {
     'name': 'Однопородна група (без секцій)',
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
    'uk': {
     'name': 'Азійські шпіци та споріднені породи',
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
    'uk': {
     'name': 'Європейські шпіци',
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
    'uk': {
     'name': 'Північні мисливські собаки',
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
    'uk': {
     'name': 'Північні санні собаки',
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
    'uk': {
     'name': 'Північні сторожові та пастуші собаки',
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
    'uk': {
     'name': 'Примітивний тип',
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
    'uk': {
     'name': 'Примітивний тип – мисливські собаки',
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
    'uk': {
     'name': 'Гончаки на повідку (за запахом)',
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
    'uk': {
     'name': 'Споріднені породи',
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
    'uk': {
     'name': 'Гончаки за запахом',
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
    'uk': {
     'name': 'Британські та ірландські лягаві та сетери',
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
    'uk': {
     'name': 'Континентальні лягаві',
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
    'uk': {
     'name': 'Болотні собаки',
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
    'uk': {
     'name': 'Ретривери',
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
    'uk': {
     'name': 'Водяні собаки',
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
    'uk': {
     'name': 'Бішони та споріднені породи',
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
    'uk': {
     'name': 'Чихуахуеньо',
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
    'uk': {
     'name': 'Континентальні іграшкові спанієлі та інші',
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
    'uk': {
     'name': 'Англійські іграшкові спанієлі',
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
    'uk': {
     'name': 'Голі собаки',
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
    'uk': {
     'name': 'Японський чин і пекінес',
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
    'uk': {
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
    'uk': {
     'name': 'Пуделі',
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
    'uk': {
     'name': 'Малі бельгійські собаки',
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
    'uk': {
     'name': 'Малі молосоїдні собаки',
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
    'uk': {
     'name': 'Тибетські породи',
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
    'uk': {
     'name': 'Довгошерсті або бахромасті хорти',
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
    'uk': {
     'name': 'Жорсткошерсті хорти',
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
    'uk': {
     'name': 'Короткошерсті хорти',
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
    'uk': {
     'name': 'Визнані іншими кінологічними клубами',
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
    'uk': {
     'name': 'Невизнані, але задокументовані породи',
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
   'uk': {
    'name': 'Афганістан',
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
   'uk': {
    'name': 'Бельгія',
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
   'uk': {
    'name': 'Бельгія, Франція',
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
   'uk': {
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
   'uk': {
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
   'uk': {
    'name': 'Хорватія',
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
   'uk': {
    'name': 'Чехословаччина',
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
   'uk': {
    'name': 'Франція',
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
   'uk': {
    'name': 'Німеччина',
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
   'uk': {
    'name': 'Велика Британія',
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
   'uk': {
    'name': 'Угорщина',
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
   'uk': {
    'name': 'Ірландія',
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
   'uk': {
    'name': 'Італія',
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
   'uk': {
    'name': 'Японія',
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
   'uk': {
    'name': 'Малі',
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
   'uk': {
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
   'uk': {
    'name': 'Близький Схід',
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
   'uk': {
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
   'uk': {
    'name': 'Північна Росія, Сибір',
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
   'uk': {
    'name': 'Норвегія',
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
   'uk': {
    'name': 'Португалія',
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
   'uk': {
    'name': 'Російська Федерація',
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
  },
  'Spain': {
   'en': {
    'name': 'Spain',
   },
   'ru': {
    'name': 'Испания',
   },
   'uk': {
    'name': 'Іспанія',
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
   'uk': {
    'name': 'Швеція',
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
   'uk': {
    'name': 'Швейцарія',
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
   'uk': {
    'name': 'Нідерланди',
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
   'uk': {
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
   'uk': {
    'name': 'Туреччина',
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
   'uk': {
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
   'uk': {
    'name': 'Шнурова',
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
   'uk': {
    'name': 'Кучерява',
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
   'uk': {
    'name': 'Подвійна',
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
   'uk': {
    'name': 'Гола',
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
   'uk': {
    'name': 'Жорстка',
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
   'uk': {
    'name': 'Шовковиста',
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
   'uk': {
    'name': 'Гладка',
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
   'uk': {
    'name': 'Хвиляста',
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
   'uk': {
    'name': 'Щетиниста',
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
   'uk': {
    'name': 'Довга',
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
   'uk': {
    'name': 'Середня',
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
   'uk': {
    'name': 'Коротка',
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
   'uk': {
    'name': 'Активний',
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
  'Adaptable': {
   'en': {
    'name': 'Adaptable',
   },
   'ru': {
    'name': 'Уживчивый',
   },
   'uk': {
    'name': 'Адаптивний',
   },
   'de': {
    'name': 'Anpassungsfähig',
   },
   'it': {
    'name': 'Adattabile',
   },
   'es': {
    'name': 'Adaptable',
   },
   'sr_latn': {
    'name': 'Prilagodljiv',
   },
  },
  'Affectionate': {
   'en': {
    'name': 'Affectionate',
   },
   'ru': {
    'name': 'Ласковый',
   },
   'uk': {
    'name': 'Ласкавий до людей',
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
  'Agile': {
   'en': {
    'name': 'Agile',
   },
   'ru': {
    'name': 'Проворный',
   },
   'uk': {
    'name': 'Спритний',
   },
   'de': {
    'name': 'Agil',
   },
   'it': {
    'name': 'Agile',
   },
   'es': {
    'name': 'Ágil',
   },
   'sr_latn': {
    'name': 'Okretan',
   },
  },
  'Alert': {
   'en': {
    'name': 'Alert',
   },
   'ru': {
    'name': 'Живой',
   },
   'uk': {
    'name': 'Пильний',
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
  'Aloof': {
   'en': {
    'name': 'Aloof',
   },
   'ru': {
    'name': 'Сдержанный',
   },
   'uk': {
    'name': 'Відсторонений',
   },
   'de': {
    'name': 'Distanziert',
   },
   'it': {
    'name': 'Distaccato',
   },
   'es': {
    'name': 'Distante',
   },
   'sr_latn': {
    'name': 'Povučen',
   },
  },
  'Brave': {
   'en': {
    'name': 'Brave',
   },
   'ru': {
    'name': 'Храбрый',
   },
   'uk': {
    'name': 'Хоробрий',
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
   'uk': {
    'name': 'Спокійний',
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
  'Charming': {
   'en': {
    'name': 'Charming',
   },
   'ru': {
    'name': 'Обаятельный',
   },
   'uk': {
    'name': 'Чарівний',
   },
   'de': {
    'name': 'Charmant',
   },
   'it': {
    'name': 'Affascinante',
   },
   'es': {
    'name': 'Encantador',
   },
   'sr_latn': {
    'name': 'Šarmantan',
   },
  },
  'Cheerful': {
   'en': {
    'name': 'Cheerful',
   },
   'ru': {
    'name': 'Жизнерадостный',
   },
   'uk': {
    'name': 'Веселий',
   },
   'de': {
    'name': 'Fröhlich',
   },
   'it': {
    'name': 'Allegro',
   },
   'es': {
    'name': 'Alegre',
   },
   'sr_latn': {
    'name': 'Vedar',
   },
  },
  'Confident': {
   'en': {
    'name': 'Confident',
   },
   'ru': {
    'name': 'Уверенный',
   },
   'uk': {
    'name': 'Впевнений',
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
   'uk': {
    'name': 'Хоробрий',
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
  'Determined': {
   'en': {
    'name': 'Determined',
   },
   'ru': {
    'name': 'Упорный',
   },
   'uk': {
    'name': 'Рішучий',
   },
   'de': {
    'name': 'Entschlossen',
   },
   'it': {
    'name': 'Determinato',
   },
   'es': {
    'name': 'Decidido',
   },
   'sr_latn': {
    'name': 'Odlučan',
   },
  },
  'Devoted': {
   'en': {
    'name': 'Devoted',
   },
   'ru': {
    'name': 'Преданный',
   },
   'uk': {
    'name': 'Відданий',
   },
   'de': {
    'name': 'Hingebungsvoll',
   },
   'it': {
    'name': 'Devoto',
   },
   'es': {
    'name': 'Devoto',
   },
   'sr_latn': {
    'name': 'Odan',
   },
  },
  'Dignified': {
   'en': {
    'name': 'Dignified',
   },
   'ru': {
    'name': 'Достойный',
   },
   'uk': {
    'name': 'Гідний',
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
   'uk': {
    'name': 'Охочий',
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
  'Easygoing': {
   'en': {
    'name': 'Easygoing',
   },
   'ru': {
    'name': 'Спокойный',
   },
   'uk': {
    'name': 'Легкий у спілкуванні',
   },
   'de': {
    'name': 'Unkompliziert',
   },
   'it': {
    'name': 'Tranquillo',
   },
   'es': {
    'name': 'Complaciente',
   },
   'sr_latn': {
    'name': 'Ležeran',
   },
  },
  'Energetic': {
   'en': {
    'name': 'Energetic',
   },
   'ru': {
    'name': 'Энергичный',
   },
   'uk': {
    'name': 'Енергійний',
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
   'uk': {
    'name': 'Рівноважний',
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
  'Fast': {
   'en': {
    'name': 'Fast',
   },
   'ru': {
    'name': 'Быстрый',
   },
   'uk': {
    'name': 'Швидкий',
   },
   'de': {
    'name': 'Schnell',
   },
   'it': {
    'name': 'Veloce',
   },
   'es': {
    'name': 'Rápido',
   },
   'sr_latn': {
    'name': 'Brz',
   },
  },
  'Fearless': {
   'en': {
    'name': 'Fearless',
   },
   'ru': {
    'name': 'Бесстрашный',
   },
   'uk': {
    'name': 'Безстрашний',
   },
   'de': {
    'name': 'Furchtlos',
   },
   'it': {
    'name': 'Impavido',
   },
   'es': {
    'name': 'Sin miedo',
   },
   'sr_latn': {
    'name': 'Neustrašiv',
   },
  },
  'Focused': {
   'en': {
    'name': 'Focused',
   },
   'ru': {
    'name': 'Сфокусированный',
   },
   'uk': {
    'name': 'Зосереджений',
   },
   'de': {
    'name': 'Fokussiert',
   },
   'it': {
    'name': 'Concentrato',
   },
   'es': {
    'name': 'Concentrado',
   },
   'sr_latn': {
    'name': 'Usredsređen',
   },
  },
  'Friendly': {
   'en': {
    'name': 'Friendly',
   },
   'ru': {
    'name': 'Дружелюбный',
   },
   'uk': {
    'name': 'Дружелюбний',
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
  'Game': {
   'en': {
    'name': 'Game',
   },
   'ru': {
    'name': 'Азартный',
   },
   'uk': {
    'name': 'Готовий до гри',
   },
   'de': {
    'name': 'Spielmutig',
   },
   'it': {
    'name': 'Combattivo',
   },
   'es': {
    'name': 'Batallador',
   },
   'sr_latn': {
    'name': 'Spreman',
   },
  },
  'Gentle': {
   'en': {
    'name': 'Gentle',
   },
   'ru': {
    'name': 'Нежный',
   },
   'uk': {
    'name': 'Ніжний',
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
  'Good-natured': {
   'en': {
    'name': 'Good-natured',
   },
   'ru': {
    'name': 'Добродушный',
   },
   'uk': {
    'name': 'Добродушний',
   },
   'de': {
    'name': 'Gutmütig',
   },
   'it': {
    'name': 'Di buon carattere',
   },
   'es': {
    'name': 'De buen natural',
   },
   'sr_latn': {
    'name': 'Dobrodušan',
   },
  },
  'Happy': {
   'en': {
    'name': 'Happy',
   },
   'ru': {
    'name': 'Радостный',
   },
   'uk': {
    'name': 'Щасливий',
   },
   'de': {
    'name': 'Fröhlich',
   },
   'it': {
    'name': 'Felice',
   },
   'es': {
    'name': 'Feliz',
   },
   'sr_latn': {
    'name': 'Srećan',
   },
  },
  'Hardworking': {
   'en': {
    'name': 'Hardworking',
   },
   'ru': {
    'name': 'Работоспособный',
   },
   'uk': {
    'name': 'Працьовитий',
   },
   'de': {
    'name': 'Fleißig',
   },
   'it': {
    'name': 'Laborioso',
   },
   'es': {
    'name': 'Trabajador',
   },
   'sr_latn': {
    'name': 'Marljiv',
   },
  },
  'Hardy': {
   'en': {
    'name': 'Hardy',
   },
   'ru': {
    'name': 'Выносливый',
   },
   'uk': {
    'name': 'Витривалий',
   },
   'de': {
    'name': 'Robust',
   },
   'it': {
    'name': 'Robusto',
   },
   'es': {
    'name': 'Resistente',
   },
   'sr_latn': {
    'name': 'Otporan',
   },
  },
  'Independent': {
   'en': {
    'name': 'Independent',
   },
   'ru': {
    'name': 'Независимый',
   },
   'uk': {
    'name': 'Самостійний',
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
  'Inquisitive': {
   'en': {
    'name': 'Inquisitive',
   },
   'ru': {
    'name': 'Любопытный',
   },
   'de': {
    'name': 'Neugierig',
   },
   'it': {
    'name': 'Curioso',
   },
   'sr_latn': {
    'name': 'Radoznao',
   },
  },
  'Intelligent': {
   'en': {
    'name': 'Intelligent',
   },
   'ru': {
    'name': 'Умный',
   },
   'uk': {
    'name': 'Розумний',
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
  'Laid-back': {
   'en': {
    'name': 'Laid-back',
   },
   'ru': {
    'name': 'Спокойный',
   },
   'uk': {
    'name': 'Розслаблений',
   },
   'de': {
    'name': 'Locker',
   },
   'it': {
    'name': 'Rilassato',
   },
   'es': {
    'name': 'Relajado',
   },
   'sr_latn': {
    'name': 'Opušten',
   },
  },
  'Loving': {
   'en': {
    'name': 'Loving',
   },
   'ru': {
    'name': 'Любящий',
   },
   'uk': {
    'name': 'Ласкавий',
   },
   'de': {
    'name': 'Liebevoll',
   },
   'it': {
    'name': 'Amorevole',
   },
   'es': {
    'name': 'Cariñoso',
   },
   'sr_latn': {
    'name': 'Pun ljubavi',
   },
  },
  'Loyal': {
   'en': {
    'name': 'Loyal',
   },
   'ru': {
    'name': 'Верный',
   },
   'uk': {
    'name': 'Віданий',
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
  'Outgoing': {
   'en': {
    'name': 'Outgoing',
   },
   'ru': {
    'name': 'Общительный',
   },
   'uk': {
    'name': 'Відкритий',
   },
   'de': {
    'name': 'Aufgeschlossen',
   },
   'it': {
    'name': 'Estroverso',
   },
   'es': {
    'name': 'Abierto',
   },
   'sr_latn': {
    'name': 'Društven',
   },
  },
  'Patient': {
   'en': {
    'name': 'Patient',
   },
   'ru': {
    'name': 'Терпеливый',
   },
   'uk': {
    'name': 'Терплячий',
   },
   'de': {
    'name': 'Geduldig',
   },
   'it': {
    'name': 'Paziente',
   },
   'es': {
    'name': 'Paciente',
   },
   'sr_latn': {
    'name': 'Strpljiv',
   },
  },
  'Persistent': {
   'en': {
    'name': 'Persistent',
   },
   'ru': {
    'name': 'Настойчивый',
   },
   'uk': {
    'name': 'Наполегливий',
   },
   'de': {
    'name': 'Beharrlich',
   },
   'it': {
    'name': 'Persistente',
   },
   'es': {
    'name': 'Persistente',
   },
   'sr_latn': {
    'name': 'Ustrajan',
   },
  },
  'Playful': {
   'en': {
    'name': 'Playful',
   },
   'ru': {
    'name': 'Игривый',
   },
   'uk': {
    'name': 'Грайливий',
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
  'Plucky': {
   'en': {
    'name': 'Plucky',
   },
   'ru': {
    'name': 'Отважный',
   },
   'uk': {
    'name': 'Сміливий',
   },
   'de': {
    'name': 'Mutig',
   },
   'it': {
    'name': 'Spavaldo',
   },
   'es': {
    'name': 'Animoso',
   },
   'sr_latn': {
    'name': 'Smel',
   },
  },
  'Protective': {
   'en': {
    'name': 'Protective',
   },
   'ru': {
    'name': 'Защитный',
   },
   'uk': {
    'name': 'Охоронний',
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
  'Quiet': {
   'en': {
    'name': 'Quiet',
   },
   'ru': {
    'name': 'Спокойный',
   },
   'uk': {
    'name': 'Тихий',
   },
   'de': {
    'name': 'Ruhig',
   },
   'it': {
    'name': 'Quieto',
   },
   'es': {
    'name': 'Silencioso',
   },
   'sr_latn': {
    'name': 'Tih',
   },
  },
  'Reserved': {
   'en': {
    'name': 'Reserved',
   },
   'ru': {
    'name': 'Сдержанный',
   },
   'uk': {
    'name': 'Стриманий',
   },
   'de': {
    'name': 'Zurückhaltend',
   },
   'it': {
    'name': 'Riservato',
   },
   'es': {
    'name': 'Reservado',
   },
   'sr_latn': {
    'name': 'Rezervisan',
   },
  },
  'Self-important': {
   'en': {
    'name': 'Self-important',
   },
   'ru': {
    'name': 'Важный',
   },
   'uk': {
    'name': 'Самооцінний',
   },
   'de': {
    'name': 'Selbstgewiss',
   },
   'it': {
    'name': 'Pieno di sé',
   },
   'es': {
    'name': 'Presumido',
   },
   'sr_latn': {
    'name': 'Uobražen',
   },
  },
  'Sensitive': {
   'en': {
    'name': 'Sensitive',
   },
   'ru': {
    'name': 'Чувствительный',
   },
   'uk': {
    'name': 'Чутливий',
   },
   'de': {
    'name': 'Sensibel',
   },
   'it': {
    'name': 'Sensibile',
   },
   'es': {
    'name': 'Sensible',
   },
   'sr_latn': {
    'name': 'Osetljiv',
   },
  },
  'Smart': {
   'en': {
    'name': 'Smart',
   },
   'ru': {
    'name': 'Умный',
   },
   'uk': {
    'name': 'Розумний',
   },
   'de': {
    'name': 'Klug',
   },
   'it': {
    'name': 'Sveglio',
   },
   'es': {
    'name': 'Listo',
   },
   'sr_latn': {
    'name': 'Pametan',
   },
  },
  'Sociable': {
   'en': {
    'name': 'Sociable',
   },
   'ru': {
    'name': 'Общительный',
   },
   'uk': {
    'name': 'Товариський',
   },
   'de': {
    'name': 'Kontaktfreudig',
   },
   'it': {
    'name': 'Socievole',
   },
   'es': {
    'name': 'Sociable',
   },
   'sr_latn': {
    'name': 'Komunikativan',
   },
  },
  'Social': {
   'en': {
    'name': 'Social',
   },
   'ru': {
    'name': 'Общительный',
   },
   'uk': {
    'name': 'Соціальний',
   },
   'de': {
    'name': 'Gesellig',
   },
   'it': {
    'name': 'Sociale',
   },
   'es': {
    'name': 'Social',
   },
   'sr_latn': {
    'name': 'Druželjubiv',
   },
  },
  'Spirited': {
   'en': {
    'name': 'Spirited',
   },
   'ru': {
    'name': 'Живой',
   },
   'uk': {
    'name': 'Жвавий',
   },
   'de': {
    'name': 'Temperamentvoll',
   },
   'it': {
    'name': 'Vivace',
   },
   'es': {
    'name': 'Espirituoso',
   },
   'sr_latn': {
    'name': 'Živahan',
   },
  },
  'Strong-willed': {
   'en': {
    'name': 'Strong-willed',
   },
   'ru': {
    'name': 'Упрямый',
   },
   'uk': {
    'name': 'Вольовий',
   },
   'de': {
    'name': 'Willensstark',
   },
   'it': {
    'name': 'Volitivo',
   },
   'es': {
    'name': 'De carácter fuerte',
   },
   'sr_latn': {
    'name': 'Snažne volje',
   },
  },
  'Stubborn': {
   'en': {
    'name': 'Stubborn',
   },
   'ru': {
    'name': 'Упрямый',
   },
   'uk': {
    'name': 'Впертий',
   },
   'de': {
    'name': 'Stur',
   },
   'it': {
    'name': 'Testardo',
   },
   'es': {
    'name': 'Testarudo',
   },
   'sr_latn': {
    'name': 'Tvrdoglav',
   },
  },
  'Trainable': {
   'en': {
    'name': 'Trainable',
   },
   'ru': {
    'name': 'Дрессируемый',
   },
   'uk': {
    'name': 'Дресований',
   },
   'de': {
    'name': 'Trainierbar',
   },
   'it': {
    'name': 'Addestrabile',
   },
   'es': {
    'name': 'Entrenable',
   },
   'sr_latn': {
    'name': 'Dresabilan',
   },
  },
 },
}
