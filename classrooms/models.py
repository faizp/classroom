from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name

class secCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


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


class Classroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sec_category = models.ForeignKey(secCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    students = models.IntegerField()
    language = models.CharField(max_length = 64)
    start_date = models.DateField()
    duration = models.IntegerField()
    description = models.CharField(max_length=256)
    video = models.FileField(upload_to='preview_videos')

