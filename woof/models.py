from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from smart_selects.db_fields import ChainedForeignKey


class CoatType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CoatLength(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Temperament(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    """Country of origin for breeds.

    The base ``name`` field holds the English spelling; translations
    (``name_ru``, ``name_de``, ...) are added by django-modeltranslation,
    so choosing a country once in English shows it translated on the site
    in every language automatically.
    """

    name = models.CharField(
        max_length=100, unique=True, db_index=True, verbose_name="Country"
    )
    sort_order = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Country of origin"
        verbose_name_plural = "Countries of origin"


class NativeLanguage(models.Model):
    """Language of a breed's native name, shown after it: "Deutscher Boxer (German)".

    The base ``name`` holds the English spelling; modeltranslation adds the
    other languages, so it is chosen once from a list and shows translated
    on the site everywhere.
    """

    name = models.CharField(
        max_length=60, unique=True, db_index=True, verbose_name="Language"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Native name language"
        verbose_name_plural = "Native name languages"


class Dogs(models.Model):
    BARKING_CHOICES = [
        ("necessary", _("When necessary (rare, purposeful)")),
        ("infrequent", _("Infrequent (occasional barking)")),
        ("medium", _("Medium (regular alert barking)")),
        ("frequent", _("Frequent (barks often)")),
        ("vocal", _("Very vocal (howls, talks, barks)")),
    ]

    SIZE_CHOICES = [
        ("small", _("Small")),
        ("medium", _("Medium")),
        ("large", _("Large")),
    ]

    SIZE_INDEX = {
        "small": 1,
        "medium": 2,
        "large": 3,
    }

    TRAINABILITY_CHOICES = [
        ("independent", _("Independent (thinks for itself)")),
        ("stubborn", _("May be stubborn (patience)")),
        ("agreeable", _("Agreeable (trainable)")),
        ("eager", _("Eager to please (quick learner)")),
        ("easy", _("Easy training (very easy to train)")),
    ]

    ACTIVITY_CHOICES = [
        ("calm", _("Calm (low energy)")),
        ("regular", _("Regular exercise (daily walks)")),
        ("high", _("Needs lots of activity")),
        ("energetic", _("Very energetic (high endurance)")),
    ]

    # The field measures shedding, so the labels say so: "hypoallergenic" is a
    # medical promise a database cannot keep.
    HYPOALLERGENIC_CHOICES = [
        ("no", _("Heavy shedding")),
        ("low", _("Noticeable shedding")),
        ("moderate", _("Moderate shedding")),
        ("high", _("Minimal shedding")),
    ]

    FAMILY_FRIENDLINESS_CHOICES = [
        ("low", _("Low (better with adults, limited tolerance)")),
        ("medium", _("Medium (family-oriented, needs supervision)")),
        ("high", _("High (affectionate, good with family)")),
        ("excellent", _("Excellent (very gentle, great with kids)")),
    ]

    PREY_CHOICES = [
        ("low", _("Low")),
        ("moderate", _("Moderate")),
        ("high", _("High (chases small animals)")),
    ]

    # main
    title = models.CharField(max_length=255, verbose_name="Breed")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Group")

    section = ChainedForeignKey(
        "Section",
        chained_field="cat",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True,
        verbose_name="Section",
    )

    varieties = models.CharField(max_length=255, blank=True, verbose_name="Varieties")

    country = models.ForeignKey(
        "Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dogs",
        verbose_name="Country of origin",
    )

    native_name = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Native name",
        help_text="Name in the country of origin (FCI original name). Not translated.",
    )

    # photo
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Main photo")

    photo_thumb = ImageSpecField(
        source="photo",
        processors=[ResizeToFill(400, 300)],
        format="WEBP",
        options={"quality": 90},
    )

    photo_medium = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(1200, 800)],
        format="WEBP",
        options={"quality": 90},
    )

    photo_card = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(700, 500)],
        format="WEBP",
        options={"quality": 82},
    )

    native_language = models.ForeignKey(
        NativeLanguage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dogs",
        verbose_name="Native name language",
    )

    fci_standard = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="FCI standard number",
        help_text="Official FCI breed number. Leave empty for breeds outside the FCI.",
    )

    photo_author = models.CharField(
        max_length=255, blank=True, verbose_name="Main photo author"
    )

    # characteristics
    size = models.CharField(
        max_length=30, choices=SIZE_CHOICES, default="small", verbose_name="Size"
    )

    coat_type = models.ManyToManyField(CoatType, blank=True, verbose_name="Coat type")

    coat_length = models.ManyToManyField(
        CoatLength, blank=True, verbose_name="Coat length"
    )

    temperament = models.ManyToManyField(
        "Temperament", blank=True, verbose_name="Character (temperament)"
    )

    trainability = models.CharField(
        max_length=15,
        choices=TRAINABILITY_CHOICES,
        default="independent",
        verbose_name="Trainability",
    )

    activity_level = models.CharField(
        max_length=15,
        choices=ACTIVITY_CHOICES,
        default="calm",
        verbose_name="Activity level",
    )

    barking_level = models.CharField(
        max_length=20,
        choices=BARKING_CHOICES,
        default="necessary",
        verbose_name="Barking level",
    )

    family_friendliness = models.CharField(
        max_length=10,
        choices=FAMILY_FRIENDLINESS_CHOICES,
        default="medium",
        verbose_name="Family friendliness",
    )

    hypoallergenic = models.CharField(
        max_length=10,
        choices=HYPOALLERGENIC_CHOICES,
        default="no",
        verbose_name="Shedding",
    )

    life_expectancy = models.CharField(
        max_length=255, blank=True, verbose_name="Life expectancy"
    )
    height_male = models.CharField(
        max_length=50, blank=True, verbose_name="Height, male (cm)"
    )
    height_female = models.CharField(
        max_length=50, blank=True, verbose_name="Height, female (cm)"
    )
    weight_male = models.CharField(
        max_length=50, blank=True, verbose_name="Weight, male (kg)"
    )
    weight_female = models.CharField(
        max_length=50, blank=True, verbose_name="Weight, female (kg)"
    )
    colors = models.CharField(max_length=255, blank=True, verbose_name="Colors")

    # description
    summary = models.TextField(blank=True, verbose_name="Summary")
    history = models.TextField(blank=True, verbose_name="History & origin")
    care = models.TextField(blank=True, verbose_name="Care")
    good_fit = models.TextField(
        blank=True,
        verbose_name="Good fit if",
        help_text="One short point per line.",
    )
    think_twice = models.TextField(
        blank=True,
        verbose_name="Think twice if",
        help_text="One short point per line.",
    )
    daily_life = models.TextField(
        blank=True,
        verbose_name="A day with the breed",
        help_text='One line per topic, written as "Walks: ..." (the part before the colon is bold). '
        'Start a line with "- " for a bullet; **word** is bold.',
    )
    quirks = models.TextField(
        blank=True,
        verbose_name="What surprises owners",
        help_text="Two or three real-life observations.",
    )

    # more parameters
    prey_drive = models.CharField(
        max_length=20, blank=True, choices=PREY_CHOICES, verbose_name="Prey drive"
    )

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
        return reverse(
            "post", kwargs={"cat_slug": self.cat.slug, "post_slug": self.slug}
        )

    class Meta:
        verbose_name = "Dog breed"
        verbose_name_plural = "Dog breeds"
        ordering = ["title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    desc = models.TextField(blank=True, verbose_name="Description")
    short_desc = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Short description",
        help_text="One sentence for the group card on the Groups page.",
    )
    fci_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["fci_number"]


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Section")

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="Category",
    )

    position = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Position",
        help_text="Sections with a lower number come first; equal ones go by name.",
    )

    def __str__(self):
        return self.name

    def clean(self):
        if not self.pk and self.category.sections.count() >= 10:
            raise ValidationError("Maximum 10 sections per category.")

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"
        ordering = ["position", "name"]


class DogImage(models.Model):
    dog = models.ForeignKey(Dogs, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/dogs/gallery/")

    image_thumb = ImageSpecField(
        source="image",
        processors=[ResizeToFill(160, 160)],
        format="WEBP",
        options={"quality": 90},
    )

    image_large = ImageSpecField(
        source="image",
        processors=[ResizeToFit(1200, 900)],
        format="WEBP",
        options={"quality": 90},
    )

    author = models.CharField(max_length=255, blank=True, verbose_name="Photo Author")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Dog photo"
        verbose_name_plural = "Dog photos"

    def __str__(self):
        return f"{self.dog.title} photo"


class ConsentLog(models.Model):
    """Server-side record of a cookie-banner decision (Art. 7 GDPR evidence).

    One row per decision; the client-generated ``consent_id`` ties the event
    history of a single visitor together. No cookies, no sessions — only the
    choice, the page, the notice version and the timestamp.
    """

    consent_id = models.CharField(max_length=64, unique=True, db_index=True)
    action = models.CharField(max_length=32)
    analytics = models.BooleanField(default=False)
    notice_version = models.PositiveSmallIntegerField(default=1)
    page = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Consent log entry"
        verbose_name_plural = "Consent log"

    def __str__(self):
        return f"{self.action} {self.consent_id}"


class ContactMessage(models.Model):
    """A message sent through the contact form, kept in the site database."""

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    email = models.EmailField(blank=True, default="")
    message = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact message"
        verbose_name_plural = "Contact messages"

    def __str__(self):
        return f"{self.created_at:%Y-%m-%d %H:%M} {self.email or '—'}"
