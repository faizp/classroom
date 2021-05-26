from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.announcements, name='announcements'),
    path('add-announcement/<int:id>', views.add_announcement, name='add-announcement'),
    path('annoucements/', views.all_announcements, name='all-announcements'),
    path('mark-read/<int:id>', views.mark_read, name='mark-read')
]