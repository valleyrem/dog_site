"""Archived one-off content scripts (not registered as management commands).

These modules were used to fill and re-balance breed content while the site
was being built. Their *result* now lives in two places:

  * the database (source of truth for what visitors see),
  * ``woof/content/`` — one module with every text, applied by
    ``manage.py fill_content``.

So nothing here is needed to run or deploy the site; the files are kept only
because they document how the texts were derived. They are plain modules: to
run one, copy it back into ``woof/management/commands/`` first.
"""
