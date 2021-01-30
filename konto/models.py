from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  primary_key=True, on_delete=models.CASCADE, )
    biography = models.TextField(max_length=399, null=True, blank=True, verbose_name='Bio')
    profileAvatar = models.ImageField(upload_to='profilePhoto', default='profilePhoto/default.jpg',
                                      blank=True, verbose_name='Img')
    birthDate = models.DateField(null=True, blank=True, verbose_name='Birthday')
    currentLocation = models.CharField(max_length=99, null=True, blank=True , verbose_name='Location')
    countryOrigin = models.CharField(max_length=99, null=True, blank=True , verbose_name='Country')

    def __str__(self):
        return str('Informacje o użytkowniku {}.'.format(self.user))
