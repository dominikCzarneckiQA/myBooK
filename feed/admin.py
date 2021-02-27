from django.contrib import admin
from .models import Post, Comment, Activity


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['postAuthor', 'postDate', 'postContent']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['commentAuthor', 'commentContent', 'commentDate', 'post']


@admin.register(Activity)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'track', 'creation_date']
    list_filter = ['creation_date']
    search_fields = ['action']
