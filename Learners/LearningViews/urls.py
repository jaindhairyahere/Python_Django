from django.urls import path
from .views import *


urlpatterns = [
	path('base/',L_BaseView.as_view(),name='baseview'),
	path('context/',L_ContentMixin.as_view(),name='contextmixin'),
	path('template/',L_TemplateView.as_view(),name='templateview'),
	path('redirect/',L_RedirectView.as_view(),name='redirectview'),
	path('detail/<int:pk>/',L_DetailView.as_view(),name='student-detail'),
	path('list/',L_ListView.as_view(),name='student-list'),
	path('',L_ListView.as_view(),name='student-list'),
	path('create/',L_CreateView.as_view(),name='createview'),
	path('delete/<int:pk>/',L_DeleteView.as_view(),name='deleteview'),
	path('update/<int:pk>/',L_UpdateView.as_view(),name='updateview'),

]
