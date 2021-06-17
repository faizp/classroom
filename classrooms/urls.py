from django.urls import path
from . import views
from chat import views as chat_views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-classroom/', views.create_classroom, name='create-classroom'),
    path('classroom-tutor/<int:id>', views.classroom_tutor, name='classroom-tutor'),
    path('manage-days/<int:id>', views.manage_days, name='manage-days'),
    path('add-new-day/<int:id>', views.add_day, name='add-new-day'),
    path('join-classroom/<int:id>', views.join_classroom, name='join-classroom'),
    path('classroom-student/<int:id>', views.classroom_student, name='classroom-student'),
    path('my-classroom/', views.my_classroom, name='my-classroom'),
    path('enroll-classroom/<int:id>', views.enroll_classroom, name='enroll-classroom'),
    path('content/<int:id>', views.content, name='content'),
    path('manage-students/<int:id>', views.manage_students, name='manage-students'),
    path('remove-student/<int:c_id>/<int:u_id>', views.remove_student, name='remove-student'),
    path('publish-content/<int:id>', views.publish_day, name='publish-content'),
    path('delete-content/<int:id>', views.delete_content, name='delete-content'),
    path('ask-question/<int:id>', views.ask_question, name='ask-question'),
    path('ask-question-tutor/<int:id>', views.ask_question_tutor, name='ask-question-tutor'),
    path('answer-question/<int:id>', views.answer_question, name='answer-question'),
    path('answer-question-tutor/<int:id>', views.answer_question_tutor, name='answer-question-tutor'),
    path('q-and-a/<int:id>', views.q_and_a, name='q-and-a'),   
    path('delete-question-tutor/<int:id>', views.delete_question_tutor, name='delete-question-tutor'),
    path('delete-answer-tutor/<int:id>', views.delete_answer_tutor, name='delete-answer-tutor'),
    path('delete-question/<int:id>', views.delete_question, name='delete-question'),
    path('delete-answer/<int:id>', views.delete_answer, name='delete-answer'),
    path('live-class/', chat_views.live_class, name='live-class')
]
