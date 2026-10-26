"""Доводит количество черт характера до пяти у тех пород, где их четыре.

Пятая черта берётся только из существующего справочника Temperament
(все черты уже переведены на 7 языков) — новых записей не создаётся.
Команда идемпотентна: повторный запуск ничего не меняет.

    python manage.py fill_temperament_fifth
    python manage.py fill_temperament_fifth --dry-run
"""

from django.core.management.base import BaseCommand

from woof.models import Dogs, Temperament

TARGET = 5

# slug породы -> имя пятой черты (должно совпадать с Temperament.name)
FIFTH = {
    "afghan-hound": "Playful",
    "airedale-terrier": "Energetic",
    "akita": "Protective",
    "alaskan-malamute": "Energetic",
    "american-cocker-spaniel": "Social",
    "american-eskimo-dog": "Energetic",
    "american-staffordshire-terrier": "Playful",
    "anatolian-shepherd-dog": "Alert",
    "australian-shepherd": "Eager",
    "azawakh": "Independent",
    "barbado-da-terceira": "Loyal",
    "basset-hound": "Stubborn",
    "bedlington-terrier": "Brave",
    "bichon-frise": "Social",
    "black-and-tan-coonhound": "Determined",
    "bloodhound": "Patient",
    "bolognese": "Playful",
    "border-collie": "Loyal",
    "border-terrier": "Intelligent",
    "borzoi": "Aloof",
    "boxer": "Affectionate",
    "brussels-griffon": "Playful",
    "bulldog": "Stubborn",
    "bull-terrier": "Courageous",
    "cane-corso": "Brave",
    "catahoula-leopard-dog": "Energetic",
    "cavalier-king-charles-spaniel": "Playful",
    "collie-rough": "Active",
    "czechoslovakian-wolfdog": "Independent",
    "dachshund": "Alert",
    "dalmatian": "Intelligent",
    "dobermann": "Protective",
    "drever": "Alert",
    "dutch-shepherd-dog": "Trainable",
    "english-setter": "Energetic",
    "french-bulldog": "Charming",
    "german-shepherd-dog": "Alert",
    "german-shorthaired-pointer": "Trainable",
    "german-spitz": "Intelligent",
    "golden-retriever": "Eager",
    "great-dane": "Patient",
    "hovawart": "Intelligent",
    "irish-red-setter": "Playful",
    "irish-wolfhound": "Courageous",
    "italian-sighthound": "Agile",
    "italian-spinone": "Friendly",
    "kai": "Independent",
    "keeshond-wolfspitz": "Cheerful",
    "kleiner-munsterlander": "Trainable",
    "labrador-retriever": "Eager",
    "nederlandse-kooikerhondje": "Intelligent",
    "norwegian-elkhound-grey": "Energetic",
    "nova-scotia-duck-tolling-retriever": "Eager",
    "old-english-sheepdog": "Playful",
    "otterhound": "Friendly",
    "pekingese": "Self-important",
    "pembroke-welsh-corgi": "Alert",
    "pomeranian": "Alert",
    "poodle": "Playful",
    "portuguese-podengo": "Alert",
    "pug": "Social",
    "puli": "Hardworking",
    "rat-terrier": "Playful",
    "romagna-water-dog": "Affectionate",
    "rottweiler": "Protective",
    "saint-bernard": "Calm",
    "saluki": "Aloof",
    "samoyed": "Loving",
    "scottish-terrier": "Stubborn",
    "shar-pei": "Aloof",
    "shih-tzu": "Charming",
    "siberian-husky": "Strong-willed",
    "sloughi": "Fast",
    "stabijhoun": "Affectionate",
    "treeing-walker-coonhound": "Determined",
    "weimaraner": "Affectionate",
    "whippet": "Playful",
    "wire-fox-terrier": "Spirited",
    "xoloitzcuintli": "Intelligent",
    "yakutian-laika": "Hardy",
    "yorkshire-terrier": "Stubborn",
}


class Command(BaseCommand):
    help = "Добавляет пятую черту характера породам, у которых их четыре"

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="только показать, что будет добавлено",
        )

    def handle(self, *args, **options):
        dry = options["dry_run"]
        traits = {t.name: t for t in Temperament.objects.all()}

        missing = sorted({n for n in FIFTH.values() if n not in traits})
        if missing:
            self.stdout.write(self.style.ERROR(f"нет в справочнике: {missing}"))
            return

        added, skipped, unknown = 0, 0, []
        for slug, trait_name in sorted(FIFTH.items()):
            dog = Dogs.objects.filter(slug=slug).prefetch_related("temperament").first()
            if not dog:
                unknown.append(slug)
                continue
            current = {t.name for t in dog.temperament.all()}
            if len(current) >= TARGET or trait_name in current:
                skipped += 1
                continue
            if dry:
                self.stdout.write(f"  {slug}: + {trait_name}")
            else:
                dog.temperament.add(traits[trait_name])
            added += 1

        prefix = "будет добавлено" if dry else "добавлено"
        self.stdout.write(self.style.SUCCESS(f"{prefix}: {added}, уже по пять: {skipped}"))
        if unknown:
            self.stdout.write(self.style.WARNING(f"нет таких пород: {unknown}"))
