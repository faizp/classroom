from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]