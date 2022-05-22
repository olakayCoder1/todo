from re import template
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [ 
    path('register/',views.register , name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html') ,name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html')  , name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete')
]