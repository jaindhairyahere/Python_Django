from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('events', eventview,name='events'),
    path('register', register_view,name='register'),
    # path('register/2', SpeedMentoring_View.as_view(),name='speed'),
    # path('register/3', MIGD_View.as_view(),name='migd'),
]
