from django import urls
from django.urls import path
from . import views
#  writing urls from here
urlpatterns=[
    path('student_profile/', views.student_profile,name='StudentProfilse'),
    
    path('edit_profile/', views.edit_profile,name='Edit Profile'),

    path('student/join_gurkul/', views.join_gurkul,name='Join Gurkul Form'),

]