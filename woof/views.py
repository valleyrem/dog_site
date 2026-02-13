from django.http import JsonResponse
from django.shortcuts import render
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

        size_icons = []
        base_size = 0.9
        step = 0.2
        for i in range(1, 6):
            size_icons.append({
                "active": i == post.size_index,
                "size": base_size + step*(i-1)
            })
        context['size_icons'] = size_icons

        # previous/next posts
        dogs_qs = Dogs.objects.filter(is_published=True).order_by('id')
        context['prev_post'] = dogs_qs.filter(id__lt=post.id).last() or dogs_qs.last()
        context['next_post'] = dogs_qs.filter(id__gt=post.id).first() or dogs_qs.first()

        # related dogs
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


class DogFilterView(DataMixin, ListView):
    model = Dogs
    template_name = 'woof/filter.html'
    context_object_name = 'dogs'
    paginate_by = None

    def get_queryset(self):
        queryset = Dogs.objects.filter(is_published=True)

        sizes = self.request.GET.getlist('size')
        family = self.request.GET.getlist('family')
        hypo = self.request.GET.getlist('hypo')
        activity = self.request.GET.getlist('activity')

        if sizes:
            queryset = queryset.filter(size__in=sizes)

        if family:
            queryset = queryset.filter(family_friendliness__in=family)

        if hypo:
            queryset = queryset.filter(hypoallergenic__in=hypo)

        if activity:
            queryset = queryset.filter(activity_level__in=activity)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string(
                'woof/dog_cards.html',
                context,
                request=self.request
            )
            return JsonResponse({'html': html})

        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['size_choices'] = Dogs.SIZE_CHOICES
        context['family_choices'] = Dogs.FAMILY_FRIENDLINESS_CHOICES
        context['hypo_choices'] = Dogs.HYPOALLERGENIC_CHOICES
        context['activity_choices'] = Dogs.ACTIVITY_CHOICES

        context['all_breeds'] = Dogs.objects.filter(
            is_published=True
        ).order_by('title')

        context['is_home'] = False

        return self.get_user_context(
            **context,
            title='Find Your Perfect Dog'
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
