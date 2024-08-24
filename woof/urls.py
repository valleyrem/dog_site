from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import *

urlpatterns = [
    path('', DogsHome.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', DogsCategory.as_view(), name='category'),
    path('cookie-policy/', CookiePolicyView.as_view(), name='cookie-policy'),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms-and-conditions'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('my-posts/', UserPosts.as_view(), name='my_posts')

]