from django.db.models import Case, Count, IntegerField, Q, Value, When
from django.conf import settings
from modeltranslation.utils import build_localized_fieldname
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils import timezone, translation
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, FormView, ListView, TemplateView

from datetime import date
from pathlib import Path
import random
import re
import secrets
from django.core.cache import cache

from .forms import ContactForm
from .models import Category, Dogs
from .og_card import build_og_card_bytes
from .quotes import MARQUEE_QUOTES
from .utils import DEFAULT_META_DESCRIPTION, DataMixin, sex_pair

from django.templatetags.static import static as static_url


class DogFilterMixin:
    """Apply the optional ?size= and ?trainability= filters of the list pages."""

    def filter_by_query_params(self, qs):
        # Unknown values are ignored rather than turned into an empty page.
        sizes = {value for value, _label in Dogs.SIZE_CHOICES}
        trainabilities = {value for value, _label in Dogs.TRAINABILITY_CHOICES}

        size = self.request.GET.get("size")
        trainability = self.request.GET.get("trainability")

        if size in sizes:
            qs = qs.filter(size=size)
        if trainability in trainabilities:
            qs = qs.filter(trainability=trainability)

        return qs


class StaticPageView(DataMixin, TemplateView):
    """Generic page that only needs a template and a title."""

    page_title = ""
    page_heading = ""  # clean title for Article markup (no site suffix)
    page_description = ""
    page_is_article = False
    page_created = ""  # ISO date; shown with the update date on guides
    page_updated = ""  # ISO date; overrides the site-wide update date
    page_og_key = ""  # guide key in GUIDE_OG: gives the page its own share card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.page_created:
            context["page_created"] = date.fromisoformat(self.page_created)
            context["page_updated"] = date.fromisoformat(
                self.page_updated or settings.SITE_CONTENT_UPDATED
            )
        elif self.page_updated:
            context["page_updated"] = date.fromisoformat(self.page_updated)
        if self.page_is_article:
            context["article"] = {
                "headline": self.page_heading or self.page_title,
                "description": self.page_description,
                "updated": settings.SITE_CONTENT_UPDATED,
            }
        if self.page_description:
            context["meta_description"] = self.page_description
        if self.page_og_key:
            context["og_image"] = self.request.build_absolute_uri(
                reverse("guide_og", kwargs={"key": self.page_og_key})
            )
        return self.get_user_context(**context, title=self.page_title)


HOME_GUIDE_KEYS = [
    "choosing",
    "puppy",
    "training",
    "health",
    "behavior",
    "living",
    "feeding",
    "games",
]


class DogsHome(DataMixin, TemplateView):
    template_name = "woof/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dogs = list(
            Dogs.objects.filter(is_published=True)
            .select_related("cat", "section", "country")
            .order_by("title")
        )
        context["posts"] = dogs
        if dogs:
            # one breed per calendar day; the button on the page picks others
            context["breed_of_day"] = dogs[timezone.localdate().toordinal() % len(dogs)]
            context["breeds_data"] = [
                {
                    "u": dog.get_absolute_url(),
                    "t": dog.title,
                    "g": str(dog.cat),
                    "p": dog.photo_medium.url if dog.photo else "",
                    "s": dog.summary,
                    "z": dog.get_size_display(),
                    "w": "\n".join(
                        sex_pair(dog.weight_male, dog.weight_female, "kg").split(", ")
                    ),
                    "l": dog.life_expectancy
                    and _("%(years)s years") % {"years": dog.life_expectancy},
                    "o": dog.country.name if dog.country else "",
                }
                for dog in dogs
            ]
        context["home_guides"] = random.sample(HOME_GUIDE_KEYS, 3)
        context["quotes"] = MARQUEE_QUOTES.get(
            translation.get_language(), MARQUEE_QUOTES["en"]
        )
        context["is_home"] = True
        return self.get_user_context(**context, title=_("Woof Dogs — Dog Breed Guide"))


class DogsList(DataMixin, DogFilterMixin, ListView):
    model = Dogs
    template_name = "woof/dogs_list.html"
    context_object_name = "posts"
    paginate_by = None

    def get_queryset(self):
        return self.filter_by_query_params(
            Dogs.objects.filter(is_published=True).select_related("cat", "section")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_user_context(
            **context,
            title=_("Dog Breeds - Woof Dogs"),
            meta_description=_(
                "Browse all dog breeds on one page and compare size, coat, "
                "temperament and care needs."
            ),
        )


class DogsCategory(DataMixin, DogFilterMixin, ListView):
    model = Dogs
    template_name = "woof/dogs_list.html"
    context_object_name = "posts"
    allow_empty = False
    paginate_by = None

    def get_queryset(self):
        qs = Dogs.objects.filter(
            cat__slug=self.kwargs["cat_slug"], is_published=True
        ).select_related("cat")
        return self.filter_by_query_params(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs["cat_slug"])
        context["current_category"] = category
        context["og_image"] = self.request.build_absolute_uri(
            reverse("group_og", kwargs={"slug": category.slug})
        )
        return self.get_user_context(
            **context,
            title=_("{name} - Woof Dogs").format(name=category.name),
            meta_description=category.short_desc or DEFAULT_META_DESCRIPTION,
            cat_selected=category.pk,
        )


# Ordered scales, mildest first: a breed is "calmer" or "quieter" than another
# when it sits lower on the same scale.
_ACTIVITY = ["calm", "regular", "high", "energetic"]
_BARKING = ["necessary", "infrequent", "medium", "frequent", "vocal"]
# the model lists shedding from heavy to minimal, so a bigger index sheds less
_SHEDDING = ["no", "low", "moderate", "high"]


def _mean_weight(dog):
    """Average of the numbers in both weight fields ("25-32", "8"), or None."""
    numbers = [
        float(n.replace(",", "."))
        for text in (dog.weight_male, dog.weight_female)
        for n in re.findall(r"\d+(?:[.,]\d+)?", text or "")
    ]
    return sum(numbers) / len(numbers) if numbers else None


def breed_differences(base, other):
    """Up to two short phrases on how `other` differs from `base`."""

    def step(scale, a, b):
        if a in scale and b in scale:
            return scale.index(b) - scale.index(a)
        return 0

    found = []

    move = step(_ACTIVITY, base.activity_level, other.activity_level)
    if move:
        found.append(_("calmer") if move < 0 else _("more energetic"))

    mine, theirs = _mean_weight(base), _mean_weight(other)
    if mine and theirs:
        ratio = theirs / mine
        if ratio < 0.75:
            found.append(_("lighter"))
        elif ratio > 1.33:
            found.append(_("heavier"))

    move = step(_BARKING, base.barking_level, other.barking_level)
    if abs(move) >= 2:
        found.append(_("quieter") if move < 0 else _("barks more"))

    move = step(_SHEDDING, base.hypoallergenic, other.hypoallergenic)
    if abs(move) >= 2:
        found.append(_("sheds more") if move < 0 else _("sheds less"))

    return found[:2] or [_("very similar overall")]


# old breed slugs -> current ones, so the old links keep working
RENAMED_BREEDS = {"anatolian-shepherd-dog": "kangal-shepherd-dog"}


class ShowPost(DataMixin, DetailView):
    model = Dogs
    template_name = "woof/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_queryset(self):
        return Dogs.objects.filter(
            slug=self.kwargs["post_slug"],
            cat__slug=self.kwargs["cat_slug"],
            is_published=True,
        ).select_related("cat", "section")

    def get(self, request, *args, **kwargs):
        # a breed that moved to another group keeps its old links working
        if not self.get_queryset().exists():
            slug = RENAMED_BREEDS.get(kwargs["post_slug"], kwargs["post_slug"])
            moved = (
                Dogs.objects.filter(slug=slug, is_published=True)
                .select_related("cat")
                .first()
            )
            if moved:
                return HttpResponsePermanentRedirect(moved.get_absolute_url())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]

        # previous/next breed in the same order the lists use (title, then
        # id for equal names), wrapping around at the ends
        dogs_qs = Dogs.objects.filter(is_published=True).order_by("title", "id")
        earlier = Q(title__lt=post.title) | Q(title=post.title, id__lt=post.id)
        later = Q(title__gt=post.title) | Q(title=post.title, id__gt=post.id)
        context["prev_post"] = dogs_qs.filter(earlier).last() or dogs_qs.last()
        context["next_post"] = dogs_qs.filter(later).first() or dogs_qs.first()

        # Similar breeds: same size class first, then the same coat length,
        # the same coat type and finally the same activity level. Size is the
        # only hard requirement, so the block is never empty.
        coat_ids = list(post.coat_length.values_list("id", flat=True))
        type_ids = list(post.coat_type.values_list("id", flat=True))
        context["similar_dogs"] = list(
            Dogs.objects.filter(is_published=True, size=post.size)
            .exclude(pk=post.pk)
            .select_related("cat")
            .annotate(
                coat_hits=Count(
                    "coat_length",
                    filter=Q(coat_length__in=coat_ids),
                    distinct=True,
                ),
                type_hits=Count(
                    "coat_type",
                    filter=Q(coat_type__in=type_ids),
                    distinct=True,
                ),
                activity_hits=Case(
                    When(activity_level=post.activity_level, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                ),
            )
            .order_by("-coat_hits", "-type_hits", "-activity_hits", "title")[:5]
        )

        for mate in context["similar_dogs"]:
            mate.differences = breed_differences(post, mate)

        # related breeds from the same group
        context["related_dogs"] = (
            Dogs.objects.filter(cat=post.cat, is_published=True)
            .select_related("cat", "section")
            .exclude(pk=post.pk)
            .order_by("title")
        )

        # SEO: page description + share image for this breed
        context["meta_description"] = post.summary or DEFAULT_META_DESCRIPTION

        # Share preview (Telegram/WhatsApp/iMessage): the title and the group.
        # Character traits are deliberately left out of the link preview.
        context["og_description"] = str(post.cat.name)

        # branded share card (breed photo + "woof dogs" panel), generated on demand
        if post.photo:
            context["og_image"] = self.request.build_absolute_uri(
                reverse("breed_og", kwargs={"slug": post.slug})
            )

        return self.get_user_context(
            **context,
            title=_("{name} - Woof Dogs").format(name=post.title),
            cat_selected=post.cat_id,
        )


OG_CACHE_DAYS = 30

# guide URL key -> (heading, photo of the guide)
GUIDE_OG = {
    "choosing_dog": (_("Choosing the dog"), "choosing_a_dog.webp"),
    "training": (_("Training"), "dog_training_fundamentals.webp"),
    "health": (_("Dog health & care"), "dog_health_care.webp"),
    "behavior": (_("Dog behavior"), "dog_behavior.webp"),
    "living-with-dog": (_("Living with a dog"), "living_with_a_dog.webp"),
    "puppy": (_("Raising a puppy"), "raising_a_puppy.webp"),
    "feeding": (_("Feeding your dog"), "feeding_your_dog.webp"),
    "games": (_("Games & activities"), "games_activities.webp"),
}


def _og_response(key, build):
    """JPEG response for a share card; ``build`` renders it on a cache miss."""
    jpeg = cache.get(key)
    if jpeg is None:
        jpeg = build()
        cache.set(key, jpeg, timeout=60 * 60 * 24 * OG_CACHE_DAYS)
    response = HttpResponse(jpeg, content_type="image/jpeg")
    response["Cache-Control"] = "public, max-age=2592000, s-maxage=2592000"
    response["Content-Length"] = str(len(jpeg))
    return response


def breed_og_image(request, slug):
    """Share card for a breed: its main photo, name and group."""
    dog = (
        Dogs.objects.filter(slug=slug, is_published=True).select_related("cat").first()
    )
    if dog is None:
        raise Http404("No published dog matches the given slug.")
    if not dog.photo:
        return HttpResponseRedirect(static_url("og-cover.jpg"))

    def build():
        with dog.photo.open("rb") as photo_file:
            return build_og_card_bytes(photo_file, str(dog.title), str(dog.cat.name))

    return _og_response(
        f"og2:breed:{translation.get_language()}:{dog.photo.name}:{dog.title}", build
    )


def group_og_image(request, slug):
    """Share card for a breed group: the group picture and its name."""
    category = get_object_or_404(Category, slug=slug)
    image = (
        "nofci.webp"
        if category.slug == "breeds-outside-fci-classification"
        else f"group{category.fci_number}.webp"
    )
    path = Path(settings.BASE_DIR) / "static" / image
    if not path.exists():
        return HttpResponseRedirect(static_url("og-cover.jpg"))

    def build():
        return build_og_card_bytes(path, str(category.name))

    return _og_response(
        f"og2:group:{translation.get_language()}:{category.slug}:{category.name}", build
    )


def guide_og_image(request, key):
    """Share card for a guide: the guide picture and its heading."""
    if key not in GUIDE_OG:
        raise Http404("No such guide.")
    heading, image = GUIDE_OG[key]

    def build():
        return build_og_card_bytes(
            Path(settings.BASE_DIR) / "static" / image, str(heading)
        )

    return _og_response(f"og2:guide:{translation.get_language()}:{key}", build)


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = "woof/contact.html"
    success_url = reverse_lazy("home")
    CAPTCHA_TTL = 600  # 10 minutes

    def _make_captcha(self):
        """Fresh math captcha: the answer lives in the cache keyed by a
        random token, so no session/cookie is created for guests."""
        a = secrets.randbelow(9) + 1
        b = secrets.randbelow(9) + 1
        token = secrets.token_hex(16)
        cache.set(f"contact_captcha:{token}", a + b, timeout=self.CAPTCHA_TTL)
        return {"a": a, "b": b, "token": token}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cap = self._make_captcha()
        context.update(
            {
                "captcha_a": cap["a"],
                "captcha_b": cap["b"],
                "captcha_token": cap["token"],
            }
        )
        return self.get_user_context(
            **context,
            title=_("Contact - Woof Dogs"),
            meta_description=_(
                "Contact Woof Dogs: questions, corrections, photo credits or "
                "suggestions for new breeds."
            ),
        )

    def form_invalid(self, form):
        # Refresh the captcha, so a failed attempt always shows a new example.
        return JsonResponse(
            {
                "success": False,
                "errors": form.errors,
                "captcha": self._make_captcha(),
            },
            status=400,
        )

    def form_valid(self, form):
        if not form.save_message():
            return JsonResponse(
                {
                    "success": False,
                    "errors": {
                        "__all__": [
                            "Message could not be sent. Please try again later."
                        ]
                    },
                },
                status=503,
            )
        # On success also hand out a fresh captcha and token so the hidden
        # captcha can be reset for the next message.
        return JsonResponse(
            {
                "success": True,
                "captcha": self._make_captcha(),
            }
        )


class BreedsView(DataMixin, TemplateView):
    """Every published breed as one grid with a multi-select filter panel."""

    template_name = "woof/breeds.html"

    # One row of filters, each covering a range of values from a single model
    # field (the field name is in the comment next to it). Filters that belong
    # to the same field are OR-ed, different fields are AND-ed.
    FILTERS = [
        # size
        (
            "size-small-medium",
            _("Small & Medium Size"),
            "size",
            {"size__in": ["small", "medium"]},
        ),
        ("size-large", _("Large Size"), "size", {"size": "large"}),
        # coat_length
        (
            "coat-short-medium",
            _("Short & Medium Coat"),
            "coat",
            {"coat_length__name_en__in": ["Short", "Medium"]},
        ),
        ("coat-long", _("Long coat"), "coat", {"coat_length__name_en__in": ["Long"]}),
        # hypoallergenic
        (
            "low-shedding",
            _("Low-Shedding"),
            "shedding",
            {"hypoallergenic__in": ["moderate", "high"]},
        ),
        # activity_level
        (
            "calm",
            _("Calm & Moderate"),
            "activity",
            {"activity_level__in": ["calm", "regular"]},
        ),
        (
            "active",
            _("Active & Energetic"),
            "activity",
            {"activity_level__in": ["high", "energetic"]},
        ),
        # trainability
        (
            "independent",
            _("Independent & Strong-Willed"),
            "training",
            {"trainability__in": ["independent", "stubborn"]},
        ),
        (
            "cooperative",
            _("Cooperative & Easy to Train"),
            "training",
            {"trainability__in": ["agreeable", "eager", "easy"]},
        ),
        # family_friendliness
        (
            "supervision",
            _("Needs More Supervision"),
            "family",
            {"family_friendliness__in": ["low", "medium"]},
        ),
        (
            "family",
            _("Family friendly"),
            "family",
            {"family_friendliness__in": ["high", "excellent"]},
        ),
    ]

    # Barking is not in the button row: it lives in the "More filters" panel
    # next to the country, temperament and coat-type drop-downs.
    BARKING_FILTERS = [
        ("quiet", _("Rarely bark"), {"barking_level__in": ["necessary", "infrequent"]}),
        ("talkative", _("Bark often"), {"barking_level__in": ["frequent", "vocal"]}),
    ]

    @staticmethod
    def _matches(dog, lookups):
        """Does a loaded breed fall under a filter button?

        The lookups in FILTERS are plain Django lookups, but they only touch
        fields of the already loaded objects (plus coat_length, which is
        prefetched), so evaluating them in Python costs nothing — unlike a
        separate filter() query per button.
        """
        for lookup, expected in lookups.items():
            if lookup.endswith("__name_en__in"):
                field = lookup[: -len("__name_en__in")]
                names = {
                    getattr(obj, "name_en", "") for obj in getattr(dog, field).all()
                }
                if not names.intersection(expected):
                    return False
            elif lookup.endswith("__in"):
                if getattr(dog, lookup[: -len("__in")]) not in expected:
                    return False
            elif getattr(dog, lookup) != expected:
                return False
        return True

    @staticmethod
    def _search_fields(dog):
        """Text the search box looks through: names and varieties in every site
        language (so "таксы" finds the dachshund on the English page too),
        origin and group."""
        languages = [code for code, _name in settings.LANGUAGES]
        titles = [
            getattr(dog, build_localized_fieldname("title", code), "") or ""
            for code in languages
        ]
        varieties = [
            getattr(dog, build_localized_fieldname("varieties", code), "") or ""
            for code in languages
        ]
        parts = [dog.title, dog.title_en, *titles, dog.varieties, *varieties]
        parts.append(dog.cat.name)
        if dog.country_id:
            parts.append(dog.country.name)
        dog.search_text = " ".join(p for p in dict.fromkeys(parts) if p)
        dog.search_names = "|".join(dict.fromkeys(t for t in [dog.title, *titles] if t))

    def _annotate(self, dogs):
        """Give every dog the keys of all the filters it matches, so the browser
        can combine them without asking the server again. Returns the countries
        and coat types that occur, as {pk: name}."""
        countries, coat_types = {}, {}
        for dog in dogs:
            keys = [
                key
                for key, _title, _group, lookups in self.FILTERS
                if self._matches(dog, lookups)
            ]
            keys += [
                key
                for key, _title, lookups in self.BARKING_FILTERS
                if self._matches(dog, lookups)
            ]
            if dog.country_id:
                keys.append(f"country-{dog.country_id}")
                countries[dog.country_id] = dog.country.name
            for c in dog.coat_type.all():
                keys.append(f"coattype-{c.pk}")
                coat_types[c.pk] = c.name
            dog.filter_keys = " ".join(keys)
            self._search_fields(dog)
        return countries, coat_types

    def _filter_buttons(self):
        group_labels = {
            "size": _("Size"),
            "coat": _("Coat"),
            "activity": _("Activity level"),
            "training": _("Trainability"),
            "family": _("Family"),
        }
        # low-shedding and barking are choices of their own, but they sit in the
        # coat and activity rows (a row may show two groups, one choice each)
        row_of = {"shedding": "coat", "barking": "activity"}
        entries = [(key, title, group) for key, title, group, _lookups in self.FILTERS]
        last_activity = max(i for i, e in enumerate(entries) if e[2] == "activity")
        entries[last_activity + 1 : last_activity + 1] = [
            (key, title, "barking") for key, title, _lookups in self.BARKING_FILTERS
        ]
        return [
            {
                "key": key,
                "title": title,
                "group": group,
                "row": row_of.get(group, group),
                "row_label": group_labels[row_of.get(group, group)],
            }
            for key, title, group in entries
        ]

    @staticmethod
    def _options(prefix, names):
        return [
            {"key": f"{prefix}-{pk}", "title": name}
            for pk, name in sorted(names.items(), key=lambda kv: kv[1])
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dogs = list(
            Dogs.objects.filter(is_published=True)
            .select_related("cat", "section", "country")
            .prefetch_related("coat_length", "coat_type")
            .order_by("title")
        )
        countries, coat_types = self._annotate(dogs)
        context["dogs"] = dogs
        context["filters"] = self._filter_buttons()
        context["extra_filters"] = [
            {
                "group": "country",
                "label": _("Country"),
                "any": _("Any country"),
                "options": self._options("country", countries),
            },
            {
                "group": "coattype",
                "label": _("Coat type"),
                "any": _("Any coat type"),
                "options": self._options("coattype", coat_types),
            },
        ]
        return self.get_user_context(
            **context,
            title=_("Breeds - Woof Dogs"),
            meta_description=_(
                "Find a dog breed by size, coat, activity level and other traits."
            ),
        )


class GroupsPageView(DataMixin, TemplateView):
    """FCI groups and sections overview."""

    template_name = "woof/groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = Category.objects.prefetch_related("sections").order_by(
            "fci_number"
        )
        return self.get_user_context(
            **context,
            title=_("Groups - Woof Dogs"),
            meta_description=_(
                "All FCI dog groups and their sections, with the breeds that "
                "belong to each."
            ),
        )


@require_GET
def breed_api(request, pk):
    dog = get_object_or_404(
        Dogs.objects.select_related("cat", "section").prefetch_related(
            "coat_type", "coat_length"
        ),
        pk=pk,
        is_published=True,
    )

    # A DB record may point to a missing file; degrade to "no photo" instead
    # of rendering a broken image (one storage call, and the response below is
    # cached for an hour so the compare table rarely repeats it).
    photo_url = ""
    if dog.photo:
        try:
            if dog.photo.storage.exists(dog.photo.name):
                photo_url = dog.photo_medium.url
        except OSError:
            photo_url = ""

    response = JsonResponse(
        {
            "id": dog.id,
            "title": dog.title,
            "url": dog.get_absolute_url(),
            "photo": photo_url,
            "section": dog.section.name if dog.section else "",
            "varieties": dog.varieties,
            "country": dog.country.name if dog.country else "",
            "size": dog.get_size_display(),
            "life": dog.life_expectancy,
            "height": sex_pair(dog.height_male, dog.height_female, "cm"),
            "weight": sex_pair(dog.weight_male, dog.weight_female, "kg"),
            "trainability": dog.get_trainability_display(),
            "activity": dog.get_activity_level_display(),
            "colors": dog.colors,
            "cat": dog.cat.name if dog.cat else "",
            "barking": dog.get_barking_level_display(),
            "hypoallergenic": dog.get_hypoallergenic_display(),
            "family_friendliness": dog.get_family_friendliness_display(),
            "coat_length": " / ".join(c.name for c in dog.coat_length.all()),
            "coat_type": " / ".join(c.name for c in dog.coat_type.all()),
        }
    )
    # The compare table asks for the same breeds again and again.
    response["Cache-Control"] = "public, max-age=3600"
    return response


def page_not_found(request, exception):
    return render(request, "woof/404.html", status=404)
