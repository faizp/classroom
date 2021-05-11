from django.contrib import admin
from .models import Category, secCategory, Questions, Answer

# Register your models here.
admin.site.register(Category)
admin.site.register(secCategory)
admin.site.register(Questions)
admin.site.register(Answer)