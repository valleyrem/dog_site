from importlib import import_module

from django.db import migrations

from woof.migrations._content import apply_translations

PARTS = [
    "_tr_1a", "_tr_1b", "_tr_2a", "_tr_2b", "_tr_2c", "_tr_3a", "_tr_3b", "_tr_5a", "_tr_5b", "_tr_5c", "_tr_6a", "_tr_6b", "_tr_7a", "_tr_7b", "_tr_7c", "_tr_8a", "_tr_8b", "_tr_9a", "_tr_9b", "_tr_11a", "_tr_11b", "_tr_12a", "_tr_12b",
]


DACHSHUND_QUIRKS = {
    "de": [
        "Ein Dackel gräbt sich absichtlich in Decken, Kissen und das Sofa ein: Das ist der Instinkt eines Bauhundjägers und für die Rasse sehr typisch.",
        "Seine Nase bestimmt den Spaziergang: Er bleibt vielleicht eine Minute an einer Stelle stehen und will nicht weiter, weil er die Gerüche liest.",
        "Ein Dackel namens Waldi war 1972 in München das erste offizielle Maskottchen der Olympischen Spiele.",
    ],
    "it": [
        "Il bassotto si infila di proposito tra coperte, cuscini e divano: è l'istinto di un cacciatore di tane di tasso, molto tipico della razza.",
        "È il naso a guidare la passeggiata: può fermarsi un minuto in un punto e rifiutarsi di proseguire, perché sta leggendo gli odori.",
        "Un bassotto di nome Waldi è stato la prima mascotte ufficiale dei Giochi Olimpici, a Monaco nel 1972.",
    ],
    "es": [
        "El teckel se mete a propósito entre mantas, cojines y el sofá: es el instinto de un cazador de tejoneras, muy típico de la raza.",
        "Su nariz dirige el paseo: puede detenerse un minuto en un punto y negarse a seguir, porque está leyendo los olores.",
        "Un teckel llamado Waldi fue la primera mascota oficial de los Juegos Olímpicos, en Múnich en 1972.",
    ],
    "sr_latn": [
        "Jazavičar se namerno zavlači među ćebad, jastuke i kauč: to je nagon lovca na jazbine jazavaca i veoma je tipičan za rasu.",
        "Šetnjom upravlja njegov nos: može da se zaustavi na jednom mestu minut i odbije da krene dalje, jer čita mirise.",
        "Jazavičar po imenu Valdi bio je prva zvanična maskota Olimpijskih igara, u Minhenu 1972. godine.",
    ],
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug="dachshund").update(
        **{f"quirks_{lang}": "\n".join(lines) for lang, lines in DACHSHUND_QUIRKS.items()}
    )
    for part in PARTS:
        module = import_module(f"woof.migrations.{part}")
        apply_translations(apps, module.TR)


class Migration(migrations.Migration):
    dependencies = [("woof", "0079_group12_content")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
