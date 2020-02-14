from .models import *
from django import forms


class TodoprojectForm(forms.ModelForm):
    todo = forms.CharField(max_length=30)