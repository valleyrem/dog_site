# Woof Dogs — сайт о породах собак

Django-приложение каталога пород собак по группам FCI (woofdogs.world).

## Структура проекта

```
dog_site/
├── config/                # Конфигурация проекта (бывший dogsite/)
│   ├── settings.py        # Основные настройки, всё чувствительное — в .env
│   ├── settings_test.py   # SQLite-настройки для локального прогона тестов
│   ├── urls.py            # Корневые URL: admin, chaining, media, debug-toolbar
│   ├── wsgi.py, asgi.py   # Точки входа (gunicorn использует config.wsgi)
│   └── .env               # Переменные окружения (в git НЕ попадает)
│
├── woof/                  # Единственное приложение — весь бизнес
│   ├── models.py          # Dogs, Category, Section, DogImage, CoatType, CoatLength
│   ├── views.py           # StaticPageView, списки/карточки, breed API, контакт
│   ├── urls.py            # Все URL приложения
│   ├── forms.py           # ContactForm → отправка в Telegram (timeout 10с)
│   ├── utils.py           # DataMixin (общий контекст), меню, кэш категорий
│   ├── admin.py           # Админка: галереи-инлайны, фильтры, превью
│   ├── tests.py           # 12 smoke-тестов
│   ├── templatetags/      # (пусто — библиотеки выпилены как неиспользуемые)
│   ├── templates/woof/    # 23 шаблона
│   └── migrations/        # 16 миграций
│
├── templates/admin/       # Переопределение шаблона админки Django
│
├── static/                # ВСЯ статика-исходники (в git)
│   ├── fonts/             # ClashDisplay-*.woff2 — на них ссылается styles.css
│   ├── woof/css/          # styles.css, mobile.css, dark.css, admin.css
│   ├── woof/js/           # scripts.js
│   └── *.png, favicon.ico # Иллюстрации главной, слайдер (1–20.png), логотип
│
├── staticfiles/           # Генерится collectstatic'ом (НЕ в git)
├── media/                 # Пользовательский контент (см. раздел «Media»)
├── cache/                 # Файловый кэш Django (НЕ в git)
│
├── requirements.txt
├── Dockerfile             # python:3.13-slim, collectstatic при сборке, gunicorn
└── manage.py
```

## Директории static / staticfiles / media — в чём разница

Частая путаница, поэтому отдельно:

| Каталог | Что это | В git | Кто пишет |
|---|---|---|---|
| `static/` | **Исходники** статики: шрифты, css, js, картинки | да | человек |
| `staticfiles/` | **Продукт** `collectstatic`: копия всех исходников + админ-статика Django, сжатая и с content-hash в именах + `staticfiles.json` (манифест) | нет | collectstatic |
| `media/` | **Пользовательский контент**: фото собак, галереи, превьюшки imagekit | да (пока) | сайт при загрузке |

Цепочка работы статики:

```
static/  ──collectstatic──▶  staticfiles/  ◀── раздаёт whitenoise
                                     (при деплое / после правок css)
woof-админ-статика ─────────▶  staticfiles/admin/  (берётся из пакета Django,
                                в git её быть не должно)
```

Нюансы, на которые наступали:

- **`STATIC_ROOT = staticfiles/`**, а НЕ `static/`. Раньше было наоборот —
  collectstatic ссыпал выхлоп прямо в исходники (`static/admin/`,
  `static/CACHE/`), и этот мусор тащился в git. Вычищено.
- Правки css/js видны сразу только при `DEBUG=True`. В прод-режиме после
  правок нужен повторный `collectstatic` (в Docker это происходит на сборке).
- Манифест-хранилище (whitenoise) требует **наличия всех файлов**,
  на которые ссылается `{% static %}`. Ссылка на несуществующий путь
  (`css/admin.css` вместо `woof/css/admin.css`) даёт **500 на всей странице**
  в не-DEBUG режиме, а не тихую 404, как раньше. Это ловили в админке.
- Media в прод пока кладётся прямо в контейнер (`COPY . .` в Dockerfile
  не исключает media). В перспективе — объектное хранилище, volume или CDN.

## Media: почему в git, а превьюшки — нет

Git в текущий момент — **бэкап фотографий** (430 исходников в
`media/photos/` и `media/groups/`). Это временное решение до перехода на
нормальное хранилище, осознанное.

При этом `media/CACHE/` (превьюшки webp, которые imagekit генерит из
исходников) в `.gitignore` — они **пересоздаются автоматически** при
первом обращении, бэкапить их бессмысленно.

Грабля, на которую наступили: gitignore-правило `cache/` на macOS
(регистронезависимая FS) матчило и `media/CACHE/`. Поэтому правило
сужено до `/cache/` — игнорируется только файловый кэш Django в корне.

## Кэш

- Прод: `FileBasedCache` в `./cache/` (300 файлов `*.djcache`,
  в git НЕ попадают). Кэшируется список категорий на 15 минут
  (`DataMixin._get_categories`).
- Тесты: `LocMemCache` + `MEDIA_ROOT` во временный tempdir
  (`config/settings_test.py`) — иначе файловый кэш и превьюшки imagekit
  травят тесты между прогонами.

## Запуск локально

```bash
# venv на Python 3.13 (Django 6 будет требовать >=3.12, задел сделан)
.venv/bin/python manage.py migrate          # схема в postgres из .env

# Вариант 1: разработка (debug-toolbar, правки статики видны сразу)
DEBUG=True .venv/bin/python manage.py runserver

# Вариант 2: как прод, без дебага
.venv/bin/python manage.py collectstatic --noinput   # один раз / после правок css
.venv/bin/python manage.py runserver
```

Сайт — http://127.0.0.1:8000 (в `ALLOWED_HOSTS` из `.env` только он),
админка — /admin/. База — PostgreSQL, креды в `config/.env`.

## Тесты

Без postgres, на SQLite:

```bash
DJANGO_SETTINGS_MODULE=config.settings_test SECRET_KEY=test \
    .venv/bin/python manage.py test woof
```

## Деплой

Dockerfile: `python:3.13-slim`, при сборке образа выполняется
`collectstatic` (SECRET_KEY на шаге сборки — плейсхолдер, реальный
приезжает в рантайме), прод-сервер — **gunicorn** (3 воркера).
Старый вариант с `manage.py runserver` в прод-контейнере выпилен.

## Переменные окружения (config/.env)

| Переменная | Назначение |
|---|---|
| `SECRET_KEY` | ключ Django |
| `DEBUG` | True/False (по умолчанию False) |
| `ALLOWED_HOSTS` | список через запятую |
| `DATABASE_NAME/USER/PASS` | PostgreSQL |
| `DB_HOST/PORT` | PostgreSQL |
| `TOKEN`, `CHAT_ID` | Telegram-бот контактной формы |

`.env` читается из `config/.env` по явному пути (см. `settings.py`) —
не полагаемся на стек-магию django-environ.

## Технический долг / что дальше

- История git ~388 MB (старые media в коммитах). Чистка `git filter-repo`
  запланирована отдельной операцией, с зеркальным бэкапом и force-push.
  Media из текущего дерева при этом НЕ трогаем.
- `django-smart-selects` — библиотека без обновлений, проверена на
  Django 5.2 (виджет и /chaining/ работают), но однажды встанет вопрос
  замены на самописный JS-виджет.
- Media: переход с «git как бэкап» на объектное хранилище.
- Апгрейд до Django 6.0: требует Python >=3.12 (готово), deprecation-предупреждений
  в кодовой базе нет (проверено `-W error::DeprecationWarning`).
