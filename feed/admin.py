from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug' ,'img', 'creation_date']
    list_filter = ['creation_date']
