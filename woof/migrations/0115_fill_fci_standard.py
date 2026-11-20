from django.db import migrations

# Official FCI standard numbers (fci.be nomenclature, groups 1-10). Breeds
# outside the FCI, and breeds the FCI does not list, stay empty.
FCI_STANDARD = {
    # group 1
    "Australian Shepherd": 342,
    "Belgian Shepherd Dog": 15,
    "Border Collie": 297,
    "Collie Rough": 156,
    "Czechoslovakian Wolfdog": 332,
    "Dutch Shepherd Dog": 223,
    "German Shepherd Dog": 166,
    "Old English Sheepdog": 16,
    "Pembroke Welsh Corgi": 39,
    "Puli": 55,
    # group 2
    "Boxer": 144,
    "Bulldog": 149,
    "Dobermann": 143,
    "Great Dane": 235,
    "Hovawart": 190,
    "Italian Cane Corso": 343,
    "Miniature Pinscher": 185,
    "Rottweiler": 147,
    "Saint Bernard": 61,
    "Shar Pei": 309,
    "Tibetan Mastiff": 230,
    # group 3
    "Airedale Terrier": 7,
    "American Staffordshire Terrier": 286,
    "Bedlington Terrier": 9,
    "Border Terrier": 10,
    "Bull Terrier": 11,
    "Jack Russell Terrier": 345,
    "Scottish Terrier": 73,
    "Welsh Terrier": 78,
    "Wire Fox Terrier": 169,
    "Yorkshire Terrier": 86,
    # group 4
    "Dachshund": 148,
    # group 5 (Pomeranian and Keeshond are varieties of the German Spitz)
    "Akita": 255,
    "Alaskan Malamute": 243,
    "German Spitz": 97,
    "Ibizan Podenco": 89,
    "Kai": 317,
    "Keeshond (Wolfspitz)": 97,
    "Norwegian Elkhound Grey": 242,
    "Pomeranian": 97,
    "Portuguese Podengo": 94,
    "Samoyed": 212,
    "Siberian Husky": 270,
    "Xoloitzcuintli": 234,
    # group 6
    "Basset Hound": 163,
    "Beagle": 161,
    "Bloodhound": 84,
    "Dalmatian": 153,
    "Drever": 130,
    "Rhodesian Ridgeback": 146,
    "Slovakian Hound": 244,
    # group 7
    "English Pointer": 1,
    "English Setter": 2,
    "German Shorthaired Pointer": 119,
    "Gordon Setter": 6,
    "Hungarian Short-Haired Pointer (Vizsla)": 57,
    "Hungarian Wire-Haired Pointer": 239,
    "Irish Red Setter": 120,
    "Italian Spinone": 165,
    "Kleiner Münsterländer": 102,
    "Large Munsterlander": 118,
    "Stabijhoun (Stabyhoun)": 222,
    "Weimaraner": 99,
    # group 8
    "American Cocker Spaniel": 167,
    "Chesapeake Bay Retriever": 263,
    "German Spaniel": 104,
    "Golden Retriever": 111,
    "Labrador Retriever": 122,
    "Nederlandse Kooikerhondje": 314,
    "Nova Scotia Duck Tolling Retriever": 312,
    "Portuguese Water Dog": 37,
    "Romagna Water Dog": 298,
    "Wetterhoun": 221,
    # group 9
    "Bichon Frise": 215,
    "Bolognese": 196,
    "Brussels Griffon": 80,
    "Cavalier King Charles Spaniel": 136,
    "Chihuahua": 218,
    "French Bulldog": 101,
    "Pekingese": 207,
    "Poodle": 172,
    "Pug": 253,
    "Shih Tzu": 208,
    "Tibetan Terrier": 209,
    # group 10
    "Afghan Hound": 228,
    "Azawakh": 307,
    "Borzoi (Russian Hunting Sighthound)": 193,
    "Greyhound": 158,
    "Irish Wolfhound": 160,
    "Italian Sighthound": 200,
    "Saluki": 269,
    "Sloughi": 188,
    "Spanish Greyhound": 285,
    "Whippet": 162,
}


def fill(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for title, number in FCI_STANDARD.items():
        Dogs.objects.filter(title=title).update(fci_standard=number)


class Migration(migrations.Migration):

    dependencies = [
        ("woof", "0114_dog_fci_standard"),
    ]

    operations = [
        migrations.RunPython(fill, migrations.RunPython.noop),
    ]
