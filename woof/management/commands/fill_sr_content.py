"""Fill Serbian (Latin) names and short traits for dogs, categories,
sections and vocabularies. Idempotent: only fills empty *_sr_latn fields.

Mirrors fill_de_content / fill_it_content; keys are exact English values
currently stored in the database.
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

DOGS_TITLES_SR = {
    "Dobermann": "Doberman",
    "Rottweiler": "Rotvajler",
    "Weimaraner": "Vajmarski ptičar",
    "Dalmatian": "Dalmatinac",
    "Afghan Hound": "Avganistanski hrt",
    "Collie Rough": "Kolija (dugodlaka)",
    "Scottish Terrier": "Škotski terijer",
    "Shih Tzu": "Ši cu",
    "Cavalier King Charles Spaniel": "Kavalir King Čarls španijel",
    "Pomeranian": "Pomeranski špic",
    "Siberian Husky": "Sibirski haski",
    "Alaskan Malamute": "Aljaški malamut",
    "Samoyed": "Samojed",
    "Old English Sheepdog": "Staroengleski ovčar",
    "Bloodhound": "Krvavi gonič",
    "Pembroke Welsh Corgi": "Velški korgi pembruk",
    "Bull Terrier": "Bul terijer",
    "Labrador Retriever": "Labrador retriver",
    "Akita": "Akita",
    "Australian Shepherd": "Australijski ovčar",
    "Golden Retriever": "Zlatni retriver",
    "Italian Sighthound": "Italijanski hrt",
    "English Setter": "Engleski seter",
    "Basset Hound": "Baset hound",
    "Norwegian Elkhound Grey": "Norveški elkhund (sivi)",
    "Pug": "Mops",
    "Kai": "Kai",
    "Drever": "Drever",
    "German Shorthaired Pointer": "Nemački kratkodlaki ptičar",
    "Wire Fox Terrier": "Žičanodlaki foks terijer",
    "Black and Tan Coonhound": "Black and Tan Coonhound",
    "Treeing Walker Coonhound": "Treeing Walker Coonhound",
    "Whippet": "Vipet",
    "Borzoi": "Borzoj",
    "Anatolian Shepherd Dog": "Anatolski ovčar",
    "Irish Wolfhound": "Irski vučji hrt",
    "Azawakh": "Azavak",
    "Italian Cane Corso": "Kane korso",
    "Great Dane": "Nemačka doga",
    "Yorkshire Terrier": "Jorkširski terijer",
    "Saint Bernard": "Sveti Bernard",
    "French Bulldog": "Francuski buldog",
    "Bichon Frise": "Bišon frize",
    "Bolognese": "Bolonjez",
    "Bulldog": "Buldog",
    "Portuguese Podengo": "Portugalski podengo",
    "German Spitz": "Nemački špic",
    "Yakutian Laika": "Jakutska lajka",
    "Kleiner Münsterländer": "Mali minsterlander",
    "German Shepherd Dog": "Nemački ovčar",
    "Puli": "Puli",
    "Border Collie": "Border koli",
    "Italian Spinone": "Italijanski spinone",
    "Nederlandse Kooikerhondje": "Holandski kooikerhondje",
    "Romagna Water Dog": "Lagoto romanjolo",
    "American Cocker Spaniel": "Američki koker španijel",
    "Pekingese": "Pekinezer",
    "Brussels Griffon": "Briselski grifon",
    "Catahoula Leopard Dog": "Katahula leopard pas",
    "Czechoslovakian Wolfdog": "Čehoslovački vučjak",
    "Dutch Shepherd Dog": "Holandski ovčar",
    "American Eskimo Dog": "Američki eskimski pas",
    "Xoloitzcuintli": "Ksolockuintli",
    "Shar Pei": "Šar pei",
    "Poodle": "Pudlica",
    "Border Terrier": "Border terijer",
    "American Staffordshire Terrier": "Američki stafordšir terijer",
    "Rat Terrier": "Pacovski terijer",
    "Bedlington Terrier": "Bedlington terijer",
    "Hovawart": "Hovavart",
    "Boxer": "Bokser",
    "Barbado da Terceira": "Barbado da Terceira",
    "Airedale Terrier": "Erdel terijer",
    "Dachshund": "Jazavičar",
    "Keeshond (Wolfspitz)": "Kešond (vučji špic)",
    "Nova Scotia Duck Tolling Retriever": "Novoškotski retriver za patke",
    "Sloughi": "Slugi",
}

CATEGORY_NAMES_SR = {
    "Sheepdogs and Cattledogs (except Swiss Cattledogs)": "Ovčarski i stočarski psi (osim švajcarskih stočarskih pasa)",
    "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs": "Pinčer i šnaucer — molosoidni, švajcarski planinski i stočarski psi",
    "Terriers": "Terijeri",
    "Dachshunds": "Jazavičari",
    "Spitz and primitive types": "Špic i primitivni tipovi",
    "Scent hounds and related breeds": "Goniči po mirisu i srodne rase",
    "Pointing Dogs": "Ptičari",
    "Retrievers - Flushing Dogs - Water Dogs": "Retriveri — španijeli i vodeni psi",
    "Companion and Toy Dogs": "Psi za društvo i patuljasti psi",
    "Sighthounds": "Hrtovi",
    "Breeds outside FCI classification": "Rase izvan FCI klasifikacije",
}

CATEGORY_DESC_SR = {
    "Breeds outside FCI classification": "Ova kategorija obuhvata rase pasa koje ne priznaje Fédération Cynologique Internationale (FCI), ali su zvanično registrovane ili široko prihvaćene od strane drugih kinoloških saveza poput AKC ili UKC. Ove rase često imaju jedinstveno poreklo i istoriju i cenjene su širom sveta zbog svojih specifičnih kvaliteta.",
    "Sheepdogs and Cattledogs (except Swiss Cattledogs)": "Ovčarski i stočarski psi su inteligentne radne rase razvijene za upravljanje stokom sa preciznošću i kontrolom. Poznati su po snažnim instinktima, oštroj reakciji i sposobnosti da rade u bliskoj saradnji sa čovekom. Ovim psima je potrebno dosledno vođenje i dovoljno aktivnosti.",
    "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs": "Ova grupa obuhvata moćne i svestrane rase sa snažnim zaštitničkim instinktima i samouverenim prisustvom. Mnogi od ovih pasa su prvobitno uzgajani za zaštitu, poljoprivredne poslove i društvo. Skloni su odanosti, stabilnosti i posvećenosti porodici.",
    "Terriers": "Terijeri su živahni, odlučni i puni ličnosti. Prvobitno uzgajani za lov i suzbijanje štetočina, poznati su po hrabrosti i istrajnosti. Ovi psi su često energični i radoznali, sa snažnom nezavisnošću i velikim duhom.",
    "Dachshunds": "Jazavičari su posebna grupa poznata po izduženom telu i snažnoj lovačkoj tradiciji. Prvobitno uzgajani za praćenje i izgon životinja iz jazbina, hrabri su i odlučni. Uprkos svojoj veličini, često pokazuju iznenađujuće samopouzdanje.",
    "Spitz and primitive types": "Špic rase i psi primitivnog tipa spadaju među najstarije i najprirodnije grupe rasa. Često imaju gustu dlaku, uspravne uši i zavijen rep. Mnoge od ovih rasa zadržale su snažne instinkte i nezavisno razmišljanje. Energični su, odani i zahtevaju jasno i dosledno vođenje.",
    "Scent hounds and related breeds": "Goniči po mirisu vode se snažnim čulom mirisa i prirodnom sposobnošću praćenja tragova. Razvijeni su da prate tragove na velikim udaljenostima sa koncentracijom i izdržljivošću. Ovi psi su često strpljivi, odlučni i nezavisni.",
    "Pointing Dogs": "Ptičari su vešti lovački pratioci, poznati po preciznosti i koncentraciji. Obučeni su da pronađu divljač i ukažu na njeno prisustvo karakterističnim stavom. Ove rase su obično energične, prisebne i željne rada.",
    "Retrievers - Flushing Dogs - Water Dogs": "Ova grupa obuhvata druželjubive i svestrane lovne pse sa snažnim instinktom donošenja i pomaganja. Često su poznati po mekom ustima i saradljivoj prirodi. Mnoge rase ovde su veoma društvene i vole rad u bliskoj saradnji sa čovekom.",
    "Companion and Toy Dogs": "Psi za društvo i patuljasti psi uzgajani su pre svega radi ljudskog društva i emotivne povezanosti. Često su male veličine, ali bogati ličnošću i šarmom. Mnoge rase iz ove grupe su privržene, druželjubive i pažljive prema vlasniku.",
    "Sighthounds": "Hrtovi su elegantni i atletski psi uzgajani za brzinu i vizuelno praćenje. Oslanjaju se na vid, više nego na miris, kada jure pokretne mete. Ove rase su često smirene i nežne kod kuće, uprkos neverovatnoj brzini.",
}

SECTION_NAMES_SR = {
    "Asian Spitz and related breeds": "Azijski špic i srodne rase",
    "Bichons and related breeds": "Bišoni i srodne rase",
    "British and Irish Pointers and Setters": "Britanski i irski ptičari i seteri",
    "Bull type Terriers": "Terijeri bul tipa",
    "Cattledogs (except Swiss Cattledogs)": "Stočarski psi (osim švajcarskih stočarskih pasa)",
    "Chihuahueno": "Čivava",
    "Continental Pointing Dogs": "Kontinentalni ptičari",
    "Continental Toy Spaniel and others": "Kontinentalni patuljasti španijeli i ostali",
    "English Toy Spaniels": "Engleski patuljasti španijeli",
    "European Spitz": "Evropski špic",
    "Flushing Dogs": "Španijeli",
    "Hairless Dogs": "Psi bez dlake",
    "Japan Chin and Pekingese": "Japanski čin i pekinezer",
    "Kromfohrländer": "Kromforlender",
    "Large and medium sized Terriers": "Veliki i srednji terijeri",
    "Leash (scent) Hounds": "Goniči na povocu (po mirisu)",
    "Long-haired or fringed Sighthounds": "Dugodlaki ili resasti hrtovi",
    "Molossian type": "Molosoidni tip",
    "Nordic Hunting Dogs": "Nordijski lovački psi",
    "Nordic Sledge Dogs": "Nordijski psi za saonice",
    "Nordic Watchdogs and Herders": "Nordijski psi čuvari i pastiri",
    "Pinscher and Schnauzer type": "Pinčeri i šnauceri",
    "Poodle": "Pudla",
    "Primitive type": "Primitivni tip",
    "Primitive type - Hunting Dogs": "Primitivni tip — lovački psi",
    "Recognized by Other Kennel Clubs": "Priznate od strane drugih kinoloških saveza",
    "Related breeds": "Srodne rase",
    "Retrievers": "Retriveri",
    "Rough-haired Sighthounds": "Grubodlaki hrtovi",
    "Scent hounds": "Goniči po mirisu",
    "Sheepdogs": "Ovčarski psi",
    "Short-haired Sighthounds": "Kratkodlaki hrtovi",
    "Single breed group (no sections)": "Grupa sa jednom rasom (bez sekcija)",
    "Small Belgian Dogs": "Mali belgijski psi",
    "Small Molossian type Dogs": "Mali psi molosoidnog tipa",
    "Small sized Terriers": "Mali terijeri",
    "Swiss Mountain and Cattledogs": "Švajcarski planinski i stočarski psi",
    "Tibetan breeds": "Tibetanske rase",
    "Toy Terriers": "Patuljasti terijeri",
    "Unrecognized but Documented Breeds": "Nepriznate, ali dokumentovane rase",
    "Water Dogs": "Vodeni psi",
}

COATTYPE_SR = {
    "Curly": "Kudrava",
    "Wavy": "Talasaasta",
    "Corded": "Užadasta",
    "Hairless": "Bez dlake",
    "Smooth": "Glatka",
    "Double coat": "Dvostruka dlaka",
    "Silky": "Svilenkasta",
    "Rough": "Gruba",
    "Wiry": "Žičana",
}

COATLEN_SR = {
    "Short": "Kratka",
    "Medium": "Srednja",
    "Long": "Duga",
}

TEMPERAMENT_SR = {
    "Patient": "Strpljiv",
    "Laid-back": "Opušten",
    "Spirited": "Živahan",
    "Easygoing": "Ležeran",
    "Devoted": "Odan",
    "Eager": "Revnostan",
    "Focused": "Usredsređen",
    "Game": "Spreman",
    "Plucky": "Smel",
    "Quiet": "Tih",
    "Self-important": "Uobražen",
    "Stubborn": "Tvrdoglav",
    "Social": "Druželjubiv",
    "Active": "Aktivan",
    "Playful": "Razigran",
    "Brave": "Hrabar",
    "Friendly": "Prijazan",
    "Intelligent": "Inteligentan",
    "Alert": "Budan",
    "Inquisitive": "Radoznao",
    "Happy": "Srećan",
    "Loving": "Pun ljubavi",
    "Determined": "Odlučan",
    "Confident": "Samouveren",
    "Good-natured": "Dobrodušan",
    "Charming": "Šarmantan",
    "Courageous": "Odvažan",
    "Protective": "Zaštitnički",
    "Loyal": "Veran",
    "Calm": "Smiren",
    "Outgoing": "Društven",
    "Affectionate": "Privržen",
    "Agile": "Okretan",
    "Strong-willed": "Snažne volje",
    "Gentle": "Nežan",
    "Cheerful": "Vedar",
    "Energetic": "Energičan",
    "Reserved": "Rezervisan",
    "Fast": "Brz",
    "Hardworking": "Marljiv",
    "Fearless": "Neustrašiv",
    "Hardy": "Otporan",
    "Aloof": "Povučen",
    "Persistent": "Ustrajan",
    "Independent": "Nezavisan",
    "Even-tempered": "Staložen",
    "Adaptable": "Prilagodljiv",
    "Smart": "Pametan",
    "Dignified": "Dostojanstven",
    "Sensitive": "Osetljiv",
    "Sociable": "Komunikativan",
    "Trainable": "Dresabilan",
}

VARIETIES_SR = {
    "Color variations": "Varijacije boja",
    "It's a variety of German Spitz": "To je varijetet nemačkog špica",
    "No variations": "Nema varijeteta",
    "Rabbit, Miniature, Standard": "Zečji, patuljasti, standardni",
    "Size variations": "Varijacije po veličini",
    "Small, Medium-sized, Large": "Mali, srednje veličine, veliki",
    "Standard, Medium, Miniature, Toy": "Standardni, srednji, patuljasti, toy",
    "Standart, Intermediate, Miniature": "Standardni, srednji, patuljasti",
    "Toy, Miniature, Standard": "Toy, patuljasti, standardni",
    "described in «About the Breed»": "opisano u „O rasi“",
}

COUNTRY_SR = {
    "Afganistan": "Avganistan",
    "Belgium": "Belgija",
    "Belgium, France": "Belgija, Francuska",
    "Canada": "Kanada",
    "China": "Kina",
    "Croatia": "Hrvatska",
    "Czechoslovakia": "Čehoslovačka",
    "France": "Francuska",
    "Germany": "Nemačka",
    "Great Britain": "Velika Britanija",
    "Hungary": "Mađarska",
    "Irleand": "Irska",
    "Italy": "Italija",
    "Japan": "Japan",
    "Mali": "Mali",
    "Mexico": "Meksiko",
    "Morocco": "Maroko",
    "Northern Russia": "Severna Rusija",
    "Northern Russia, Siberia": "Severna Rusija, Sibir",
    "Norway": "Norveška",
    "Portugal": "Portugal",
    "Russian Federation": "Ruska Federacija",
    "Siberia": "Sibir",
    "Sweden": "Švedska",
    "Switzerland": "Švajcarska",
    "The Netherlands": "Holandija",
    "Tibet (China)": "Tibet (Kina)",
    "Turkey": "Turska",
    "USA": "SAD",
}

COLORS_SR = {
    "Black & Rust, Black & Mahogany, Black & Tan": "Crna i riđa, crna i mahagoni, crna i tan",
    "Black & Rust, Red & Rust, Blue & Rust, Fawn & Rust, White": "Crna i riđa, crvena i riđa, plava i riđa, žutosmeđa i riđa, bela",
    "Black & Tan, Liver & Tan, Red": "Crna i tan, đigerica i tan, crvena",
    "Black & White, Gray & White, Red & White, Agouti, All-White": "Crna i bela, siva i bela, crvena i bela, aguti, potpuno bela",
    "Black & white, red & white, tricolor, blue merle, sable, and other variations": "Crna i bela, crvena i bela, trobojna, plavi merle, sable i druge varijacije",
    "Black and tan (signature coat pattern with rich tan markings over a deep black base)": "Crna i tan (prepoznatljiva šara dlake sa bogatim tan oznakama na dubokoj crnoj osnovi)",
    "Black and tan, black and red, sable, solid black, black and cream, black and silver": "Crna i tan, crna i crvena, sable, jednobojna crna, crna i krem, crna i srebrna",
    "Black and tan, grizzle and tan": "Crna i tan, prosedo siva i tan",
    "Black, Blue, Cream, Fawn, Red, Brindle, White, Gold, Grey": "Crna, plava, krem, žutosmeđa, crvena, tigrasta, bela, zlatna, siva",
    "Black, Brindle, Wheaten, Silver Brindle": "Crna, tigrasta, žitna, srebrno tigrasta",
    "Black, Gray, Fawn, Red, Brindle": "Crna, siva, žutosmeđa, crvena, tigrasta",
    "Black, Gray, White": "Crna, siva, bela",
    "Black, White, Gold, Brindle, Liver, Silver, Mixed": "Crna, bela, zlatna, tigrasta, đigerica, srebrna, mešovita",
    "Black, Yellow, Chocolate": "Crna, žuta, čokoladna",
    "Black, black and gold, blonde": "Crna, crna i zlatna, svetla",
    "Black, blue, fawn, red, brindle, white, solid or patched combinations": "Crna, plava, žutosmeđa, crvena, tigrasta, bela, jednobojne ili šarane kombinacije",
    "Black, gray, slate, red, bronze, liver, solid or spotted": "Crna, siva, škriljasta, crvena, bronzana, đigerica, jednobojna ili pegava",
    "Black, red, buff, brown, parti-color (white with patches), roan variations": "Crna, crvena, žućkasta, smeđa, šarena (bela sa šarama), runaste varijacije",
    "Black, white, brown, apricot, red, silver, cream, gray, blue, parti-color": "Crna, bela, smeđa, kajsijasta, crvena, srebrna, krem, siva, plava, šarena",
    "Black, white, cream, brown, orange, sable": "Crna, bela, krem, smeđa, narandžasta, sable",
    "Black, white, tan, chocolate, blue, lemon, red; bicolor and tricolor patterns": "Crna, bela, tan, čokoladna, plava, limun, crvena; dvobojne i trobojne šare",
    "Blenheim, Tricolor, Black & Tan, Ruby": "Blenhajm, trobojna, crna i tan, rubin",
    "Blue Belton, Lemon Belton, Orange Belton, Tricolor": "Plavi belton, limun belton, narandžasti belton, trobojna",
    "Blue Merle, Red Merle, Black, Red, White Markings": "Plavi merle, crveni merle, crna, crvena, bele oznake",
    "Blue, liver, sandy, blue & tan, liver & tan": "Plava, đigerica, peščana, plava i tan, đigerica i tan",
    "Brindle (gold or silver), sometimes with black patterning": "Tigrasta (zlatna ili srebrna), ponekad sa crnim šarama",
    "Brindle, Fawn, White, Pied, Cream": "Tigrasta, žutosmeđa, bela, šarena, krem",
    "Brown & white, brown roan": "Smeđa i bela, smeđa runasta",
    "Cream, sand, red fawn, mahogany, brindle, black mask, black ears, with or without small white markings": "Krem, peščana, crveno žutosmeđa, mahagoni, tigrasta, crna maska, crne uši, sa ili bez malih belih oznaka",
    "Fawn, Black, Apricot, Silver Fawn": "Žutosmeđa, crna, kajsijasta, srebrno žutosmeđa",
    "Fawn, Blue, Black, Red, White, Cream": "Žutosmeđa, plava, crna, crvena, bela, krem",
    "Fawn, Brindle, Black, Blue, Red, White, Mixed": "Žutosmeđa, tigrasta, crna, plava, crvena, bela, mešovita",
    "Fawn, Brindle, Blue, Black, Harlequin, Mantle": "Žutosmeđa, tigrasta, plava, crna, arlekin, mantl",
    "Fawn, Brindle, Red, Black, Blue": "Žutosmeđa, tigrasta, crvena, crna, plava",
    "Fawn, Brindle, White, Piebald, Red, Fallow": "Žutosmeđa, tigrasta, bela, pegava, crvena, svetlosmeđa",
    "Fawn, White, Brindle, Sable, Masked": "Žutosmeđa, bela, tigrasta, sable, sa maskom",
    "Fawn, brindle, white markings": "Žutosmeđa, tigrasta, bele oznake",
    "Gold, red, sable, cream, black, black & tan, parti-color": "Zlatna, crvena, sable, krem, crna, crna i tan, šarena",
    "Golden shades (light to dark)": "Zlatne nijanse (od svetle do tamne)",
    "Gray & White, Blue & White, Blue Merle, Grizzle & White": "Siva i bela, plava i bela, plavi merle, prosedo siva i bela",
    "Gray, Black-tipped": "Siva, sa crnim vrhovima",
    "Gray, Brindle, Red, Black, Fawn, White": "Siva, tigrasta, crvena, crna, žutosmeđa, bela",
    "Grey with black shading, cream, variations of wolf-grey": "Siva sa crnim senčenjem, krem, varijacije vučje sive",
    "Light gray, Black, Sable, Red, Seal, White": "Svetlo siva, crna, sable, crvena, seal, bela",
    "Liver, Liver & White, Roan": "Đigerica, đigerica i bela, runasta",
    "Merle, blue merle, red merle, black, brindle, solid colors with patterns": "Merle, plavi merle, crveni merle, crna, tigrasta, jednobojne boje sa šarama",
    "Off-white, white with orange or brown patches, brown, orange, roan": "Skoro bela, bela sa narandžastim ili smeđim šarama, smeđa, narandžasta, runasta",
    "Orange, Black, White, Cream, Blue, Brown, Sable, Chocolate Merle, Brindle, Beaver": "Narandžasta, crna, bela, krem, plava, smeđa, sable, čokoladni merle, tigrasta, dabrova",
    "Red & White, Brindle & White, Mostly White": "Crvena i bela, tigrasta i bela, uglavnom bela",
    "Red, Sable, Fawn, Black & Tan, Tricolor": "Crvena, sable, žutosmeđa, crna i tan, trobojna",
    "Red, black & tan, chocolate & tan, cream, dapple, brindle, piebald": "Crvena, crna i tan, čokoladna i tan, krem, mermerasta, tigrasta, pegava",
    "Red, black, black & tan, belge (reddish-brown with black mask), solid black": "Crvena, crna, crna i tan, belge (crvenkastosmeđa sa crnom maskom), jednobojna crna",
    "Red, grizzle and tan, blue and tan, wheaten": "Crvena, prosedo siva i tan, plava i tan, žitna",
    "Sable & White, Tricolor, Blue Merle, White, Blue Merle & White": "Sable i bela, trobojna, plavi merle, bela, plavi merle i bela",
    "Shades of red and orange with white markings often present on chest, feet, tail tip, or face": "Nijanse crvene i narandžaste sa belim oznakama koje se često nalaze na grudima, šapama, vrhu repa ili njušci",
    "Silver gray, Blue, Gray": "Srebrno siva, plava, siva",
    "Solid colors: cream, red, fawn, black, blue, chocolate, sable": "Jednobojne: krem, crvena, žutosmeđa, crna, plava, čokoladna, sable",
    "Steel blue & Tan": "Čelično plava i tan",
    "Tiger brindle (brown/black stripes)": "Tigrasta (smeđe/crne pruge)",
    "Tri-color, Bi-color, Lemon & White, Red & White, Tan & White": "Trobojna, dvobojna, limun i bela, crvena i bela, tan i bela",
    "Tricolor (Black, White, Tan)": "Trobojna (crna, bela, tan)",
    "White": "Bela",
    "White (sometimes with apricot, cream, or buff shadings)": "Bela (ponekad sa nijansama kajsije, krema ili žućkaste)",
    "White or white with cream (biscuit)": "Bela ili bela sa krem (biskvit)",
    "White with black or brown markings": "Bela sa crnim ili smeđim oznakama",
    "White with black or liver spots, White & Orange, White & Lemon, White Black & Tan": "Bela sa crnim ili đigerica pegama, bela i narandžasta, bela i limun, bela crna i tan",
    "White with orange-red patches": "Bela sa narandžasto-crvenim šarama",
    "White, Black, Gold, Brindle, Various combinations": "Bela, crna, zlatna, tigrasta, razne kombinacije",
    "White, Brindle, Fawn, Black, Red": "Bela, tigrasta, žutosmeđa, crna, crvena",
    "White, Cream, Biscuit": "Bela, krem, biskvit",
    "White, Red, Brindle, Fawn, Sesame, Piebald": "Bela, crvena, tigrasta, žutosmeđa, sezam, pegava",
    "White, black, brown, gray, piebald / tricolor combinations": "Bela, crna, smeđa, siva, pegave / trobojne kombinacije",
    "White, white & orange, orange roan, white & brown, brown roan": "Bela, bela i narandžasta, narandžasta runasta, bela i smeđa, smeđa runasta",
    "Yellow, Fawn, Black & Tan": "Žuta, žutosmeđa, crna i tan",
    "Yellow, Fawn, Chestnut, Gray, Gold, Red, Orange and mixed": "Žuta, žutosmeđa, kestenjasta, siva, zlatna, crvena, narandžasta i mešovita",
    "Yellow, gray, black, fawn, wolf-gray, often with white markings": "Žuta, siva, crna, žutosmeđa, vučje siva, često sa belim oznakama",
    "Yellow-gray, silver-gray, dark gray, with light mask": "Žućkasto siva, srebrno siva, tamno siva, sa svetlom maskom",
}


class Command(BaseCommand):
    help = "Fill Serbian (Latin) names and short traits for dogs, categories, sections and vocabularies."

    def handle(self, *args, **options):
        with translation.override("sr-latn"):
            dog_updated = 0
            for dog in Dogs.objects.all():
                sr = DOGS_TITLES_SR.get(dog.title)
                if sr and not dog.title_sr_latn:
                    dog.title_sr_latn = sr
                    dog.save(update_fields=["title_sr_latn"])
                    dog_updated += 1
            self.stdout.write(f"Dogs.title_sr_latn filled: {dog_updated}")

            for model, fname, mapping in (
                (Category, "name_sr_latn", CATEGORY_NAMES_SR),
                (Section, "name_sr_latn", SECTION_NAMES_SR),
                (CoatType, "name_sr_latn", COATTYPE_SR),
                (CoatLength, "name_sr_latn", COATLEN_SR),
                (Temperament, "name_sr_latn", TEMPERAMENT_SR),
            ):
                updated = 0
                for obj in model.objects.all():
                    sr = mapping.get(obj.name)
                    if sr and not getattr(obj, fname):
                        setattr(obj, fname, sr)
                        obj.save(update_fields=[fname])
                        updated += 1
                self.stdout.write(f"{model.__name__}.{fname} filled: {updated}")

            # category descriptions (keyed by EN name; cat.name may already return Serbian)
            rev_names = {v: k for k, v in CATEGORY_NAMES_SR.items()}
            desc_updated = 0
            for cat in Category.objects.all():
                en_key = rev_names.get(cat.name) or cat.name
                sr = CATEGORY_DESC_SR.get(en_key)
                if sr and not cat.desc_sr_latn:
                    cat.desc_sr_latn = sr
                    cat.save(update_fields=["desc_sr_latn"])
                    desc_updated += 1
            self.stdout.write(f"Category.desc_sr_latn filled: {desc_updated}")

            short_updates = {
                "varieties_sr_latn": VARIETIES_SR,
                "country_sr_latn": COUNTRY_SR,
                "colors_sr_latn": COLORS_SR,
            }
            for fname, mapping in short_updates.items():
                count = 0
                for dog in Dogs.objects.all():
                    en = getattr(dog, fname[: -len("_sr_latn")])
                    sr = mapping.get(en)
                    if sr and not getattr(dog, fname):
                        setattr(dog, fname, sr)
                        dog.save(update_fields=[fname])
                        count += 1
                self.stdout.write(f"Dogs.{fname} filled: {count}")
