from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ("id",)
        read_only_fields = ['id',]
    

