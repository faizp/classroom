from django.db import models
from classrooms.models import Classroom, Day
from django.contrib.auth.models import User


class ReportClassroom(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
    resolved = models.BooleanField(default=False)
    report_date = models.DateTimeField(auto_now_add=True)