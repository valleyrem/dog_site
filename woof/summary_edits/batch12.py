"""Batch 12: the last 13 places where a summary still echoed the History band."""

EDITS = {
    "ru": {
        "alaskan-malamute": [
            (
                "маламуты — одна из древнейших ездовых пород",
                "маламуты — одна из самых выносливых ездовых пород",
            )
        ]
    },
    "it": {
        "afghan-hound": [
            (
                "richiede comprensione della sua natura antica e nobile",
                "richiede comprensione della sua natura indipendente e nobile",
            )
        ],
        "azawakh": [
            (
                "L'Azawakh è un levriero africano antico ed elegante, dal fisico asciutto e leggero.",
                "L'Azawakh è un levriero elegante dal fisico asciutto e leggero.",
            )
        ],
        "barbado-da-terceira": [
            (
                "è una razza da lavoro antica e ancora poco diffusa",
                "è una razza da lavoro ancora poco diffusa",
            )
        ],
        "pekingese": [
            (
                "Il Pechinese è una razza antica e regale",
                "Il Pechinese è una razza regale",
            )
        ],
        "shih-tzu": [
            (" È stato allevato esclusivamente come cane da compagnia.", ""),
        ],
        "yakutian-laika": [
            (
                "La Laika della Jacuzia è un'antica razza siberiana, sviluppata per il traino delle slitte, la caccia e la sopravvivenza in condizioni artiche estreme.",
                "La Laika della Jacuzia è una razza forte e resistente.",
            )
        ],
    },
    "sr_latn": {
        "borzoi": [
            (
                "Uprkos lovačkom poreklu, borzoji nisu preterano agresivni",
                "Uprkos snažnom instinktu, borzoji nisu preterano agresivni",
            )
        ],
        "collie-rough": [
            (
                "Uprkos radnom poreklu, kolije su privrženi i nježni saputnici",
                "Kolije su privrženi i nježni saputnici",
            )
        ],
        "kleiner-munsterlander": [
            (
                "Njegovo radno poreklo čini ga prirodno budnim, fokusiranim i vođenim mirisima i pokretom.",
                "Prirodno je budan, fokusiran i vođen mirisima i pokretom.",
            )
        ],
        "portuguese-podengo": [
            (
                "Uprkos radnom poreklu, podengo pekeno je i privržen i razigran saputnik",
                "Podengo pekeno je i privržen i razigran saputnik",
            )
        ],
        "rat-terrier": [
            (
                "kombinujući radno poreklo sa prijateljskim i društvenim temperamentom",
                "kombinujući radne sposobnosti sa prijateljskim i društvenim temperamentom",
            )
        ],
        "yakutian-laika": [
            (
                "Uprkos radnom poreklu, poznat je po tome što je privržen",
                "Poznat je po tome što je privržen",
            )
        ],
    },
}

# last duplicate left in Italian (samoyed / yakutian-laika shared one sentence)
EDITS["it"]["yakutian-laika"] = [
    (
        "È affettuoso, socievole e molto legato alla famiglia.",
        "È molto legato alla sua famiglia e cerca sempre la compagnia dei suoi umani.",
    )
]
