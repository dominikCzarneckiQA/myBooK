from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
# from django.utils.text import slugify
from django.db.models.signals import post_save


# Create your models here.
##################################################################################
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    aboutMe = models.CharField(max_length=199, blank=True)
    email = models.EmailField(default='example@gmail.com')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='default.jpg')

    def __str__(self):
        return str('Informacje o użytkowniku {}.'.format(self.user))

   # def get_absolute_url(self):
    #    return "/users/{}".format(self.slug)
