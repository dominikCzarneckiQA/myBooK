from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,
                                on_delete=models.CASCADE)
    aboutMe = models.TextField(max_length=199, null=True, blank=True)
    birthDay = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/profilePhoto', default='media/profilePhoto/default.jpg')

    def __str__(self):
        return str('Informacje o użytkowniku {}.'.format(self.user))

# ef get_absolute_url(self):
#    return "/users/{}".format(self.slug)
