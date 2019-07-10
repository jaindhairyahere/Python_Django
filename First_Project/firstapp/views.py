from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em><h1>Hello World</h1></em>")

def help(request):
    helpdict = {'help_insert': "This is from Help Dict"}
    return render(request,'help.html', context = helpdict)
