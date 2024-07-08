from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo

        fields = [ 'Task', 'Status','Deadline']

        widgets = {
            'Deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})}