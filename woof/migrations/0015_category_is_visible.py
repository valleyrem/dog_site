# Generated by Django 5.1 on 2024-08-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woof', '0014_dogs_activity_level_dogs_trainability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
