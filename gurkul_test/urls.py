from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('test_series/',views.gurkul_test_index,name='Gurkul test index page'),

    path('test_series/academic_test_series_category/',views.academic_test_series_category,name='Academic test series category'),

    path('test_series/competition_test_series_category/',views.competition_test_series_category,name='Competition test series category'),

    path('test_series/edit_test_series/',views.edit_test_series,name='Editing test series questions'),
]