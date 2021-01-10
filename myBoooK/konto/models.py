from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=99, default='')
    phoneNumber = models.IntegerField(default=0)
    email = models.EmailField(_('email address'), blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Informacje o użytkowniku {}.'.format(self.user.username)
