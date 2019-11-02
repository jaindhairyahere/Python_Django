from django.urls import path,re_path
from .models import *
from .views import *

#Creating URL Patterns Here

urlpatterns = [
	path('createstaff/',CreateStaff.as_view(),name='create'),
]
