from django.contrib import admin
from .models import Questions, Answer, TestPassed

# Register your models here.
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(TestPassed)