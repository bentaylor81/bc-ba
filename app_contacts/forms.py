from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ["name", "company", "position", "address", "zip_code", "phone", "email", "website", "comments",]

