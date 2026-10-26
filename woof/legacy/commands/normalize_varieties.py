"""
Заменяет «чистые» значения varieties вида «Color variations» (и их переводы)
на «No variations» (и соответствующие переводы).

Заменяются ТОЛЬКО точные совпадения — значения с пояснениями
(«Short-haired, Long-haired; Color variations», «Color variations: Black, ...»)
не трогаются. Команда идемпотентна.
"""

from django.core.management.base import BaseCommand

from woof.models import Dogs

# поле -> {старое точное значение: новое}
MAP = {
    "varieties": {
        "Color variations": "No variations",
    },
    "varieties_ru": {
        "Различные окрасы": "Без разновидностей",
        "Вариации окраса": "Без разновидностей",
    },
    "varieties_uk": {
        "Варіації забарвлення": "Без варіацій",
        "Різні забарвлення": "Без варіацій",
    },
    "varieties_sr_latn": {
        "Varijacije boja": "Nema varijeteta",
        "Varijeteti boje": "Nema varijeteta",
    },
    "varieties_de": {
        "Farbvariationen": "Keine Varietäten",
        "Farbvarianten": "Keine Varietäten",
        # заодно чиним оставшийся английский текст у 9 пород
        "No variations": "Keine Varietäten",
    },
    "varieties_it": {
        "Varietà di colore": "Nessuna varietà",
    },
    "varieties_es": {
        "Variaciones de color": "Sin variaciones",
    },
}


class Command(BaseCommand):
    help = "Normalise «Color variations» varieties to «No variations» (exact matches only)."

    def handle(self, *args, **options):
        total = 0
        for field, mapping in MAP.items():
            for old, new in mapping.items():
                n = Dogs.objects.filter(**{field: old}).update(**{field: new})
                if n:
                    self.stdout.write(f"{field}: {old!r} -> {new!r}: {n}")
                total += n
        self.stdout.write(self.style.SUCCESS(f"Всего обновлено: {total}"))
