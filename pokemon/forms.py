from django import forms


# Simple form backing the "Contact" page.
class ContactForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=100)
    last_name = forms.CharField(label="Nom", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
