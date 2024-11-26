from django.shortcuts import render
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy
from django.views import View


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    success_message = gettext_lazy('You are logged in')
    next_page = reverse_lazy('list')
    extra_context = {'title': gettext_lazy('Authorisation'),
                     'button_text': gettext_lazy('Enter'), }


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('list')

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, gettext_lazy('You are logged out'))  # noqa: E501
        return super().dispatch(request, *args, **kwargs)


class ListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'list.html')
