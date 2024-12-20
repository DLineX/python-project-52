# from django.shortcuts import render
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter
from django_filters.views import FilterView

from task_manager.labels.models import Labels
from task_manager.mixins import AuthorMixin, LoginUserMixin
from task_manager.statuses.models import Status
from task_manager.users.models import User

from .forms import TasksCreateForm
from .models import Tasks


class CreateTasksView(LoginUserMixin, SuccessMessageMixin, CreateView):
    form_class = TasksCreateForm
    template_name = 'form.html'
    success_message = gettext_lazy('Task created successfully!')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'title': gettext_lazy('Create task'),
                     'button_text': gettext_lazy('Create'), }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTasksView(LoginUserMixin, SuccessMessageMixin, UpdateView):
    model = Tasks
    form_class = TasksCreateForm
    template_name = 'form.html'
    success_message = gettext_lazy('Task updated successfully!')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'title': gettext_lazy('Update task'),
                     'button_text': gettext_lazy('Submit changes'), }


class DeleteTasksView(LoginUserMixin, SuccessMessageMixin,
                      AuthorMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_message = gettext_lazy('Task deleted successfully!')
    success_url = reverse_lazy('tasks_list')
    check_author_error_message = gettext_lazy(
        'You can\'t delete this task, because only the author of the task can delete it')  # noqa: E501
    redirect_url = reverse_lazy('tasks_list')
    extra_context = {'question': gettext_lazy(
        'Are you sure you want to delete this task?'),
        'button_text': gettext_lazy('Yes, delete!')}


class FilterTasks(FilterSet):
    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label=gettext_lazy('Status'),
                               field_name='status', )
    label = ModelChoiceFilter(queryset=Labels.objects.all(),
                              label=gettext_lazy('Label'),
                              field_name='labels', )
    executor = ModelChoiceFilter(queryset=User.objects.all(),
                                 label=gettext_lazy('Executor'),
                                 field_name='executor', )
    owned_tasks = BooleanFilter(method='task_owner',
                                widget=forms.CheckboxInput,
                                label=gettext_lazy('Only my tasks'),)

    def task_owner(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'label', 'owned_tasks']


class ListTasksView(LoginUserMixin, FilterView):
    model = Tasks
    filterset_class = FilterTasks
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    extra_context = {'title': gettext_lazy('Tasks'),
                     'button_text': gettext_lazy('Show'), }


class DetailTasksView(LoginUserMixin, DetailView):
    model = Tasks
    template_name = 'tasks/show.html'
    context_object_name = 'task'
    extra_context = {'title': gettext_lazy('Task details')}
