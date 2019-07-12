from django.urls import path
from .views import index, register, users, base

#TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns = [
	path('base',base,name='base'),
	path('register',register,name='register'),
	path('',index,name='index'),
	path('users/', users, name='users'),
]
