from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.manage_reports, name='reports'),
    path('<int:id>', views.report, name='report-video')
]