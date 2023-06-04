from django import urls
from django.urls import path
from . import views
#  writing urls from here
urlpatterns=[
    path('student_profile/', views.student_profile,name='StudentProfilse'),
    
    path('edit_profile/', views.edit_profile,name='Edit Profile'),

    path('edit_educational_profile/', views.edit_educational_profile,name='Edit Educational Data of Student Profile'),

    path('load_old_educational_profile/', views.load_old_educational_profile,name='Load Old Educational Data of Student Profile'),

    path('student/join_gurkul/', views.join_gurkul,name='Join Gurkul Form'),

]