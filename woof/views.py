from django.http import JsonResponse
from django.shortcuts import render
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
    template_name = 'woof/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        context['posts'] = dogs
        context['is_home'] = True

        return self.get_user_context(
            **context,
            title='Woof Dogs'
        )


class DogsList(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/dogs_list.html'
    context_object_name = 'posts'
    paginate_by = None

    def get_queryset(self):
        qs = Dogs.objects.filter(is_published=True).select_related('cat')

        # фильтры из GET-параметров
        size = self.request.GET.get('size')
        trainability = self.request.GET.get('trainability')
        coat = self.request.GET.get('coat')

        if size:
            qs = qs.filter(size=size)
        if trainability:
            qs = qs.filter(trainability=trainability)
        if coat:
            qs = qs.filter(coat_type=coat)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_breeds'] = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        return self.get_user_context(
            **context,
            title='Dog Breeds'
        )


class DogsCategory(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/dogs_list.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = None

    def get_queryset(self):
        qs = Dogs.objects.filter(
            cat__slug=self.kwargs['cat_slug'],
            is_published=True
        ).select_related('cat')

        # фильтры из GET-параметров
        size = self.request.GET.get('size')
        trainability = self.request.GET.get('trainability')
        coat = self.request.GET.get('coat')

        if size:
            qs = qs.filter(size=size)
        if trainability:
            qs = qs.filter(trainability=trainability)
        if coat:
            qs = qs.filter(coat_type=coat)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.get(
            slug=self.kwargs['cat_slug']
        )

        context['current_category'] = category
        context['all_breeds'] = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        return self.get_user_context(
            **context,
            title=f'Category — {category.name}',
            cat_selected=category.pk

        )


class ShowPost(DataMixin, DetailView):
    model = Dogs
    template_name = 'woof/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']

        dogs_qs = Dogs.objects.filter(is_published=True).order_by('id')

        # previous
        prev_post = dogs_qs.filter(id__lt=post.id).last()
        if not prev_post:
            prev_post = dogs_qs.last()

        # next
        next_post = dogs_qs.filter(id__gt=post.id).first()
        if not next_post:
            next_post = dogs_qs.first()

        context['prev_post'] = prev_post
        context['next_post'] = next_post

        context['related_dogs'] = Dogs.objects.filter(
            cat=post.cat,
            is_published=True
        ).exclude(pk=post.pk).order_by('title')

        return self.get_user_context(
            **context,
            title=post.title,
            cat_selected=post.cat_id
        )

class AboutView(DataMixin, TemplateView):
    template_name = 'woof/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_breeds'] = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        context['is_home'] = False

        return self.get_user_context(
            **context,
            title='About'
        )


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'woof/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_breeds'] = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        context['is_home'] = False

        return self.get_user_context(
            **context,
            title='Contact'
        )

    def form_valid(self, form):
        form.process_form()
        return super().form_valid(form)

    def form_invalid(self, form):
        return JsonResponse(
            {'success': False, 'errors': form.errors},
            status=400
        )


class CookiePolicyView(DataMixin, TemplateView):
    template_name = 'woof/cookie_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_home'] = False
        return self.get_user_context(
            **context,
            title='Cookie Policy'
        )


class TermsAndConditionsView(DataMixin, TemplateView):
    template_name = 'woof/terms_and_conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_home'] = False
        return self.get_user_context(
            **context,
            title='Terms of Use'
        )


class PrivacyPolicyView(DataMixin, TemplateView):
    template_name = 'woof/privacy_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_home'] = False
        return self.get_user_context(
            **context,
            title='Privacy Policy'
        )


def pageNotFound(request, exception):
    return render(request, 'woof/404.html', status=404)
