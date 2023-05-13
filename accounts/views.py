from django.contrib import messages
from .forms import MyUserCreationForm, MyAuthenticationForm, PostForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


def home(request):
    user = request.user

    content = {
        'user': user,
    }
    return render(request, 'home_page.html', content)


def login_view(request):

    a = User.objects.all()
    for u in a:
        print(u.username)

    form = MyAuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or Username is incorrect!')

    content = {
        'form': form,
    }

    return render(request, 'login.html', content)


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


def logout_page(request):
    logout(request)
    return redirect('login')


def user_profile(request):
    return render(request, 'user_profile.html')


def post(request, username):

    form = PostForm()

    content = {
        'form': form,
    }

    return render(request, 'post.html', content)



