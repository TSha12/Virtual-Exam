from django.db import models

# Create your models here.
from Teachers.models import Exam

class QuestionPaper(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255, blank=True, null=True)
    option_4 = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.CharField(max_length=255, help_text="Specify correct option (e.g., 'option_1')")
    time_limit = models.IntegerField(help_text="Time limit in seconds per question")
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.question_paper.title} - {self.text}"
