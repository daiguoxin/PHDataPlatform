from django.urls import path

from PHHCDataPro.views import views_opt

urlpatterns = [

    # 医院数据管理主页：医院列表
    path('customer_data/customer_list/', views_opt.customer_data_customer_list),

    # 数据采集
    path('customer_data/data_acquisition/', views_opt.customer_data_data_acquisition),
    path('customer_data/drug_relation_checked/', views_opt.customer_data_drug_relation_checked),

    # 运营日志
    path('opt_log/', views_opt.opt_log),
    path('add_opt_log/', views_opt.add_opt_log),



    # 数据关联
    # 医院列表页
    path('customer_data_relation/customer_list/', views_opt.customer_data_relation_customer_list),
    path('customer_data_relation/data_mapping_drug/', views_opt.customer_data_relation_data_mapping_drug),
    path('customer_data_relation/data_mapping_disease/', views_opt.customer_data_relation_data_mapping_disease),
    path('customer_data_relation/data_mapping_dict/', views_opt.customer_data_relation_data_mapping_dict),
    path('customer_data_relation/data_mapping_piece/', views_opt.customer_data_relation_data_mapping_piece),



    path('my_data_mapping/', views_opt.my_data_mapping),
    path('my_data_mapping_sys/', views_opt.my_data_mapping_sys),
    path('my_data_mapping_disease/', views_opt.my_data_mapping_disease),
    path('my_data_mapping_dict/', views_opt.my_data_mapping_dict),

    path('my_data_mapping_relation/', views_opt.my_data_mapping_relation),
    path('my_data_mapping_relation_opt/', views_opt.my_data_mapping_relation_opt),

    path('my_data_mapping_audit/', views_opt.my_data_mapping_audit),

    path('my_phdata_drug/', views_opt.my_phdata_drug),
    path('my_phdata_disease/', views_opt.my_phdata_disease),
    path('my_phdata_rule/', views_opt.my_phdata_rule),



    path('opt_sys_tasks/', views_opt.opt_sys_tasks),

    path('my/statistics/', views_opt.opt_my_statistics),

    path('customer/', views_opt.customer),
    path('my/drug/', views_opt.my_drug),
    path('my/disease/', views_opt.my_disease),
    path('my/otherdict/', views_opt.my_otherdict),

    path('my/set_check_result/', views_opt.my_set_check_result),
    path('my/add_opt_task/', views_opt.my_add_opt_task),
    path('my/check_detail/', views_opt.my_check_detail),

    path('my/opt_tasks/', views_opt.my_opt_tasks),
    path('my/opt_task_detail/', views_opt.my_opt_tasks_detail),
    path('my/prod/prod_tasks/', views_opt.prod_tasks),
    path('my/prod/data_mapping_tasks/', views_opt.data_mapping_tasks),
    path('my/prod/dict_opt_taks/', views_opt.dict_opt_taks),
    path('my/prod/data_mapping_task_detail/', views_opt.data_mapping_task_detail),
    path('my/prod/data_mapping_task_detail2/', views_opt.data_mapping_task_detail2),
    path('my/prod/data_mapping_task_detail3/', views_opt.data_mapping_task_detail3),
    path('my/prod/dict_customer/', views_opt.dict_customer),

    path('my/prod/add_dm_task/', views_opt.add_dm_task),

    # # 生产任务-药品
    # path('my/prod/prod_task_detail/', views_opt.prod_task_detail),
    # # 生产任务-诊断
    # path('my/prod/prod_task_detail2/', views_opt.prod_task_detail2),
    # # 生产任务-规则
    # path('my/prod/prod_task_detail3/', views_opt.prod_task_detail3),
    # # 生产任务-统计
    # path('my/prod/prod_task_detail4/', views_opt.prod_task_detail4),
    # path('my/prod/dict_check_item/', views_opt.dict_check_item),

    # # 任务分配
    # path('manage/', views_opt.manage),

]
