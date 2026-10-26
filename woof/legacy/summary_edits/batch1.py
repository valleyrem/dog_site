"""Summary <-> History & origin: remove the repeated facts from the summaries.

Rule applied everywhere: the summary describes what a breed is like (look,
coat, temperament, needs, family fit); the History & origin band keeps the
country, the region, the dates, the creators and the original working
purpose.  Anything the History band already tells is therefore removed from
the summary and, where the sentence would become empty, replaced by a fact
about appearance, character or care.

Format: EDITS[language][slug] = [(text to find, text to put in its place)]
An empty replacement deletes the fragment (the trailing space is part of the
fragment on purpose, so no double space is left behind).

Run with:  python manage.py rebalance_texts
"""

EDITS = {
    "en": {
        "afghan-hound": [
            (
                "Originally bred for hunting large game in the mountains of Afghanistan, this breed combines speed, agility, and endurance.",
                "This breed combines speed, agility, and endurance, and its long coat needs regular brushing.",
            )
        ],
        "airedale-terrier": [
            (
                "Originally developed in England\u2019s Aire Valley, it was bred as an all-purpose working dog capable of hunting, guarding, and retrieving both on land and in water.",
                "It is an all-purpose dog that loves long walks, swimming, and any activity that keeps it busy beside its owner.",
            )
        ],
        "akita": [
            (
                "The Akita is a powerful and dignified breed from Japan, known",
                "The Akita is a powerful and dignified breed known",
            ),
            (
                "Once used by Japanese nobility for hunting large game such as bears, boars, and deer, the Akita has a strong prey drive and impressive physical prowess.",
                "The Akita has a strong prey drive and impressive physical prowess, and it needs an owner who is calm and consistent.",
            ),
            (
                "Beyond their working history, Akitas have become symbols of devotion and protection in Japanese culture — the famous story of Hachikō, an Akita who waited every day for his deceased owner at a train station, exemplifies their legendary loyalty. ",
                "",
            ),
        ],
        "alaskan-malamute": [
            (
                "The Alaskan Malamute is a strong and majestic Arctic breed, originally developed by the native Mahlemut tribe of Alaska to haul heavy sleds across long distances.",
                "The Alaskan Malamute is a strong and majestic Arctic breed built to haul heavy loads across long distances.",
            )
        ],
        "american-cocker-spaniel": [
            (
                "The Cocker Spaniel is a cheerful and affectionate sporting breed originally developed for flushing and retrieving game birds.",
                "The Cocker Spaniel is a compact, sturdy sporting breed that adapts well to family life.",
            ),
            (
                "It is the smallest spaniel It is the smallest spaniel recognized by the FCI",
                "It is the smallest spaniel recognized by the FCI",
            ),
        ],
        "american-eskimo-dog": [
            (
                "The breed comes in three size varieties: toy, miniature, and standard. The American Eskimo Dog is a small-to-medium spitz-type breed known for its striking white coat, intelligence, and lively personality. Despite its name, the breed originated from German Spitz dogs brought to the United States by immigrants. Eskies",
                "The American Eskimo Dog is a small-to-medium spitz-type breed known for its striking white coat, intelligence, and lively personality. It comes in three size varieties: toy, miniature, and standard. Eskies",
            )
        ],
        "american-staffordshire-terrier": [
            (
                "The American Staffordshire Terrier is a medium-sized, muscular and athletic breed developed in the United States from bull-and-terrier-type dogs.",
                "The American Staffordshire Terrier is a medium-sized, muscular and athletic breed with a broad head and a powerful, compact build.",
            )
        ],
        "anatolian-shepherd-dog": [
            (
                "The Anatolian Shepherd Dog is a large, powerful breed originally from Turkey, known",
                "The Anatolian Shepherd Dog is a large, powerful breed known",
            ),
            (
                "This breed was traditionally used to protect livestock, particularly sheep, from predators in the rugged terrain of Anatolia.",
                "It is at its best with plenty of space to patrol, a clear daily routine, and a real job to do.",
            ),
        ],
        "australian-shepherd": [
            (
                "Despite the name, the breed was actually developed in the United States to work as a herding dog, and its origins are somewhat debated. ",
                "",
            )
        ],
    },
    "ru": {
        "afghan-hound": [
            (
                "\u0412\u044b\u0432\u0435\u0434\u0435\u043d\u043d\u0430\u044f \u0434\u043b\u044f \u043e\u0445\u043e\u0442\u044b \u043d\u0430 \u043a\u0440\u0443\u043f\u043d\u0443\u044e \u0434\u0438\u0447\u044c \u0432 \u0433\u043e\u0440\u0430\u0445 \u0410\u0444\u0433\u0430\u043d\u0438\u0441\u0442\u0430\u043d\u0430, \u044d\u0442\u0430 \u043f\u043e\u0440\u043e\u0434\u0430 \u0441\u043e\u0447\u0435\u0442\u0430\u0435\u0442 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c, \u043b\u043e\u0432\u043a\u043e\u0441\u0442\u044c \u0438 \u0432\u044b\u043d\u043e\u0441\u043b\u0438\u0432\u043e\u0441\u0442\u044c.",
                "\u042d\u0442\u0430 \u043f\u043e\u0440\u043e\u0434\u0430 \u0441\u043e\u0447\u0435\u0442\u0430\u0435\u0442 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c, \u043b\u043e\u0432\u043a\u043e\u0441\u0442\u044c \u0438 \u0432\u044b\u043d\u043e\u0441\u043b\u0438\u0432\u043e\u0441\u0442\u044c, \u0430 \u0435\u0451 \u0434\u043b\u0438\u043d\u043d\u0443\u044e \u0448\u0435\u0440\u0441\u0442\u044c \u043d\u0443\u0436\u043d\u043e \u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e \u0440\u0430\u0441\u0447\u0451\u0441\u044b\u0432\u0430\u0442\u044c.",
            )
        ],
        "airedale-terrier": [
            (
                "\u0412\u044b\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0439 \u0432 \u0434\u043e\u043b\u0438\u043d\u0435 \u0440\u0435\u043a\u0438 \u042d\u0439\u0440 \u0432 \u0410\u043d\u0433\u043b\u0438\u0438, \u043e\u043d \u0431\u044b\u043b \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u0441\u043e\u0431\u0430\u043a\u043e\u0439, \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0439 \u043e\u0445\u043e\u0442\u0438\u0442\u044c\u0441\u044f, \u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u0438 \u043f\u043e\u0434\u0430\u0432\u0430\u0442\u044c \u0434\u0438\u0447\u044c \u043a\u0430\u043a \u043d\u0430 \u0441\u0443\u0448\u0435, \u0442\u0430\u043a \u0438 \u0432 \u0432\u043e\u0434\u0435.",
                "\u042d\u0442\u043e \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043e\u0431\u0430\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0443\u0436\u043d\u044b \u0434\u043e\u043b\u0433\u0438\u0435 \u043f\u0440\u043e\u0433\u0443\u043b\u043a\u0438, \u043f\u043b\u0430\u0432\u0430\u043d\u0438\u0435 \u0438 \u043b\u044e\u0431\u043e\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0435 \u0440\u044f\u0434\u043e\u043c \u0441 \u0445\u043e\u0437\u044f\u0438\u043d\u043e\u043c.",
            )
        ],
        "akita": [
            (
                "\u0410\u043a\u0438\u0442\u0430 \u2014 \u043c\u043e\u0449\u043d\u0430\u044f \u0438 \u0434\u043e\u0441\u0442\u043e\u0439\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430 \u0438\u0437 \u042f\u043f\u043e\u043d\u0438\u0438, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f",
                "\u0410\u043a\u0438\u0442\u0430 \u2014 \u043c\u043e\u0449\u043d\u0430\u044f \u0438 \u0434\u043e\u0441\u0442\u043e\u0439\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f",
            ),
            (
                "\u041a\u043e\u0433\u0434\u0430-\u0442\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0432\u0448\u0430\u044f\u0441\u044f \u044f\u043f\u043e\u043d\u0441\u043a\u043e\u0439 \u0437\u043d\u0430\u0442\u044c\u044e \u0434\u043b\u044f \u043e\u0445\u043e\u0442\u044b \u043d\u0430 \u043a\u0440\u0443\u043f\u043d\u0443\u044e \u0434\u0438\u0447\u044c \u2014 \u043c\u0435\u0434\u0432\u0435\u0434\u0435\u0439, \u043a\u0430\u0431\u0430\u043d\u043e\u0432 \u0438 \u043e\u043b\u0435\u043d\u0435\u0439, \u0430\u043a\u0438\u0442\u0430 \u043e\u0431\u043b\u0430\u0434\u0430\u0435\u0442 \u0441\u0438\u043b\u044c\u043d\u044b\u043c \u043e\u0445\u043e\u0442\u043d\u0438\u0447\u044c\u0438\u043c \u0438\u043d\u0441\u0442\u0438\u043d\u043a\u0442\u043e\u043c \u0438 \u0432\u043f\u0435\u0447\u0430\u0442\u043b\u044f\u044e\u0449\u0435\u0439 \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043c\u043e\u0449\u044c\u044e.",
                "\u0410\u043a\u0438\u0442\u0430 \u043e\u0431\u043b\u0430\u0434\u0430\u0435\u0442 \u0441\u0438\u043b\u044c\u043d\u044b\u043c \u043e\u0445\u043e\u0442\u043d\u0438\u0447\u044c\u0438\u043c \u0438\u043d\u0441\u0442\u0438\u043d\u043a\u0442\u043e\u043c \u0438 \u0432\u043f\u0435\u0447\u0430\u0442\u043b\u044f\u044e\u0449\u0435\u0439 \u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043c\u043e\u0449\u044c\u044e, \u0438 \u0435\u0439 \u043d\u0443\u0436\u0435\u043d \u0441\u043f\u043e\u043a\u043e\u0439\u043d\u044b\u0439, \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0432\u043b\u0430\u0434\u0435\u043b\u0435\u0446.",
            ),
            (
                "\u041f\u043e\u043c\u0438\u043c\u043e \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0438, \u0430\u043a\u0438\u0442\u044b \u0441\u0442\u0430\u043b\u0438 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u043c \u043f\u0440\u0435\u0434\u0430\u043d\u043d\u043e\u0441\u0442\u0438 \u0438 \u0437\u0430\u0449\u0438\u0442\u044b \u0432 \u044f\u043f\u043e\u043d\u0441\u043a\u043e\u0439 \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u0435 \u2014 \u0437\u043d\u0430\u043c\u0435\u043d\u0438\u0442\u0430\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0425\u0430\u0442\u0438\u043a\u043e, \u0430\u043a\u0438\u0442\u044b, \u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e \u0436\u0434\u0430\u0432\u0448\u0435\u0433\u043e \u0441\u0432\u043e\u0435\u0433\u043e \u0443\u043c\u0435\u0440\u0448\u0435\u0433\u043e \u0445\u043e\u0437\u044f\u0438\u043d\u0430 \u043d\u0430 \u0432\u043e\u043a\u0437\u0430\u043b\u0435, \u043e\u043b\u0438\u0446\u0435\u0442\u0432\u043e\u0440\u044f\u0435\u0442 \u0438\u0445 \u043b\u0435\u0433\u0435\u043d\u0434\u0430\u0440\u043d\u0443\u044e \u0432\u0435\u0440\u043d\u043e\u0441\u0442\u044c. ",
                "",
            ),
        ],
        "alaskan-malamute": [
            (
                "\u0410\u043b\u044f\u0441\u043a\u0438\u043d\u0441\u043a\u0438\u0439 \u043c\u0430\u043b\u0430\u043c\u0443\u0442 \u2014 \u0441\u0438\u043b\u044c\u043d\u0430\u044f \u0438 \u0432\u0435\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0430\u0440\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u0438\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u043d\u0430\u044f \u043a\u043e\u0440\u0435\u043d\u043d\u044b\u043c \u043f\u043b\u0435\u043c\u0435\u043d\u0435\u043c \u043c\u0430\u043b\u0435\u043c\u0443\u0442\u043e\u0432 \u043d\u0430 \u0410\u043b\u044f\u0441\u043a\u0435 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u043a\u0438 \u0442\u044f\u0436\u0451\u043b\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432 \u043d\u0430 \u0441\u0430\u043d\u044f\u0445 \u043d\u0430 \u0434\u0430\u043b\u044c\u043d\u0438\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f.",
                "\u0410\u043b\u044f\u0441\u043a\u0438\u043d\u0441\u043a\u0438\u0439 \u043c\u0430\u043b\u0430\u043c\u0443\u0442 \u2014 \u0441\u0438\u043b\u044c\u043d\u0430\u044f \u0438 \u0432\u0435\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0430\u0440\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u0430\u044f \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u0438\u0442\u044c \u0442\u044f\u0436\u0451\u043b\u044b\u0435 \u0433\u0440\u0443\u0437\u044b \u043d\u0430 \u0441\u0430\u043d\u044f\u0445 \u043d\u0430 \u0434\u0430\u043b\u044c\u043d\u0438\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f.",
            )
        ],
        "american-cocker-spaniel": [
            (
                "\u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0439 \u043a\u043e\u043a\u0435\u0440-\u0441\u043f\u0430\u043d\u0438\u0435\u043b\u044c \u2014 \u0436\u0438\u0437\u043d\u0435\u0440\u0430\u0434\u043e\u0441\u0442\u043d\u0430\u044f \u0438 \u043b\u0430\u0441\u043a\u043e\u0432\u0430\u044f \u043f\u043e\u0434\u0440\u0443\u0436\u0435\u0439\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u0438\u0437\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u043d\u0430\u044f \u0434\u043b\u044f \u043e\u0445\u043e\u0442\u044b \u043d\u0430 \u043f\u0442\u0438\u0446\u0443: \u0432\u0441\u043f\u0443\u0433\u0438\u0432\u0430\u043d\u0438\u044f \u0438 \u043f\u043e\u0434\u0430\u0447\u0438 \u0434\u0438\u0447\u0438.",
                "\u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0439 \u043a\u043e\u043a\u0435\u0440-\u0441\u043f\u0430\u043d\u0438\u0435\u043b\u044c \u2014 \u0436\u0438\u0437\u043d\u0435\u0440\u0430\u0434\u043e\u0441\u0442\u043d\u0430\u044f \u0438 \u043b\u0430\u0441\u043a\u043e\u0432\u0430\u044f \u043f\u043e\u0434\u0440\u0443\u0436\u0435\u0439\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0445\u043e\u0440\u043e\u0448\u043e \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u0436\u0438\u0437\u043d\u0438 \u0432 \u0441\u0435\u043c\u044c\u0435.",
            ),
            (
                "\u042d\u0442\u043e \u0441\u0430\u043c\u044b\u0439 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439 \u0441\u043f\u0430\u043d\u0438\u0435\u043b\u044c, \u042d\u0442\u043e \u0441\u0430\u043c\u044b\u0439 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439 \u0441\u043f\u0430\u043d\u0438\u0435\u043b\u044c, \u043f\u0440\u0438\u0437\u043d\u0430\u043d\u043d\u044b\u0439 FCI",
                "\u042d\u0442\u043e \u0441\u0430\u043c\u044b\u0439 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439 \u0441\u043f\u0430\u043d\u0438\u0435\u043b\u044c, \u043f\u0440\u0438\u0437\u043d\u0430\u043d\u043d\u044b\u0439 FCI",
            ),
            (
                " \u041c\u043d\u043e\u0433\u0438\u0435 \u043f\u043e\u0440\u043e\u0434\u044b \u0437\u0434\u0435\u0441\u044c \u043e\u0447\u0435\u043d\u044c \u043e\u0431\u0449\u0438\u0442\u0435\u043b\u044c\u043d\u044b \u0438 \u043b\u044e\u0431\u044f\u0442 \u0442\u0435\u0441\u043d\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443 \u0441 \u043b\u044e\u0434\u044c\u043c\u0438.",
                "",
            ),
        ],
        "american-eskimo-dog": [
            (
                "\u041f\u043e\u0440\u043e\u0434\u0430 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u0442\u0440\u0451\u0445 \u0440\u043e\u0441\u0442\u043e\u0432\u044b\u0445 \u0440\u0430\u0437\u043d\u043e\u0432\u0438\u0434\u043d\u043e\u0441\u0442\u044f\u0445: \u0442\u043e\u0439, \u043c\u0438\u043d\u0438\u0430\u0442\u044e\u0440\u043d\u0430\u044f \u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f. \u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u044d\u0441\u043a\u0438\u043c\u043e\u0441\u0441\u043a\u0430\u044f \u0441\u043e\u0431\u0430\u043a\u0430 \u2014 \u043f\u043e\u0440\u043e\u0434\u0430 \u0448\u043f\u0438\u0446\u0435\u0432\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0433\u043e \u0438\u043b\u0438 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f \u044d\u0444\u0444\u0435\u043a\u0442\u043d\u043e\u0439 \u0431\u0435\u043b\u043e\u0439 \u0448\u0435\u0440\u0441\u0442\u044c\u044e, \u0443\u043c\u043e\u043c \u0438 \u0436\u0438\u0432\u044b\u043c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043e\u043c. \u041d\u0435\u0441\u043c\u043e\u0442\u0440\u044f \u043d\u0430 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0440\u043e\u0434\u0430 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043e\u0442 \u043d\u0435\u043c\u0435\u0446\u043a\u0438\u0445 \u0448\u043f\u0438\u0446\u0435\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043f\u0440\u0438\u0432\u0435\u0437\u043b\u0438 \u0432 \u0421\u0428\u0410 \u0438\u043c\u043c\u0438\u0433\u0440\u0430\u043d\u0442\u044b. \u042d\u0441\u043a\u0438",
                "\u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u044d\u0441\u043a\u0438\u043c\u043e\u0441\u0441\u043a\u0430\u044f \u0441\u043e\u0431\u0430\u043a\u0430 \u2014 \u043f\u043e\u0440\u043e\u0434\u0430 \u0448\u043f\u0438\u0446\u0435\u0432\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0433\u043e \u0438\u043b\u0438 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f \u044d\u0444\u0444\u0435\u043a\u0442\u043d\u043e\u0439 \u0431\u0435\u043b\u043e\u0439 \u0448\u0435\u0440\u0441\u0442\u044c\u044e, \u0443\u043c\u043e\u043c \u0438 \u0436\u0438\u0432\u044b\u043c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043e\u043c. \u041e\u043d\u0430 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u0442\u0440\u0451\u0445 \u0440\u043e\u0441\u0442\u043e\u0432\u044b\u0445 \u0440\u0430\u0437\u043d\u043e\u0432\u0438\u0434\u043d\u043e\u0441\u0442\u044f\u0445: \u0442\u043e\u0439, \u043c\u0438\u043d\u0438\u0430\u0442\u044e\u0440\u043d\u0430\u044f \u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f. \u042d\u0441\u043a\u0438",
            )
        ],
        "american-staffordshire-terrier": [
            (
                "\u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0444\u0444\u043e\u0440\u0434\u0448\u0438\u0440\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u044c\u0435\u0440 \u2014 \u043c\u0443\u0441\u043a\u0443\u043b\u0438\u0441\u0442\u0430\u044f \u0438 \u0430\u0442\u043b\u0435\u0442\u0438\u0447\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430, \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u043d\u0430\u044f \u0432 \u0421\u0428\u0410 \u0438\u0437 \u0441\u043e\u0431\u0430\u043a \u0442\u0438\u043f\u0430 \u00ab\u0431\u044b\u043a-\u044d\u043d\u0434-\u0442\u0435\u0440\u044c\u0435\u0440\u00bb.",
                "\u0410\u043c\u0435\u0440\u0438\u043a\u0430\u043d\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0444\u0444\u043e\u0440\u0434\u0448\u0438\u0440\u0441\u043a\u0438\u0439 \u0442\u0435\u0440\u044c\u0435\u0440 \u2014 \u043c\u0443\u0441\u043a\u0443\u043b\u0438\u0441\u0442\u0430\u044f \u0438 \u0430\u0442\u043b\u0435\u0442\u0438\u0447\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0441 \u0448\u0438\u0440\u043e\u043a\u043e\u0439 \u0433\u043e\u043b\u043e\u0432\u043e\u0439 \u0438 \u043c\u043e\u0449\u043d\u044b\u043c \u043a\u043e\u043c\u043f\u0430\u043a\u0442\u043d\u044b\u043c \u0441\u043b\u043e\u0436\u0435\u043d\u0438\u0435\u043c.",
            )
        ],
        "anatolian-shepherd-dog": [
            (
                "\u0410\u043d\u0430\u0442\u043e\u043b\u0438\u0439\u0441\u043a\u0430\u044f \u043e\u0432\u0447\u0430\u0440\u043a\u0430 \u2014 \u043a\u0440\u0443\u043f\u043d\u0430\u044f, \u043c\u043e\u0449\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430 \u0440\u043e\u0434\u043e\u043c \u0438\u0437 \u0422\u0443\u0440\u0446\u0438\u0438, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f",
                "\u0410\u043d\u0430\u0442\u043e\u043b\u0438\u0439\u0441\u043a\u0430\u044f \u043e\u0432\u0447\u0430\u0440\u043a\u0430 \u2014 \u043a\u0440\u0443\u043f\u043d\u0430\u044f, \u043c\u043e\u0449\u043d\u0430\u044f \u043f\u043e\u0440\u043e\u0434\u0430, \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f",
            ),
            (
                "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043e\u043d\u043d\u043e \u044d\u0442\u0443 \u043f\u043e\u0440\u043e\u0434\u0443 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043b\u0438 \u0434\u043b\u044f \u0437\u0430\u0449\u0438\u0442\u044b \u0434\u043e\u043c\u0430\u0448\u043d\u0435\u0433\u043e \u0441\u043a\u043e\u0442\u0430, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u043e\u0432\u0435\u0446, \u043e\u0442 \u0445\u0438\u0449\u043d\u0438\u043a\u043e\u0432 \u0432 \u043f\u0435\u0440\u0435\u0441\u0435\u0447\u0451\u043d\u043d\u043e\u0439 \u043c\u0435\u0441\u0442\u043d\u043e\u0441\u0442\u0438 \u0410\u043d\u0430\u0442\u043e\u043b\u0438\u0438.",
                "\u0415\u0439 \u043d\u0443\u0436\u043d\u044b \u043f\u0440\u043e\u0441\u0442\u043e\u0440 \u0434\u043b\u044f \u00ab\u043e\u0431\u0445\u043e\u0434\u043e\u0432\u00bb, \u0447\u0451\u0442\u043a\u0438\u0439 \u0440\u0430\u0441\u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0434\u043d\u044f \u0438 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430.",
            ),
        ],
        "australian-shepherd": [
            (
                "\u041d\u0435\u0441\u043c\u043e\u0442\u0440\u044f \u043d\u0430 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0440\u043e\u0434\u0430 \u0431\u044b\u043b\u0430 \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u0430 \u0432 \u0421\u0428\u0410 \u043a\u0430\u043a \u043f\u0430\u0441\u0442\u0443\u0448\u044c\u044f \u0441\u043e\u0431\u0430\u043a\u0430, \u0438 \u0435\u0451 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0434\u043e \u0441\u0438\u0445 \u043f\u043e\u0440 \u0432\u044b\u0437\u044b\u0432\u0430\u0435\u0442 \u0441\u043f\u043e\u0440\u044b. ",
                "",
            )
        ],
    },
    "de": {
        "afghan-hound": [
            (
                "Ursprünglich gezüchtet für die Jagd auf Großwild in den Bergen Afghanistans, vereint diese Rasse Schnelligkeit, Wendigkeit und Ausdauer.",
                "Die Rasse vereint Schnelligkeit, Wendigkeit und Ausdauer, und ihr langes Fell muss regelmäßig gebürstet werden.",
            )
        ],
        "airedale-terrier": [
            (
                "Ursprünglich im Aire-Tal in England entwickelt, wurde er als Allround-Arbeitshund gezüchtet, der jagen, bewachen und sowohl an Land als auch im Wasser apportieren konnte.",
                "Er ist ein Allround-Hund, der lange Spaziergänge, Wasser und jede gemeinsame Aufgabe mit seinem Menschen liebt.",
            ),
            (" Viele Terrier graben gern, erkunden und sind ständig beschäftigt.", ""),
        ],
        "akita": [
            (
                "Der Akita ist eine kraftvolle und würdevolle Rasse aus Japan, bekannt",
                "Der Akita ist eine kraftvolle und würdevolle Rasse, bekannt",
            ),
            (
                "Einst von japanischen Adeligen zur Jagd auf Großwild wie Bären, Wildschweine und Hirsche eingesetzt, hat der Akita einen starken Jagdtrieb und beeindruckende körperliche Fähigkeiten.",
                "Der Akita hat einen starken Jagdtrieb und beeindruckende körperliche Fähigkeiten und braucht einen ruhigen, konsequenten Besitzer.",
            ),
            (
                "Über seine Arbeitsgeschichte hinaus sind Akitas in der japanischen Kultur zu Symbolen der Hingabe und des Schutzes geworden — die berühmte Geschichte von Hachikō, einem Akita, der täglich am Bahnhof auf seinen verstorbenen Besitzer wartete, veranschaulicht ihre legendäre Treue. ",
                "",
            ),
        ],
        "alaskan-malamute": [
            (
                "Der Alaskan Malamute ist eine kräftige und majestätische Arktis-Rasse, ursprünglich vom Mahlemut-Stamm Alaskas entwickelt, um schwere Schlitten über lange Strecken zu ziehen.",
                "Der Alaskan Malamute ist eine kräftige und majestätische Arktis-Rasse, gebaut, um schwere Schlitten über lange Strecken zu ziehen.",
            )
        ],
        "american-cocker-spaniel": [
            (
                "Der Amerikanische Cocker Spaniel ist eine fröhliche und anhängliche Jagdhundrasse, ursprünglich gezüchtet zum Aufstöbern und Apportieren von Federwild.",
                "Der Amerikanische Cocker Spaniel ist eine fröhliche und anhängliche Jagdhundrasse, die sich gut ins Familienleben einfügt.",
            ),
            (
                "Er ist der kleinste Er ist der kleinste von der FCI anerkannte Spaniel und verbindet kompakte Größe mit einer aktiven und verspielten Natur. kompakte Größe mit einer aktiven und verspielten Natur.",
                "Er ist der kleinste von der FCI anerkannte Spaniel und verbindet kompakte Größe mit einer aktiven und verspielten Natur.",
            ),
            (
                " Viele Rassen hier sind sehr sozial und arbeiten gern eng mit Menschen.",
                "",
            ),
        ],
        "american-eskimo-dog": [
            (
                "Die Rasse gibt es in drei Größen: Toy, Zwerg und Standard. Der American Eskimo Dog ist eine kleine bis mittelgroße Spitz-Rasse, bekannt für ihr auffälliges weißes Fell, ihre Intelligenz und ihr lebhaftes Wesen. Trotz des Namens stammt die Rasse von Deutschen Spitzen ab, die Einwanderer in die USA brachten. Eskies",
                "Der American Eskimo Dog ist eine kleine bis mittelgroße Spitz-Rasse, bekannt für ihr auffälliges weißes Fell, ihre Intelligenz und ihr lebhaftes Wesen. Die Rasse gibt es in drei Größen: Toy, Zwerg und Standard. Eskies",
            )
        ],
        "american-staffordshire-terrier": [
            (
                "Der American Staffordshire Terrier ist eine mittelgroße, muskulöse und athletische Rasse, in den USA aus Bull-and-Terrier-Hunden entwickelt.",
                "Der American Staffordshire Terrier ist eine mittelgroße, muskulöse und athletische Rasse mit breitem Kopf und kräftigem, kompaktem Körperbau.",
            )
        ],
        "anatolian-shepherd-dog": [
            (
                "Der Anatolische Hirtenhund ist eine große, kräftige Rasse aus der Türkei, bekannt",
                "Der Anatolische Hirtenhund ist eine große, kräftige Rasse, bekannt",
            ),
            (
                "Diese Rasse wurde traditionell eingesetzt, um Herden, besonders Schafe, in der rauen Landschaft Anatoliens vor Raubtieren zu schützen.",
                "Er braucht viel Platz zum Patrouillieren, einen klaren Tagesablauf und eine echte Aufgabe.",
            ),
        ],
        "australian-shepherd": [
            (
                "Trotz des Namens wurde die Rasse tatsächlich in den USA als Hütehund entwickelt; ihre Ursprünge sind umstritten. ",
                "",
            )
        ],
    },
    "it": {
        "afghan-hound": [
            (
                "Il Levriero Afgano è una delle razze più antiche ed eleganti del mondo, riconosciuta per il suo mantello lungo e setoso e per il portamento regale.",
                "Il Levriero Afgano è una razza elegante e regale, riconosciuta per il suo mantello lungo e setoso e per il portamento fiero.",
            ),
            (
                "Originario dell'Afghanistan, era usato per la caccia in terreni montuosi e desertici; la sua velocità e agilità sono eccezionali.",
                "La sua velocità e la sua agilità sono eccezionali, e il mantello lungo richiede spazzolature regolari.",
            ),
        ],
        "airedale-terrier": [
            (
                "è la più grande delle razze terrier, originaria della valle dell'Airedale in Inghilterra.",
                "è la più grande delle razze terrier, con un mantello ruvido e un carattere deciso.",
            ),
            (
                "È un cane versatile e intelligente, usato storicamente in guerra, in polizia e per la caccia.",
                "È un cane versatile e intelligente, che ama le lunghe camminate, l'acqua e ogni attività condivisa con il suo umano.",
            ),
        ],
        "akita": [
            (
                "L'Akita è una razza grande e potente, originaria del Giappone, dove è simbolo di fedeltà e coraggio.",
                "L'Akita è una razza grande e potente, simbolo di fedeltà e coraggio.",
            )
        ],
        "alaskan-malamute": [
            (
                "Il Malamute dell'Alaska è una razza grande e potente, sviluppata dagli Inuit per il traino delle slitte su lunghe distanze.",
                "Il Malamute dell'Alaska è una razza grande e potente, fatta per trainare slitte su lunghe distanze.",
            )
        ],
        "american-cocker-spaniel": [
            (
                "Originario degli Stati Uniti, è stato allevato per la caccia alla selvaggia di penna, ma oggi è soprattutto un cane da compagnia amato per il suo temperamento.",
                "Oggi è soprattutto un cane da compagnia, amato per il suo temperamento dolce e socievole.",
            )
        ],
        "american-eskimo-dog": [
            (
                "Nonostante il nome, è stato sviluppato negli Stati Uniti da discendenti dello spitz tedesco. ",
                "",
            )
        ],
        "american-staffordshire-terrier": [
            (
                "Nonostante la fama legata ai suoi antenati da combattimento, oggi è un cane da compagnia leale, coraggioso e pieno di energia, molto legato alla sua famiglia.",
                "Oggi è un cane da compagnia leale, coraggioso e pieno di energia, molto legato alla sua famiglia.",
            )
        ],
        "anatolian-shepherd-dog": [
            (
                "Il Pastore dell'Anatolia è una razza grande e potente, originaria della Turchia, dove è stata allevata per secoli a difendere il bestiame dai predatori.",
                "Il Pastore dell'Anatolia è una razza grande e potente, con un fisico robusto e un'espressione vigile.",
            )
        ],
        "australian-shepherd": [
            (
                "Il Pastore Australiano è una razza di taglia media, intelligente e piena di energia, nonostante il nome sia stato allevato negli Stati Uniti.",
                "Il Pastore Australiano è una razza di taglia media, intelligente e piena di energia.",
            )
        ],
    },
    "sr_latn": {
        "afghan-hound": [
            (
                "Prvobitno uzgajan za lov na krupnu divljač u planinama Avganistana, ova rasa kombinuje brzinu, spretnost i izdržljivost.",
                "Ova rasa kombinuje brzinu, spretnost i izdržljivost, a dugu dlaku treba redovno češljati.",
            )
        ],
        "airedale-terrier": [
            (
                "Prvobitno razvijen u engleskoj dolini Aire, uzgajan je kao višenamenski radni pas sposoban za lov, čuvanje i donošenje i na kopnu i u vodi.",
                "To je višenamenski pas koji voli duge šetnje, vodu i svaki zajednički zadatak sa svojim vlasnikom.",
            )
        ],
        "akita": [
            (
                "Akita je moćna i dostojanstvena rasa iz Japana, poznata",
                "Akita je moćna i dostojanstvena rasa, poznata",
            ),
            (
                "Nekada je japansko plemstvo koristilo akitu za lov na krupnu divljač poput medveda, veprova i jelena, pa akita ima snažan lovački nagon i impresivnu fizičku moć.",
                "Akita ima snažan lovački nagon i impresivnu fizičku moć, i potreban joj je smiren i dosledan vlasnik.",
            ),
            (
                "Pored radne istorije, akite su postale simboli odanosti i zaštite u japanskoj kulturi — čuvena priča o Hačikou, akiti koja je svakog dana čekala svog preminulog vlasnika na železničkoj stanici, svedoči o njihovoj legendarnoj odanosti. ",
                "",
            ),
        ],
        "alaskan-malamute": [
            (
                "Aljaški malamut je snažna i veličanstvena arktička rasa, prvobitno razvijena od strane plemena Mahlemut sa Aljaske za vuču teških saonica na velikim udaljenostima.",
                "Aljaški malamut je snažna i veličanstvena arktička rasa, sposobna da vuče teška saonica na velikim udaljenostima.",
            )
        ],
        "american-cocker-spaniel": [
            (
                "Koker španijel je vedra i privržena lovna rasa, prvobitno razvijena za plašenje i donošenje lovne divljači.",
                "Koker španijel je vedra i privržena lovna rasa koja se dobro uklapa u porodični život.",
            ),
            (
                "Najmanji je španijel Najmanji je španijel koji priznaje FCI",
                "Najmanji je španijel koji priznaje FCI",
            ),
        ],
        "american-eskimo-dog": [
            (
                "Rasa dolazi u tri veličine: toy, minijaturna i standardna.\nAmerički eskimski pas je rasa tipa špica male do srednje veličine, poznata po upadljivoj beloj dlaci, inteligenciji i živahnoj ličnosti. Uprkos imenu, rasa potiče od nemačkih špiceva koje su u Sjedinjene Američke Države doneli imigranti. Eskimi",
                "Američki eskimski pas je rasa tipa špica male do srednje veličine, poznata po upadljivoj beloj dlaci, inteligenciji i živahnoj ličnosti. Dolazi u tri veličine: toy, minijaturna i standardna. Eskimi",
            )
        ],
        "american-staffordshire-terrier": [
            (
                "Američki stafordšir terijer je rasa srednje veličine, mišićava i atletska, razvijena u Sjedinjenim Američkim Državama od pasa tipa bul terijer.",
                "Američki stafordšir terijer je rasa srednje veličine, mišićava i atletska, sa širokom glavom i snažnom, kompaktnom građom.",
            )
        ],
        "anatolian-shepherd-dog": [
            (
                "Anatolski ovčar je velika, moćna rasa poreklom iz Turske, poznata",
                "Anatolski ovčar je velika, moćna rasa, poznata",
            ),
            (
                "Ova rasa se tradicionalno koristila za zaštitu stoke, posebno ovaca, od predatora u krševitom terenu Anadolije.",
                "Potreban mu je prostor za obilazak, jasan dnevni ritam i pravi zadatak.",
            ),
        ],
        "australian-shepherd": [
            (
                "Uprkos imenu, rasa je zapravo razvijena u Sjedinjenim Američkim Državama kao pastirski pas, a njeno poreklo je delom sporno. ",
                "",
            )
        ],
    },
}
