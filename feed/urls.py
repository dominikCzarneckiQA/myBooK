from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('newPost/', views.CreatePostView, name='newPost'),

]
