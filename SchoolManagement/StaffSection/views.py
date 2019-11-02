from django.shortcuts import render, redirect
from django import forms
from django.views.generic import (ListView,DetailView,TemplateView,
								  CreateView,UpdateView,DeleteView)
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateStaff(CreateView):
	template_name = 'StaffSection/create.html'
	redirect_field_name = 'StaffSection/base.html'
	form_class = BecomeStaff




