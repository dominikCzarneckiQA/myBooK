from django.urls import path
from .views import postsView, postsDetailView

app_name = 'feed'

urlpatterns = [
    path('', postsView.as_view(), name='allPosts'),
    path('post/<int:pk>', postsDetailView.as_view(), name='detailPost'),
]