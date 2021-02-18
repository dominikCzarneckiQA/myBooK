from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    biography = models.TextField(max_length=150, null=True, blank=True, verbose_name='O mnie')
    profileAvatar = models.ImageField(upload_to='profilePhoto', default='profilePhoto/default.jpg',
                                      blank=True, verbose_name='Zdjęcie Profilowe')
    birthDate = models.DateField(null=True, blank=True, verbose_name='Data urodzin')
    currentLocation = models.CharField(max_length=99, null=True, blank=True, verbose_name='Miejscowość')
    countryOrigin = CountryField(blank=True, null=True,verbose_name='Kraj pochodzenia')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    github = models.URLField(null=True, blank=True, max_length=40)
    snapchat = models.CharField(null=True, blank=True, max_length=40)
    instagram = models.URLField(null=True, blank=True, max_length=40)
    facebook = models.URLField(null=True, blank=True, max_length=40)
    twitter = models.URLField(null=True, blank=True, max_length=40)

    def __str__(self):
        return str('Informacje o użytkowniku {}.'.format(self.user))


