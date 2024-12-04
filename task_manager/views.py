from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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
        messages.info(request, gettext_lazy('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


class ListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'list.html')
