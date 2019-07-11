from django.shortcuts import render
from appTwo.models import User
from .form import MyForm
# Create your views here.

def index(request):
	return render(request,'appTwo/index.html')

def users(request):

	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request,'appTwo/users.html',context = user_dict)

def form_view(request):
	form = MyForm()
	if request.method == 'POST':
		form = MyForm(request.POST)

		if form.is_valid():
			print("VALIDATION SUCCESS")

			#accessing data gathered
			print("NAME :", form.cleaned_data['name'])
			print("Email :", form.cleaned_data['email'])
			print("Text :", form.cleaned_data['text'])

	return render(request, 'appTwo/forms.html', {'form':form})
