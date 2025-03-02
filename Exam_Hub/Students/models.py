from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.timezone import now

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='lessons/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Exam(models.Model):
    subject = models.CharField(max_length=200)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name="student_results")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()
    published = models.BooleanField(default=False)  # Only show if published
    created_at = models.DateTimeField( default=now)
    
    def __str__(self):
        return f"{self.student.username} - {self.exam.subject} - {self.score}"
