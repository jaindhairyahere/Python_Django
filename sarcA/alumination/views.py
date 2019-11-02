from django.shortcuts import render, reverse, redirect
from django.views.generic import FormView
from .forms import *
from django.core import validators
# Create your views here.
def index(request):
	return render(request,'base.html')

def eventview(request):
	return render(request,'events.html')


# class Base_FormView(FormView):
# 	template_name = 'Registration.html'
# 	success_url = '/events'
# 	def form_valid(self, form):
# 		if form.is_valid():
# 			form.save()
# 			print("Saved Successfully")
# 			return super().form_valid(form)

# class Workshop_View(Base_FormView):
# 	form_class = Workshop_Form
# 	def get_context_data(self, **kwargs):
# 		a = super().get_context_data(**kwargs)
# 		a['workshop_form'] = a['form']
# 		print("Context Data",a)
# 		return a

# class SpeedMentoring_View(Base_FormView):
# 	form_class = SpeedMentoring_Form
# 	def get_context_data(self, **kwargs):
# 		a = super().get_context_data(**kwargs)
# 		a['speed_form'] = a['form']
# 		print("Context Data",a)
# 		return a

# class MIGD_View(Base_FormView):
# 	form_class = MI_GD_Form
# 	def get_context_data(self, **kwargs):
# 		a = super().get_context_data(**kwargs)
# 		a['migd_form'] = a['form']
# 		print("Context Data",a)
# 		return a

def register_view(request):
	formA = Workshop_Form
	formB = SpeedMentoring_Form
	formC = MI_GD_Form

	if (request.method=='POST'):
		formA = Workshop_Form(request.POST)
		formB = SpeedMentoring_Form(request.POST)
		formC = MI_GD_Form(request.POST)

		if ( formA.is_valid() or formB.is_valid() or formC.is_valid() ):
			if formA.is_valid():
				formA.save(commit=True)
			if formB.is_valid():
				formB.save(commit=True)
			if formC.is_valid():
				formC.save(commit=True)
			return render(request,'Registration.html',context={'workshop_form':formA,'speed_form':formB,'migd_form':formC})

	return render(request,'Registration.html',context={'workshop_form':formA,'speed_form':formB,'migd_form':formC})
