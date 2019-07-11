from django import forms
from django.core import validators
from appTwo.models import User

def check_for_d(value):
	if value[0].lower() !='d':
		raise forms.ValidationError("Name needs to start with D")

class MyForm(forms.Form):
	name = forms.CharField(validators= [check_for_d])
	email = forms.EmailField()
	verify_email = forms.EmailField(label="Enter Your Email Again")
	text = forms.CharField(widget = forms.Textarea, label="Your Reviews")
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data = super(MyForm, self).clean()
		email = all_clean_data['email']
		vemail = all_clean_data['verify_email']
		if email!= vemail:
			raise forms.ValidationError("Emails Dont Match")

class Modelform(forms.ModelForm):
	#form fields go here

	class Meta:
		model = User
		fields = "__all__"

