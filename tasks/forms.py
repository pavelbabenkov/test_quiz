from django import forms
from .models import Task, Q_logic

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Q_logic
        fields = ['q_text', 'correct_answer']