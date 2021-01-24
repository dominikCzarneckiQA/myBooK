from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    user = models.ForeignKey(User,default=None, blank=True ,null=False, on_delete=models.CASCADE)
    description = models.TextField(default='some')
    creationDate = models.DateTimeField(default=timezone.now)


class Comments(models.Model):
    user = models.ForeignKey(User,default=None,blank=True ,null=False, on_delete=models.CASCADE)
    comment = models.TextField()
    creationDate = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
