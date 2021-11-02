from django.urls import re_path, path, include

from PHHCDataPro.views import views_rules, views_rules_pro, views_object

urlpatterns = [
    path('production/manage/index/', views_object.production_manage_index),
    path('production/manage/prod_tasks/', views_object.production_manage_prod_tasks),

    path('production/drug/', views_object.drug),
    path('production/manual/', views_object.manual),
    path('production/generic/', views_object.generic),
    path('production/basic/', views_object.basic),
    path('production/product/', views_object.product),
    path('production/drugdetail/', views_object.drugdetail),
]
