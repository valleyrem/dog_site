from django.db import migrations

# breed slug -> file name of the gallery photo that becomes the main one; the
# current main photo takes its place in the gallery
SWAPS = {
    "shih-tzu": "photos/dogs/gallery/2-nikolay-tchaouchev-shih-tzu_11zon.webp",
    "azawakh": "photos/dogs/gallery/4-rita-ivanauskas-azawakh-flickr.webp",
}


def swap(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    DogImage = apps.get_model("woof", "DogImage")
    for slug, gallery_file in SWAPS.items():
        dog = Dogs.objects.filter(slug=slug).first()
        image = (
            DogImage.objects.filter(dog=dog, image=gallery_file).first()
            if dog
            else None
        )
        if not image:
            continue
        dog.photo, image.image = gallery_file, dog.photo.name
        dog.photo_author, image.author = image.author, dog.photo_author
        dog.save()
        image.save()


class Migration(migrations.Migration):
    dependencies = [("woof", "0127_native_language_by_standard")]
    operations = [migrations.RunPython(swap, migrations.RunPython.noop)]
