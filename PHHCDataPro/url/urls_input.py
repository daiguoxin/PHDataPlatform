from django.urls import re_path, path, include

from PHHCDataPro.views import views_rules, views_phdata, views_medical_insurance, views_input

urlpatterns = [

    path('index/', views_input.index),

]
