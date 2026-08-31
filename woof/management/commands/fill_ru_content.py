"""Fill Russian names for Dogs, Category and Section.

Idempotent: only fills empty values. Run:
    python manage.py fill_ru_content
"""
from django.core.management.base import BaseCommand
from django.utils import translation

from woof.models import Category, Dogs, Section

DOGS_TITLES = {
    "Afghan Hound": "Афганская борзая",
    "Airedale Terrier": "Эрдельтерьер",
    "Akita": "Акита",
    "Alaskan Malamute": "Аляскинский маламут",
    "American Cocker Spaniel": "Американский кокер-спаниель",
    "American Eskimo Dog": "Американская эскимосская собака",
    "American Staffordshire Terrier": "Американский стаффордширский терьер",
    "Anatolian Shepherd Dog": "Анатолийская овчарка",
    "Australian Shepherd": "Австралийская овчарка",
    "Azawakh": "Азавак",
    "Barbado da Terceira": "Барбадо да Терсейра",
    "Basset Hound": "Бассет-хаунд",
    "Bedlington Terrier": "Бедлингтон-терьер",
    "Bichon Frise": "Бишон фризе",
    "Black and Tan Coonhound": "Блэк-энд-тан кунхаунд",
    "Bloodhound": "Бладхаунд",
    "Bolognese": "Болоньез",
    "Border Collie": "Бордер-колли",
    "Border Terrier": "Бордер-терьер",
    "Borzoi": "Русская псовая борзая",
    "Boxer": "Боксёр",
    "Brussels Griffon": "Брюссельский гриффон",
    "Bulldog": "Английский бульдог",
    "Bull Terrier": "Бультерьер",
    "Catahoula Leopard Dog": "Катахула",
    "Cavalier King Charles Spaniel": "Кавалер-кинг-чарльз-спаниель",
    "Collie Rough": "Колли (длинношёрстный)",
    "Czechoslovakian Wolfdog": "Чехословацкая волчья собака",
    "Dachshund": "Такса",
    "Dalmatian": "Далматин",
    "Dobermann": "Доберман",
    "Drever": "Древер",
    "Dutch Shepherd Dog": "Голландская овчарка",
    "English Setter": "Английский сеттер",
    "French Bulldog": "Французский бульдог",
    "German Shepherd Dog": "Немецкая овчарка",
    "German Shorthaired Pointer": "Немецкий курцхаар",
    "German Spitz": "Немецкий шпиц",
    "Golden Retriever": "Золотистый ретривер",
    "Great Dane": "Немецкий дог",
    "Hovawart": "Ховаварт",
    "Irish Wolfhound": "Ирландский волкодав",
    "Italian Cane Corso": "Итальянский кане-корсо",
    "Italian Sighthound": "Итальянская борзая (левретка)",
    "Italian Spinone": "Итальянский спиноне",
    "Kai": "Каи",
    "Keeshond (Wolfspitz)": "Кеесхонд (вольфшпиц)",
    "Kleiner Münsterländer": "Малый мюнстерлендер",
    "Labrador Retriever": "Лабрадор-ретривер",
    "Nederlandse Kooikerhondje": "Койкерхондье",
    "Norwegian Elkhound Grey": "Норвежский элкхунд (серый)",
    "Nova Scotia Duck Tolling Retriever": "Новошотландский ретривер",
    "Old English Sheepdog": "Бобтейл (староанглийская овчарка)",
    "Pekingese": "Пекинес",
    "Pembroke Welsh Corgi": "Вельш-корги пемброк",
    "Pomeranian": "Померанский шпиц",
    "Poodle": "Пудель",
    "Portuguese Podengo": "Португальский поденгу",
    "Pug": "Мопс",
    "Puli": "Пули",
    "Rat Terrier": "Рэт-терьер",
    "Romagna Water Dog": "Лаготто-романьоло",
    "Rottweiler": "Ротвейлер",
    "Saint Bernard": "Сенбернар",
    "Samoyed": "Самоед",
    "Scottish Terrier": "Скотч-терьер",
    "Shar Pei": "Шарпей",
    "Shih Tzu": "Ши-тцу",
    "Siberian Husky": "Сибирский хаски",
    "Sloughi": "Слюги",
    "Treeing Walker Coonhound": "Триинг-уокер кунхаунд",
    "Weimaraner": "Веймаранер",
    "Whippet": "Уиппет",
    "Wire Fox Terrier": "Жесткошёрстный фокстерьер",
    "Xoloitzcuintli": "Ксолоитцкуинтли",
    "Yakutian Laika": "Якутская лайка",
    "Yorkshire Terrier": "Йоркширский терьер",
}

CATEGORY_NAMES = {
    "Breeds outside FCI classification": "Породы вне классификации FCI",
    "Sheepdogs and Cattledogs (except Swiss Cattledogs)": "Пастушьи и скотогонные собаки (кроме швейцарских скотогонных)",
    "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs": "Пинчеры и шнауцеры — молоссоиды, швейцарские горные и скотогонные собаки",
    "Terriers": "Терьеры",
    "Dachshunds": "Таксы",
    "Spitz and primitive types": "Шпицы и породы примитивного типа",
    "Scent hounds and related breeds": "Гончие и родственные породы",
    "Pointing Dogs": "Легавые",
    "Retrievers - Flushing Dogs - Water Dogs": "Ретриверы — спаниели — водяные собаки",
    "Companion and Toy Dogs": "Компаньоны и декоративные собаки",
    "Sighthounds": "Борзые",
}

SECTION_NAMES = {
    "Asian Spitz and related breeds": "Азиатские шпицы и родственные породы",
    "Bichons and related breeds": "Бишоны и родственные породы",
    "British and Irish Pointers and Setters": "Британские и ирландские пойнтеры и сеттеры",
    "Bull type Terriers": "Терьеры буль-типа",
    "Cattledogs (except Swiss Cattledogs)": "Скотогонные собаки (кроме швейцарских скотогонных)",
    "Chihuahueno": "Чихуахуэно",
    "Continental Pointing Dogs": "Континентальные легавые",
    "Continental Toy Spaniel and others": "Континентальные декоративные спаниели и другие",
    "English Toy Spaniels": "Английские декоративные спаниели",
    "European Spitz": "Европейские шпицы",
    "Flushing Dogs": "Спаниели",
    "Hairless Dogs": "Голые собаки",
    "Japan Chin and Pekingese": "Японский хин и пекинес",
    "Kromfohrländer": "Кромфорлендер",
    "Large and medium sized Terriers": "Крупные и средние терьеры",
    "Leash (scent) Hounds": "Гончие по следу",
    "Long-haired or fringed Sighthounds": "Длинношёрстные борзые",
    "Molossian type": "Молоссы",
    "Nordic Hunting Dogs": "Северные охотничьи собаки",
    "Nordic Sledge Dogs": "Северные ездовые собаки",
    "Nordic Watchdogs and Herders": "Северные сторожевые и пастушьи собаки",
    "Pinscher and Schnauzer type": "Пинчеры и шнауцеры",
    "Poodle": "Пудель",
    "Primitive type": "Примитивный тип",
    "Primitive type - Hunting Dogs": "Примитивный тип — охотничьи собаки",
    "Recognized by Other Kennel Clubs": "Признаны другими кинологическими клубами",
    "Related breeds": "Родственные породы",
    "Retrievers": "Ретриверы",
    "Rough-haired Sighthounds": "Жесткошёрстные борзые",
    "Scent hounds": "Гончие",
    "Sheepdogs": "Овчарки",
    "Short-haired Sighthounds": "Короткошёрстные борзые",
    "Single breed group (no sections)": "Группа из одной породы (без разделов)",
    "Small Belgian Dogs": "Мелкие бельгийские собаки",
    "Small Molossian type Dogs": "Мелкие молоссы",
    "Small sized Terriers": "Мелкие терьеры",
    "Swiss Mountain and Cattledogs": "Швейцарские горные и скотогонные собаки",
    "Tibetan breeds": "Тибетские породы",
    "Toy Terriers": "Той-терьеры",
    "Unrecognized but Documented Breeds": "Непризнанные, но документально подтверждённые породы",
    "Water Dogs": "Водяные собаки",
}




class Command(BaseCommand):
    help = "Fill *__ru_ names for dogs, categories and sections."

    def handle(self, *args, **options):
        with translation.override("ru"):
            dog_updated = 0
            for dog in Dogs.objects.all():
                ru = DOGS_TITLES.get(dog.title)
                if ru and not dog.title_ru:
                    dog.title_ru = ru
                    dog.save(update_fields=["title_ru"])
                    dog_updated += 1
            self.stdout.write(f"Dogs.title_ru filled: {dog_updated}")

            cat_updated = 0
            for c in Category.objects.all():
                ru = CATEGORY_NAMES.get(c.name)
                if ru and not c.name_ru:
                    c.name_ru = ru
                    c.save(update_fields=["name_ru"])
                    cat_updated += 1
            self.stdout.write(f"Category.name_ru filled: {cat_updated}")

            sec_updated = 0
            for s in Section.objects.all():
                ru = SECTION_NAMES.get(s.name)
                if ru and not s.name_ru:
                    s.name_ru = ru
                    s.save(update_fields=["name_ru"])
                    sec_updated += 1
            self.stdout.write(f"Section.name_ru filled: {sec_updated}")
