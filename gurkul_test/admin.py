from django.contrib import admin
from gurkul_test.models import *

# Register your models here.
admin.site.register(gurkul_academic_test_series_model)
admin.site.register(gurkul_competition_test_series_model)
admin.site.register(all_academic_available_test_series)
admin.site.register(all_competition_available_test_series)