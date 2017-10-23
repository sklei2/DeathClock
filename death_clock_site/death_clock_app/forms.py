from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    user_name = forms.CharField(required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')


