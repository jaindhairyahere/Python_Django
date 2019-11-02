from django import forms
from .models import *

#Creating Forms Here
class BecomeStaff(forms.Form):
	available_staff_types  = [
		('T','Teacher'),('D','Driver'),('H','Helper')
	]
	staff_type = forms.ChoiceField(choices=available_staff_types)



class StaffForm(forms.ModelForm):
	class Meta():
		model = Staff
		exclude = ('salary',)

class TeacherForm(forms.ModelForm):

	class Meta():
		model = Teacher
		fields = ('department','highest_degree','experience',)

class DriverForm(forms.ModelForm):

	class Meta():
		model = Driver
		fields = ('experience',)

class HelperForm(forms.ModelForm):

	class Meta():
		fields = ('area',)



