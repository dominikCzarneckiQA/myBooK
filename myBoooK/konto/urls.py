from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stronaWejsciowa, name="stronaWejsciowa"),
    path('zaloguj/', auth_views.LoginView.as_view(),name='login'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),
    path('tablica/', views.tablica, name='dashboard'),
    # URL zmiana hasła
    path('zmiana_hasla/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('zmiana_hasla/gotowe/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # URL resetowanie hasla
    path('reset_hasla/',  auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_hasla/gotowe/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # URL TOKEN resetowanie hasla
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/gotowe/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('rejestracja/', views.rejestracja, name='register'),
    path('edycja/', views.edycja, name='edycja'),
]
