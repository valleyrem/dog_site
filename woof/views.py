from django.db.models import Case, Count, IntegerField, Q, Value, When
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils import translation
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, FormView, ListView, TemplateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.page_is_article:
            context["article"] = {
                "headline": self.page_heading or self.page_title,
                "description": self.page_description,
                "updated": settings.SITE_CONTENT_UPDATED,
            }
        return self.get_user_context(**context, title=self.page_title)


class DogsHome(DataMixin, TemplateView):
    template_name = "woof/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = (
            Dogs.objects.filter(is_published=True)
            .select_related("cat", "section")
            .order_by("title")
        )
        context["quotes"] = MARQUEE_QUOTES.get(
            translation.get_language(), MARQUEE_QUOTES["en"]
        )
        context["is_home"] = True
        return self.get_user_context(**context, title="Woof Dogs")


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
        return self.get_user_context(**context, title=_("Dog Breeds - Woof Dogs"))


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
        return self.get_user_context(
            **context,
            title=_("{name} - Woof Dogs").format(name=category.name),
            cat_selected=category.pk,
        )


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
            .order_by("-coat_hits", "-type_hits", "-activity_hits", "title")[:6]
        )

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


def breed_og_image(request, slug):
    """Serve the branded 1200x630 share card for a breed.

    Photo on the left (cover-cropped like the homepage hero), the "woof
    dogs" brand panel on the right. Generated once per photo and cached;
    the key includes the photo file name, so a new upload invalidates it.
    """
    dog = Dogs.objects.filter(slug=slug, is_published=True).first()
    if dog is None:
        raise Http404("No published dog matches the given slug.")
    if not dog.photo:
        return HttpResponseRedirect(static_url("og-cover.jpg"))

    key = f"og_breed:{dog.photo.name}"
    jpeg = cache.get(key)
    if jpeg is None:
        with dog.photo.open("rb") as photo_file:
            jpeg = build_og_card_bytes(photo_file)
        # Not "forever": the file cache culls old entries anyway, and a month
        # is plenty for a card that only depends on the photo.
        cache.set(key, jpeg, timeout=60 * 60 * 24 * 30)

    response = HttpResponse(jpeg, content_type="image/jpeg")
    response["Cache-Control"] = "public, max-age=2592000, s-maxage=2592000"
    response["Content-Length"] = str(len(jpeg))
    return response


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
        return self.get_user_context(**context, title=_("Contact - Woof Dogs"))

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
        if not form.send_message_to_telegram():
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
                names = {getattr(obj, "name_en", "") for obj in getattr(dog, field).all()}
                if not names.intersection(expected):
                    return False
            elif lookup.endswith("__in"):
                if getattr(dog, lookup[: -len("__in")]) not in expected:
                    return False
            elif getattr(dog, lookup) != expected:
                return False
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = list(
            Dogs.objects.filter(is_published=True)
            .select_related("cat", "section")
            .prefetch_related("coat_length")
            .order_by("title")
        )

        # every dog gets the keys of all the filters it matches, so the browser
        # can combine them without asking the server again
        for dog in dogs:
            dog.filter_keys = " ".join(
                key
                for key, _title, _group, lookups in self.FILTERS
                if self._matches(dog, lookups)
            )

        context["dogs"] = dogs
        context["filters"] = [
            {"key": key, "title": title, "group": group}
            for key, title, group, _lookups in self.FILTERS
        ]
        return self.get_user_context(**context, title=_("Breeds - Woof Dogs"))


class GroupsPageView(DataMixin, TemplateView):
    """FCI groups and sections overview."""

    template_name = "woof/groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = Category.objects.prefetch_related("sections").order_by(
            "fci_number"
        )
        return self.get_user_context(**context, title=_("Groups - Woof Dogs"))


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
