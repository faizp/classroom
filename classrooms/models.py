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


class ClassroomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Classroom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sec_category = models.ForeignKey(secCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    students = models.IntegerField()
    language = models.CharField(max_length = 64)
    start_date = models.DateField()
    duration = models.IntegerField()
    description = models.CharField(max_length=2048)
    video = models.FileField(upload_to='preview_videos')
    started = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_classrooms = ClassroomManager()


class Day(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    video = models.FileField(upload_to='course_content')
    video_title = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
    publish = models.BooleanField(default=False)
    

class ClassroomEnrolled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

