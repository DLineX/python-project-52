# from django.shortcuts import render
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView)
from .forms import LabelsForm
from .models import Labels
from task_manager.mixins import (LoginUserMixin, ProtectionMixin)


class CreateLabelsView(SuccessMessageMixin, LoginUserMixin, CreateView):
    form_class = LabelsForm
    template_name = 'form.html'
    success_message = gettext_lazy('Label created successfully!')
    success_url = reverse_lazy('labels_list')
    extra_context = {'title': gettext_lazy('Create label'),
                     'button_text': gettext_lazy('Create'), }


class UpdateLabelsView(SuccessMessageMixin, LoginUserMixin, UpdateView):
    model = Labels
    form_class = LabelsForm
    template_name = 'form.html'
    success_message = gettext_lazy('Label updated successfully!')
    success_url = reverse_lazy('labels_list')
    extra_context = {'title': gettext_lazy('Update label'),
                     'button_text': gettext_lazy('Submit changes'), }


class DeleteLabelsView(LoginUserMixin, SuccessMessageMixin, ProtectionMixin,
                       DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_list')
    success_message = gettext_lazy('Label deleted successfully!')
    protected_url = reverse_lazy('labels_list')
    protected_message = gettext_lazy('You can\'t delete this label, because it is used in tasks')  # noqa: E501
    extra_context = {'question': gettext_lazy(
        'Are you sure you want to delete this label?'),
        'button_text': gettext_lazy('Yes, delete!'), }


class ListLabelsView(LoginUserMixin, ListView):
    model = Labels
    template_name = 'labels/list.html'
    context_object_name = 'labels'
    extra_context = {'title': gettext_lazy('Labels')}
