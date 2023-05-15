from django.contrib import messages
from .forms import MyUserCreationForm, MyAuthenticationForm, PostForm, ProfileForm, SearchForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Follow, Post
from django.contrib.auth.decorators import login_required
from random import shuffle


def home(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('login')

    print(f'METHOD = {request.method}')

    form = SearchForm(request.GET)
    res = []
    if form.is_valid() and form.cleaned_data['search_text']:
        # print(f'SEARCH_TEXT = {request.GET.get("search_text")}')
        res = Profile.objects.filter(user__username__icontains=request.GET['search_text'])

    fellas = []
    for f in Follow.objects.all():
        if f.follower == user:
            fellas.append(f.followed)

    all = []
    for f in fellas:
        profile = Profile.objects.get(user=f)
        ps = Post.objects.filter(creator=f)
        for p in ps:
            all.append((profile, p))

    shuffle(all)

    content = {
        'user': user,
        'all': all,
        'res': res,
        'form': form,
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
    print(f'USERNAME = {username}')
    exist = 0
    for u in User.objects.all():
        if u.username == username:
            exist = 1
            break

    if exist == 0:
        messages.info(request,
            f'There is not such profile with username = {username}. Instead you can create new profile with such username!')
        return redirect('register')

    print(f'METHOD = {request.method}')
    #
    # if request.method == 'GET':
    #     print(f'SEARCH_TEXT = {request.GET["search_text"]}')
    #     return

    print(f'username = {username}')
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(creator=user)

    global_profile = Profile.objects.get(user=request.user)

    text = 'Follow'
    for f in Follow.objects.all():
        if f.followed == profile.user and f.follower == global_profile.user:
            text = 'Unfollow'

    content = {
        'posts': posts,
        'profile': profile,
        'publications': len(posts),
        'button_text': text,
        'ok': True,
        'global_profile': global_profile,
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


def edit_profile(request, username):
    exist = 0
    for u in User.objects.all():
        if u.username == username:
            exist = 1
            break

    if exist == 0:
        messages.info(request,
            f'There is not such profile with username = {username}. Instead you can create new profile with such username!')
        return redirect('register')

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    if user != request.user:
        messages.info(request, f"You should be logged in as {username}!")
        return redirect('login')

    form = ProfileForm(instance=profile)
    img_url = profile.img.url


    if request.method != 'POST':
        content = {
            'form': form,
            'img_url': img_url,
        }



        return render(request, 'edit_profile.html', content)

    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        new_profile = form.save(commit=False)
        new_profile.save()

    content = {
        'form': form,
    }

    # print(f'url = {form.img.url}')
    return redirect('profile', username=username)


def following(request, username, idx):

    user = User.objects.get(username=username)
    followed = User.objects.get(id=idx)

    index = -1
    for f in Follow.objects.all():
        if f.followed == followed and f.follower == user:
            index = f.id
            break

    if index == -1:
        Follow.objects.create(followed=followed, follower=user)
    else:
        Follow.objects.get(id=index).delete()

    return redirect('profile', username=followed.username)



