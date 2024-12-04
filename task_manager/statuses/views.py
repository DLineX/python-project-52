# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.mixins import LoginUserMixin, ProtectionMixin

from .forms import StatusCreateForm
from .models import Status


class CreateStatusView(SuccessMessageMixin, LoginUserMixin, CreateView):
    form_class = StatusCreateForm
    template_name = 'form.html'
    success_message = gettext_lazy('Status created successfully!')
    success_url = reverse_lazy('statuses_list')
    extra_context = {'title': gettext_lazy('Create status'),
                     'button_text': gettext_lazy('Create'), }


class UpdateStatusView(SuccessMessageMixin, LoginUserMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusCreateForm
    success_message = gettext_lazy('Status updated successfully!')
    success_url = reverse_lazy('statuses_list')
    extra_context = {'title': gettext_lazy('Update status'),
                     'button_text': gettext_lazy('Submit changes'), }


class DeleteStatusView(
    SuccessMessageMixin, LoginUserMixin, ProtectionMixin, DeleteView
):
    model = Status
    template_name = 'statuses/delete.html'
    success_message = gettext_lazy('Status deleted successfully!')
    success_url = reverse_lazy('statuses_list')
    protected_message = gettext_lazy(
        'You can\'t delete this status, because it is used in tasks')
    protected_url = reverse_lazy('statuses_list')
    extra_context = {
        'question':
            gettext_lazy('Are you sure you want to delete this status?'),
        'button_text': gettext_lazy('Yes, delete!'), }


class ListStatusView(LoginUserMixin, ListView):
    model = Status
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'
    extra_context = {'title': gettext_lazy('Statuses')}
