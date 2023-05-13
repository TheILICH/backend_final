from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Follow(models.Model):
    followed = models.ForeignKey(Profile, related_name='followed', on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, related_name='follower', on_delete=models.CASCADE)


class Post(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
