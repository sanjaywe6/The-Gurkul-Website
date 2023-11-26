from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('student_registration/', views.student_registration, name='SMS Std. Registration'),
    
    path('all_student_data/', views.all_student_data, name='SMS Std. Data'),

    path('all_student_data/<str:sno>/', views.student_data_with_sno, name='SMS Std. Data with sno'),

]