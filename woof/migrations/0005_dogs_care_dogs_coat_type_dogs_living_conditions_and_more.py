# Generated by Django 5.1 on 2024-08-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woof', '0004_rename_birth_date_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='care',
            field=models.TextField(blank=True, verbose_name='Уход'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='coat_type',
            field=models.CharField(choices=[('smooth', 'Smooth-haired'), ('curly', 'Curly'), ('long', 'Long-haired'), ('fluffy', 'Fluffy'), ('hairless', 'Hairless')], default='smooth', max_length=10, verbose_name='Тип шерсти'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='living_conditions',
            field=models.TextField(blank=True, verbose_name='Условия содержания'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='small', max_length=10, verbose_name='Размер'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
