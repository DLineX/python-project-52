from django import forms
from django.utils.translation import gettext_lazy

from .models import Status


class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           required=True,
                           label=gettext_lazy('Name'))

    class Meta:
        model = Status
        fields = ('name', )
