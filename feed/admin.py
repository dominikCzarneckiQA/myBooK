from django.contrib import admin
from .models import Posts, Comments


# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'creationDate', 'description']

@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'creationDate', 'post']
