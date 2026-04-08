from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Simple registration form (not a `ModelForm`) so we can control validation
# and explicitly create the user in the corresponding view.
class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="Pseudo", max_length=100, required=True)
    password = forms.CharField(label="Mot de passe", max_length=100, required=True, widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirmation de mot de passe", max_length=100, required=True,
                                 widget=forms.PasswordInput)

    def clean(self):
        # Cross-field validation: matching passwords + unique username.
        if self.cleaned_data['password'] != self.cleaned_data['password_2']:
            raise ValidationError("Mot de passe différent")
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError("Ce pseudo est déjà utilisé")
        return super().clean()
