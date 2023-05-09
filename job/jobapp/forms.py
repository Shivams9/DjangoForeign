from django.core import validators
from django import forms
from .models import jobModel



class Registration(forms.ModelForm):
    class Meta:
        model = jobModel

        fields = ['name','email','contact']