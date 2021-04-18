from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['postAuthor', 'postDate', 'postContent']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['commentAuthor', 'commentContent', 'commentDate', 'post']




