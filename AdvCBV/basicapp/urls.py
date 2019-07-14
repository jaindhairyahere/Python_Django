
#Creating Views

from django.urls import re_path,path
from basicapp.views import CBVview, IndexView, SchoolListView, SchoolDetaillView,SchoolCreateView,SchoolUpdateView, SchoolDeleteView

app_name = 'basicapp'

urlpatterns = [
    path('<int:pk>/',SchoolDetaillView.as_view(),name='detailview'),
    path('',SchoolListView.as_view(),name='listview'),
	path('create/',SchoolCreateView.as_view(),name='createview'),
	path('delete/<int:pk>/',SchoolDeleteView.as_view(),name='deleteview'),
	path('update/<int:pk>/',SchoolUpdateView.as_view(),name='updateview'),
    path('tempview/',CBVview.as_view(),name='tempview'),
]
