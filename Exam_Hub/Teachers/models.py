from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subjects = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)  # Approval field

    def __str__(self):
        return self.user.username


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming teachers use Django's User model
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
    
class Exam(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default="MCA")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

from .models import Exam  # Import Exam model

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name="teacher_results")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.exam.title} - {self.score}"
