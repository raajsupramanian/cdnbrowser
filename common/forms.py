from django import forms
from .models import AccessCredentials
from django.forms import ModelForm, PasswordInput


class AccessForm(ModelForm):
    access_key = forms.CharField(widget=PasswordInput(render_value=True))
    secret = forms.CharField(widget=PasswordInput(render_value=True))

    class Meta:
        model = AccessCredentials
        fields = '__all__'
