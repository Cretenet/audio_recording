# forms.py
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class AudioForm(forms.Form):
    audio_file = forms.FileField()

class LoginForm(AuthenticationForm):
    #username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())