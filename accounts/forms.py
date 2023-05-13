from django import forms
from .models import Post
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
        fields = '__all__'
