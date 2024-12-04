from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext


class LoginUserMixin(LoginRequiredMixin):
    auth_messages = gettext('You are not logged in yet! Please log in')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_messages)
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class AuthorizationMixin(LoginRequiredMixin, UserPassesTestMixin):
    no_login_message = None
    permission_message = None
    permission_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.permission_message)
        else:
            messages.error(self.request, self.no_login_message)
        return redirect(self.success_url)


class ProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class AuthorMixin(UserPassesTestMixin):
    redirect_url = None
    check_author_error_message = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.check_author_error_message)
        return redirect(self.redirect_url)
