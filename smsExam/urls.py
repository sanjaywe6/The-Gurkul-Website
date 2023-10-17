from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('student_registration/', views.student_registration, name='SMS Std. Registration')
]