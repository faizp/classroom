from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.manage_reports, name='reports'),
    path('<int:id>', views.report, name='report-video'),
    path('review-report/<int:id>', views.review_report, name='review-report'),
    path('delete-reported-classroom/<int:id>', views.delete_reported_classroom, name='delete-reported-classroom'),
    path('delete-block-reported-classroom/<int:id>', views.delete_block_reported_classroom, name='delete-block-reported-classroom'),
    path('block_warn_classroom/<int:id>', views.block_warn_classroom, name='block-warn-classroom'),
    path('reported-classroom/<int:id>', views.reported_classroom, name='reported-classroom'),
    path('send-message-admin/<int:id>', views.send_message_admin, name='send-message-admin'),
    path('unblock-reported-classroom/<int:id>', views.unblock_reported_classroom, name='unblock-reported-classroom'),
    path('delete-report/<int:id>', views.delete_report, name='delete-report')
]