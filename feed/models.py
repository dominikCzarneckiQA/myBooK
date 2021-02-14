from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    postAuthor = models.ForeignKey(User, default=None, blank=True, null=False, on_delete=models.CASCADE)
    postContent = models.TextField(verbose_name='')
    postDate = models.DateTimeField(default=timezone.now)
    postLikes = models.ManyToManyField(User, blank=True, related_name='postlikes')
    postImages = models.ImageField(null=True, blank=True, upload_to='images/%Y/%m/%D/', verbose_name='')
    postUrl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.postAuthor.first_name


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE)
    commentContent = models.TextField(verbose_name='')
    commentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.commentAuthor.first_name
