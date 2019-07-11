from django.contrib import admin
from django.urls import path, include
from firstapp.views import index, newView
urlpatterns = [
    path('newView/', newView, name = 'newview'),
    path('index/', index, name = 'index')
]
