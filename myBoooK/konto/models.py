from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    email = models.EmailField(default='example@gmail.com')
    phoneNumber = models.IntegerField(default=111-111-111)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Informacje o użytkowniku {}.'.format(self.user)

#do Poprawy
#class Wpis(models.Model):
 #   tytul = models.CharField(max_length=200)
  #  autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
   # tresc = models.TextField()

    #def __str__(self):
     #   return 'Autor wpisu: .'.format(self.autor)
