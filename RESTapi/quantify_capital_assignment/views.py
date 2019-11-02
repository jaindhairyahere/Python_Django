from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Movie
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer
import numpy as np
import pandas as pd
import sqlite3

class MovieRUDView(generics.RetrieveAPIView):
    lookup_field = 'pk'  #slug or id
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all().order_by('rating')

from django.db.models import Q,F
class MovieAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs= Movie.objects.all()
        query = self.request.GET.get("q")
        order = self.request.GET.get("order")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(description__icontains=query))
            if order is not None:
                qs = qs.order_by(order)
                return qs
            qs = qs.order_by('-rating')
            return qs
        if order is not None:
            qs = qs.order_by(order)
            return qs
        qs = qs.order_by('-rating')
        return qs
