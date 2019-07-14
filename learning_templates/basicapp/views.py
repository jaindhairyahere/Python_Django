from django.shortcuts import render
from .forms import UserProfileForm, UserForm
from .models import customer
# Create your views here.
def index(request):
	return render(request,'basicapp/index.html')

def register(request):
	registered = False
	if request.method =="POST":
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			user.set_password(user.password)

			profile = profile_form.save(commit=False)
			profile.user= user

			if 'profile.picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered =True
			print("Successfully Registered")
			return index(request)
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		print(request.method)

	return render(request,'basicapp/register.html',{'user_form':user_form,
													'profile_form':profile_form})

def users(request):
	users = customer.objects.order_by('name')
	return render(request,'basicapp/users.html',{'users':users})

def base(request):
	return render(request,'basicapp/base.html')
