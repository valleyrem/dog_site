from django.db import migrations

# Breeds whose FCI standard is looked after by another country than the one
# they come from (the "patronage" in the FCI standard).
SENTENCES = {
    "afghan-hound": {
        "en": "Its FCI standard is maintained by Great Britain, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Великобритания, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Großbritannien, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Gran Bretagna, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Gran Bretaña, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Velika Britanija, a ne zemlja njenog porekla.",
    },
    "azawakh": {
        "en": "Its FCI standard is maintained by France, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Франция, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Frankreich, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Francia, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Francia, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Francuska, a ne zemlja njenog porekla.",
    },
    "czechoslovakian-wolfdog": {
        "en": "Its FCI standard is maintained by Slovakia, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Словакия, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut die Slowakei, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Slovacchia, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Eslovaquia, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Slovačka, a ne zemlja njenog porekla.",
    },
    "pekingese": {
        "en": "Its FCI standard is maintained by Great Britain, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Великобритания, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Großbritannien, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Gran Bretagna, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Gran Bretaña, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Velika Britanija, a ne zemlja njenog porekla.",
    },
    "pug": {
        "en": "Its FCI standard is maintained by Great Britain, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Великобритания, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Großbritannien, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Gran Bretagna, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Gran Bretaña, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Velika Britanija, a ne zemlja njenog porekla.",
    },
    "shih-tzu": {
        "en": "Its FCI standard is maintained by Great Britain, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Великобритания, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Großbritannien, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Gran Bretagna, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Gran Bretaña, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Velika Britanija, a ne zemlja njenog porekla.",
    },
    "tibetan-terrier": {
        "en": "Its FCI standard is maintained by Great Britain, not by the country the breed comes from.",
        "ru": "Стандарт породы в FCI ведёт Великобритания, а не страна её происхождения.",
        "de": "Den FCI-Standard der Rasse betreut Großbritannien, nicht ihr Herkunftsland.",
        "it": "Lo standard FCI della razza è curato dalla Gran Bretagna, non dal suo paese d'origine.",
        "es": "El estándar FCI de la raza lo mantiene Gran Bretaña, no su país de origen.",
        "sr_latn": "FCI standard rase vodi Velika Britanija, a ne zemlja njenog porekla.",
    },
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, texts in SENTENCES.items():
        dog = Dogs.objects.filter(slug=slug).first()
        if not dog:
            continue
        for lang, text in texts.items():
            field = f"history_{lang}"
            current = getattr(dog, field) or ""
            if text not in current:
                setattr(dog, field, (current + " " + text).strip())
        if SENTENCES[slug]["en"] not in dog.history:
            dog.history = (dog.history + " " + SENTENCES[slug]["en"]).strip()
        dog.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0124_samoyed_native_name")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
