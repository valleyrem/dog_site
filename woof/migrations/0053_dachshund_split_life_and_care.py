from django.db import migrations

EN_CARE = (
    "Coat care depends on the variety: smooth coats need a weekly wipe, long coats a brush a few times a week, "
    "wire coats a brush and occasional trimming. Check the ears and teeth regularly.\n"
    "Keep your Dachshund lean: extra weight is hard on a long back. Use ramps or steps for the sofa and car, "
    "do not let it jump from heights, and support its chest and hindquarters when you lift it. "
    "Book routine vet visits, and ask the breeder about the parents' health checks."
)
RU_CARE = (
    "Уход за шерстью зависит от разновидности: гладкошёрстную достаточно протирать раз в неделю, длинношёрстную "
    "расчёсывать несколько раз в неделю, жёсткошёрстную расчёсывать и иногда тримминговать. Регулярно проверяйте уши и зубы.\n"
    "Следите, чтобы такса не полнела: лишний вес тяжело сказывается на длинной спине. Используйте пандус или ступеньки "
    "для дивана и машины, не давайте прыгать с высоты и поддерживайте грудь и заднюю часть, когда берёте на руки. "
    "Ходите на плановые осмотры к ветеринару и спросите заводчика о проверках здоровья родителей."
)


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    dog = Dogs.objects.filter(slug="dachshund").first()
    if not dog:
        return

    def without_coat(text):
        lines = [l for l in (text or "").splitlines() if not l.startswith(("Coat care", "Уход зависит"))]
        return "\n".join(lines)

    Dogs.objects.filter(pk=dog.pk).update(
        daily_life=without_coat(dog.daily_life),
        daily_life_en=without_coat(dog.daily_life_en),
        daily_life_ru=without_coat(dog.daily_life_ru),
        care=EN_CARE,
        care_en=EN_CARE,
        care_ru=RU_CARE,
    )


class Migration(migrations.Migration):
    dependencies = [("woof", "0052_slim_breed_params")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
