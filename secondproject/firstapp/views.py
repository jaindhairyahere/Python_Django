from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import AccessRecord, Website, Topic
# Create your views here.

def index(request):
	return  HttpResponse("<p>Hello This is a para from Http response Django .</p>")

def newView(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list , 'tag1': "Hello This is from a template tag1 DJANGO." }
	return render(request,'firstapp/index.html',context=date_dict )

