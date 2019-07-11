from django.urls import path
from appTwo import views

urlpatterns = [
	path('forms.html',views.form_view,name='form_view'),
	path('',views.index,name='index'),
	path('users/',views.users,name='users'),
]
