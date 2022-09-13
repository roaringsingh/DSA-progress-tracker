from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import home_view, register_view, profile_view, delete_account_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/profile/delete/', delete_account_view, name='deleteaccount'),
]
