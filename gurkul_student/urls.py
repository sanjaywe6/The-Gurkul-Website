from django import urls
from django.urls import path
from . import views
#  writing urls from here
urlpatterns=[
    path('student_profile/', views.student_profile,name='StudentProfilse'),
    
    path('edit_profile/', views.edit_profile,name='Edit Profilse'),

    path('student/join_gurkul/', views.join_gurkul,name='Join Gurkul Form'),

    path('complete_profile/', views.complete_profile,name='complete profile Form of user'),
]