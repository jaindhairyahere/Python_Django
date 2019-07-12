from django import forms
from .models import user

class RegForm(forms.ModelForm):
	class Meta():
		model = user
		fields = '__all__'
