from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    breed_api,
    breed_og_image,
    group_og_image,
    guide_og_image,
    BreedsView,
    ContactFormView,
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
    path(
        "about/",
        StaticPageView.as_view(
            template_name="woof/about.html",
            page_title=_("About us - Woof Dogs"),
            page_description=_(
                "About Woof Dogs: a non-commercial guide to dog breeds, how "
                "the project began and who it is for."
            ),
        ),
        name="about",
    ),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("groups/<slug:cat_slug>/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path(
        "og/breed/<slug:slug>.jpg",
        breed_og_image,
        name="breed_og",
    ),
    path("og/group/<slug:slug>.jpg", group_og_image, name="group_og"),
    path("og/guide/<slug:key>.jpg", guide_og_image, name="guide_og"),
    path("groups/<slug:cat_slug>/", DogsCategory.as_view(), name="category"),
    path(
        "cookie-policy/",
        StaticPageView.as_view(
            template_name="woof/cookie_policy.html",
            page_updated="2026-11-03",
            page_title=_("Cookie Policy - Woof Dogs"),
        ),
        name="cookie-policy",
    ),
    path(
        "terms-of-use/",
        StaticPageView.as_view(
            template_name="woof/terms_and_conditions.html",
            page_updated="2026-11-03",
            page_title=_("Terms of Use - Woof Dogs"),
        ),
        name="terms-of-use",
    ),
    path(
        "privacy-policy/",
        StaticPageView.as_view(
            template_name="woof/privacy_policy.html",
            page_updated="2026-11-03",
            page_title=_("Privacy Policy - Woof Dogs"),
        ),
        name="privacy-policy",
    ),
    path("breeds/", BreedsView.as_view(), name="breeds"),
    path("groups/", GroupsPageView.as_view(), name="groups"),
    path(
        "guides/",
        StaticPageView.as_view(
            template_name="woof/guides.html",
            page_title=_("Dog Guides - Woof Dogs"),
            page_description=_(
                "Guides on choosing, training, feeding and caring for a dog, "
                "from the first days with a puppy to everyday health."
            ),
        ),
        name="guides",
    ),
    path(
        "guides/choosing_dog/",
        StaticPageView.as_view(
            template_name="woof/choosing_dog.html",
            page_created="2026-05-26",
            page_title=_("Choosing the dog - Woof Dogs"),
            page_heading=_("Choosing the dog"),
            page_description=_(
                "Learn how to choose a breed that matches your lifestyle, activity level and living space."
            ),
            page_is_article=True,
            page_og_key="choosing_dog",
        ),
        name="guide-choosing-dog",
    ),
    path(
        "guides/training/",
        StaticPageView.as_view(
            template_name="woof/training.html",
            page_created="2026-05-26",
            page_title=_("Dog Training Fundamentals - Woof Dogs"),
            page_heading=_("Training"),
            page_description=_(
                "Understand basic training principles, communication and learning consistency."
            ),
            page_is_article=True,
            page_og_key="training",
        ),
        name="guide-training",
    ),
    path(
        "guides/health/",
        StaticPageView.as_view(
            template_name="woof/health.html",
            page_created="2026-05-26",
            page_title=_("Dog Health & Care - Woof Dogs"),
            page_heading=_("Dog health & care"),
            page_description=_(
                "Learn about grooming, nutrition, preventive care and general health basics."
            ),
            page_is_article=True,
            page_og_key="health",
        ),
        name="guide-health",
    ),
    path(
        "guides/behavior/",
        StaticPageView.as_view(
            template_name="woof/behavior.html",
            page_created="2026-05-26",
            page_title=_("Dog Behavior - Woof Dogs"),
            page_heading=_("Dog behavior"),
            page_description=_(
                "Discover how dogs communicate, express emotions and react to the world around them."
            ),
            page_is_article=True,
            page_og_key="behavior",
        ),
        name="guide-behavior",
    ),
    path(
        "guides/living-with-dog/",
        StaticPageView.as_view(
            template_name="woof/living_with_dog.html",
            page_created="2026-05-26",
            page_title=_("Living with a Dog - Woof Dogs"),
            page_heading=_("Living with a dog"),
            page_description=_(
                "Daily routines, home adaptation and long-term lifestyle organization with a dog."
            ),
            page_is_article=True,
            page_og_key="living-with-dog",
        ),
        name="guide-living",
    ),
    path(
        "guides/puppy/",
        StaticPageView.as_view(
            template_name="woof/puppy.html",
            page_created="2026-05-26",
            page_title=_("Raising a Puppy - Woof Dogs"),
            page_heading=_("Raising a puppy"),
            page_description=_(
                "Learn about early puppy development, socialization, routines and first-life stages."
            ),
            page_is_article=True,
            page_og_key="puppy",
        ),
        name="guide-puppy",
    ),
    path(
        "guides/feeding/",
        StaticPageView.as_view(
            template_name="woof/feeding.html",
            page_created="2026-09-09",
            page_title=_("Feeding your dog - Woof Dogs"),
            page_heading=_("Feeding your dog"),
            page_description=_(
                "Learn how to choose food, feed by age and build a healthy drinking regime."
            ),
            page_is_article=True,
            page_og_key="feeding",
        ),
        name="guide-feeding",
    ),
    path(
        "guides/games/",
        StaticPageView.as_view(
            template_name="woof/games.html",
            page_created="2026-09-09",
            page_title=_("Games & activities - Woof Dogs"),
            page_heading=_("Games & activities"),
            page_description=_(
                "Discover safe games and activities that keep your dog active, engaged and happy."
            ),
            page_is_article=True,
            page_og_key="games",
        ),
        name="guide-games",
    ),
    path("api/breed/<int:pk>/", breed_api, name="breed-api"),
]
