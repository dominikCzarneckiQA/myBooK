from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from konto.models import Profile
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Post(models.Model):
    postAuthor = models.ForeignKey(User, default=None, blank=True, null=False, on_delete=models.CASCADE)
    postContent = models.TextField(verbose_name='', max_length=200)
    postDate = models.DateTimeField(default=timezone.now)
    postLikes = models.ManyToManyField(User, blank=True, related_name='postlikes')
    postImages = models.ImageField(null=True, blank=True, upload_to='images/%Y/%m/%d', verbose_name='')
    postUrl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.postAuthor


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE)
    commentContent = models.TextField(verbose_name='')
    commentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.commentAuthor


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Activity(models.Model):
    user = models.ForeignKey(User, related_name='activity', db_index=True, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)

    targetContentType = models.ForeignKey(ContentType, blank=True, null=True, related_name='targetOBJ',
                                          on_delete=models.CASCADE)
    targetID = models.PositiveIntegerField(null=True,
                                           blank=True,
                                           db_index=True)
    track = GenericForeignKey('targetContentType', 'targetID')
    creation_date = models.DateField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-creation_date']
