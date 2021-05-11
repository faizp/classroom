from django.contrib import admin
from .models import Category, secCategory, Questions, Answer, TestPassed, Classroom

# Register your models here.
admin.site.register(Category)
admin.site.register(secCategory)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(TestPassed)
admin.site.register(Classroom)