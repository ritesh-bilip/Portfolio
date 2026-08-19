
from django import forms
from .models import Certification, ContactMessage, Education, Profile, Project, Skill

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

