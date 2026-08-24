import io

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from PIL import Image

from .models import Category, CoatLength, CoatType, DogImage, Dogs, Section


def make_photo(name="photo.png"):
    """Minimal in-memory PNG for ImageField/ImageKit fields."""
    buffer = io.BytesIO()
    Image.new("RGB", (10, 10), "red").save(buffer, format="PNG")
    return SimpleUploadedFile(name, buffer.getvalue())


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(
            name="Group 1 - Sheepdogs", slug="group-1", fci_number=1
        )

    def test_str_methods(self):
        dog = Dogs.objects.create(
            title="Labrador",
            slug="labrador",
            cat=self.cat,
            photo="photos/test.jpg",
        )
        section = Section.objects.create(name="Sheepdogs", category=self.cat)
        coat_type = CoatType.objects.create(name="Smooth")
        coat_length = CoatLength.objects.create(name="Short")

        self.assertEqual(str(self.cat), "Group 1 - Sheepdogs")
        self.assertEqual(str(dog), "Labrador")
        self.assertEqual(str(section), "Sheepdogs")
        self.assertEqual(str(coat_type), "Smooth")
        self.assertEqual(str(coat_length), "Short")

    def test_get_absolute_url(self):
        dog = Dogs.objects.create(
            title="Labrador",
            slug="labrador",
            cat=self.cat,
            photo="photos/test.jpg",
        )
        self.assertEqual(dog.get_absolute_url(), "/groups/group-1/labrador/")

    def test_size_index(self):
        dog = Dogs.objects.create(
            title="Husky",
            slug="husky",
            cat=self.cat,
            photo="photos/test.jpg",
            size="large",
        )
        self.assertEqual(dog.size_index, 4)
        dog.size = "medium_large"
        self.assertEqual(dog.size_index, 1)  # unmapped sizes fall back to 1

    def test_section_limit_per_category(self):
        for i in range(10):
            Section.objects.create(name=f"Section {i}", category=self.cat)

        eleventh = Section(name="Section 10", category=self.cat)
        with self.assertRaises(ValidationError):
            eleventh.full_clean()

    def test_dog_image_str(self):
        dog = Dogs.objects.create(
            title="Labrador",
            slug="labrador",
            cat=self.cat,
            photo="photos/test.jpg",
        )
        image = DogImage(dog=dog, image="photos/dogs/gallery/test.jpg")
        self.assertEqual(str(image), "Labrador photo")


class BreedApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(name="Group 1", slug="group-1")
        cls.published = Dogs.objects.create(
            title="Labrador",
            slug="labrador",
            cat=cls.cat,
            photo=make_photo("labrador.png"),
            is_published=True,
        )
        cls.draft = Dogs.objects.create(
            title="Secret Breed",
            slug="secret-breed",
            cat=cls.cat,
            photo=make_photo("secret.png"),
            is_published=False,
        )

    def test_api_returns_published_breed(self):
        response = self.client.get(reverse("breed-api", args=[self.published.pk]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "Labrador")
        self.assertTrue(data["photo"])

    def test_api_survives_missing_photo_file(self):
        # DB record exists, but the file behind photo/ is gone.
        self.published.photo.name = "photos/nonexistent.png"
        self.published.save(update_fields=["photo"])
        response = self.client.get(reverse("breed-api", args=[self.published.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["photo"], "")

    def test_api_hides_unpublished_breed(self):
        response = self.client.get(reverse("breed-api", args=[self.draft.pk]))
        self.assertEqual(response.status_code, 404)


class PageSmokeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(name="Group 1", slug="group-1")
        cls.dog = Dogs.objects.create(
            title="Labrador",
            slug="labrador",
            cat=cls.cat,
            photo=make_photo("labrador.png"),
            is_published=True,
        )

    def test_static_pages_return_200(self):
        pages = [
            "home",
            "dogs_list",
            "about",
            "guides",
            "guide-choosing-dog",
            "guide-training",
            "guide-health",
            "guide-behavior",
            "guide-living",
            "guide-puppy",
            "dog-explore",
            "groups",
            "contact",
            "cookie-policy",
            "terms-of-use",
            "privacy-policy",
        ]
        for name in pages:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_category_and_post_pages_return_200(self):
        response = self.client.get(
            reverse("category", kwargs={"cat_slug": self.cat.slug})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse(
                "post",
                kwargs={"cat_slug": self.cat.slug, "post_slug": self.dog.slug},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_unknown_post_returns_404(self):
        response = self.client.get("/groups/group-1/nope/")
        self.assertEqual(response.status_code, 404)

    def test_dogs_list_query_filters(self):
        response = self.client.get(reverse("dogs_list") + "?size=small")
        self.assertEqual(response.status_code, 200)
