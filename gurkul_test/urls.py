from django import urls
from django.urls import path
from . import views

urlpatterns = [

    path('test_series/GTA_questions',views.GTA_index,name='GTA Home page'),

    path('test_series/GTA_questions/get__GTA_question_form',views.get__GTA_question_form,name='Get data of questions from page'),

    path('test_series/GTA_questions/return_gta_question',views.return_gta_question,name='Return filtered questions'),

    path('test_series/GTA_questions/return_question_with_id',views.return_question_with_id,name='Returning a question filtered with given id'),

    path('test_series/GTA_test_index',views.GTA_test_index,name='Test Series Index Page'),

    path('test_series/GTA_test_paper_index',views.GTA_test_paper_index,name='Test paper Index Page'),

    path('test_series/GTA_test_paper_data',views.GTA_test_paper_data,name='For fetching test series question and data'),

    path('test_series/match_GTA_test_paper_option',views.match_GTA_test_paper_option,name='Getting que. id and option from page and verifying in database'),

]