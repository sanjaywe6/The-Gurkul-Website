from django import urls
from django.urls import path
from . import views

#  writing urls from here
urlpatterns=[
    path('branch_profile/', views.branch_index,name='Branch web home page'),

    path('branch_profile/update_profile', views.update_branch_profile,name='Branch profile update'),
    
]