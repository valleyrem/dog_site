# Generated by Django 5.1 on 2024-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woof', '0022_dogs_barking_level_dogs_coat_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='activity_level',
            field=models.CharField(choices=[('calm', 'Calm'), ('regular', 'Regular Exercise'), ('high', 'Needs Lots Of Activity'), ('energetic', 'Energetic')], default='calm', max_length=10, verbose_name='Activity Level'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='barking_level',
            field=models.CharField(choices=[('necessary', 'When Necessary'), ('infrequent', 'Infrequent'), ('medium', 'Medium'), ('frequent', 'Frequent'), ('vocal', 'Likes To Be Vocal')], default='necessary', max_length=20, verbose_name='Barking level'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='trainability',
            field=models.CharField(choices=[('independent', 'Independent'), ('eager', 'Eager To Please'), ('agreeable', 'Agreeable'), ('stubborn', 'May Be Stubborn'), ('easy', 'Easy Training')], default='independent', max_length=11, verbose_name='Trainability'),
        ),
    ]