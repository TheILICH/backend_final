from django.shortcuts import render
from .forms import MyUserCreationForm
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
        else:
            print('FORM IS NOT VALID')

    content = {
        'form': form,
    }

    return render(request, 'register.html', content)
