from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='admin-login'),
    path('', views.admin_home, name='admin-home'),
    path('add-category/', views.add_category, name='add-category')
]