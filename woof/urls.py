from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    breed_api,
    ContactFormView,
    DogGroupsView,
    DogsCategory,
    DogsHome,
    DogsList,
    GroupsPageView,
    ShowPost,
    StaticPageView,
)

urlpatterns = [
    path("", DogsHome.as_view(), name="home"),
    path("dogs/", DogsList.as_view(), name="dogs_list"),
    path("about/", StaticPageView.as_view(
        template_name="woof/about.html",
        page_title=_("About us - Woof Dogs"),
    ), name="about"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("groups/<slug:cat_slug>/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("groups/<slug:cat_slug>/", DogsCategory.as_view(), name="category"),
    path("cookie-policy/", StaticPageView.as_view(
        template_name="woof/cookie_policy.html",
        page_title=_("Cookie Policy - Woof Dogs"),
    ), name="cookie-policy"),
    path("terms-of-use/", StaticPageView.as_view(
        template_name="woof/terms_and_conditions.html",
        page_title=_("Terms of Use - Woof Dogs"),
    ), name="terms-of-use"),
    path("privacy-policy/", StaticPageView.as_view(
        template_name="woof/privacy_policy.html",
        page_title=_("Privacy Policy - Woof Dogs"),
    ), name="privacy-policy"),
    path("explore/", DogGroupsView.as_view(), name="dog-explore"),
    path("groups/", GroupsPageView.as_view(), name="groups"),
    path("guides/", StaticPageView.as_view(
        template_name="woof/guides.html",
        page_title=_("Dog Guides - Woof Dogs"),
    ), name="guides"),
    path("guides/choosing_dog/", StaticPageView.as_view(
        template_name="woof/choosing_dog.html",
        page_title=_("Choosing the right dog - Woof Dogs"),
    ), name="guide-choosing-dog"),
    path("guides/training/", StaticPageView.as_view(
        template_name="woof/training.html",
        page_title=_("Dog Training Fundamentals - Woof Dogs"),
    ), name="guide-training"),
    path("guides/health/", StaticPageView.as_view(
        template_name="woof/health.html",
        page_title=_("Dog Health & Care - Woof Dogs"),
    ), name="guide-health"),
    path("guides/behavior/", StaticPageView.as_view(
        template_name="woof/behavior.html",
        page_title=_("Dog Behavior & Communication - Woof Dogs"),
    ), name="guide-behavior"),
    path("guides/living-with-dog/", StaticPageView.as_view(
        template_name="woof/living_with_dog.html",
        page_title=_("Living with a Dog - Woof Dogs"),
    ), name="guide-living"),
    path("guides/puppy/", StaticPageView.as_view(
        template_name="woof/puppy.html",
        page_title=_("Raising a Puppy - Woof Dogs"),
    ), name="guide-puppy"),
    path("api/breed/<int:pk>/", breed_api, name="breed-api"),
]
