"""Fill Italian content for Dogs, Category, Section, CoatType, CoatLength and Temperament.

Mirrors fill_de_content.py. Idempotent: only fills empty values. Run:
    python manage.py fill_it_content
"""

from django.core.management.base import BaseCommand
from django.utils import translation

from woof.models import (
    Category,
    CoatLength,
    CoatType,
    Dogs,
    Section,
    Temperament,
)

DOGS_TITLES_IT = {
    "Afghan Hound": "Levriero Afgano",
    "Airedale Terrier": "Airedale Terrier",
    "Akita": "Akita",
    "Alaskan Malamute": "Malamute dell'Alaska",
    "American Cocker Spaniel": "Cocker Spaniel Americano",
    "American Eskimo Dog": "American Eskimo Dog",
    "American Staffordshire Terrier": "American Staffordshire Terrier",
    "Anatolian Shepherd Dog": "Pastore dell'Anatolia",
    "Australian Shepherd": "Pastore Australiano",
    "Azawakh": "Azawakh",
    "Barbado da Terceira": "Barbado da Terceira",
    "Basset Hound": "Basset Hound",
    "Bedlington Terrier": "Bedlington Terrier",
    "Bichon Frise": "Bichon a pelo riccio",
    "Black and Tan Coonhound": "Black and Tan Coonhound",
    "Bloodhound": "Bloodhound",
    "Bolognese": "Bolognese",
    "Border Collie": "Border Collie",
    "Border Terrier": "Border Terrier",
    "Borzoi": "Borzoi",
    "Boxer": "Boxer",
    "Brussels Griffon": "Grifone di Bruxelles",
    "Bulldog": "Bulldog",
    "Bull Terrier": "Bull Terrier",
    "Catahoula Leopard Dog": "Catahoula Leopard Dog",
    "Cavalier King Charles Spaniel": "Cavalier King Charles Spaniel",
    "Collie Rough": "Collie (a pelo lungo)",
    "Czechoslovakian Wolfdog": "Cane Lupo Cecoslovacco",
    "Dachshund": "Bassotto",
    "Dalmatian": "Dalmata",
    "Dobermann": "Dobermann",
    "Drever": "Drever",
    "Dutch Shepherd Dog": "Pastore Olandese",
    "English Setter": "Setter Inglese",
    "French Bulldog": "Bouledogue Francese",
    "German Shepherd Dog": "Pastore Tedesco",
    "German Shorthaired Pointer": "Bracco Tedesco a pelo corto",
    "German Spitz": "Spitz Tedesco",
    "Golden Retriever": "Golden Retriever",
    "Great Dane": "Alano",
    "Hovawart": "Hovawart",
    "Irish Wolfhound": "Levriero Irlandese",
    "Italian Cane Corso": "Cane Corso",
    "Italian Sighthound": "Piccolo Levriero Italiano",
    "Italian Spinone": "Spinone Italiano",
    "Kai": "Kai",
    "Keeshond (Wolfspitz)": "Keeshond (Wolfspitz)",
    "Kleiner Münsterländer": "Piccolo Münsterländer",
    "Labrador Retriever": "Labrador Retriever",
    "Nederlandse Kooikerhondje": "Kooikerhondje",
    "Norwegian Elkhound Grey": "Elkhound norvegese grigio",
    "Nova Scotia Duck Tolling Retriever": "Nova Scotia Duck Tolling Retriever",
    "Old English Sheepdog": "Bobtail",
    "Pekingese": "Pechinese",
    "Pembroke Welsh Corgi": "Welsh Corgi Pembroke",
    "Pomeranian": "Volpino di Pomerania",
    "Poodle": "Barbone",
    "Portuguese Podengo": "Podengo Portoghese",
    "Pug": "Carlino",
    "Puli": "Puli",
    "Rat Terrier": "Rat Terrier",
    "Romagna Water Dog": "Lagotto Romagnolo",
    "Rottweiler": "Rottweiler",
    "Saint Bernard": "San Bernardo",
    "Samoyed": "Samoiedo",
    "Scottish Terrier": "Scottish Terrier",
    "Shar Pei": "Shar Pei",
    "Shih Tzu": "Shih Tzu",
    "Siberian Husky": "Husky Siberiano",
    "Sloughi": "Sloughi",
    "Treeing Walker Coonhound": "Treeing Walker Coonhound",
    "Weimaraner": "Weimaraner",
    "Whippet": "Whippet",
    "Wire Fox Terrier": "Fox Terrier a pelo duro",
    "Xoloitzcuintli": "Xoloitzcuintle",
    "Yakutian Laika": "Laika della Jacuzia",
    "Yorkshire Terrier": "Yorkshire Terrier",
}

CATEGORY_NAMES_IT = {
    "Breeds outside FCI classification": "Razze fuori dalla classificazione FCI",
    "Sheepdogs and Cattledogs (except Swiss Cattledogs)": "Cani da pastore e bovari (eccetto bovari svizzeri)",
    "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs": "Pinscher e Schnauzer - Molossoidi e cani svizzeri da montagna e bovari",
    "Terriers": "Terrier",
    "Dachshunds": "Bassotti",
    "Spitz and primitive types": "Spitz e tipi primitivi",
    "Scent hounds and related breeds": "Segugi e razze affini",
    "Pointing Dogs": "Cani da ferma",
    "Retrievers - Flushing Dogs - Water Dogs": "Cani da riporto - Cani da cerca - Cani da acqua",
    "Companion and Toy Dogs": "Cani da compagnia e da salotto",
    "Sighthounds": "Levrieri",
}

SECTION_NAMES_IT = {
    "Asian Spitz and related breeds": "Spitz asiatici e razze affini",
    "Bichons and related breeds": "Bichon e razze affini",
    "British and Irish Pointers and Setters": "Cani da ferma britannici e irlandesi",
    "Bull type Terriers": "Terrier di tipo Bull",
    "Cattledogs (except Swiss Cattledogs)": "Cani bovari (eccetto bovari svizzeri)",
    "Chihuahueno": "Chihuahueño",
    "Continental Pointing Dogs": "Cani da ferma continentali",
    "Continental Toy Spaniel and others": "Epagneul nani continentali e altri",
    "English Toy Spaniels": "Epagneul nani inglesi",
    "European Spitz": "Spitz europei",
    "Flushing Dogs": "Cani da cerca",
    "Hairless Dogs": "Cani nudi",
    "Japan Chin and Pekingese": "Chin giapponesi e Pechinesi",
    "Kromfohrländer": "Kromfohrländer",
    "Large and medium sized Terriers": "Terrier di taglia grande e media",
    "Leash (scent) Hounds": "Segugi da traccia (da fiuto)",
    "Long-haired or fringed Sighthounds": "Levrieri a pelo lungo o frangiato",
    "Molossian type": "Tipo molossoide",
    "Nordic Hunting Dogs": "Cani nordici da caccia",
    "Nordic Sledge Dogs": "Cani nordici da slitta",
    "Nordic Watchdogs and Herders": "Cani nordici da guardia e da pastore",
    "Pinscher and Schnauzer type": "Tipo Pinscher e Schnauzer",
    "Poodle": "Barbone",
    "Primitive type": "Tipo primitivo",
    "Primitive type - Hunting Dogs": "Tipo primitivo - cani da caccia",
    "Recognized by Other Kennel Clubs": "Riconosciute da altri club cinofili",
    "Related breeds": "Razze affini",
    "Retrievers": "Cani da riporto",
    "Rough-haired Sighthounds": "Levrieri a pelo duro",
    "Scent hounds": "Segugi da fiuto",
    "Sheepdogs": "Cani da pastore",
    "Short-haired Sighthounds": "Levrieri a pelo corto",
    "Single breed group (no sections)": "Gruppo di singola razza (senza sezioni)",
    "Small Belgian Dogs": "Piccoli cani belgi",
    "Small Molossian type Dogs": "Cani di tipo molossoide di piccola taglia",
    "Small sized Terriers": "Terrier di piccola taglia",
    "Swiss Mountain and Cattledogs": "Cani svizzeri da montagna e bovari",
    "Tibetan breeds": "Razze tibetane",
    "Toy Terriers": "Terrier toy",
    "Unrecognized but Documented Breeds": "Razze non riconosciute ma documentate",
    "Water Dogs": "Cani da acqua",
}

VARIETIES_IT = {
    "Color variations": "Varietà di colore",
    "described in «About the Breed»": "descritte in «Sulla razza»",
    "It's a variety of German Spitz": "È una varietà dello Spitz tedesco",
    "No variations": "Nessuna varietà",
    "Rabbit, Miniature, Standard": "Coniglio, Nano, Standard",
    "Size variations": "Varietà di taglia",
    "Small, Medium-sized, Large": "Piccola, Media, Grande",
    "Standard, Medium, Miniature, Toy": "Standard, Media, Nano, Toy",
    "Standart, Intermediate, Miniature": "Standard, Intermedia, Nano",
    "Toy, Miniature, Standard": "Toy, Nano, Standard",
}
COLORS_IT = {
    "Black and tan, black and red, sable, solid black, black and cream, black and silver": "Nero focato, nero e rosso, sabbia, nero uniforme, nero e crema, nero e argento",
    "Black and tan, grizzle and tan": "Nero focato, grigio-blu focato",
    "Black and tan (signature coat pattern with rich tan markings over a deep black base)": "Nero focato (tipico mantello con focature ricche su base nera profonda)",
    "Black, black and gold, blonde": "Nero, nero e dorato, biondo",
    "Black, Blue, Cream, Fawn, Red, Brindle, White, Gold, Grey": "Nero, blu, crema, fulvo, rosso, tigrato, bianco, dorato, grigio",
    "Black, blue, fawn, red, brindle, white, solid or patched combinations": "Nero, blu, fulvo, rosso, tigrato, bianco, uniformi o con chiazze",
    "Black, Brindle, Wheaten, Silver Brindle": "Nero, tigrato, grano, tigrato argento",
    "Black, Gray, Fawn, Red, Brindle": "Nero, grigio, fulvo, rosso, tigrato",
    "Black, gray, slate, red, bronze, liver, solid or spotted": "Nero, grigio, ardesia, rosso, bronzo, fegato, uniformi o maculati",
    "Black, Gray, White": "Nero, grigio, bianco",
    "Black, red, buff, brown, parti-color (white with patches), roan variations": "Nero, rosso, beige, marrone, bicolore (bianco con chiazze), roano nelle sue varietà",
    "Black & Rust, Black & Mahogany, Black & Tan": "Nero e ruggine, nero e mogano, nero focato",
    "Black & Rust, Red & Rust, Blue & Rust, Fawn & Rust, White": "Nero e ruggine, rosso e ruggine, blu e ruggine, fulvo e ruggine, bianco",
    "Black & Tan, Liver & Tan, Red": "Nero focato, fegato focato, rosso",
    "Black, white, brown, apricot, red, silver, cream, gray, blue, parti-color": "Nero, bianco, marrone, albicocca, rosso, argento, crema, grigio, blu, bicolore",
    "Black, white, cream, brown, orange, sable": "Nero, bianco, crema, marrone, arancio, sabbia",
    "Black, White, Gold, Brindle, Liver, Silver, Mixed": "Nero, bianco, dorato, tigrato, fegato, argento, misto",
    "Black & White, Gray & White, Red & White, Agouti, All-White": "Nero e bianco, grigio e bianco, rosso e bianco, agouti, tutto bianco",
    "Black & white, red & white, tricolor, blue merle, sable, and other variations": "Nero e bianco, rosso e bianco, tricolore, blu merle, sabbia e altre varietà",
    "Black, white, tan, chocolate, blue, lemon, red; bicolor and tricolor patterns": "Nero, bianco, focato, cioccolato, blu, limone, rosso; disegni bicolori e tricolori",
    "Black, Yellow, Chocolate": "Nero, giallo, cioccolato",
    "Blenheim, Tricolor, Black & Tan, Ruby": "Blenheim, tricolore, nero focato, rubino",
    "Blue Belton, Lemon Belton, Orange Belton, Tricolor": "Blu belton, limone belton, arancio belton, tricolore",
    "Blue, liver, sandy, blue & tan, liver & tan": "Blu, fegato, sabbia, blu focato, fegato focato",
    "Blue Merle, Red Merle, Black, Red, White Markings": "Blu merle, rosso merle, nero, rosso, con segni bianchi",
    "Brindle, Fawn, White, Pied, Cream": "Tigrato, fulvo, bianco, pezzato, crema",
    "Brindle (gold or silver), sometimes with black patterning": "Tigrato (dorato o argento), talvolta con disegni neri",
    "Brown & white, brown roan": "Marrone e bianco, roano marrone",
    "Cream, sand, red fawn, mahogany, brindle, black mask, black ears, with or without small white markings": "Crema, sabbia, fulvo rosso, mogano, tigrato, maschera nera, orecchie nere, con o senza piccoli segni bianchi",
    "Fawn, Black, Apricot, Silver Fawn": "Fulvo, nero, albicocca, fulvo argento",
    "Fawn, Blue, Black, Red, White, Cream": "Fulvo, blu, nero, rosso, bianco, crema",
    "Fawn, Brindle, Black, Blue, Red, White, Mixed": "Fulvo, tigrato, nero, blu, rosso, bianco, misto",
    "Fawn, Brindle, Blue, Black, Harlequin, Mantle": "Fulvo, tigrato, blu, nero, arlecchino, mantello",
    "Fawn, Brindle, Red, Black, Blue": "Fulvo, tigrato, rosso, nero, blu",
    "Fawn, brindle, white markings": "Fulvo, tigrato, con segni bianchi",
    "Fawn, Brindle, White, Piebald, Red, Fallow": "Fulvo, tigrato, bianco, pezzato, rosso, cammello",
    "Fawn, White, Brindle, Sable, Masked": "Fulvo, bianco, tigrato, sabbia, con maschera",
    "Golden shades (light to dark)": "Sfumature del dorato (dal chiaro allo scuro)",
    "Gold, red, sable, cream, black, black & tan, parti-color": "Dorato, rosso, sabbia, crema, nero, nero focato, bicolore",
    "Gray, Black-tipped": "Grigio, con punte nere",
    "Gray, Brindle, Red, Black, Fawn, White": "Grigio, tigrato, rosso, nero, fulvo, bianco",
    "Gray & White, Blue & White, Blue Merle, Grizzle & White": "Grigio e bianco, blu e bianco, blu merle, grigio-blu e bianco",
    "Grey with black shading, cream, variations of wolf-grey": "Grigio con sfumature nere, crema, varietà del grigio lupo",
    "Light gray, Black, Sable, Red, Seal, White": "Grigio chiaro, nero, sabbia, rosso, foca, bianco",
    "Liver, Liver & White, Roan": "Fegato, fegato e bianco, roano",
    "Merle, blue merle, red merle, black, brindle, solid colors with patterns": "Merle, blu merle, rosso merle, nero, tigrato, colori uniformi con disegni",
    "Off-white, white with orange or brown patches, brown, orange, roan": "Bianco sporco, bianco con chiazze arancio o marroni, marrone, arancio, roano",
    "Orange, Black, White, Cream, Blue, Brown, Sable, Chocolate Merle, Brindle, Beaver": "Arancio, nero, bianco, crema, blu, marrone, sabbia, cioccolato merle, tigrato, castoro",
    "Red, black, black & tan, belge (reddish-brown with black mask), solid black": "Rosso, nero, nero focato, belga (marrone-rossastro con maschera nera), nero uniforme",
    "Red, black & tan, chocolate & tan, cream, dapple, brindle, piebald": "Rosso, nero focato, cioccolato focato, crema, maculato, tigrato, pezzato",
    "Red, grizzle and tan, blue and tan, wheaten": "Rosso, grigio-blu focato, blu focato, grano",
    "Red, Sable, Fawn, Black & Tan, Tricolor": "Rosso, sabbia, fulvo, nero focato, tricolore",
    "Red & White, Brindle & White, Mostly White": "Rosso e bianco, tigrato e bianco, prevalentemente bianco",
    "Sable & White, Tricolor, Blue Merle, White, Blue Merle & White": "Sabbia e bianco, tricolore, blu merle, bianco, blu merle e bianco",
    "Shades of red and orange with white markings often present on chest, feet, tail tip, or face": "Sfumature di rosso e arancio con segni bianchi spesso presenti su petto, zampe, punta della coda o muso",
    "Silver gray, Blue, Gray": "Grigio argento, blu, grigio",
    "Solid colors: cream, red, fawn, black, blue, chocolate, sable": "Colori uniformi: crema, rosso, fulvo, nero, blu, cioccolato, sabbia",
    "Steel blue & Tan": "Blu acciaio e focato",
    "Tiger brindle (brown/black stripes)": "Tigrato tigre (strisce marroni/nere)",
    "Tri-color, Bi-color, Lemon & White, Red & White, Tan & White": "Tricolore, bicolore, limone e bianco, rosso e bianco, focato e bianco",
    "Tricolor (Black, White, Tan)": "Tricolore (nero, bianco, focato)",
    "White": "Bianco",
    "White, black, brown, gray, piebald / tricolor combinations": "Bianco, nero, marrone, grigio, pezzato / combinazioni tricolori",
    "White, Black, Gold, Brindle, Various combinations": "Bianco, nero, dorato, tigrato, varie combinazioni",
    "White, Brindle, Fawn, Black, Red": "Bianco, tigrato, fulvo, nero, rosso",
    "White, Cream, Biscuit": "Bianco, crema, biscuit",
    "White or white with cream (biscuit)": "Bianco o bianco con crema (biscuit)",
    "White, Red, Brindle, Fawn, Sesame, Piebald": "Bianco, rosso, tigrato, fulvo, sesamo, pezzato",
    "White (sometimes with apricot, cream, or buff shadings)": "Bianco (talvolta con sfumature albicocca, crema o beige)",
    "White, white & orange, orange roan, white & brown, brown roan": "Bianco, bianco e arancio, roano arancio, bianco e marrone, roano marrone",
    "White with black or brown markings": "Bianco con segni neri o marroni",
    "White with black or liver spots, White & Orange, White & Lemon, White Black & Tan": "Bianco con macchie nere o fegato, bianco e arancio, bianco e limone, bianco nero focato",
    "White with orange-red patches": "Bianco con chiazze rosso-arancio",
    "Yellow, Fawn, Black & Tan": "Giallo, fulvo, nero focato",
    "Yellow, Fawn, Chestnut, Gray, Gold, Red, Orange and mixed": "Giallo, fulvo, castano, grigio, dorato, rosso, arancio e misto",
    "Yellow, gray, black, fawn, wolf-gray, often with white markings": "Giallo, grigio, nero, fulvo, grigio lupo, spesso con segni bianchi",
    "Yellow-gray, silver-gray, dark gray, with light mask": "Giallo-grigio, grigio argento, grigio scuro, con maschera chiara",
}

COUNTRY_IT = {
    "Afganistan": "Afghanistan",
    "Belgium": "Belgio",
    "Belgium, France": "Belgio, Francia",
    "Canada": "Canada",
    "China": "Cina",
    "Croatia": "Croazia",
    "Czechoslovakia": "Cecoslovacchia",
    "France": "Francia",
    "Germany": "Germania",
    "Great Britain": "Gran Bretagna",
    "Hungary": "Ungheria",
    "Irleand": "Irlanda",
    "Italy": "Italia",
    "Japan": "Giappone",
    "Mali": "Mali",
    "Mexico": "Messico",
    "Morocco": "Marocco",
    "Northern Russia, Siberia": "Russia settentrionale, Siberia",
    "Norway": "Norvegia",
    "Portugal": "Portogallo",
    "Russian Federation": "Federazione Russa",
    "Sweden": "Svezia",
    "Switzerland": "Svizzera",
    "The Netherlands": "Paesi Bassi",
    "Tibet (China)": "Tibet (Cina)",
    "Turkey": "Turchia",
    "USA": "Stati Uniti",
}

COATTYPE_IT = {
    "Curly": "Riccio",
    "Wavy": "Mosso",
    "Corded": "Cordonato",
    "Hairless": "Nudo",
    "Smooth": "Liscio",
    "Double coat": "Doppio mantello",
    "Silky": "Setoso",
    "Rough": "Ruvido",
    "Wiry": "Duro (fil di ferro)",
}

COATLEN_IT = {
    "Short": "Corto",
    "Medium": "Medio",
    "Long": "Lungo",
}

TEMPERAMENT_IT = {
    "Active": "Attivo",
    "Adaptable": "Adattabile",
    "Affectionate": "Affettuoso",
    "Agile": "Agile",
    "Alert": "Vigile",
    "Aloof": "Distaccato",
    "Brave": "Audace",
    "Calm": "Calmo",
    "Charming": "Affascinante",
    "Cheerful": "Allegro",
    "Confident": "Sicuro di sé",
    "Courageous": "Coraggioso",
    "Determined": "Determinato",
    "Devoted": "Devoto",
    "Dignified": "Dignitoso",
    "Eager": "Desideroso",
    "Easygoing": "Tranquillo",
    "Energetic": "Energico",
    "Even-tempered": "Equilibrato",
    "Fast": "Veloce",
    "Fearless": "Impavido",
    "Focused": "Concentrato",
    "Friendly": "Amichevole",
    "Game": "Combattivo",
    "Gentle": "Gentile",
    "Good-natured": "Di buon carattere",
    "Happy": "Felice",
    "Hardworking": "Laborioso",
    "Hardy": "Robusto",
    "Independent": "Indipendente",
    "Inquisitive": "Curioso",
    "Intelligent": "Intelligente",
    "Laid-back": "Rilassato",
    "Loving": "Amorevole",
    "Loyal": "Leale",
    "Outgoing": "Estroverso",
    "Patient": "Paziente",
    "Persistent": "Persistente",
    "Playful": "Giocoso",
    "Plucky": "Spavaldo",
    "Protective": "Protettivo",
    "Quiet": "Quieto",
    "Reserved": "Riservato",
    "Self-important": "Pieno di sé",
    "Sensitive": "Sensibile",
    "Smart": "Sveglio",
    "Sociable": "Socievole",
    "Social": "Sociale",
    "Spirited": "Vivace",
    "Strong-willed": "Volitivo",
    "Stubborn": "Testardo",
    "Trainable": "Addestrabile",
}

CATEGORY_DESC_IT = {
    "Breeds outside FCI classification": "Questa categoria comprende razze canine non riconosciute dalla Fédération Cynologique Internationale (FCI), ma registrate ufficialmente o ampiamente accettate da altri club cinofili come AKC o UKC. Queste razze hanno spesso origini e storie uniche e sono apprezzate in tutto il mondo per le loro qualità specifiche.",
    "Sheepdogs and Cattledogs (except Swiss Cattledogs)": "I cani da pastore e bovari sono razze da lavoro intelligenti, sviluppate per gestire il bestiame con precisione e controllo. Sono noti per i forti istinti, la reattività e la capacità di lavorare a stretto contatto con l'uomo. Questi cani richiedono una guida coerente e buona attività.",
    "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs": "Questo gruppo comprende razze potenti e versatili con forti istinti di guardia e una presenza sicura. Molti di questi cani sono stati allevati originariamente per la protezione, il lavoro agricolo e la compagnia. Tendono a essere leali, stabili e devoti alla famiglia.",
    "Terriers": "I Terrier sono vivaci, determinati e pieni di personalità. Allevati originariamente per cacciare e tenere sotto controllo i parassiti, sono noti per il coraggio e la tenacia. Questi cani sono spesso energici e curiosi, con una forte indipendenza e grande spirito.",
    "Dachshunds": "I Bassotti sono un gruppo distinto, noto per il corpo allungato e la forte tradizione da caccia. Allevati originariamente per tracciare e stanare gli animali scavatori, sono coraggiosi e determinati. Nonostante la taglia, mostrano spesso una sorprendente fiducia in sé.",
    "Spitz and primitive types": "Gli Spitz e i cani di tipo primitivo sono tra i gruppi più antichi e naturali di razze. Hanno spesso mantelli folti, orecchie erette e coda arrotolata. Molte di queste razze conservano istinti forti e un pensiero indipendente. Sono energici, fedeli e richiedono una guida chiara e costante.",
    "Scent hounds and related breeds": "I segugi da fiuto sono guidati dal potente senso dell'olfatto e dalla naturale capacità di seguire tracce. Sono stati sviluppati per seguire piste su lunghe distanze con concentrazione e resistenza. Questi cani sono spesso pazienti, determinati e indipendenti.",
    "Pointing Dogs": "I cani da ferma sono abili compagni di caccia, noti per precisione e concentrazione. Sono addestrati a individuare la selvaggina e a segnalarne la presenza con una postura caratteristica. Queste razze sono in genere energiche, reattive e desiderose di lavorare.",
    "Retrievers - Flushing Dogs - Water Dogs": "Questo gruppo comprende cani sportivi amichevoli e versatili con un forte istinto di riporto e assistenza. Sono spesso noti per la bocca morbida e la natura cooperativa. Molte razze qui sono molto socievoli e amano lavorare a stretto contatto con l'uomo.",
    "Companion and Toy Dogs": "I cani da compagnia e da salotto sono allevati soprattutto per la compagnia umana e il legame emotivo. Sono spesso di piccola taglia ma ricchi di personalità e fascino. Molte razze di questo gruppo sono affettuose, socievoli e attente al proprietario.",
    "Sighthounds": "I Levrieri sono cani eleganti e atletici, allevati per la velocità e il tracciamento visivo. Si affidano alla vista, più che all'olfatto, per inseguire bersagli in movimento. Queste razze sono spesso calme e gentili in casa, nonostante la loro incredibile velocità.",
}

CATEGORY_DESC_KEYS = list(CATEGORY_DESC_IT)


class Command(BaseCommand):
    help = "Fill Italian names and short traits for dogs, categories, sections and vocabularies."

    def handle(self, *args, **options):
        with translation.override("it"):
            dog_updated = 0
            for dog in Dogs.objects.all():
                it = DOGS_TITLES_IT.get(dog.title)
                if it and not dog.title_it:
                    dog.title_it = it
                    dog.save(update_fields=["title_it"])
                    dog_updated += 1
            self.stdout.write(f"Dogs.title_it filled: {dog_updated}")

            for model, fname, mapping in (
                (Category, "name_it", CATEGORY_NAMES_IT),
                (Section, "name_it", SECTION_NAMES_IT),
                (CoatType, "name_it", COATTYPE_IT),
                (CoatLength, "name_it", COATLEN_IT),
                (Temperament, "name_it", TEMPERAMENT_IT),
            ):
                updated = 0
                for obj in model.objects.all():
                    it = mapping.get(obj.name)
                    if it and not getattr(obj, fname):
                        setattr(obj, fname, it)
                        obj.save(update_fields=[fname])
                        updated += 1
                self.stdout.write(f"{model.__name__}.{fname} filled: {updated}")

            # category descriptions (keyed by EN name; cat.name may already return Italian)
            rev_names = {v: k for k, v in CATEGORY_NAMES_IT.items()}
            desc_updated = 0
            for cat in Category.objects.all():
                en_key = rev_names.get(cat.name) or cat.name
                it = CATEGORY_DESC_IT.get(en_key)
                if it and not cat.desc_it:
                    cat.desc_it = it
                    cat.save(update_fields=["desc_it"])
                    desc_updated += 1
            self.stdout.write(f"Category.desc_it filled: {desc_updated}")

            short_updates = {
                "varieties_it": VARIETIES_IT,
                "country_it": COUNTRY_IT,
                "colors_it": COLORS_IT,
            }
            for fname, mapping in short_updates.items():
                count = 0
                for dog in Dogs.objects.all():
                    en = getattr(dog, fname[:-3])
                    it = mapping.get(en)
                    if it and not getattr(dog, fname):
                        setattr(dog, fname, it)
                        dog.save(update_fields=[fname])
                        count += 1
                self.stdout.write(f"Dogs.{fname} filled: {count}")
