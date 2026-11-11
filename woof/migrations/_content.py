LABELS = {
    "en": ["Walks", "Being alone", "At home", "Children", "Other animals", "Play and activities", "Daily routine"],
    "ru": ["Прогулки", "Одиночество", "Дома", "Дети", "Другие животные", "Игры и занятия", "Распорядок дня"],
}

FIELDS = ("summary", "care", "good_fit", "think_twice", "daily_life", "quirks")


def apply_content(apps, dogs):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, data in dogs.items():
        values = {"prey_drive": data["prey"]}
        for lang in ("en", "ru"):
            block = data[lang]
            texts = {
                "summary": block["summary"],
                "care": "\n".join(block["care"]),
                "good_fit": "\n".join(block["good_fit"]),
                "think_twice": "\n".join(block["think_twice"]),
                "daily_life": "\n\n".join(f"{l}: {t}" for l, t in zip(LABELS[lang], block["daily"])),
                "quirks": "\n".join(block["quirks"]),
            }
            for field, text in texts.items():
                values[f"{field}_{lang}"] = text
                if lang == "en":
                    values[field] = text
        for lang in ("de", "it", "es", "sr_latn"):
            for field in FIELDS:
                values[f"{field}_{lang}"] = ""
        Dogs.objects.filter(slug=slug).update(**values)


TR_LABELS = {
    "de": ["Spaziergänge", "Alleinsein", "Zu Hause", "Kinder", "Andere Tiere", "Spiel und Beschäftigung", "Tagesablauf"],
    "it": ["Passeggiate", "Da solo", "In casa", "Bambini", "Altri animali", "Gioco e attività", "Routine quotidiana"],
    "es": ["Paseos", "Quedarse solo", "En casa", "Niños", "Otros animales", "Juegos y actividades", "Rutina diaria"],
    "sr_latn": ["Šetnje", "Boravak sam", "Kod kuće", "Deca", "Druge životinje", "Igra i aktivnosti", "Dnevna rutina"],
}


def apply_translations(apps, translations):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, langs in translations.items():
        values = {}
        for lang, (summary, care, good_fit, think_twice, daily, quirks) in langs.items():
            values[f"summary_{lang}"] = summary
            values[f"care_{lang}"] = "\n".join(care)
            values[f"good_fit_{lang}"] = "\n".join(good_fit)
            values[f"think_twice_{lang}"] = "\n".join(think_twice)
            values[f"daily_life_{lang}"] = "\n\n".join(f"{l}: {t}" for l, t in zip(TR_LABELS[lang], daily))
            values[f"quirks_{lang}"] = "\n".join(quirks)
        Dogs.objects.filter(slug=slug).update(**values)
