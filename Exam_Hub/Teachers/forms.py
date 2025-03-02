from django import forms
from .models import Lesson, Exam, Result

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']  # Excluding 'teacher' since it will be set automatically

    def __init__(self, *args, **kwargs):
        self.teacher = kwargs.pop('teacher', None)  # Extract teacher from kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        lesson = super().save(commit=False)
        if self.teacher:
            lesson.teacher = self.teacher  # Assign the teacher automatically
        if commit:
            lesson.save()
        return lesson


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'subject', 'date']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'exam', 'score', 'published']

