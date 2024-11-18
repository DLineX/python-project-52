from django import forms
from .models import Status
from django.utils.translation import gettext_lazy


class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=120,
                           required=True,
                           label=gettext_lazy('Name'))

    class Meta:
        model = Status
        fields = ('name', )
