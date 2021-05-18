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


class Classroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sec_category = models.ForeignKey(secCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    students = models.IntegerField()
    language = models.CharField(max_length = 64)
    start_date = models.DateField()
    duration = models.IntegerField()
    description = models.CharField(max_length=512)
    video = models.FileField(upload_to='preview_videos')


class Day(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    video = models.FileField(upload_to='course_content')
    video_title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    publish = models.BooleanField(default=False)
    

class ClassroomEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

