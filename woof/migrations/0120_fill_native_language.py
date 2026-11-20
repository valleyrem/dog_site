from django.db import migrations

# language -> (ru, de, it, es, sr_latn)
LANGUAGES = {
    "English": ("английский", "Englisch", "inglese", "inglés", "engleski"),
    "German": ("немецкий", "Deutsch", "tedesco", "alemán", "nemački"),
    "French": ("французский", "Französisch", "francese", "francés", "francuski"),
    "Italian": ("итальянский", "Italienisch", "italiano", "italiano", "italijanski"),
    "Spanish": ("испанский", "Spanisch", "spagnolo", "español", "španski"),
    "Portuguese": (
        "португальский",
        "Portugiesisch",
        "portoghese",
        "portugués",
        "portugalski",
    ),
    "Dutch": ("нидерландский", "Niederländisch", "olandese", "neerlandés", "holandski"),
    "Frisian": ("фризский", "Friesisch", "frisone", "frisón", "frizijski"),
    "Hungarian": ("венгерский", "Ungarisch", "ungherese", "húngaro", "mađarski"),
    "Slovak": ("словацкий", "Slowakisch", "slovacco", "eslovaco", "slovački"),
    "Croatian": ("хорватский", "Kroatisch", "croato", "croata", "hrvatski"),
    "Swedish": ("шведский", "Schwedisch", "svedese", "sueco", "švedski"),
    "Norwegian": ("норвежский", "Norwegisch", "norvegese", "noruego", "norveški"),
    "Russian": ("русский", "Russisch", "russo", "ruso", "ruski"),
    "Turkish": ("турецкий", "Türkisch", "turco", "turco", "turski"),
    "Japanese": ("японский", "Japanisch", "giapponese", "japonés", "japanski"),
    "Chinese": ("китайский", "Chinesisch", "cinese", "chino", "kineski"),
    "Tibetan": ("тибетский", "Tibetisch", "tibetano", "tibetano", "tibetanski"),
    "Afrikaans": ("африкаанс", "Afrikaans", "afrikaans", "afrikáans", "afrikans"),
}

# language -> breeds whose native name is written in it. Left empty on purpose
# where the origin of the spelling is unclear: Saluki, Azawakh, Sloughi, Xoloitzcuintli.
DOGS = {
    "English": [
        "Afghan Hound",
        "Nova Scotia Duck Tolling Retriever",
        "Pekingese",
        "American Eskimo Dog",
        "Airedale Terrier",
        "Basset Hound",
        "Beagle",
        "Bedlington Terrier",
        "Border Collie",
        "Border Terrier",
        "Bulldog",
        "Bull Terrier",
        "Cavalier King Charles Spaniel",
        "Collie Rough",
        "English Pointer",
        "English Setter",
        "Golden Retriever",
        "Gordon Setter",
        "Greyhound",
        "Jack Russell Terrier",
        "Labrador Retriever",
        "Old English Sheepdog",
        "Pembroke Welsh Corgi",
        "Scottish Terrier",
        "Welsh Terrier",
        "Whippet",
        "Wire Fox Terrier",
        "Yorkshire Terrier",
        "Irish Red Setter",
        "Irish Wolfhound",
        "Rhodesian Ridgeback",
        "Tibetan Terrier",
        "Alaskan Malamute",
        "American Bulldog",
        "American Cocker Spaniel",
        "American Pit Bull Terrier",
        "American Staffordshire Terrier",
        "Australian Shepherd",
        "Bluetick Coonhound",
        "Boykin Spaniel",
        "Catahoula Leopard Dog",
        "Chesapeake Bay Retriever",
        "Rat Terrier",
        "Siberian Husky",
        "Treeing Walker Coonhound",
    ],
    "German": [
        "Boxer",
        "Dachshund",
        "Dobermann",
        "German Shepherd Dog",
        "German Shorthaired Pointer",
        "German Spaniel",
        "German Spitz",
        "Great Dane",
        "Hovawart",
        "Keeshond (Wolfspitz)",
        "Kleiner Münsterländer",
        "Large Munsterlander",
        "Miniature Pinscher",
        "Pomeranian",
        "Rottweiler",
        "Weimaraner",
        "Saint Bernard",
        "Pug",
    ],
    "French": [
        "Belgian Shepherd Dog",
        "Bloodhound",
        "Brussels Griffon",
        "Bichon Frise",
        "French Bulldog",
        "Poodle",
    ],
    "Italian": [
        "Bolognese",
        "Italian Cane Corso",
        "Italian Sighthound",
        "Italian Spinone",
        "Romagna Water Dog",
    ],
    "Spanish": ["Chihuahua", "Ibizan Podenco", "Spanish Greyhound"],
    "Portuguese": ["Barbado da Terceira", "Portuguese Podengo", "Portuguese Water Dog"],
    "Dutch": ["Dutch Shepherd Dog", "Nederlandse Kooikerhondje"],
    "Frisian": ["Stabijhoun (Stabyhoun)", "Wetterhoun"],
    "Hungarian": [
        "Hungarian Short-Haired Pointer (Vizsla)",
        "Hungarian Wire-Haired Pointer",
        "Puli",
    ],
    "Slovak": ["Czechoslovakian Wolfdog", "Slovakian Hound"],
    "Croatian": ["Dalmatian"],
    "Swedish": ["Drever"],
    "Norwegian": ["Norwegian Elkhound Grey"],
    "Russian": ["Samoyed", "Borzoi (Russian Hunting Sighthound)", "Yakutian Laika"],
    "Turkish": ["Kangal Shepherd Dog"],
    "Japanese": ["Akita", "Kai"],
    "Chinese": ["Shar Pei", "Shih Tzu"],
    "Tibetan": ["Tibetan Mastiff"],
    "Afrikaans": ["Boerboel"],
}


def forwards(apps, schema_editor):
    NativeLanguage = apps.get_model("woof", "NativeLanguage")
    Dogs = apps.get_model("woof", "Dogs")
    for name, (ru, de, it, es, sr) in LANGUAGES.items():
        lang, _ = NativeLanguage.objects.get_or_create(name=name)
        lang.name_en = name
        lang.name_ru, lang.name_de, lang.name_it = ru, de, it
        lang.name_es, lang.name_sr_latn = es, sr
        lang.save()
    for name, titles in DOGS.items():
        lang = NativeLanguage.objects.get(name=name)
        Dogs.objects.filter(title__in=titles).update(native_language=lang)


class Migration(migrations.Migration):
    dependencies = [("woof", "0119_native_language")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
