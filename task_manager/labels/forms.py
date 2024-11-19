from django import forms
from .models import Labels
from django.utils.translation import gettext


class LabelsForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           required=True,
                           label=gettext('Name'), )

    class Meta:
        model = Labels
        fields =('name',)
