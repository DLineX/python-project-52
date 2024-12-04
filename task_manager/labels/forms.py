from django import forms
from django.utils.translation import gettext

from .models import Labels


class LabelsForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           required=True,
                           label=gettext('Name'), )

    class Meta:
        model = Labels
        fields = ('name',)
