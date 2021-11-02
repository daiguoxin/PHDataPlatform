"""PHHCDataPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.url import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.url'))
"""
from django.contrib import admin
from django.urls import path, include

from PHHCDataPro.url import urls_rules, urls_phdata, urls_drug, urls_medical_insurance
from PHHCDataPro.views import views, views_opt, views_basic, views_object, views_common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('', views.login),
    path('index/', views.index),
    path('hos_index/', views.hos_index),
    path('opt_index/', views.opt_index),
    path('core_index/', views.core_index),
    
    path('home/console/', views.home_console),

    path('opt/index/', views_opt.index),
    path('opt/manage/', views_opt.manage),
    path('opt/my_data_mapping/', views_opt.my_data_mapping),
    path('opt/my_data_mapping_sys/', views_opt.my_data_mapping_sys),
    path('opt/my_data_mapping_disease/', views_opt.my_data_mapping_disease),
    path('opt/my_data_mapping_dict/', views_opt.my_data_mapping_dict),

    path('opt/my_data_mapping_relation/', views_opt.my_data_mapping_relation),
    path('opt/my_data_mapping_relation_opt/', views_opt.my_data_mapping_relation_opt),

    path('opt/my_data_mapping_audit/', views_opt.my_data_mapping_audit),




    path('opt/my_phdata_drug/', views_opt.my_phdata_drug),
    path('opt/my_phdata_disease/', views_opt.my_phdata_disease),
    path('opt/my_phdata_rule/', views_opt.my_phdata_rule),

    path('opt/opt_log/', views_opt.opt_log),
    path('opt/add_opt_log/', views_opt.add_opt_log),
    path('opt/opt_sys_tasks/', views_opt.opt_sys_tasks),

    path('opt/my/statistics/', views_opt.opt_my_statistics),


    path('opt/customer/', views_opt.customer),
    path('opt/my/drug/', views_opt.my_drug),
    path('opt/my/disease/', views_opt.my_disease),
    path('opt/my/otherdict/', views_opt.my_otherdict),
    path('opt/my/index/', views_opt.my_index),
    path('opt/my/set_check_result/', views_opt.my_set_check_result),
    path('opt/my/add_opt_task/', views_opt.my_add_opt_task),
    path('opt/my/check_detail/', views_opt.my_check_detail),

    path('opt/my/opt_tasks/', views_opt.my_opt_tasks),
    path('opt/my/opt_task_detail/', views_opt.my_opt_tasks_detail),
    path('opt/my/prod/prod_tasks/', views_opt.prod_tasks),
    path('opt/my/prod/data_mapping_tasks/', views_opt.data_mapping_tasks),
    path('opt/my/prod/dict_opt_taks/', views_opt.dict_opt_taks),
    path('opt/my/prod/data_mapping_task_detail/', views_opt.data_mapping_task_detail),
    path('opt/my/prod/data_mapping_task_detail2/', views_opt.data_mapping_task_detail2),
    path('opt/my/prod/data_mapping_task_detail3/', views_opt.data_mapping_task_detail3),
    path('opt/my/prod/dict_customer/', views_opt.dict_customer),

    path('opt/my/prod/add_dm_task/', views_opt.add_dm_task),

    # 生产任务-药品
    path('opt/my/prod/prod_task_detail/', views_opt.prod_task_detail),
    # 生产任务-诊断
    path('opt/my/prod/prod_task_detail2/', views_opt.prod_task_detail2),
    # 生产任务-规则
    path('opt/my/prod/prod_task_detail3/', views_opt.prod_task_detail3),
    # 生产任务-统计
    path('opt/my/prod/prod_task_detail4/', views_opt.prod_task_detail4),
    path('opt/my/prod/dict_check_item/', views_opt.dict_check_item),

    path('basic/index/', views_basic.index),
    path('basic/data_input/', views_basic.data_input),

    path('object/drugproduct/', views_object.drugproduct),
    path('object/drugmanual/', views_object.drugmanual),

    path('object/uploaddrugmanual/', views_object.uploaddrugmanual),

    path('common/uploadfile/', views_common.uploadfile),
    path('common/logview/', views_common.logview),

    # 规则数据管理
    path('rule/', include(urls_rules.urlpatterns)),

    path('phdata/', include(urls_phdata.urlpatterns)),
    path('drug/', include(urls_drug.urlpatterns)),

    path('mi/', include(urls_medical_insurance.urlpatterns)),
]
