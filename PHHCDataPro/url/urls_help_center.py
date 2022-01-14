from django.urls import path

from PHHCDataPro.views import views_opt, views_help_center

urlpatterns = [
    # 医院数据管理主页：医院列表
    path('page/', views_help_center.page),
]
