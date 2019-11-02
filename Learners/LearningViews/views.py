from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.utils.decorators import classonlymethod
from .models import Student
#This Base View is basically django.views.View or django.views.generic.base(.py).View(cls)
from django.views import View   #or '''from django.views.generic.base import View'''

class L_BaseView(View):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		print("\nInstantiating Object")
		print(self)
		print("Only Attribute of Base View Class :",self.http_method_names)

	def myview(self):
		return HttpResponse("Hello world")

	def setup(self, request, *args, **kwargs):
		super().setup(request,*args,**kwargs)
		print("\n running setup() : View class ,Now Setting Up SELF AND REQUEST variable")
		print(self.request)

	def dispatch(self, request, *args, **kwargs):
		print("\nUsing dispatch method() of View class"
			  ," ....accepts a request argument plus arguments, and returns a HTTP response.")
		print(self.request,self.args,self.kwargs)
		print(self.myview())
		return super().dispatch(request, *args, **kwargs)

	@classonlymethod
	def as_view(cls,**initkwargs):
		if print("\nRunning as_view() Method of View class"):
			pass

		return super().as_view(**initkwargs)

	def options(self, request, *args, **kwargs):
		print("\nOptions() method running from View class")
		return super().options(request,*args,**kwargs)

#These are base classes of Template View
from django.views.generic.base import TemplateResponse,TemplateResponseMixin,ContextMixin, TemplateView
class L_ContentMixin(ContextMixin,L_BaseView):
	'''
		extra_context = {..}	... sets context_dict keys, can be passes as an argument to
									<ClassName>.as_view() call in urls.py

		get_context_data(self,**kwargs) : adds extra_context to already passed kwargs dictionary
										  :returns **kwargs
	'''
	extra_context = {'title':'My Shit', 'description':'Just trying it'}
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("\nRunning get_context_data() method of ContentMixin class")
		print("**kwargs :",context)
		return context

class L_TemplateResponseMixin(TemplateResponseMixin):
	'''
		template_engine(default) = None
		content_type(default) = None
		response_class(default) = TemplateResponse(Unconfigured)
		template_name = 'path/file.html'	... renders/sends context_dict templates to file.html

		get_template_name(self):	:returns template_name if exists otherwise throws an error

		render_to_response(self,context,**response_kwargs) : SETS configuration to return self.response_class object

				calls get_template_name() to store self.template_name = get_template_name()
				sets **response_kwargs['content_type'] = self.content_type

				:returns 	self.response_class(request,using=template_engine,template(name),context,**response_kwargs)
					A response_class with configuration

	'''
	#template_name = 'LearningViews/base.html'
	template_name = 'LearningViews/base.html'
	def render_to_response(self, context, **response_kwargs):
		print("\nRunning render_to_response() method of TemplateResponseMixin Class")
		return super().render_to_response(context,**response_kwargs)

	def get_template_names(self):
		temp = super().get_template_names()
		print("Template Name :",temp)
		return temp

class L_TemplateView(L_TemplateResponseMixin,L_ContentMixin,TemplateView):
	'''
		get() : returns a response class(by calling TemplateResponseMixin's render_to_response() method)
		get_context_data() : sets context dict to that passed in **kwargs
							 can be overridden to add manual context_dict keys
	'''
	def get(self, request, *args, **kwargs):
		print("\nRunning get() method of TemplateView Class")
		return super().get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['inject'] = "This is an injection"
		print("\ncontext dict :",context)

		print("extra_context dict makes additional templates into context dict")
		return context

#Redirect View..... inherits only base View class
from django.views.generic.base import RedirectView
class L_RedirectView(L_BaseView,RedirectView):

	url = '/list/'
	# permanent = False
	#
	def get_redirect_url(self, *args, **kwargs):
		print("Kwargs supplied to get_redirect_url() :",kwargs)
		try:
			stud = get_object_or_404(Student, pk='1')
			print(type(stud.__class__.objects))
			for student in stud.__class__.objects.all():
				print(str(student),)
			student.print_something()

		except:
			pass
		return super().get_redirect_url(*args,**kwargs)
##############################################################################################
##############################################################################################

# Display Views : Detail View and List View
'''	
	Detail View: returns context of 'object':<object> to template_name file ... IE, A Single Object
				
	List View:  returns context of 'object':<object> to template_name file ... IE, An Object List
					
'''
#Detail View
from django.views.generic.detail import DetailView

class L_DetailView(DetailView):
	'''

	Detail View: has attributes model, context_object_name and other inherited attributes
		1	context_object_name = 'string'.... creates a new key in context dict with same value as key('object')

		2	model= models.<ModelName> ....  sets the model whose details you want to get.
		  		   context_dict is:   .... {'object':<model | pk={}> ,
											'<ModelName or context_object_name = >': <model | pk={}>,
											'view': view object}

		  		   url.py : .... path('<slug>/<pk>',<ClassName>.as_view(),name='<ModelName>-detail')
							.... i.e. name = 'modelname-detail'

		3	template_name = 'path/file.html'
							... renders/sends context_dict templates to file.html
								if not specified then sends context_dict templates to
										<AppName>/<ModelName>_detail.html


	'''
	model = Student
	context_object_name = 'students_class'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("New Context Dict is :",context)
		return context

	def get_template_names(self):
		names = super().get_template_names()
		print("Template Names : ",names)
		return names

#ListView
from django.views.generic.list import ListView
class L_ListView(ListView):
	'''
	List View: has attributes model, context_object_name and other inherited attributes
		1	context_object_name = 'string'.... creates a new key in context dict with same value as key('object')

		2	model= models.<ModelName> ....  sets the model whose details you want to get.
				   context_dict is:   .... {'object_list':<Queryset {all object list}> ,
											'<ModelName or context_object_name = >': <QuerySet {all object list}>,
											'view': view object
											'paginator':________, 'is_paginated':<status,None by default>
											'page_obj':None}

				   url.py : .... path('<slug>/<pk>',<ClassName>.as_view(),name='<ModelName>-list')
								 i.e. name = 'modelname-list'

		3	template_name = 'path/file.html'
					... renders/sends context_dict templates to file.html
						if not specified then sends context_dict templates to
							<AppName>/<ModelName>_list.html
	'''
	model = Student
	context_object_name = 'students_class'
	template_name = None
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("New Context Dict is :",context)
		if context['object_list']==context['students_class']:
			print("The Template returned by default ..i.e \"object_list\" is same as that set by context_object_name attribute")
		return context
	def get_template_names(self):
		names = super().get_template_names()
		print("\nTemplate Names : ",names)
		print("Setting \"template_name\" attribute adds to the Templates name list, but <model>_list.html is still there")
		print("But it will render templates only to last template_name added by setting the attribute")
		return names

##############################################################################################
##############################################################################################

# Editing Views : CRUD .. Create Retrieve(Form) Update Detele
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentForm
from django import forms
#FormView
class L_FormView(FormView):
	form_class = StudentForm
	template_name = 'LearningViews/myform.html'
	success_url = '/redirect/'
	def form_valid(self, form):
		is_valid = super().form_valid(form)
		return is_valid
	def get_template_names(self):
		names = super().get_template_names()
		print('Template Name of FormView is: ',names)
		return names
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("\nContext Dict in FormView is :",context)
		return context

	def login(self):
		pass

#CreateView
class L_CreateView(LoginRequiredMixin,CreateView):
	'''
		CreateView : creates a form on its own
	'''

	model = Student
	fields = ('name','age','email')
	login_url = '/login/'
	def get_template_names(self):
		names= super().get_template_names()
		print("TEmplate Name of CreateView is :",names)
		return names

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("\nContext Dict in CreateView is :",context)
		print("forms : ",context['form'])
		return context

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		forms = super().form_valid(form)

		print("Form Parameter is :",form)
		if self.object.email:
			self.sendEmail('ishita2277@gmail.com',str(self.object.email))
		else:
			self.sendEmail('ishita2277@gmail.com','jaindhairya2001@gmail.com')
		return forms

	def sendEmail(self,SENDER,RECEIVER):
		import smtplib
		import os
		from email.message import EmailMessage
		PASSWORD = os.environ.get("GMAIL_PASSWORD")
		text = "Successfully Registered\n Name : "+str(self.object.name)+" \nAge : "+str(self.object.age)
		if self.object.email:
			text += "\nEmail Registered: "+str(self.object.email)
		message = EmailMessage()
		message['Subject'] = "Welcome To London School of Economics"
		message['From'] = SENDER
		message['To'] = RECEIVER
		message.set_content(text)

		mail = smtplib.SMTP('smtp.gmail.com',587)

		mail.ehlo()
		mail.starttls()
		mail.login(user='jaindhairya2001@gmail.com',password=PASSWORD)

		mail.send_message(message)

		mail.close()

class L_DeleteView(DeleteView):
	model = Student
	success_url = '/redirect/'

class L_UpdateView(UpdateView):
	model = Student
	fields = ('email',)
	success_url = '/redirect/'
	def get_template_names(self):
		names= super().get_template_names()
		print("\nTEmplate Name of UpdateView is :",names)
		return names

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print("Context Dict in UpdateView is :",context)
		print("What is \"self.object\" ? : ",self.object)
		return context

#############################################################################################
#django.contrib.auth.models.User model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import authenticate
from django.contrib.auth.decorators import login_required
