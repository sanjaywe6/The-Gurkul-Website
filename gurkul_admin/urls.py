from django import urls
from django.urls import path
from . import views

#  writing urls from here
urlpatterns=[
    path('admin_index/', views.gurkul_admin_index,name='Gurkul Admin Index Page'),
    
]