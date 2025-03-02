from django import forms
from Exams.models import Question

class ExamAttemptForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(question.option_1, question.option_1), (question.option_2, question.option_2),
                         (question.option_3, question.option_3), (question.option_4, question.option_4)],
                widget=forms.RadioSelect,
                required=True
            )

    def calculate_score(self):
        score = 0
        for field_name, selected_option in self.cleaned_data.items():
            question_id = int(field_name.split('_')[1])
            question = Question.objects.get(id=question_id)
            if selected_option == getattr(question, question.correct_option):
                score += question.marks
        return score
