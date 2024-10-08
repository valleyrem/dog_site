# Generated by Django 5.1 on 2024-08-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woof', '0008_remove_dogs_coat_types_dogs_coat_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coattype',
            name='name',
            field=models.CharField(choices=[('smooth', 'Smooth-haired'), ('curly', 'Curly'), ('long', 'Long-haired'), ('fluffy', 'Fluffy'), ('hairless', 'Hairless'), ('wirehaired', 'Wirehaired'), ('silky', 'Silky'), ('double', 'Double Coat')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='coat_type',
            field=models.CharField(choices=[('smooth', 'Smooth-haired'), ('curly', 'Curly'), ('long', 'Long-haired'), ('fluffy', 'Fluffy'), ('hairless', 'Hairless'), ('wirehaired', 'Wirehaired'), ('silky', 'Silky'), ('double', 'Double Coat')], default='smooth', max_length=10, verbose_name='Coat type'),
        ),
    ]
