from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from user.forms import UserRegistrationForm


class SignUpView(FormView):
    form_class = UserRegistrationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        messages.add_message(self.request, messages.ERROR, "Inscription réussie !")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_default_redirect_url(self):
        return reverse_lazy("dashboard")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
