"""Summary <-> History & origin: the text replacements that remove repeated facts.

The rule applied everywhere: the summary tells what a breed is like (look,
coat, temperament, needs, family fit); the History & origin band keeps the
country, the region, the dates, the creators and the original working
purpose.  Facts the History band already tells are removed from the summary
and, where a sentence would become empty, replaced by a fact about
appearance, character or care.

The pairs are split over per-batch modules only to keep each file readable;
they are merged here into one mapping:

    EDITS[language][slug] = [(text to find, text to put in its place), ...]

Run with:  python manage.py rebalance_texts
"""

from importlib import import_module

BATCHES = tuple("batch%d" % n for n in range(1, 21))

EDITS = {}


def _merge(edits):
    for lang, dogs in edits.items():
        target = EDITS.setdefault(lang, {})
        for slug, pairs in dogs.items():
            target.setdefault(slug, []).extend(pairs)


for _name in BATCHES:
    try:
        _module = import_module("woof.summary_edits.%s" % _name)
    except ModuleNotFoundError:
        continue
    _merge(_module.EDITS)
