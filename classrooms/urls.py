from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-classroom/', views.create_classroom, name='create-classroom'),
    path('classroom-tutor/<int:id>', views.classroom_tutor, name='classroom-tutor'),
    path('manage-days/<int:id>', views.manage_days, name='manage-days'),
    path('add-new-day/<int:id>', views.add_day, name='add-new-day'),
    path('join-classroom/<int:id>', views.join_classroom, name='join-classroom'),
    path('classroom-student/<int:id>', views.classroom_student, name='classroom-student'),
]
