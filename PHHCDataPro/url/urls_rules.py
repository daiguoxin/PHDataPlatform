from django.urls import re_path, path, include

from PHHCDataPro.views import views_rules, views_rules_pro, views_rules_data

urlpatterns = [

    path('cus/module/index/', views_rules.cus_module_index),
    path('cus/module/statistics/', views_rules.cus_module_statistics),
    path('cus/module/upload_table/', views_rules.cus_module_upload_table),
    path('cus/module/upload_rules/', views_rules.cus_module_upload_rules),

    path('cus_rules/index/', views_rules.rules_index),
    re_path(r'cus_rules/one_obj/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.one_obj),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/one_obj_generic/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.one_obj_generic),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/one_obj_basic/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.one_obj_basic),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/one_obj_product/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.one_obj_product),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})

    re_path(r'cus_rules/one_obj_condi/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.one_obj_condi),

    re_path(r'cus_rules/two_obj/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.two_obj),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/two_obj_generic/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.two_obj_generic),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/two_obj_basic/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.two_obj_basic),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})
    re_path(r'cus_rules/two_obj_product/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.two_obj_product),  # (?P[0-9]{1}[-]{1}[0-9]{1,2})

    re_path(r'cus_rules/two_obj_condi_query/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.two_obj_condi_query),

    re_path(r'cus_rules/many_obj_generic_condi_conclu/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.many_obj_generic_condi_conclu),
    re_path(r'cus_rules/many_obj_basic_condi_conclu/(?P<arg1>[0-9]{1}[-]{1}[0-9]{1,2})/', views_rules.many_obj_basic_condi_conclu),

    path('cus_rules/one_obj_condi2/', views_rules.one_obj_condi2),
    path('cus_rules/one_obj_condi_conclu/', views_rules.one_obj_condi_conclu),
    path('cus_rules/two_obj_condi/', views_rules.two_obj_condi),
    path('cus_rules/two_obj_condi2/', views_rules.two_obj_condi2),

    path('cus_rules/two_obj_condi_query_result/', views_rules.two_obj_condi_query_result),
    path('cus_rules/rules_add/', views_rules.rules_add),
    path('cus_rules/rules_add2/', views_rules.rules_add2),
    path('cus_rules/rules_add_group/', views_rules.rules_add_group),

    path('cus_rules/dict_select/', views_rules.dict_select),
    path('cus_rules/add_item/', views_rules.add_item),

    path('production/manage/index/', views_rules_pro.production_manage_index),
    path('production/manage/prod_tasks/', views_rules_pro.production_manage_prod_tasks),

    path('production/crowd/index/', views_rules_pro.production_crowd_index),
    path('production/crowd/manual/', views_rules_pro.production_crowd_manual),
    path('production/crowd/manualrules/', views_rules_pro.production_crowd_manualrules),

    path('production/crowd/genericname/', views_rules_pro.production_crowd_genericname),
    path('production/crowd/generic/', views_rules_pro.production_crowd_generic),
    path('production/crowd/basic/', views_rules_pro.production_crowd_basic),
    path('production/crowd/product/', views_rules_pro.production_crowd_product),

    path('cus/sys_rule_manage/', views_rules.cus_sys_rule_manage),
    path('cus/copy_rules/', views_rules.cus_copy_rules),
    path('cus/copy_cus_rules/', views_rules.cus_copy_cus_rules),
    path('cus/copy_tasks/', views_rules.copy_tasks),
    path('cus/copy_from_drug/', views_rules.copy_from_drug),

    path('service_opt/service_opt_index/', views_rules.service_opt_index),

    re_path(r'cus_rules/many_obj_condi_conclu/', views_rules.many_obj_condi_conclu),
    re_path(r'cus_rules/many_obj_condi_conclu_class/', views_rules.many_obj_condi_conclu_class),
    re_path(r'cus_rules/many_obj_condi_conclu_generic/', views_rules.many_obj_condi_conclu_generic),
    re_path(r'cus_rules/many_obj_condi_conclu_basic/', views_rules.many_obj_condi_conclu_basic),
    re_path(r'cus_rules/many_obj_condi_conclu_product/', views_rules.many_obj_condi_conclu_product),
    re_path(r'cus_rules/many_obj_condi_conclu_cus_drug/', views_rules.many_obj_condi_conclu_cus_drug),

    re_path(r'data/many_obj_condi_conclu/', views_rules_data.many_obj_condi_conclu),
    path('cus_rules/rules_add_not_only_object/', views_rules.rules_add_not_only_object),
]
