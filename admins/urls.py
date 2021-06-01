from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='admin-login'),
    path('', views.admin_home, name='admin-home'),
    path('add-category/', views.add_category, name='add-category'),
    path('sec-category/', views.sec_category, name='sec-category'),
    path('choose-category/', views.choose_category, name='choose-category'),
    path('add-sec-category/', views.add_sec_category, name='add-sec-category'),
    path('manage-classrooms/', views.manage_classroom, name='manage-classrooms'),
    path('delete-classroom/<int:id>', views.delete_classroom, name='delete-classroom'),
    path('block-classroom/<int:id>', views.block_classroom, name='block-classroom'),
    path('unblock-classroom/<int:id>', views.unblock_classroom, name='unblock-classroom'),
    path('logout/', views.logout_admin, name='admin-logout')
]