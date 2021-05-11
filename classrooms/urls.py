from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teach/', views.teach, name='teach'),
    path('test/', views.test, name='test'),
    path('create-classroom/', views.create_classroom, name='create-classroom'),
    path('classroom-tutor/<int:id>', views.classroom_tutor, name='classroom-tutor'),
    path('manage-days/', views.manage_days, name='manage-days')
]
