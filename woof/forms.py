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

    class Meta:
        model = Dogs
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'size', 'coat_type', 'care',
                  'living_conditions']
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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    captcha = CaptchaField(label='Enter the letters from the image')

