from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.tablica, name='dashboard'),
    # URL zmiana hasła
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # URL resetowanie hasla
    path('password_reset/',  auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # URL TOKEN resetowanie hasla
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/', views.rejestracja, name='register'),
    path('edit/', views.edycja, name='edycja'),


]
