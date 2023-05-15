from django import forms
from django.forms import ClearableFileInput

from .models import Post, Profile, Follow
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['creator']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'status']
        labels = {
            'img': '',
        }
        # widgets = {
        #     'image': ClearableFileInput(
        #         attrs={'class': 'custom-file-input', 'accept': 'image/*', 'multiple': False, 'id': 'imagefile',
        #                'data-clearable': False}),
        # }
