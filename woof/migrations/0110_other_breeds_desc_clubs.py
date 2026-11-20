from django.db import migrations

SLUG = "breeds-outside-fci-classification"

# FCI is already spelled out on the Groups page, the other clubs are not.
FCI_FULL = "Fédération Cynologique Internationale (FCI)"
CLUBS = {
    "en": (
        "the AKC or UKC",
        "the American Kennel Club (AKC), the United Kennel Club (UKC) or others",
    ),
    "ru": (
        "AKC или UKC",
        "American Kennel Club (AKC), United Kennel Club (UKC) или другими",
    ),
    "de": (
        "dem AKC oder UKC",
        "dem American Kennel Club (AKC), dem United Kennel Club (UKC) oder anderen",
    ),
    "it": (
        "AKC o UKC",
        "l'American Kennel Club (AKC), lo United Kennel Club (UKC) o altri",
    ),
    "es": (
        "el AKC o el UKC",
        "el American Kennel Club (AKC), el United Kennel Club (UKC) u otros",
    ),
    "sr_latn": (
        "AKC ili UKC",
        "American Kennel Club (AKC), United Kennel Club (UKC) ili drugih",
    ),
}


def forwards(apps, schema_editor):
    Category = apps.get_model("woof", "Category")
    try:
        category = Category.objects.get(slug=SLUG)
    except Category.DoesNotExist:
        return
    for lang, (old, new) in CLUBS.items():
        field = f"desc_{lang}"
        text = getattr(category, field, None)
        if not text:
            continue
        text = text.replace(FCI_FULL, "FCI").replace(old, new)
        setattr(category, field, text)
        if lang == "en":
            category.desc = text
    category.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0109_shorter_group_descriptions")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
