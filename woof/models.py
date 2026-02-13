from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class Dogs(models.Model):
    BARKING_CHOICES = [
        ('necessary', 'When necessary (rare, purposeful)'),
        ('infrequent', 'Infrequent (occasional barking)'),
        ('medium', 'Medium (regular alert barking)'),
        ('frequent', 'Frequent (barks often)'),
        ('vocal', 'Very vocal (howls, talks, barks)'),
    ]

    SIZE_CHOICES = [
        ('xsmall', 'XSmall'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xlarge', 'XLarge'),
    ]

    SIZE_INDEX = {
        'xsmall': 1,
        'small': 2,
        'medium': 3,
        'large': 4,
        'xlarge': 5,
    }


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
        ('double', 'Double Coat'),
    ]

    TRAINABILITY_CHOICES = [
        ('independent', 'Independent (thinks for itself)'),
        ('stubborn', 'May be stubborn (patience)'),
        ('agreeable', 'Agreeable (trainable)'),
        ('eager', 'Eager to please (quick learner)'),
        ('easy', 'Easy training (very easy to train)'),
    ]

    ACTIVITY_CHOICES = [
        ('calm', 'Calm (low energy)'),
        ('regular', 'Regular exercise (daily walks)'),
        ('high', 'Needs lots of activity'),
        ('energetic', 'Very energetic (high endurance)'),
    ]

    HYPOALLERGENIC_CHOICES = [
        ('no', 'No (not hypoallergenic)'),
        ('low', 'Low (sheds a lot)'),
        ('moderate', 'Moderate (some shedding)'),
        ('high', 'High (minimal shedding)'),
    ]

    FAMILY_FRIENDLINESS_CHOICES = [
        ('low', 'Low (better with adults, limited tolerance)'),
        ('medium', 'Medium (family-oriented, needs supervision)'),
        ('high', 'High (affectionate, good with family)'),
        ('excellent', 'Excellent (very gentle, great with kids)'),
    ]

    # main
    title = models.CharField(max_length=255, verbose_name="Breed")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name="Group"
    )

    # photo
    photo = models.ImageField( upload_to="photos/%Y/%m/%d/",verbose_name="Main photo")
    photo_author = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Main photo author"
    )

    # characteristics
    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default='small',
        verbose_name="Size"
    )

    coat_type = models.CharField(
        max_length=15,
        choices=COAT_CHOICES,
        default='short',
        verbose_name="Coat type"
    )

    coat_length = models.CharField(
        max_length=10,
        choices=COAT_LENGTH_CHOICES,
        default='short',
        verbose_name="Coat length"
    )

    trainability = models.CharField(
        max_length=15,
        choices=TRAINABILITY_CHOICES,
        default='independent',
        verbose_name="Trainability"
    )

    activity_level = models.CharField(
        max_length=15,
        choices=ACTIVITY_CHOICES,
        default='calm',
        verbose_name="Activity level"
    )

    barking_level = models.CharField(
        max_length=20,
        choices=BARKING_CHOICES,
        default='necessary',
        verbose_name="Barking level"
    )

    family_friendliness = models.CharField(
        max_length=10,
        choices=FAMILY_FRIENDLINESS_CHOICES,
        default='medium',
        verbose_name="Family friendliness"
    )

    hypoallergenic = models.CharField(
        max_length=10,
        choices=HYPOALLERGENIC_CHOICES,
        default='no',
        verbose_name="Hypoallergenic"
    )

    life_expectancy = models.CharField(max_length=255, blank=True, verbose_name="Life expectancy")
    height = models.CharField(max_length=255, blank=True, verbose_name="Height")
    weight = models.CharField(max_length=255, blank=True, verbose_name="Weight")
    colors = models.CharField(max_length=255, blank=True, verbose_name="Colors")

    #description
    summary = models.TextField(blank=True, verbose_name="Summary")
    care = models.TextField(blank=True, verbose_name="Care")
    living_conditions = models.TextField(blank=True, verbose_name="Conditions")

    # general
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time updated")
    is_published = models.BooleanField(default=True, verbose_name="Published")


    def __str__(self):
        return self.title

    @property
    def size_index(self):
        return self.SIZE_INDEX.get(self.size, 1)

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


class DogImage(models.Model):
    dog = models.ForeignKey(
        Dogs,
        related_name='gallery',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='photos/dogs/gallery/')
    author = models.CharField(max_length=255, blank=True, verbose_name="Photo Author")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Dog photo'
        verbose_name_plural = 'Dog photos'

    def __str__(self):
        return f"{self.dog.title} photo"

