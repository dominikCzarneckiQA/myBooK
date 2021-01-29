from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  primary_key=True, verbose_name='user',
                                related_name='profile', on_delete=models.CASCADE, )
    biography = models.TextField(max_length=399, null=True, blank=True)
    profileAvatar = models.ImageField(upload_to='profilePhoto', default='profilePhoto/default.jpg', blank=True)
    birthDate = models.DateField(null=True, blank=True, )
    currentLocation = models.CharField(max_length=99, null=True, blank=True)
    countryOrigin = models.CharField(max_length=99, null=True, blank=True)


    def __str__(self):
        return str('Informacje o użytkowniku {}.'.format(self.user))
