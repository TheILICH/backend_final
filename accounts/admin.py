from django.contrib import admin
from .models import Follow, Post, Profile

admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Profile)
