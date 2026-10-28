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
        size = self.request.GET.get("size")
        trainability = self.request.GET.get("trainability")

        if size:
            qs = qs.filter(size=size)
        if trainability:
            qs = qs.filter(trainability=trainability)

        return qs


class StaticPageView(DataMixin, TemplateView):
    """Generic page that only needs a template and a title."""

    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

        base_size = 0.9
        step = 0.2
        context["size_icons"] = [
            {"active": i == post.size_index, "size": base_size + step * (i - 1)}
            for i in range(1, 6)
        ]

        # previous/next posts (wrap around at the ends)
        dogs_qs = Dogs.objects.filter(is_published=True).order_by("id")
        context["prev_post"] = dogs_qs.filter(id__lt=post.id).last() or dogs_qs.last()
        context["next_post"] = dogs_qs.filter(id__gt=post.id).first() or dogs_qs.first()

        # related breeds from the same group
        context["related_dogs"] = (
            Dogs.objects.filter(cat=post.cat, is_published=True)
            .select_related("cat", "section")
            .exclude(pk=post.pk)
            .order_by("title")
        )

        # SEO: page description + share image for this breed
        context["meta_description"] = post.summary or DEFAULT_META_DESCRIPTION

        # Share preview (Telegram/WhatsApp/iMessage): title, group, character
        traits = [str(t) for t in post.temperament.all()[:4]]
        context["og_description"] = (
            (f"{post.cat.name} · " + " · ".join(traits))
            if traits
            else str(post.cat.name)
        )

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
        cache.set(key, jpeg, timeout=None)

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
    """Every published breed as one grid with filter buttons (Breeds page)."""

    template_name = "woof/breeds.html"

    # the curated collections the old Explore page used; each key is a
    # filter button, the lookups stay here so the templates stay dumb
    FILTERS = [
        (
            "small",
            _("Small \U0001f43e"),
            dict(size="small"),
        ),
        (
            "medium",
            _("Medium \U0001f539"),
            dict(size="medium"),
        ),
        (
            "large",
            _("Large \U0001f9ae"),
            dict(size="large"),
        ),
        (
            "shortcoat",
            _("Short coat \U0001f415"),
            dict(coat_length__name_en__in=["Short"]),
        ),
        (
            "longcoat",
            _("Long coat \U0001f429"),
            dict(coat_length__name_en__in=["Long"]),
        ),
        (
            "first_time",
            _("Great for first-time owners \U0001f195"),
            dict(
                trainability__in=["agreeable", "easy", "eager"],
                activity_level__in=["calm", "regular"],
            ),
        ),
        (
            "experienced",
            _("For experienced owners \U0001f4aa"),
            dict(
                activity_level__in=["high", "energetic"],
                trainability__in=["independent", "stubborn"],
            ),
        ),
        (
            "family",
            _("Best family \U0001f436"),
            dict(
                family_friendliness__in=["high", "excellent"],
                barking_level__in=["necessary", "infrequent"],
                activity_level__in=["calm", "regular"],
            ),
        ),
        (
            "trainable",
            _("Easy to train \U0001f9e0"),
            dict(trainability__in=["eager", "easy"]),
        ),
        (
            "hypoallergenic",
            _("Hypoallergenic breeds \U0001f33f"),
            dict(hypoallergenic__in=["moderate", "high"]),
        ),
        (
            "energy",
            _("High energy \u26a1"),
            dict(activity_level="energetic"),
        ),
        (
            "apartment",
            _("Apartment-friendly \U0001f3e2"),
            dict(
                size__in=["small", "medium"],
                activity_level__in=["calm", "regular"],
                barking_level__in=["necessary", "infrequent"],
                coat_length__name_en__in=["Short", "Medium"],
            ),
        ),
        (
            "yard",
            _("Best for houses with yard \U0001f3e1"),
            dict(
                size__in=["medium", "large"],
                activity_level__in=["high", "energetic"],
                barking_level__in=["vocal", "frequent"],
            ),
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

        # every dog gets the list of filter keys it belongs to
        for dog in dogs:
            dog.filter_keys = " ".join(
                key
                for key, _title, lookups in self.FILTERS
                if self._matches(dog, lookups)
            )

        # Alphabet: the first letter of the title *as shown*, so the row
        # follows the page language (ru "Афганская борзая" -> А, sr "Španski" -> Š).
        for dog in dogs:
            first = dog.title.strip()[:1]
            dog.first_letter = first.upper() if first.isalpha() else ""

        context["dogs"] = dogs
        context["letters"] = sorted({dog.first_letter for dog in dogs if dog.first_letter})
        context["filters"] = [
            {"key": key, "title": title} for key, title, _lookups in self.FILTERS
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

    # A DB record may point to a missing file; degrade gracefully.
    photo_url = ""
    if dog.photo and dog.photo.storage.exists(dog.photo.name):
        photo_url = dog.photo_medium.url

    return JsonResponse(
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


def page_not_found(request, exception):
    return render(request, "woof/404.html", status=404)
