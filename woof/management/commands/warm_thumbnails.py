"""Generate all imagekit thumbnails ahead of time.

Why: imagekit generates a thumbnail lazily the first time ``.url`` is
touched during template rendering, which makes the *first* visitor (or a
fresh deploy / empty cache) pay the whole bill at once. Running this
command after deploy (or after uploading photos) moves that cost to the
build step.

Usage:
    python manage.py warm_thumbnails
"""

from django.core.management.base import BaseCommand

from woof.models import Dogs, DogImage


class Command(BaseCommand):
    help = "Pre-generate imagekit thumbnails for all dog photos."

    def handle(self, *args, **options):
        count = 0

        dogs = Dogs.objects.filter(
            photo__isnull=False, is_published=True
        ).only("id", "title", "photo")

        for dog in dogs:
            for spec in ("photo_thumb", "photo_medium", "photo_card"):
                try:
                    getattr(dog, spec).generate()
                    count += 1
                except Exception as exc:  # noqa: BLE001 — keep going
                    self.stderr.write(f"  skip {dog.title} {spec}: {exc}")

        gallery = DogImage.objects.all()
        for img in gallery:
            for spec in ("image_thumb", "image_large"):
                try:
                    getattr(img, spec).generate()
                    count += 1
                except Exception as exc:  # noqa: BLE001
                    self.stderr.write(f"  skip gallery {img.pk} {spec}: {exc}")

        self.stdout.write(self.style.SUCCESS(f"Warmed {count} thumbnails."))