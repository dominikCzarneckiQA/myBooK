from django.urls import path
from .views import PostView

app_name = 'feed'

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),


]