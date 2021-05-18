from django.db import models
from classrooms.models import secCategory
from django.contrib.auth.models import User


class Questions(models.Model):
    sec_category = models.ForeignKey(secCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256, null=True)
    correct = models.CharField(max_length=12)


class TestPassed(models.Model):
    sec_category = models.ForeignKey(secCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)