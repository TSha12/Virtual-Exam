from django import forms
from .models import QuestionPaper, Question

class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['title', 'subject', 'total_marks']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_paper', 'text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option', 'time_limit', 'marks']
