from django import forms

from .models import Tasks


class TasksCreateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'status', 'executor', 'labels')
