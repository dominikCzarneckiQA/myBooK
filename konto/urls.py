from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import UserProfileView, UpdateProfileView, UserFollow, UserUnfollow, UsersListView, UserSearchView


urlpatterns = [
    path('', views.entryPageView, name="stronaStartowa"),

    # URL zmiana hasła
    path('zmiana_hasla/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('zmiana_hasla/gotowe/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # URL resetowanie hasla
    path('reset_hasla/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_hasla/gotowe/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # URL TOKEN resetowanie hasla
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/gotowe/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('rejestracja/', views.registerView, name='register'),
    path('edycja/', views.editView, name='edit'),

    path('zaloguj/', auth_views.LoginView.as_view(), name='login'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),

    path('profil/<int:pk>/przyjaciele/dodaj', UserFollow.as_view(), name='user_follow'),
    path('profil/<int:pk>/przyjaciele/usun', UserUnfollow.as_view(), name='user_unfollow'),

    path('feed/', include('feed.urls')),

    path('profil/<int:pk>', UserProfileView.as_view(), name='userProfile'),
    path('profil/edycja/<int:pk>/', UpdateProfileView.as_view(), name='profile_edit'),


    path('uzytkownicy/', UsersListView.as_view(), name='all_users'),
    path('wyszukaj/', UserSearchView.as_view(), name='user_search'),

    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),



]
