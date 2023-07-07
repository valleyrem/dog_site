# Generated by Django 4.2.2 on 2023-07-03 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('woof', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dogs',
            options={'ordering': ['id'], 'verbose_name': 'Породы собак', 'verbose_name_plural': 'Породы собак'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('bio', models.TextField()),
                ('article_count', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
