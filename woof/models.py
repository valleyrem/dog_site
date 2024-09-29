from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Dogs(models.Model):
    BARKING_CHOICES = [
        ('necessary', 'When Necessary'),
        ('infrequent', 'Infrequent'),
        ('medium', 'Medium'),
        ('frequent', 'Frequent'),
        ('vocal', 'Likes To Be Vocal'),
    ]
    SIZE_CHOICES = [
        ('xsmall', 'XSmall'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xlarge', 'XLarge'),
    ]
    COAT_LENGTH_CHOICES = [
        ('short', 'Short'),
        ('medium', 'Medium'),
        ('long', 'Long'),
    ]
    COAT_CHOICES = [
        ('curly', 'Curly'),
        ('wavy', 'Wavy'),
        ('rough', 'Rough-haired'),
        ('corded', 'Corded'),
        ('hairless', 'Hairless'),
        ('short', 'Short-haired'),
        ('medium', 'Medium-haired'),
        ('long', 'Long-haired'),
        ('smooth', 'Smooth-haired'),
        ('wiry', 'Wiry'),
        ('silky', 'Silky'),
        ('double', 'Double Coat')
    ]
    TRAINABILITY_CHOICES = [
        ('independent', 'Independent'),
        ('eager', 'Eager To Please'),
        ('agreeable', 'Agreeable'),
        ('stubborn', 'May Be Stubborn'),
        ('easy', 'Easy Training'),
    ]
    ACTIVITY_CHOICES = [
        ('calm', 'Calm'),
        ('regular', 'Regular Exercise'),
        ('high', 'Needs Lots Of Activity'),
        ('energetic', 'Energetic'),
    ]

    user_email = models.EmailField(blank=True, default='', verbose_name="User Email")
    title = models.CharField(max_length=255, verbose_name="Вreed")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Summary")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name="Size", default='small')
    coat_type = models.CharField(max_length=10, choices=COAT_CHOICES, verbose_name="Coat type", default='cirly')
    care = models.TextField(blank=True, verbose_name="Care")
    living_conditions = models.TextField(blank=True, verbose_name="Conditions")
    trainability = models.CharField(max_length=11, choices=TRAINABILITY_CHOICES,verbose_name="Trainability", default='independent')
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_CHOICES, verbose_name="Activity Level", default='calm')
    coat_length = models.CharField(max_length=10, choices=COAT_LENGTH_CHOICES, verbose_name="Coat length", default='short')
    barking_level = models.CharField(max_length=20, choices=BARKING_CHOICES, verbose_name="Barking level", default='necessary')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time update")
    is_published = models.BooleanField(default=True, verbose_name="Published")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Group")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Dog breed'
        verbose_name_plural = 'Dog breeds'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    desc = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
