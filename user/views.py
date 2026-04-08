from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from user.forms import UserRegistrationForm


# Account creation flow: validate the form, create a Django `User`, then send the user to login.
class SignUpView(FormView):
    form_class = UserRegistrationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        data = form.cleaned_data
        username = data["username"]
        password = data["password"]

        # Create the user and hash the password properly via `set_password`.
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        # Flash message shown after successful registration. The message will be displayed in the template using the `messages` tag.
        messages.add_message(self.request, messages.ERROR, "Inscription réussie !")
        return super().form_valid(form)


# Login view that redirects to the dashboard after authentication.
class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_default_redirect_url(self):
        return reverse_lazy("dashboard")


# Simple protected page for authenticated users.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
