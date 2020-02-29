from django import forms
from .models import board_members

class BoardmembersForm(forms.ModelForm):
    class Meta:
        model = board_members
        fields = ["member_name", "profile", "linkedin", "image_url", "position", "priority",]