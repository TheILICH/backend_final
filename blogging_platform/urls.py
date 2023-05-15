"""blogging_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import home, login_view, register, user_profile, logout_page, post_view, edit_profile, following

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('profiles/<str:username>/', user_profile, name='profile'),
    path('logout/', logout_page, name='logout'),
    path('profiles/<str:username>/<int:idx>/', post_view, name='edit'),
    path('profiles/<str:username>/new/', post_view, name='new_post'),
    path('profiles/<str:username>/edit/', edit_profile, name='edit_profile'),
    path('profiles/<str:username>/following/<int:idx>', following, name='following'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
