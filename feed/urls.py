from django.urls import path
from .views import FollowersPosts, DetailPostView, UpdatePostView, DeletePostView, DeleteCommentView, \
    LikePostDetailView, AllPostView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'feed'

urlpatterns = [
    path('', FollowersPosts.as_view(), name='followers-posts'),
    path('nowe/', AllPostView.as_view(), name='new-posts'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail-post'),
    path('post/usun/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('post/edycja/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('post/like/<int:pk>', LikePostDetailView, name='like-post'),

    path('post/<int:post_pk>/comment/delete/<int:pk>/', DeleteCommentView.as_view(), name='delete-comment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
