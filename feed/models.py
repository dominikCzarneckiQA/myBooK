from django.conf import settings
from django.db import models
from django.utils.text import slugify
# DOJ

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="img_created",
        on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)
    url = models.URLField,
    img = models.ImageField(upload_to='img/%Y/%m/%d')
    description = models.TextField(blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='img_liked',
                                   blank=True)
    creation_date = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post,self).save(*args, **kwargs)
