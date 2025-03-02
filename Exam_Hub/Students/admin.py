from django.contrib import admin

# Register your models here.
from .models import Lesson,Exam,Result

admin.site.register(Lesson)
admin.site.register(Exam)
admin.site.register(Result)