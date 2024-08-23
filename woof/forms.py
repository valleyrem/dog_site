from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Not selected"

        self.fields['slug'].help_text = (
            "This is a unique link to find the dog. If the name consists of one word, "
            "use it as is (e.g., dachshund). If it consists of two or more words, use a hyphen between words (e.g., 'golden-retriever'). "
            "The slug should be written in lowercase without quotes."
        )

        # Add placeholders for each field
        self.fields['title'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Basset Hound'
        })
        self.fields['slug'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'basset-hound'
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Basset Hound is ...'
        })
        self.fields['photo'].widget.attrs.update({
            'placeholder': 'Upload an image for the post'
        })
        self.fields['cat'].widget.attrs.update({
            'placeholder': 'Select a category'
        })
        self.fields['size'].widget.attrs.update({
            'placeholder': 'Specify the size of the dog'
        })
        self.fields['coat_type'].widget.attrs.update({
            'placeholder': 'Specify the coat type of the dog'
        })
        self.fields['care'].widget.attrs.update({
            'placeholder': ''
        })
        self.fields['living_conditions'].widget.attrs.update({
            'placeholder': ''
        })

    class Meta:
        model = Dogs
        fields = ['title', 'slug', 'content', 'photo', 'cat', 'size', 'coat_type', 'care', 'living_conditions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 3}),
            'care': forms.Textarea(attrs={'cols': 60, 'rows': 3}),
            'living_conditions': forms.Textarea(attrs={'cols': 60, 'rows': 3}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length exceeds 200 characters.')
        return title

    def save(self, commit=True):
        post = super().save(commit=False)
        post.is_published = False  # Set is_published to False
        if commit:
            post.save()
        return post



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat pass', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    # captcha = CaptchaField(label='Enter the letters')


