from django.urls import path
from .views import AllPostView, DetailPostView, UpdatePostView, DeletePostView, DeleteCommentView

app_name = 'feed'

urlpatterns = [
    path('', AllPostView.as_view(), name='all-posts'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail-post'),
    path('post/usun/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('post/edycja/<int:pk>', UpdatePostView.as_view(), name='update-post'),

    path('post/<int:post_pk>/comment/delete/<int:pk>/' , DeleteCommentView.as_view(), name='delete-comment'),

]
