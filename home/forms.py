from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30 , required = True)
    cfhandle = forms.CharField(max_length = 30 , required = True)
    email = forms.EmailField(max_length = 100 , required = True)
    password1 = forms.CharField(max_length = 30 , required = True)
    password2 = forms.CharField(max_length = 30 , required = True)

class SignInForm(forms.Form):
    username = forms.CharField(max_length = 30 , required = True)
    password = forms.CharField(max_length = 30 , required = True)

class UpdateUserForm(forms.Form):
    email = forms.EmailField(max_length = 100 , required = True)
    cfhandle = forms.CharField(max_length = 100 , required = True)
    password = forms.CharField(max_length = 30 , required = True)

class UpdateUserPasswordForm(forms.Form):
    username = forms.CharField(max_length = 30 , required = True)
    password1 = forms.CharField(max_length = 30 , required = True)
    password2 = forms.CharField(max_length = 30 , required = True)

    