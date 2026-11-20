from django.db import migrations

FIXES = {
    "rhodesian-ridgeback": {
        1: {
            "en": "The ridge ends in two matching whorls of hair on the shoulders, called crowns, and their shape is judged in the show ring.",
            "ru": "Гребень заканчивается двумя одинаковыми завитками шерсти на плечах, их называют «коронами», и на выставках их форму оценивают.",
            "de": "Der Kamm endet in zwei gleichen Haarwirbeln auf den Schultern, den sogenannten Kronen, und ihre Form wird im Ausstellungsring bewertet.",
            "it": "La cresta termina in due verticilli di pelo uguali sulle spalle, detti corone, e la loro forma viene valutata in esposizione.",
            "es": "La cresta termina en dos remolinos de pelo iguales sobre los hombros, llamados coronas, y su forma se juzga en las exposiciones.",
            "sr_latn": "Greben se završava dvema jednakim vrtlozima dlake na plećima, zvanim krune, a njihov oblik se ocenjuje na izložbama.",
        },
        2: {
            "en": "It is a quiet, cat-like dog: it keeps itself clean, rarely barks without a reason and loves a sunny spot to lie in.",
            "ru": "Это тихая, похожая на кошку собака: сама следит за чистотой, редко лает без повода и любит полежать на солнышке.",
            "de": "Er ist ein ruhiger, katzenartiger Hund: Er hält sich selbst sauber, bellt selten ohne Grund und liebt einen sonnigen Liegeplatz.",
            "it": "È un cane tranquillo, simile a un gatto: si tiene pulito da solo, abbaia raramente senza motivo e ama sdraiarsi in un angolo di sole.",
            "es": "Es un perro callado, parecido a un gato: se mantiene limpio solo, rara vez ladra sin motivo y adora tumbarse en un rincón soleado.",
            "sr_latn": "Tih je pas nalik mački: sam održava čistoću, retko laje bez razloga i voli da leži na sunčanom mestu.",
        },
    },
    "slovakian-hound": {
        2: {
            "en": "The tan marks above its eyes look like a second pair of eyebrows and give it an expressive, questioning face.",
            "ru": "Рыжие отметины над глазами выглядят как вторая пара бровей и придают морде выразительный, вопросительный вид.",
            "de": "Die lohfarbenen Abzeichen über den Augen sehen aus wie ein zweites Paar Augenbrauen und geben ihm ein ausdrucksvolles, fragendes Gesicht.",
            "it": "Le macchie focate sopra gli occhi sembrano un secondo paio di sopracciglia e gli danno un'espressione eloquente e interrogativa.",
            "es": "Las marcas fuego sobre los ojos parecen un segundo par de cejas y le dan una cara expresiva e interrogante.",
            "sr_latn": "Žute oznake iznad očiju izgledaju kao drugi par obrva i daju mu izražajno, upitno lice.",
        },
    },
    "stabijhoun": {
        0: {
            "en": 'The name comes from the Frisian for "stand by me", which suits a dog that stays close to its people.',
            "ru": "Название породы происходит от фризского выражения «стой рядом со мной», и это подходит собаке, которая держится рядом с людьми.",
            "de": "Der Name stammt vom friesischen „steh mir bei“, was zu einem Hund passt, der nah bei seinen Menschen bleibt.",
            "it": "Il nome deriva dal frisone per “stammi vicino”, il che si addice a un cane che resta vicino alle sue persone.",
            "es": "El nombre procede del frisón para “quédate a mi lado”, lo que encaja con un perro que se mantiene cerca de su gente.",
            "sr_latn": "Ime potiče od frizijskog izraza „stoj uz mene“, što odgovara psu koji ostaje blizu svojih ljudi.",
        },
    },
    "german-spaniel": {
        1: {
            "en": "It loves water and is a strong swimmer, so a towel in the car is useful.",
            "ru": "Он любит воду и хорошо плавает, поэтому полотенце в машине пригодится.",
            "de": "Er liebt Wasser und ist ein kräftiger Schwimmer, ein Handtuch im Auto ist daher nützlich.",
            "it": "Ama l'acqua ed è un forte nuotatore, quindi un asciugamano in macchina è utile.",
            "es": "Adora el agua y es un buen nadador, así que una toalla en el coche es útil.",
            "sr_latn": "Voli vodu i snažan je plivač, pa je peškir u kolima koristan.",
        },
    },
    "wetterhoun": {
        1: {
            "en": "It is a strong swimmer and happily goes into cold water, so dry it well after a swim.",
            "ru": "Он сильный пловец и охотно заходит в холодную воду, поэтому после купания его нужно хорошо вытереть.",
            "de": "Er ist ein kräftiger Schwimmer und geht gern in kaltes Wasser, trocknen Sie ihn daher nach dem Schwimmen gut ab.",
            "it": "È un forte nuotatore ed entra volentieri in acqua fredda, quindi asciugatelo bene dopo il nuoto.",
            "es": "Es un buen nadador y se mete con gusto en agua fría, así que séquelo bien tras nadar.",
            "sr_latn": "Snažan je plivač i rado ulazi u hladnu vodu, zato ga posle plivanja dobro osušite.",
        },
    },
    "barbado-da-terceira": {
        0: {
            "en": 'Its name means "bearded" in Portuguese, after the long hair around its face.',
            "ru": "Название породы по-португальски означает «бородатый» — из-за длинной шерсти вокруг морды.",
            "de": "Sein Name bedeutet auf Portugiesisch „bärtig“, nach dem langen Haar um sein Gesicht.",
            "it": "Il suo nome significa “barbuto” in portoghese, per il lungo pelo attorno al muso.",
            "es": "Su nombre significa “barbado” en portugués, por el pelo largo alrededor de su cara.",
            "sr_latn": "Njegovo ime na portugalskom znači „bradat“, zbog duge dlake oko lica.",
        },
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, items in FIXES.items():
        dog = Dogs.objects.filter(slug=slug).first()
        if not dog:
            continue
        values = {}
        for lang in ("en", "ru", "de", "it", "es", "sr_latn"):
            lines = (getattr(dog, f"quirks_{lang}") or "").split("\n")
            for idx, texts in items.items():
                lines[idx] = texts[lang]
            values[f"quirks_{lang}"] = "\n".join(lines)
            if lang == "en":
                values["quirks"] = values["quirks_en"]
        Dogs.objects.filter(pk=dog.pk).update(**values)


class Migration(migrations.Migration):
    dependencies = [("woof", "0080_breed_content_translations")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
