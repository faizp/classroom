from django.urls import path
from . import views

urlpatterns = [
    path('teach/', views.teach, name='teach'),
    path('', views.test, name='test'),
    path('test-passed/', views.test_passed, name='test-passed'),
    path('test-failed/', views.test_failed, name='test-failed'),
    path('questions/<int:id>', views.questions, name='questions'),
    path('answers/<int:id>', views.answers, name='answers'),
    path('add-question/', views.add_question, name='add-question'),
    path('instructor-test/', views.instructor_test, name='instructor-test'),
    path('category-test/<int:id>', views.category_test, name='category-test'),
]