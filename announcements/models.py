from django.db import models
from django.contrib.auth.models import User
from classrooms.models import Classroom


class Announcement(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    headline = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    date_posted = models.DateTimeField(auto_now_add=True)


class AnnouncementUser(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)