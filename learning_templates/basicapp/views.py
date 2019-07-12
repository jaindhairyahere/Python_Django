from django.shortcuts import render
from .forms import RegForm
from .models import user
# Create your views here.
def index(request):
	return render(request,'basicapp/index.html')

def register(request):
	form = RegForm()
	if request.method =="POST":
		form = RegForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Name :",form.cleaned_data["name"])
			print("Successfully Registered")
			return index(request)
		else:
			print("Invalid Form")

	return render(request,'basicapp/register.html',{'form':form})

def users(request):
	users = user.objects.order_by('name')
	return render(request,'basicapp/users.html',{'users':users})

def base(request):
	return render(request,'basicapp/base.html')
