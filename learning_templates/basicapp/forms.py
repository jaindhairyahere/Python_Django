from django import forms
from .models import customer
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		exclude = '__all__'
class UserProfileForm(forms.ModelForm):

	class Meta():
		model = UserProfileInfo
		fields = ('portfolio','picture')
