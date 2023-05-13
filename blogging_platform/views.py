from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, 'main page.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    form = UserCreationForm()

    content = {
        'form': form,
    }
    return render(request, 'register.html')
