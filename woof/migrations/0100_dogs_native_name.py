from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("woof", "0099_belgian_shepherd_summary")]

    operations = [
        migrations.AddField(
            model_name="dogs",
            name="native_name",
            field=models.CharField(
                blank=True,
                help_text="Name in the country of origin (FCI original name). Not translated.",
                max_length=120,
                verbose_name="Native name",
            ),
        ),
    ]
