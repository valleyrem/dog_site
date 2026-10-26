"""The site's content: every translated text, in one place.

Two generated modules (see ``tools/build_content.py``):

  breeds      -- per-slug breed texts, traits, concrete fields and relations
  vocabulary  -- translated names of the dictionaries (groups, sections,
                 countries, coat types/lengths, temperaments)

Applied idempotently by ``manage.py fill_content``. The database stays the
source of truth for what visitors see; these modules are the reproducible
copy that a fresh install (or a new breed) can be filled from.
"""

from .breeds import BREEDS
from .vocabulary import VOCABULARY

__all__ = ["BREEDS", "VOCABULARY"]
