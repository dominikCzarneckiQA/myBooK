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
    title = models.CharField(max_length=99)
    slug = models.SlugField(max_length=150, blank=True)
    #url = models.URLField(blank=True)
    #img = models.ImageField(upload_to='img/%Y/%m/%d' , blank=True)
    description = models.TextField(max_length=499, blank=True)
    creation_date = models.DateField(auto_now_add=True, db_index=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='img_liked',
                                   blank=True)

    def __str__(self):
        return self.title + '-' + str(self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
