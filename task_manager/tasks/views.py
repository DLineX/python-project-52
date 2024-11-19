# from django.shortcuts import render
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from .forms import TasksCreateForm
from .models import Tasks
from task_manager.mixins import (LoginUserMixin, AuthorMixin)
from django_filters import (FilterSet, ModelChoiceFilter, BooleanFilter)
from django_filters.views import FilterView
from task_manager.labels.models import Labels
from django import forms


class CreateTasksView(CreateView, SuccessMessageMixin, LoginUserMixin):
    form_class = TasksCreateForm
    template_name = 'form.html'
    success_message = gettext_lazy('Task created successfully!')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'title': gettext_lazy('Create task'),
                     'button_text': gettext_lazy('Create'), }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTasksView(UpdateView, SuccessMessageMixin, LoginUserMixin):
    model = Tasks
    form_class = TasksCreateForm
    template_name = 'form.html'
    success_message = gettext_lazy('Task updated successfully!')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'title': gettext_lazy('Update task'),
                     'button_text': gettext_lazy('Submit changes'), }


class DeleteTasksView(DeleteView, SuccessMessageMixin,
                      LoginUserMixin, AuthorMixin):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_message = gettext_lazy('Task deleted successfully!')
    success_url = reverse_lazy('tasks_list')
    denied_message = gettext_lazy(
        'You can\'t delete this task, because only the author of the task can delete it')  # noqa: E501
    denied_url = reverse_lazy('tasks_list')
    extra_context = {'question': gettext_lazy(
        'Are you sure you want to delete this task?'),
        'button_text': gettext_lazy('Yes, delete!')}


class FilterTasks(FilterSet):
    labels = ModelChoiceFilter(queryset=Labels.objects.all(),
                               label=gettext_lazy('Label'), )
    owned_tasks = BooleanFilter(label=gettext_lazy('Only my tasks'),
                                widget=forms.CheckboxInput,
                                method='task_owner',)

    def task_owner(self, queryset, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Tasks
        fields = ('status', 'executor', 'label', 'owned_tasks')
        labels = {'status': gettext_lazy('status'),
                  'executor': gettext_lazy('executor'),
                  'label': gettext_lazy('label'),
                  'owned_tasks': gettext_lazy('owned tasks'), }


class ListTasksView(FilterView, LoginUserMixin):
    model = Tasks
    template_name = 'tasks/list.html'
    object_name = 'tasks'
    extra_context = {'title': gettext_lazy('Tasks'),
                     'button_text': gettext_lazy('Show'), }


class DetailTasksView(DetailView, LoginUserMixin):
    model = Tasks
    template_name = 'tasks/show.html'
    object_name = 'task'
    extra_context = {'title': gettext_lazy('Task details')}
