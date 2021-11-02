from django.urls import re_path, path, include

from PHHCDataPro.views import views_rules, views_phdata

urlpatterns = [

    path('cus/index/', views_phdata.cus_index),
    path('cus/xy_disease/', views_phdata.xy_disease),
    path('cus/zy_disease/', views_phdata.zy_disease),

    path('cus/diseasesource/', views_phdata.cus_diseasesource),
    path('cus/frequenry/', views_phdata.cus_frequenry),
    path('cus/drugspecpackage/', views_phdata.cus_drugspecpackage),

]
