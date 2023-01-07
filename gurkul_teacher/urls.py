from django import urls
from django.urls import path
from . import views

#  writing urls from here
urlpatterns=[
    path('teacher_profile/', views.teacher_profile,name='Teacher profile home page'),

    path('edit_profile/', views.edit_profile,name='Teacher profile editing page'),

    
]