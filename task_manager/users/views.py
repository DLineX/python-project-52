# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import AuthorizationMixin, LoginUserMixin

from .forms import UserForm
from .models import User


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = gettext_lazy('User created successfully')
    extra_context = {'title': gettext_lazy('Registration'),
                     'button_text': gettext_lazy('Register'), }


class UpdateUserView(SuccessMessageMixin, LoginUserMixin,
                     AuthorizationMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'form.html'
    no_login_message = gettext_lazy('You are not logged in yet! Please log in')
    permission_message = gettext_lazy('You can\'t change other users')
    permission_url = reverse_lazy('users_list')
    success_message = gettext_lazy('User updated successfully!')
    success_url = reverse_lazy('users_list')
    extra_context = {'title': gettext_lazy('Update user'),
                     'button_text': gettext_lazy('Submit changes'), }


class DeleteUserView(SuccessMessageMixin, LoginUserMixin,
                     AuthorizationMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    no_login_message = gettext_lazy('You are not logged in yet! Please log in')
    permission_message = gettext_lazy('You can\'t delete other users')
    permission_url = reverse_lazy('users_list')
    protected_message = gettext_lazy(
        'User can\'t be deleted, because he have tasks')
    protected_url = reverse_lazy('users_list')
    success_message = gettext_lazy('User deleted successfully!')
    success_url = reverse_lazy('users_list')
    extra_context = {
        'question':
            gettext_lazy('Are you sure you want to delete this user?'),
        'button_text': gettext_lazy('Yes, delete!'), }


class ListUsersView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
