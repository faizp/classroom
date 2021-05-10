from django.db import models

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
    correct = models.BooleanField()