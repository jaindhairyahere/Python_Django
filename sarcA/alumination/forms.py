from django.forms import Form, ModelForm
from django import forms
from .models import *

class BasicForm(ModelForm):
	class Meta:
		exclude = ("event",)
		widgets = {
		'name' : forms.TextInput(attrs={"class":"form-label"}),
		'age' : forms.TextInput(attrs={"class":"form-label"}),
		'email' : forms.EmailInput(attrs={"class":"form-label"}),
		'phone_no' : forms.TextInput(attrs={"class":"form-label"}),
		}

class Workshop_Form(BasicForm,ModelForm):
	class Meta(BasicForm.Meta):
		model = Workshops
class SpeedMentoring_Form(BasicForm):
	class Meta(BasicForm.Meta):
		model = SpeedMentoring
class MI_GD_Form(BasicForm):
	class Meta(BasicForm.Meta):
		model = MIGD
