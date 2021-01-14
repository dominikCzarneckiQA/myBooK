from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    email = models.EmailField(default='example@gmail.com')
    phoneNumber = models.IntegerField()
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Informacje o użytkowniku {}.'.format(self.user)

    def get_absolute_url(self):
        return reverse('dashboard', args=(str(self.id)))
