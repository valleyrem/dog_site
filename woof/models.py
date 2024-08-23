from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Dogs(models.Model):
    SIZE_CHOICES = [
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('giant', 'Giant'),
    ]

    COAT_CHOICES = [
        ('curly', 'Curly'),
        ('double', 'Double Coat'),
        ('fluffy', 'Fluffy'),
        ('hairless', 'Hairless'),
        ('long', 'Long-haired'),
        ('rough', 'Rough-haired'),
        ('silky', 'Silky'),
        ('smooth', 'Smooth-haired'),
        ('wire', 'Wire-haired')
    ]

    title = models.CharField(max_length=255, verbose_name="Вreed")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Summary")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name="Size", default='small')
    coat_type = models.CharField(max_length=10, choices=COAT_CHOICES, verbose_name="Coat type", default='smooth')
    care = models.TextField(blank=True, verbose_name="Care")
    living_conditions = models.TextField(blank=True, verbose_name="Conditions")
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class CoatType(models.Model):
    name = models.CharField(max_length=20, choices=[
        ('curly', 'Curly'),
        ('double', 'Double Coat'),
        ('fluffy', 'Fluffy'),
        ('hairless', 'Hairless'),
        ('long', 'Long-haired'),
        ('rough', 'Rough-haired'),
        ('silky', 'Silky'),
        ('smooth', 'Smooth-haired'),
        ('wire', 'Wire-haired')
    ])

    def __str__(self):
        return self.get_name_display()
