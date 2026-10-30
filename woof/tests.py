import io

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
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
        self.assertEqual(dog.size_index, 3)  # small=1, medium=2, large=3
        dog.size = "gigantic"
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
        # DB record points at a file that is not in the storage. update() is
        # used on purpose: saving the instance would make imagekit try to
        # rebuild the (nonexistent) source.
        Dogs.objects.filter(pk=self.published.pk).update(
            photo="photos/nonexistent.png"
        )
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
            "breeds",
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


class BreedsFilterTests(TestCase):
    """The row of filter buttons on the Breeds page."""

    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(name="Group 1", slug="group-1")
        cls.short = CoatLength.objects.create(name="Short")
        cls.long = CoatLength.objects.create(name="Long")

        cls.small_dog = Dogs.objects.create(
            title="Beagle",
            slug="beagle",
            cat=cls.cat,
            photo=make_photo("beagle.png"),
            size="small",
            activity_level="regular",
            barking_level="infrequent",
            family_friendliness="high",
            hypoallergenic="moderate",
            trainability="eager",
            is_published=True,
        )
        cls.small_dog.coat_length.set([cls.short])

        cls.large_dog = Dogs.objects.create(
            title="Borzoi",
            slug="borzoi",
            cat=cls.cat,
            photo=make_photo("borzoi.png"),
            size="large",
            activity_level="energetic",
            barking_level="vocal",
            family_friendliness="medium",
            hypoallergenic="no",
            trainability="independent",
            is_published=True,
        )
        cls.large_dog.coat_length.set([cls.long])

        cls.draft = Dogs.objects.create(
            title="Zuchon",
            slug="zuchon",
            cat=cls.cat,
            photo=make_photo("zuchon.png"),
            is_published=False,
        )

    def test_buttons_follow_the_model_fields(self):
        response = self.client.get(reverse("breeds"))
        filters = response.context["filters"]
        self.assertEqual(len(filters), 11)
        self.assertEqual(filters[0]["key"], "size-small-medium")
        self.assertEqual(filters[0]["group"], "size")
        self.assertEqual(filters[4]["key"], "low-shedding")
        self.assertEqual(filters[10]["key"], "family")

    def test_row_has_buttons_including_reset(self):
        html = self.client.get(reverse("breeds")).content.decode()
        self.assertIn('data-filter="all"', html)
        # 11 filters plus the "all breeds" reset; the cross span is not a button
        self.assertEqual(html.count('data-filter="'), 12)
        self.assertIn("filter-btn__cross", html)
        self.assertNotIn("data-filter-group", html)  # one filter at a time
        self.assertNotIn("<fieldset", html)
        self.assertNotIn("data-filters-toggle", html)
        self.assertIn("data-filters-empty" if False else "data-breeds-empty", html)

    def test_cards_list_every_matching_filter(self):
        response = self.client.get(reverse("breeds"))
        keys = {dog.slug: dog.filter_keys for dog in response.context["dogs"]}

        # the card carries the keys of all filters it fits; the page shows one
        # selected filter at a time
        self.assertEqual(
            set(keys["beagle"].split()),
            {
                "size-small-medium",
                "coat-short-medium",
                "low-shedding",
                "calm",
                "cooperative",
                "family",
            },
        )
        self.assertEqual(
            set(keys["borzoi"].split()),
            {
                "size-large",
                "coat-long",
                "active",
                "independent",
                "supervision",
            },
        )
        self.assertNotIn("zuchon", keys)  # drafts never reach the grid

    def test_no_leftover_alphabet_or_dropdown(self):
        html = self.client.get(reverse("breeds")).content.decode()
        for gone in ("data-breeds-letters", "data-letter", "data-filters-panel"):
            self.assertNotIn(gone, html)

    def test_unknown_query_values_are_ignored(self):
        response = self.client.get(reverse("dogs_list") + "?size=huge")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 2)

    def test_canonical_drops_the_query_string(self):
        html = self.client.get(reverse("dogs_list") + "?size=small").content.decode()
        self.assertIn('rel="canonical"', html)
        self.assertNotIn("canonical\" href=\"http://testserver/dogs/?size", html)


class PostNavigationTests(TestCase):
    """Previous/next must follow the alphabetical order the lists use."""

    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(name="Group 1", slug="group-1")
        for title, slug in (("Aaa", "aaa"), ("Bbb", "bbb"), ("Ccc", "ccc")):
            Dogs.objects.create(
                title=title,
                slug=slug,
                cat=cls.cat,
                photo=make_photo(f"{slug}.png"),
                is_published=True,
            )

    def _post(self, slug):
        return self.client.get(
            reverse("post", kwargs={"cat_slug": self.cat.slug, "post_slug": slug})
        )

    def test_middle_breed_links_its_neighbours(self):
        context = self._post("bbb").context
        self.assertEqual(context["prev_post"].slug, "aaa")
        self.assertEqual(context["next_post"].slug, "ccc")

    def test_ends_wrap_around(self):
        first = self._post("aaa").context
        self.assertEqual(first["prev_post"].slug, "ccc")
        last = self._post("ccc").context
        self.assertEqual(last["next_post"].slug, "aaa")


class SitemapCacheTests(TestCase):
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

    def test_sitemap_is_cached_and_busted_by_a_save(self):
        from django.core.cache import cache
        from django.db import connection
        from django.test.utils import CaptureQueriesContext

        cache.clear()
        self.client.get(reverse("sitemap"))  # fills the cache

        with CaptureQueriesContext(connection) as quiet:
            response = self.client.get(reverse("sitemap"))
        self.assertEqual(len(quiet), 0, "cached sitemap should hit no queries")
        self.assertEqual(response.status_code, 200)

        self.dog.title = "Labrador Retriever"
        self.dog.save()  # post_save bumps the cache version

        with CaptureQueriesContext(connection) as warm:
            self.client.get(reverse("sitemap"))
        self.assertGreater(len(warm), 0, "a save must invalidate the sitemap")


class ContactCaptchaTests(TestCase):
    def test_captcha_token_is_single_use(self):
        from django.core.cache import cache

        cache.clear()
        token = "test-token"
        cache.set(f"contact_captcha:{token}", 7, 600)

        from woof.forms import ContactForm

        form = ContactForm(
            data={
                "content": "hello",
                "captcha_token": token,
                "captcha": 7,
            }
        )
        self.assertTrue(form.is_valid(), form.errors)
        self.assertIsNone(cache.get(f"contact_captcha:{token}"))

        replay = ContactForm(
            data={
                "content": "hello again",
                "captcha_token": token,
                "captcha": 7,
            }
        )
        self.assertFalse(replay.is_valid())


class ConsentLogTests(TestCase):
    url = "/consent-log/"

    def setUp(self):
        from django.core.cache import cache

        cache.clear()

    def post(self, payload, ip="203.0.113.9", xff=None):
        extra = {"REMOTE_ADDR": ip}
        if xff:
            extra["HTTP_X_FORWARDED_FOR"] = xff
        return self.client.post(
            self.url,
            data=payload,
            content_type="application/json",
            **extra,
        )

    def test_one_row_per_consent_id_and_update_in_place(self):
        from woof.models import ConsentLog

        payload = {"action": "accepted_all", "analytics": True, "id": "abc-1", "notice": 1}
        self.post(payload)
        self.assertEqual(ConsentLog.objects.count(), 1)

        self.post(payload)  # same choice again -> no second row
        self.assertEqual(ConsentLog.objects.count(), 1)

        self.post({**payload, "action": "declined", "analytics": False})
        self.assertEqual(ConsentLog.objects.count(), 1)
        record = ConsentLog.objects.get()
        self.assertEqual(record.action, "declined")
        self.assertFalse(record.analytics)

    def test_throttle_uses_the_last_forwarded_address(self):
        from woof.models import ConsentLog

        # A client that rotates the first XFF entry must not get a new bucket:
        # the address our proxy appended (the last one) stays the same.
        for i in range(25):
            self.post(
                {"action": "closed", "id": f"spoof-{i}"},
                xff=f"10.0.0.{i}, 198.51.100.7",
            )
        self.assertEqual(ConsentLog.objects.count(), 20)


class LanguageSwitchTests(TestCase):
    def test_switch_from_russian_back_to_english(self):
        response = self.client.post(
            reverse("set_language"),
            data={"language": "en", "next": "/ru/breeds/"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/breeds/")

    def test_invalid_language_is_rejected(self):
        response = self.client.post(
            reverse("set_language"), data={"language": "xx", "next": "/"}
        )
        self.assertEqual(response.status_code, 400)


class SeoTests(TestCase):
    """JSON-LD, sitemap extras and the new page blocks."""

    @classmethod
    def setUpTestData(cls):
        cls.cat = Category.objects.create(name="Group 1", slug="group-1")
        cls.dog = Dogs.objects.create(
            title="Beagle",
            slug="beagle",
            cat=cls.cat,
            photo=make_photo("beagle.png"),
            size="small",
            activity_level="regular",
            is_published=True,
        )
        cls.dog.coat_length.set([CoatLength.objects.create(name="Short")])
        cls.twin = Dogs.objects.create(
            title="Basset Hound",
            slug="basset-hound",
            cat=cls.cat,
            photo=make_photo("basset.png"),
            size="small",
            activity_level="regular",
            is_published=True,
        )
        cls.other = Dogs.objects.create(
            title="Borzoi",
            slug="borzoi",
            cat=cls.cat,
            photo=make_photo("borzoi.png"),
            size="large",
            activity_level="energetic",
            is_published=True,
        )
        # Same size and energy as the Beagle, different coats: the shared coat
        # decides which of them comes first in "Similar breeds".
        short_coat = cls.dog.coat_length.first()
        long_coat = CoatLength.objects.get_or_create(name="Long")[0]
        cls.poodle = Dogs.objects.create(
            title="Poodle",
            slug="poodle",
            cat=cls.cat,
            photo=make_photo("poodle.png"),
            size="small",
            activity_level="regular",
            is_published=True,
        )
        cls.poodle.coat_length.set([short_coat])
        cls.pug = Dogs.objects.create(
            title="Pug",
            slug="pug",
            cat=cls.cat,
            photo=make_photo("pug.png"),
            size="small",
            activity_level="regular",
            is_published=True,
        )
        cls.pug.coat_length.set([long_coat])

    def test_guide_carries_article_schema(self):
        html = self.client.get(reverse("guide-health")).content.decode()
        self.assertIn('"@type": "Article"', html)
        self.assertIn('"dateModified"', html)

    def test_home_has_no_article_schema(self):
        html = self.client.get(reverse("home")).content.decode()
        self.assertNotIn('"@type": "Article"', html)
        self.assertIn('"@type": "WebSite"', html)

    def test_breadcrumbs_schema_counts_positions(self):
        html = self.client.get(
            reverse("post", kwargs={"cat_slug": self.cat.slug, "post_slug": self.dog.slug})
        ).content.decode()
        self.assertIn('"@type": "BreadcrumbList"', html)
        for position in ('"position": 1', '"position": 2', '"position": 3', '"position": 4'):
            self.assertIn(position, html)

    def test_breed_page_lists_similar_breeds_only(self):
        response = self.client.get(
            reverse("post", kwargs={"cat_slug": self.cat.slug, "post_slug": self.dog.slug})
        )
        similar = [dog.slug for dog in response.context["similar_dogs"]]
        self.assertIn("basset-hound", similar)   # same size + activity
        self.assertNotIn("beagle", similar)      # never itself
        self.assertNotIn("borzoi", similar)      # different size and energy

    def test_similar_breeds_put_the_shared_coat_first(self):
        response = self.client.get(
            reverse("post", kwargs={"cat_slug": self.cat.slug, "post_slug": self.dog.slug})
        )
        similar = [dog.slug for dog in response.context["similar_dogs"]]
        self.assertLess(similar.index("poodle"), similar.index("pug"))

    def test_breeds_page_has_search_field(self):
        html = self.client.get(reverse("breeds")).content.decode()
        self.assertIn("data-breeds-search", html)

    def test_sitemap_contains_images_and_content_date(self):
        response = self.client.get(reverse("sitemap"))
        body = response.content.decode()
        self.assertIn("<image:loc>", body)
        self.assertIn(settings.SITE_CONTENT_UPDATED, body)
