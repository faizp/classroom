from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.admin_login, name='admin-login'),
    path('', views.admin_home, name='admin-home'),
    path('add-category/', views.add_category, name='add-category'),
    path('sec-category/', views.sec_category, name='sec-category'),
    path('instructor-test/', views.instructor_test, name='instructor-test'),
    path('category-test/<int:id>', views.category_test, name='category-test'),
    path('questions/<int:id>', views.questions, name='questions'),
    path('answers/<int:id>', views.answers, name='answers')
]