from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class add_coordinator(forms.ModelForm):
    class Meta:
        model = coordinator
        fields = ['name', 'contact_info', 'sports_type', 'status']

class add_event_form(forms.ModelForm):
    class Meta:
        model = event
        fields = "__all__"