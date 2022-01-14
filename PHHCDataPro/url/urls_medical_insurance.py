from django.urls import re_path, path, include

from PHHCDataPro.views import views_rules, views_phdata, views_medical_insurance

urlpatterns = [

    path('index/', views_medical_insurance.index),
    path('expense_details/', views_medical_insurance.expense_details),
    path('getstandarddict/', views_medical_insurance.getStandardDict),
    path('temp/', views_medical_insurance.temp),
    path('temp2/', views_medical_insurance.temp2),
    path('temp3/', views_medical_insurance.temp3),

]
