from django import forms
from app_websites.models import board_members, corp_members, resources, sponsors, pages

class BoardmembersForm(forms.ModelForm):
    class Meta:
        model = board_members
        fields = ["member_name", "profile", "linkedin", "profile_pic", "position", "priority",]

class CorpmembersForm(forms.ModelForm):
    class Meta:
        model = corp_members
        fields = ["corp_member_name", "website",]

class ResourcesForm(forms.ModelForm):
    class Meta:
        model = resources
        fields = ["resource_name", "website",]

class SponsorsForm(forms.ModelForm):
    class Meta:
        model = sponsors
        fields = ["sponsor_name", "sponsor_logo", "website",]

class PagesForm(forms.ModelForm):
    class Meta:
        model = pages
        fields = ["content"]