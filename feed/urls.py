from django.urls import path
from .views import PostsView, PostsDetailView, PostsUpdateView

app_name = 'feed'

urlpatterns = [
    path('', PostsView.as_view(), name='allPosts'),
    path('post/<int:pk>', PostsDetailView.as_view(), name='detailPost'),
    path('post/update/<int:pk>', PostsUpdateView.as_view(), name='updatePost')
]
