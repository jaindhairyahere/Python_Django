from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
urlpatterns = [
    path('',views.MovieAPIView.as_view(),name='movie-search'),
    path('<int:pk>/', views.MovieRUDView.as_view(), name='movie-retrieve'),
    
]
