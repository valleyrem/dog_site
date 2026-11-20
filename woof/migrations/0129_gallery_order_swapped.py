from django.db import migrations

# The gallery of these breeds had no order (all zeros), so after the swap the
# old main photo has to keep the place of the photo that became the main one.
ORDER = {
    "shih-tzu": [
        "photos/dogs/gallery/1-dieny-portinanni-shih-tzu_11zon.webp",
        "photos/2026/02/06/shikhar-bhatnagar-shih-tzu_11zon.webp",
        "photos/dogs/gallery/3-jen-shish-shih-tzu_11zon.webp",
        "photos/dogs/gallery/4-joshua-j-cotten-shih-tzu_11zon.webp",
    ],
    "azawakh": [
        "photos/dogs/gallery/1-bani-bangou-azawakh.webp",
        "photos/dogs/gallery/2-alan-cherubini-azawakh-flickr.webp",
        "photos/2026/02/10/sweet-dogs-azawakh-flickr.webp",
        "photos/dogs/gallery/3-cristian.vantu-azawakh.webp",
    ],
}


def forwards(apps, schema_editor):
    DogImage = apps.get_model("woof", "DogImage")
    for slug, files in ORDER.items():
        for position, name in enumerate(files):
            DogImage.objects.filter(dog__slug=slug, image=name).update(order=position)


class Migration(migrations.Migration):
    dependencies = [("woof", "0128_swap_main_photos")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
