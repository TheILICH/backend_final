from django.contrib import messages
from .forms import MyUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, 'main page.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created your account! Now please log into your account!')
            return redirect('login')

    content = {
        'form': form,
    }

    return render(request, 'register.html', content)
