from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.manage_reports, name='reports'),
    path('<int:id>', views.report, name='report-video'),
    path('review-report/<int:id>', views.review_report, name='review-report'),
    path('delete-reported-classroom/<int:id>', views.delete_reported_classroom, name='delete-reported-classroom'),
    path('delete-block-reported-classroom/<int:id>', views.delete_block_reported_classroom, name='delete-block-reported-classroom')
]