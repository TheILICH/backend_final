from django.contrib import messages
from .forms import MyUserCreationForm, MyAuthenticationForm, PostForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Follow, Post
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = request.user

    content = {
        'user': user,
    }

    return render(request, 'home_page.html', content)


def login_view(request):
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
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'You have successfully created your account! Now please log into your account!')
            return redirect('login')

    content = {
        'form': form,
    }

    return render(request, 'register.html', content)


def logout_page(request):
    logout(request)
    return redirect('login')


def user_profile(request, username):

    print(f'username = {username}')
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    post = Post.objects.get(id=6)

    content = {
        'post': post,
        'profile': profile,
    }

    return render(request, 'user_profile.html', content)


def post_view(request, username, idx=-1):

    if username != request.user.username:
        messages.info(request, f"You should be logged in as {username}!")
        return redirect('login')

    user = request.user
    post = None

    if idx > -1:
        post = Post.objects.get(id=idx)

    if request.method != 'POST':
        content = {
            'form': PostForm(instance=post)
        }

        return render(request, 'post.html', content)

    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.creator = user
        new_post.save()

        return redirect('edit', username=user.username, idx=new_post.id)

    content = {
        'form': form,
    }

    return render(request, 'post.html', content)



