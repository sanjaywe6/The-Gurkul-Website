from django import urls
from django.urls import path
from . import views

urlpatterns = [

    path('test_series/GTA_questions',views.GTA_index,name='GTA Home page'),

    path('test_series/GTA_questions/get__GTA_question_form',views.get__GTA_question_form,name='Get data of questions from page'),

    path('test_series/GTA_questions/return_gta_question',views.return_gta_question,name='Return filtered questions'),

    path('test_series/GTA_questions/return_question_with_id',views.return_question_with_id,name='Returning a question filtered with given id'),

]