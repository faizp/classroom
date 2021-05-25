from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.announcements, name='announcements'),
    path('add-announcement/<int:id>', views.add_announcement, name='add-announcement')

]