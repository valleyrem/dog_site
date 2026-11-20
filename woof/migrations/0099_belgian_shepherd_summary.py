from django.db import migrations

SLUG = "belgian-shepherd-dog"

SUMMARY = {
    "en": "A clever, attentive and energetic herding dog, known for learning quickly and for devotion to its family. It needs daily exercise and mental work, and is happiest when it has a job to do.",
    "ru": "Умная, внимательная и энергичная пастушья собака, известная быстрой обучаемостью и преданностью семье. Ей нужны ежедневная нагрузка и занятия для ума: лучше всего она чувствует себя, когда у неё есть дело.",
    "de": "Ein kluger, aufmerksamer und energischer Hütehund, bekannt für schnelles Lernen und Ergebenheit gegenüber der Familie. Er braucht täglich Bewegung und geistige Auslastung und ist am glücklichsten, wenn er eine Aufgabe hat.",
    "it": "Un cane da pastore intelligente, attento ed energico, noto per la rapidità di apprendimento e la devozione alla famiglia. Ha bisogno di movimento quotidiano e di stimoli mentali, e dà il meglio di sé quando ha un compito da svolgere.",
    "es": "Un perro pastor inteligente, atento y enérgico, conocido por su rapidez de aprendizaje y su lealtad a la familia. Necesita ejercicio diario y estimulación mental, y es más feliz cuando tiene una tarea que cumplir.",
    "sr_latn": "Pametan, pažljiv i energičan pastirski pas, poznat po brzom učenju i odanosti porodici. Potrebni su mu svakodnevno kretanje i mentalna aktivnost, a najsrećniji je kada ima zadatak.",
}


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Dogs.objects.filter(slug=SLUG).update(
        **{f"summary_{lang}": text for lang, text in SUMMARY.items()}
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0098_english_summary_care_quirks_from_ru")]

    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
