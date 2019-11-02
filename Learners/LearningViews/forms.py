from django import forms
from .models import Student

class StudentForm(forms.Form):
	username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'input'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

