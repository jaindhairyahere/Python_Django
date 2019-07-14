from django import forms
from django.contrib.auth.admin import User
from .models import Alumni
from django.core import validators
def check_PhoneNumber(value):
	if len(value) != 10:
		raise forms.ValidationError("Not a phone Number")

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username','email','password',)

class AlumniForm(forms.ModelForm):
	class Meta():
		model = Alumni
		exclude = ('user_model',)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=264)
	password = forms.CharField(widget = forms.PasswordInput())

