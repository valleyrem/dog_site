from django.urls import path
from .views import (
    DogsHome,
    DogsList,
    AboutView,
    ContactFormView,
    ShowPost,
    DogsCategory,
    CookiePolicyView,
    TermsAndConditionsView,
    PrivacyPolicyView,
    DogGroupsView,
)

urlpatterns = [
    path("", DogsHome.as_view(), name="home"),
    path("dogs/", DogsList.as_view(), name="dogs_list"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("category/<slug:cat_slug>/", DogsCategory.as_view(), name="category"),
    path("cookie-policy/", CookiePolicyView.as_view(), name="cookie-policy"),
    path("terms-of-use/", TermsAndConditionsView.as_view(), name="terms-of-use"),
    path("privacy-policy/", PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("explore/", DogGroupsView.as_view(), name="dog-explore"),
]
