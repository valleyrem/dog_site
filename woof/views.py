from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *


class DogsHome(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Paws & Tails")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Dogs.objects.filter(is_published=True).select_related('cat')


class AboutView(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/about.html'
    context_object_name = 'dogs'

    def get_queryset(self):
        return Dogs.objects.all().order_by('title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all().order_by('name')
        c_def = self.get_user_context(title='About', cats=cats, menu=menu)
        return dict(list(context.items()) + list(c_def.items()))





class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'woof/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="New Article")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            response_data = {
                'success': False,
                'errors': form.errors.get_json_data()  # Преобразуйте ошибки формы в формат JSON
            }
            return JsonResponse(response_data)
        return super().form_invalid(form)

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'woof/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Contact")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        # Просто возвращаем успешный JSON ответ
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        # Возвращаем ошибки формы, если они есть
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class ShowPost(DataMixin, DetailView):
    model = Dogs
    template_name = 'woof/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class DogsCategory(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Dogs.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - ' + str(c.name),
                                      cat_selected=c.pk,)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'woof/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'woof/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

class CookiePolicyView(DataMixin, TemplateView):
    template_name = 'woof/cookie_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Cookie Policy")
        return dict(list(context.items()) + list(c_def.items()))


class TermsAndConditionsView(DataMixin, TemplateView):
    template_name = 'woof/terms_and_conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Terms and Conditions")
        return dict(list(context.items()) + list(c_def.items()))


class PrivacyPolicyView(DataMixin, TemplateView):
    template_name = 'woof/privacy_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Privacy Policy")
        return dict(list(context.items()) + list(c_def.items()))

class UserPosts(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/my_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user_email = self.request.user.email
        return Dogs.objects.filter(user_email=user_email, is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='My Posts')  # Добавьте title или другой контекст
        return dict(list(context.items()) + list(c_def.items()))