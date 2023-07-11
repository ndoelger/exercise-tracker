from django.forms import ModelForm
from .models import Completion

class CompletionForm(ModelForm):
    class Meta:
        model = Completion
        fields = ['date', 'reps', 'sets']

