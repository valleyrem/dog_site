from django.db import migrations

from ._purposes import LANGS
from ._sum_a import SUMMARIES_A
from ._sum_b import SUMMARIES_B
from ._sum_c import SUMMARIES_C
from ._sum_d import SUMMARIES_D

SUMMARIES = {**SUMMARIES_A, **SUMMARIES_B, **SUMMARIES_C, **SUMMARIES_D}


def apply(apps, schema_editor):
    Dogs = apps.get_model("woof", "Dogs")
    for slug, texts in SUMMARIES.items():
        Dogs.objects.filter(slug=slug).update(
            **{f"summary_{lang}": text for lang, text in zip(LANGS, texts)}
        )


class Migration(migrations.Migration):
    dependencies = [("woof", "0104_fill_purposes")]

    operations = [migrations.RunPython(apply, migrations.RunPython.noop)]
