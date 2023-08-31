from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(null=True, max_length=100, default='', blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='images/', default='images/def.jpg')

    def __str__(self):
        return f'{self.user.username}'


class Follow(models.Model):
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} => {self.followed}'


class Post(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to='images/', default='images/def.jpg')

    def __str__(self):
        return f'text = {self.text} was created by {self.creator}'

