from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    postAuthor = models.ForeignKey(User, default=None, blank=True, null=False, on_delete=models.CASCADE)
    postContent = models.TextField(default='Napisz cos.. ?')
    postDate = models.DateTimeField(default=timezone.now)
    postLikes = models.ManyToManyField(User, related_name='postlikes')


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, default=None, blank=True, null=False, on_delete=models.CASCADE)
    commentContent = models.TextField()
    commentDate = models.DateTimeField(default=timezone.now)
