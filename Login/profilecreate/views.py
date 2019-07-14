from django.shortcuts import render
from django.contrib.auth.admin import User
from .forms import AlumniForm, UserForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request,'index.html')

def base_view(request):
	return render(request,'base.html')

def signup_view(request):
	registered = False

	if request.method =='POST':
		print(request.method)

		user_form = UserForm(request.POST,request.FILES)
		alumni_form = AlumniForm(request.POST,request.FILES)

		if user_form.is_valid() and alumni_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			alumni = alumni_form.save(commit=False)
			alumni.user_model = user
			if 'picture' in request.FILES:
				alumni.picture = request.FILES['picture']
				print('Picture is Here')
			else:
				print("NO They aren't")
				print(request.FILES)
			alumni.save()
			registered =True
		else:
			print(user_form.errors, alumni_form.errors)
	else:
		user_form = UserForm()
		alumni_form = AlumniForm()
		print(request.method)
	return render(request,'signup.html',context={'user_form':user_form,'alumni_form':alumni_form,'registered':registered})




def login_view(request):
	form  = LoginForm()
	logined = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		user = authenticate(username = request.POST['username'], password=request.POST['password'])

		if user:
			if user.is_active:
				logined = True
				login(request,user)
				return render(request,'base.html')
			else:
				return HttpResponse("Account Not Active")
		else:
			print(request.POST['username']," tried to login and failed")
			return HttpResponse("Try Again... LOGIN FAILED")
	return render(request,'login.html',{'logined':logined, 'form':form})

@login_required
def logout_view(request):
	logout(request)
	return render(request,'base.html')

@login_required
def after_login(request):
	return HttpResponse("Yay You are logged in now")
