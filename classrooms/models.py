from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36, unique=True)

class secCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=36, unique=True) 