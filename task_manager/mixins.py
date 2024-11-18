from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext
from django.urls import reverse_lazy
from django.db.models import ProtectedError


class LoginUserMixin(LoginRequiredMixin):
    no_login_message = gettext('You are not logged in yet! Please log in')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.no_login_message)
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class AuthorizationMixin(UserPassesTestMixin):
    permission_message = None
    permission_url = None

    def test(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class ProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
