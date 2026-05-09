from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    TemplateView,
)

from .forms import ContactForm
from .models import Dogs, Category
from .utils import DataMixin, menu


class DogsHome(DataMixin, TemplateView):
    template_name = "woof/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Dogs.objects.filter(is_published=True).order_by("title")

        context["posts"] = dogs
        context["is_home"] = True

        return self.get_user_context(**context, title="Woof Dogs")


class DogsList(DataMixin, ListView):
    model = Dogs
    template_name = "woof/dogs_list.html"
    context_object_name = "posts"
    paginate_by = None

    def get_queryset(self):
        qs = Dogs.objects.filter(is_published=True).select_related("cat")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["all_breeds"] = Dogs.objects.filter(is_published=True).order_by("title")

        return self.get_user_context(**context, title="Dog Breeds - Woof Dogs")


class DogsCategory(DataMixin, ListView):
    model = Dogs
    template_name = "woof/dogs_list.html"
    context_object_name = "posts"
    allow_empty = False
    paginate_by = None

    def get_queryset(self):
        qs = Dogs.objects.filter(
            cat__slug=self.kwargs["cat_slug"], is_published=True
        ).select_related("cat")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(Category, slug=self.kwargs["cat_slug"])

        context["current_category"] = category
        context["all_breeds"] = Dogs.objects.filter(is_published=True).order_by("title")

        return self.get_user_context(
            **context, title=f"{category.name} - Woof Dogs", cat_selected=category.pk
        )


class ShowPost(DataMixin, DetailView):
    model = Dogs
    template_name = "woof/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["post"]

        size_icons = []
        base_size = 0.9
        step = 0.2
        for i in range(1, 6):
            size_icons.append(
                {"active": i == post.size_index, "size": base_size + step * (i - 1)}
            )
        context["size_icons"] = size_icons

        # previous/next posts
        dogs_qs = Dogs.objects.filter(is_published=True).order_by("id")
        context["prev_post"] = dogs_qs.filter(id__lt=post.id).last() or dogs_qs.last()
        context["next_post"] = dogs_qs.filter(id__gt=post.id).first() or dogs_qs.first()

        # related dogs
        context["related_dogs"] = (
            Dogs.objects.filter(cat=post.cat, is_published=True)
            .exclude(pk=post.pk)
            .order_by("title")
        )

        return self.get_user_context(
            **context, title=f"{post.title} - Woof Dogs", cat_selected=post.cat_id
        )


class AboutView(DataMixin, TemplateView):
    template_name = "woof/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["all_breeds"] = Dogs.objects.filter(is_published=True).order_by("title")

        context["is_home"] = False

        return self.get_user_context(**context, title="About - Woof Dogs")


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = "woof/contact.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["all_breeds"] = Dogs.objects.filter(is_published=True).order_by("title")

        context["is_home"] = False

        return self.get_user_context(**context, title="Contact - Woof Dogs")

    def form_valid(self, form):
        form.process_form()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class DogGroupsView(DataMixin, TemplateView):
    template_name = "woof/dog_groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Dogs.objects.filter(is_published=True)

        context["groups"] = [
            # 1. Best family dogs
            {
                "title": "  Best family dogs  🐶",
                "dogs": dogs.filter(
                    family_friendliness__in=["high", "excellent"],
                    barking_level__in=["necessary", "infrequent"],
                    activity_level__in=["calm", "regular"],
                ),
            },
            # 2. Great for first-time owners
            {
                "title": "  Great for first-time owners  🆕",
                "dogs": dogs.filter(
                    trainability__in=["agreeable", "easy", "eager"],
                    activity_level__in=["calm", "regular"],
                ),
            },
            # 3. For experienced owners
            {
                "title": "  For experienced owners  💪",
                "dogs": dogs.filter(
                    activity_level__in=["high", "energetic"],
                    trainability__in=["independent", "stubborn"],
                ),
            },
            # 4. Hypoallergenic breeds
            {
                "title": "  Hypoallergenic breeds  🌿",
                "dogs": dogs.filter(hypoallergenic__in=["moderate", "high"]),
            },
            # 5. Small dogs
            {
                "title": "  Small dogs  🐾",
                "dogs": dogs.filter(size__in=["xsmall", "small"]),
            },
            # 6. Medium dogs
            {"title": "  Medium dogs  🔹", "dogs": dogs.filter(size="medium")},
            # 7. Large dogs
            {
                "title": "  Large dogs  🐕",
                "dogs": dogs.filter(size__in=["large", "xlarge"]),
            },
            # 8. Apartment-friendly dogs
            {
                "title": "  Apartment-friendly dogs  🏢",
                "dogs": dogs.filter(
                    size__in=["xsmall", "small", "medium"],
                    activity_level__in=["calm", "regular"],
                    barking_level__in=["necessary", "infrequent"],
                    coat_length__name__in=["Short", "Medium"],
                ),
            },
            # 9. Best for houses with yard
            {
                "title": "  Best for houses with yard  🏡",
                "dogs": dogs.filter(
                    size__in=["medium", "large", "xlarge"],
                    activity_level__in=["high", "energetic"],
                    barking_level__in=["vocal", "frequent"],
                ),
            },
        ]

        return self.get_user_context(**context, title="Dog Groups - Woof Dogs")


class GroupsPageView(DataMixin, TemplateView):
    template_name = 'woof/groups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.prefetch_related('sections').all()
        return self.get_user_context(**context, title="FCI Groups - Woof Dogs")

class CookiePolicyView(DataMixin, TemplateView):
    template_name = "woof/cookie_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_home"] = False
        return self.get_user_context(**context, title="Cookie Policy - Woof Dogs")


class TermsAndConditionsView(DataMixin, TemplateView):
    template_name = "woof/terms_and_conditions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_home"] = False
        return self.get_user_context(**context, title="Terms of Use - Woof Dogs")


class PrivacyPolicyView(DataMixin, TemplateView):
    template_name = "woof/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_home"] = False
        return self.get_user_context(**context, title="Privacy Policy - Woof Dogs")


def pageNotFound(request, exception):
    return render(request, "woof/404.html", status=404)

