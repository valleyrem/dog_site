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





COUNTRY = {'Afganistan': 'Афганистан', 'Belgium': 'Бельгия', 'Belgium, France': 'Бельгия, Франция', 'Canada': 'Канада', 'China': 'Китай', 'Croatia': 'Хорватия', 'Czechoslovakia': 'Чехословакия', 'France': 'Франция', 'Germany': 'Германия', 'Great Britain': 'Великобритания', 'Hungary': 'Венгрия', 'Irleand': 'Ирландия', 'Italy': 'Италия', 'Japan': 'Япония', 'Mali': 'Мали', 'Mexico': 'Мексика', 'Morocco': 'Марокко', 'Northern Russia, Siberia': 'Северная Россия, Сибирь', 'Norway': 'Норвегия', 'Portugal': 'Португалия', 'Russian Federation': 'Российская Федерация', 'Sweden': 'Швеция', 'Switzerland': 'Швейцария', 'The Netherlands': 'Нидерланды', 'Tibet (China)': 'Тибет (Китай)', 'Turkey': 'Турция', 'USA': 'США'}

VARIETIES = {'Color variations': 'Различные окрасы', "It's a variety of German Spitz": 'Разновидность немецкого шпица', 'No variations': 'Без разновидностей', 'Rabbit, Miniature, Standard': 'Кроличий, миниатюрный, стандартный', 'Size variations': 'Различные размеры', 'Small, Medium-sized, Large': 'Малый, средний, крупный', 'Standard, Medium, Miniature, Toy': 'Стандартный, средний, миниатюрный, той', 'Standart, Intermediate, Miniature': 'Стандартный, промежуточный, миниатюрный', 'Toy, Miniature, Standard': 'Той, миниатюрный, стандартный', 'described in «About the Breed»': 'описаны в разделе «О породе»'}

COLORS = {'Black, Blue, Cream, Fawn, Red, Brindle, White, Gold, Grey': 'Чёрный, голубой, кремовый, палевый, рыжий, тигровый, белый, золотистый, серый', 'Black and tan, grizzle and tan': 'Чёрно-подпалый, серо-подпалый (гризли-подпалый)', 'White, Red, Brindle, Fawn, Sesame, Piebald': 'Белый, рыжий, тигровый, палевый, сезамовый, пегий', 'Light gray, Black, Sable, Red, Seal, White': 'Светло-серый, чёрный, соболиный, рыжий, тюлений, белый', 'Black, red, buff, brown, parti-color (white with patches), roan variations': 'Чёрный, рыжий, бурый, коричневый, пёстрый (белый с пятнами), чалые вариации', 'White or white with cream (biscuit)': 'Белый или белый с кремовым (бисквитный)', 'Black, blue, fawn, red, brindle, white, solid or patched combinations': 'Чёрный, голубой, палевый, рыжий, тигровый, белый, однотонные или пятнистые сочетания', 'Fawn, White, Brindle, Sable, Masked': 'Палевый, белый, тигровый, соболиный, с маской', 'Blue Merle, Red Merle, Black, Red, White Markings': 'Голубой мерль, рыжий мерль, чёрный, рыжий, белые отметины', 'Fawn, Brindle, Red, Black, Blue': 'Палевый, тигровый, рыжий, чёрный, голубой', 'Yellow, gray, black, fawn, wolf-gray, often with white markings': 'Жёлтый, серый, чёрный, палевый, волчий серый, часто с белыми отметинами', 'Tri-color, Bi-color, Lemon & White, Red & White, Tan & White': 'Трёхцветный, двухцветный, лимонно-белый, рыже-белый, бело-подпалый', 'Blue, liver, sandy, blue & tan, liver & tan': 'Голубой, печёночный, песочный, голубо-подпалый, печёночно-подпалый', 'White (sometimes with apricot, cream, or buff shadings)': 'Белый (иногда с абрикосовыми, кремовыми или бурыми оттенками)', 'Black and tan (signature coat pattern with rich tan markings over a deep black base)': 'Чёрно-подпалый (характерный окрас с насыщенными подпалинами на глубокой чёрной основе)', 'Black & Tan, Liver & Tan, Red': 'Чёрно-подпалый, печёночно-подпалый, рыжий', 'White': 'Белый', 'Black & white, red & white, tricolor, blue merle, sable, and other variations': 'Чёрно-белый, рыже-белый, трёхцветный, голубой мерль, соболиный и другие вариации', 'Red, grizzle and tan, blue and tan, wheaten': 'Рыжий, гризли-подпалый, голубо-подпалый, пшеничный', 'White, Black, Gold, Brindle, Various combinations': 'Белый, чёрный, золотистый, тигровый, различные сочетания', 'Fawn, brindle, white markings': 'Палевый, тигровый, белые отметины', 'Red, black, black & tan, belge (reddish-brown with black mask), solid black': 'Рыжий, чёрный, чёрно-подпалый, бельж (красновато-коричневый с чёрной маской), сплошной чёрный', 'Fawn, Brindle, White, Piebald, Red, Fallow': 'Палевый, тигровый, белый, пегий, рыжий, рыжевато-жёлтый', 'White, Brindle, Fawn, Black, Red': 'Белый, тигровый, палевый, чёрный, рыжий', 'Merle, blue merle, red merle, black, brindle, solid colors with patterns': 'Мерль, голубой мерль, рыжий мерль, чёрный, тигровый, однотонные с узором', 'Blenheim, Tricolor, Black & Tan, Ruby': 'Бленхейм, трёхцветный, чёрно-подпалый, рубиновый', 'Sable & White, Tricolor, Blue Merle, White, Blue Merle & White': 'Соболино-белый, трёхцветный, голубой мерль, белый, голубой мерль с белым', 'Yellow-gray, silver-gray, dark gray, with light mask': 'Жёлто-серый, серебристо-серый, тёмно-серый, со светлой маской', 'Red, black & tan, chocolate & tan, cream, dapple, brindle, piebald': 'Рыжий, чёрно-подпалый, шоколадно-подпалый, кремовый, мраморный, тигровый, пегий', 'White with black or liver spots, White & Orange, White & Lemon, White Black & Tan': 'Белый с чёрными или печёночными пятнами, бело-оранжевый, бело-лимонный, белый чёрно-подпалый', 'Black & Rust, Red & Rust, Blue & Rust, Fawn & Rust, White': 'Чёрно-подпалый, рыже-подпалый, голубо-подпалый, палево-подпалый, белый', 'Yellow, Fawn, Black & Tan': 'Жёлтый, палевый, чёрно-подпалый', 'Brindle (gold or silver), sometimes with black patterning': 'Тигровый (золотистый или серебристый), иногда с чёрным узором', 'Blue Belton, Lemon Belton, Orange Belton, Tricolor': 'Голубой белтон, лимонный белтон, оранжевый белтон, трёхцветный', 'Brindle, Fawn, White, Pied, Cream': 'Тигровый, палевый, белый, пёстрый, кремовый', 'Black and tan, black and red, sable, solid black, black and cream, black and silver': 'Чёрно-подпалый, чёрно-рыжий, соболиный, сплошной чёрный, чёрно-кремовый, чёрно-серебристый', 'Liver, Liver & White, Roan': 'Печёночный, печёночно-белый, чалый', 'Black, white, cream, brown, orange, sable': 'Чёрный, белый, кремовый, коричневый, оранжевый, соболиный', 'Golden shades (light to dark)': 'Золотистые оттенки (от светлого до тёмного)', 'Fawn, Brindle, Blue, Black, Harlequin, Mantle': 'Палевый, тигровый, голубой, чёрный, арлекин, мантия', 'Black, black and gold, blonde': 'Чёрный, чёрно-золотистый, блонд', 'Gray, Brindle, Red, Black, Fawn, White': 'Серый, тигровый, рыжий, чёрный, палевый, белый', 'Black, Gray, Fawn, Red, Brindle': 'Чёрный, серый, палевый, рыжий, тигровый', 'Fawn, Blue, Black, Red, White, Cream': 'Палевый, голубой, чёрный, рыжий, белый, кремовый', 'White, white & orange, orange roan, white & brown, brown roan': 'Белый, бело-оранжевый, оранжево-чалый, бело-коричневый, коричнево-чалый', 'Tiger brindle (brown/black stripes)': 'Тигровый (коричневые/чёрные полосы)', 'Grey with black shading, cream, variations of wolf-grey': 'Серый с чёрным затенением, кремовый, вариации волчьего серого', 'Brown & white, brown roan': 'Коричнево-белый, коричнево-чалый', 'Black, Yellow, Chocolate': 'Чёрный, жёлтый, шоколадный', 'White with orange-red patches': 'Белый с оранжево-рыжими пятнами', 'Gray, Black-tipped': 'Серый, с чёрными кончиками', 'Shades of red and orange with white markings often present on chest, feet, tail tip, or face': 'Оттенки рыжего и оранжевого с белыми отметинами, часто на груди, лапах, кончике хвоста или морде', 'Gray & White, Blue & White, Blue Merle, Grizzle & White': 'Серо-белый, голубо-белый, голубой мерль, гризли-белый', 'Gold, red, sable, cream, black, black & tan, parti-color': 'Золотистый, рыжий, соболиный, кремовый, чёрный, чёрно-подпалый, пёстрый', 'Red, Sable, Fawn, Black & Tan, Tricolor': 'Рыжий, соболиный, палевый, чёрно-подпалый, трёхцветный', 'Orange, Black, White, Cream, Blue, Brown, Sable, Chocolate Merle, Brindle, Beaver': 'Оранжевый, чёрный, белый, кремовый, голубой, коричневый, соболиный, шоколадный мерль, тигровый, бобровый', 'Black, white, brown, apricot, red, silver, cream, gray, blue, parti-color': 'Чёрный, белый, коричневый, абрикосовый, рыжий, серебристый, кремовый, серый, голубой, пёстрый', 'Yellow, Fawn, Chestnut, Gray, Gold, Red, Orange and mixed': 'Жёлтый, палевый, каштановый, серый, золотистый, рыжий, оранжевый и смешанные', 'Fawn, Black, Apricot, Silver Fawn': 'Палевый, чёрный, абрикосовый, серебристо-палевый', 'Black, Gray, White': 'Чёрный, серый, белый', 'Black, white, tan, chocolate, blue, lemon, red; bicolor and tricolor patterns': 'Чёрный, белый, подпалый, шоколадный, голубой, лимонный, рыжий; двухцветные и трёхцветные узоры', 'Off-white, white with orange or brown patches, brown, orange, roan': 'Небелый, белый с оранжевыми или коричневыми пятнами, коричневый, оранжевый, чалый', 'Black & Rust, Black & Mahogany, Black & Tan': 'Чёрно-подпалый, чёрный с красным деревом, чёрно-подпалый', 'Red & White, Brindle & White, Mostly White': 'Рыже-белый, тигрово-белый, преимущественно белый', 'White, Cream, Biscuit': 'Белый, кремовый, бисквитный', 'Black, Brindle, Wheaten, Silver Brindle': 'Чёрный, тигровый, пшеничный, серебристо-тигровый', 'Solid colors: cream, red, fawn, black, blue, chocolate, sable': 'Однотонные: кремовый, рыжий, палевый, чёрный, голубой, шоколадный, соболиный', 'Black, White, Gold, Brindle, Liver, Silver, Mixed': 'Чёрный, белый, золотистый, тигровый, печёночный, серебристый, смешанные', 'Black & White, Gray & White, Red & White, Agouti, All-White': 'Чёрно-белый, серо-белый, рыже-белый, агути, полностью белый', 'Cream, sand, red fawn, mahogany, brindle, black mask, black ears, with or without small white markings': 'Кремовый, песочный, рыже-палевый, красно-коричневый, тигровый, чёрная маска, чёрные уши, с небольшими белыми отметинами или без них', 'Tricolor (Black, White, Tan)': 'Трёхцветный (чёрный, белый, подпалый)', 'Silver gray, Blue, Gray': 'Серебристо-серый, голубой, серый', 'Fawn, Brindle, Black, Blue, Red, White, Mixed': 'Палевый, тигровый, чёрный, голубой, рыжий, белый, смешанные', 'White with black or brown markings': 'Белый с чёрными или коричневыми отметинами', 'Black, gray, slate, red, bronze, liver, solid or spotted': 'Чёрный, серый, грифельный, рыжий, бронзовый, печёночный, однотонный или пятнистый', 'White, black, brown, gray, piebald / tricolor combinations': 'Белый, чёрный, коричневый, серый, пегий / трёхцветные сочетания', 'Steel blue & Tan': 'Стально-голубой с подпалом'}

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

            short_updates = {
                "varieties_ru": VARIETIES,
                "country_ru": COUNTRY,
                "colors_ru": COLORS,
            }
            for fname, mapping in short_updates.items():
                count = 0
                for dog in Dogs.objects.all():
                    en = getattr(dog, fname[:-3])
                    ru = mapping.get(en)
                    if ru and not getattr(dog, fname):
                        setattr(dog, fname, ru)
                        dog.save(update_fields=[fname])
                        count += 1
                self.stdout.write(f"Dogs.{fname} filled: {count}")
