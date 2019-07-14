from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .models import School,Student
#Creating Class Based Views Here
class IndexView(View):
	def get(self,request):
		return HttpResponse("Hello World")

class CBVview(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['mystring']= "This is from A Template Insertion"
		return context

class SchoolListView(ListView):
	context_object_name = 'schools'
	model = School
	template_name = 'school_list.html'

class SchoolDetaillView(DetailView):
	context_object_name = 'school_detail'
	model = School
	template_name = 'school_details.html'

class SchoolCreateView(CreateView):
	model = School
	fields = "__all__"

class SchoolUpdateView(UpdateView):
	model = School
	fields = ('name','principal')
class SchoolDeleteView(DeleteView):
	model = School
	success_url = reverse('basicapp:listview')
