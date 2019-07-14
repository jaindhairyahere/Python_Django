from django.urls import path
from .views import index,base_view, signup_view, login_view, logout_view

app_name = 'profilecreate'

urlpatterns = [
	path('base/',base_view,name='base_view'),
	path('signup/',signup_view,name='signup_view'),
	path('login/',login_view,name='login_view'),
	path('logout/',logout_view,name='logout_view'),
	path('',index,name='index'),
]
