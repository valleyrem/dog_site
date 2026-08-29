from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import ContactForm
from .models import Category, Dogs
from .utils import DataMixin

class DogFilterMixin:
    """Apply optional ?size=&trainability=&coat= query filters."""

    def filter_by_query_params(self, qs):
        size = self.request.GET.get("size")
        trainability = self.request.GET.get("trainability")
        coat = self.request.GET.get("coat")

        if size:
            qs = qs.filter(size=size)
        if trainability:
            qs = qs.filter(trainability=trainability)
        if coat:
            qs = qs.filter(coat_type=coat)

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
        context["posts"] = Dogs.objects.filter(is_published=True).order_by("title")
        context["is_home"] = True
        return self.get_user_context(**context, title="Woof Dogs")


class DogsList(DataMixin, DogFilterMixin, ListView):
    model = Dogs
    template_name = "woof/dogs_list.html"
    context_object_name = "posts"
    paginate_by = None

    def get_queryset(self):
        return self.filter_by_query_params(
            Dogs.objects.filter(is_published=True).select_related("cat")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_user_context(**context, title="Dog Breeds - Woof Dogs")


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
            **context, title=f"{category.name} - Woof Dogs", cat_selected=category.pk
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
        )

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
        context["related_dogs"] = Dogs.objects.filter(
            cat=post.cat, is_published=True
        ).exclude(pk=post.pk).order_by("title")

        return self.get_user_context(
            **context, title=f"{post.title} - Woof Dogs", cat_selected=post.cat_id
        )


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = "woof/contact.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_user_context(**context, title="Contact - Woof Dogs")

    def form_valid(self, form):
        if not form.process_form():
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
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class DogGroupsView(DataMixin, TemplateView):
    """Curated breed collections (Explore page)."""

    template_name = "woof/dog_groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Dogs.objects.filter(is_published=True)

        context["groups"] = [
            {
                "title": "  Best family dogs  🐶",
                "dogs": dogs.filter(
                    family_friendliness__in=["high", "excellent"],
                    barking_level__in=["necessary", "infrequent"],
                    activity_level__in=["calm", "regular"],
                ),
            },
            {
                "title": "  Great for first-time owners  🆕",
                "dogs": dogs.filter(
                    trainability__in=["agreeable", "easy", "eager"],
                    activity_level__in=["calm", "regular"],
                ),
            },
            {
                "title": "  For experienced owners  💪",
                "dogs": dogs.filter(
                    activity_level__in=["high", "energetic"],
                    trainability__in=["independent", "stubborn"],
                ),
            },
            {
                "title": "  Easy to train dogs  🧠",
                "dogs": dogs.filter(
                    trainability__in=["agreeable", "easy", "eager"],
                ),
            },
            {
                "title": "  Hypoallergenic breeds  🌿",
                "dogs": dogs.filter(hypoallergenic__in=["moderate", "high"]),
            },
            {
                "title": "  Small dogs  🐾",
                "dogs": dogs.filter(size__in=["xsmall", "small"]),
            },
            {
                "title": "  Medium dogs  🔹",
                "dogs": dogs.filter(size="medium"),
            },
            {
                "title": "  Large dogs  🐕",
                "dogs": dogs.filter(size__in=["large", "xlarge"]),
            },
            {
                "title": "  Apartment-friendly dogs  🏢",
                "dogs": dogs.filter(
                    size__in=["xsmall", "small", "medium"],
                    activity_level__in=["calm", "regular"],
                    barking_level__in=["necessary", "infrequent"],
                    coat_length__name__in=["Short", "Medium"],
                ),
            },
            {
                "title": "  Best for houses with yard  🏡",
                "dogs": dogs.filter(
                    size__in=["medium", "large", "xlarge"],
                    activity_level__in=["high", "energetic"],
                    barking_level__in=["vocal", "frequent"],
                ),
            },
        ]

        return self.get_user_context(**context, title="Explore - Woof Dogs")


class GroupsPageView(DataMixin, TemplateView):
    """FCI groups and sections overview."""

    template_name = "woof/groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = Category.objects.prefetch_related(
            "sections"
        ).order_by("fci_number")
        return self.get_user_context(**context, title="Groups - Woof Dogs")


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
            "country": dog.country,
            "size": dog.get_size_display(),
            "life": dog.life_expectancy,
            "height": dog.height,
            "weight": dog.weight,
            "trainability": dog.get_trainability_display(),
            "activity": dog.get_activity_level_display(),
            "colors": dog.colors,
            "cat": dog.cat.name if dog.cat else "",
            "barking": dog.get_barking_level_display(),
            "hypoallergenic": dog.get_hypoallergenic_display(),
            "family_friendliness": dog.get_family_friendliness_display(),
            "coat_length": ", ".join(c.name for c in dog.coat_length.all()),
            "coat_type": ", ".join(c.name for c in dog.coat_type.all()),
        }
    )


def page_not_found(request, exception):
    return render(request, "woof/404.html", status=404)
