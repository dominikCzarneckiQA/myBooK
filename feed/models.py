from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from konto.models import Profile


class Post(models.Model):
    postAuthor = models.ForeignKey(User, default=None, blank=True, null=False, on_delete=models.CASCADE)
    postContent = models.TextField(verbose_name='', max_length=200)
    postDate = models.DateTimeField(default=timezone.now)
    postLikes = models.ManyToManyField(User, blank=True, related_name='postlikes')
    postImages = models.ImageField(null=True, blank=True, upload_to='images/%Y/%m/%d', verbose_name='')

    def __str__(self):
        return 'Post użytkownika {}'.format(self.postAuthor)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentAuthor = models.ForeignKey(User, blank=True, null=False, on_delete=models.CASCADE)
    commentContent = models.TextField(verbose_name='')
    commentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Komentarz użytkownika {}'.format(self.commentAuthor)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
