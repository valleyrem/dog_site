from django.db import migrations

HOVAWART = {
    "en": "Black-gold, Black, Blond",
    "ru": "Чёрно-золотистый, чёрный, блонд",
    "de": "Schwarzmarken, Schwarz, Blond",
    "it": "Nero focato, nero, biondo",
    "es": "Negro y dorado, negro, rubio",
    "sr_latn": "Crno-zlatni, crni, plavi",
}


def forwards(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    Category = apps.get_model("woof", "Category")
    Section = apps.get_model("woof", "Section")

    hovawart = Dogs.objects.filter(slug="hovawart").first()
    if hovawart:
        for lang, text in HOVAWART.items():
            setattr(hovawart, f"varieties_{lang}", text)
        hovawart.varieties = HOVAWART["en"]
        hovawart.save()

    # The FCI recognises this breed as the Kangal Shepherd Dog (No. 331), group
    # 2, section 2 (Molossian type, mountain type), so it leaves "outside the FCI".
    group = Category.objects.filter(slug="pinscher-schnauzer-molossoid").first()
    section = Section.objects.filter(
        category=group, name__startswith="Section 2"
    ).first()
    anatolian = Dogs.objects.filter(slug="anatolian-shepherd-dog").first()
    if anatolian and group and section:
        anatolian.cat = group
        anatolian.section = section
        anatolian.fci_standard = 331
        anatolian.native_name = "Kangal Çoban Köpeği"
        anatolian.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0115_fill_fci_standard")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
