from django.contrib import admin
from .models import Posts


# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'creationDate' , 'description']
