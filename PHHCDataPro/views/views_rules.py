from django.shortcuts import render

from PHHCDataPro.service import AuditItem


def cus_module_index(request):
    # 规则模块-首页

    return render(request, 'views/rule/cus_rules/index.html', {})


def cus_module_statistics(request):
    # 规则模块-药品规则数据统计

    return render(request, 'views/rule/cus_rules/statistics.html', {})


def cus_module_upload_table(request):
    # 规则模块-选择表格
    return render(request, 'views/rule/cus_rules/upload_table.html', {})


def cus_module_upload_rules(request):
    # 规则模块-显示规则
    return render(request, 'views/rule/cus_rules/upload_rules.html', {})


def rules_index(request):
    """
    按模块首页
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/index.html', {})


def one_obj(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/one_obj.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def one_obj_generic(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/one_obj_generic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def one_obj_basic(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/one_obj_basic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def one_obj_product(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/one_obj_product.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def two_obj(request, arg1):
    """
    双药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/two_obj.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def two_obj_generic(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/two_obj_generic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def two_obj_basic(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/two_obj_basic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def two_obj_product(request, arg1):
    """
    单药列表页
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)
    return render(request, 'views/rule/cus_rules/two_obj_product.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def one_obj_condi(request, arg1):
    """
    单药-规则条件
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)

    return render(request, 'views/rule/cus_rules/one_obj_condi.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def one_obj_condi2(request):
    """
    单药-规则条件-第二套反规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/one_obj_condi2.html', {})


def one_obj_condi_conclu(request):
    """
    单药-规则条件结论
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/one_obj_condi_conclu.html', {})


def two_obj_condi(request):
    """
    双药-规则条件
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/two_obj_condi.html', {})


def two_obj_condi2(request):
    """
    双药-规则条件
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/two_obj_condi2.html', {})


def two_obj_condi_query(request, arg1):
    """
    双药-规则条件_查询
    :param request:
    :return:
    """
    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)

    return render(request, 'views/rule/cus_rules/two_obj_condi_query.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def two_obj_condi_query_result(request):
    """
    双药-规则条件_查询结果
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/two_obj_condi_query_result.html', {})


def rules_add(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/rules_add.html', {})


def rules_add2(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/rules_add2.html', {})


def rules_add_group(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/rules_add_group.html', {})


def cus_sys_rule_manage(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/sys_rule_manage.html', {})


def cus_copy_rules(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/copy_rules.html', {})


def cus_copy_cus_rules(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/copy_cus_rules.html', {})


def copy_sys_rules(request):
    """
    复制系统规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/copy_sys_rules.html', {})


def copy_tasks(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/copy_tasks.html', {})


def copy_from_drug(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus/copy_from_drug.html', {})


def service_opt_index(request):
    """
    service_opt_index
    :param request:
    :return:
    """
    return render(request, 'views/rule/service_opt/service_opt_index.html', {})


def service_config(request):
    """
    service_opt_index
    :param request:
    :return:
    """
    return render(request, 'views/rule/service_opt/service_config.html', {})


def dict_select(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/dict_select.html', {})


def add_item(request):
    """
    新增规则
    :param request:
    :return:
    """
    return render(request, 'views/rule/cus_rules/add_item.html', {})


def many_obj_generic_condi_conclu(request, arg1):
    """
    新增规则
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)

    return render(request, 'views/rule/cus_rules/many_obj_generic_condi_conclu.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def many_obj_basic_condi_conclu(request, arg1):
    """
    新增规则
    :param request:
    :return:
    """

    audit_item_id = arg1
    audit_item_name = AuditItem.get_audit_item_name(arg1)

    return render(request, 'views/rule/cus_rules/many_obj_basic_condi_conclu.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_name})


def many_obj_condi_conclu_class(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = request.GET['auditItem']
    manage_index_list = ['按全院管理', '按就诊类型管理', '按科室管理', '按病区管理', '按医生管理', '按患者管理', '按药品分类管理', '按抗菌药物分级管理',
                         '药品通用名', '药品通用名+规格', '药品通用名+规格+厂家', '药监局药品本位码', '医院药品编码']

    # 初始化规则生产维度，生成维度包括层级和合并关系。
    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu_class.html',
                  {'audit_item_id': audit_item_id, 'audit_item_name': audit_item_id,
                   'manage_index_list': manage_index_list})


def many_obj_condi_conclu_generic(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = request.GET['auditItem']

    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu_generic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id})


def many_obj_condi_conclu_basic(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = request.GET['auditItem']

    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu_basic.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id})


def many_obj_condi_conclu_product(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = request.GET['auditItem']

    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu_product.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id})


def many_obj_condi_conclu_cus_drug(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = request.GET['auditItem']

    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu_cus_drug.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id})


def many_obj_condi_conclu(request):
    """
    新增规则
    :param request:
    :return:
    """
    # todo 需要过滤特殊符号和内容编码，去除左右空格。
    audit_item_id = request.GET['auditItem']

    # 管理维度
    manage_index_list = getManageIndexList(audit_item_id)
    curr_manage_index = None
    if 'curr_manage_index' in request.GET:
        curr_manage_index = request.GET['curr_manage_index']
    else:
        curr_manage_index = manage_index_list[0]

    # 搜索条件
    search_condition_list = get_search_condition_list(audit_item_id, curr_manage_index)

    # 显示列
    show_col_list = get_show_col_list(audit_item_id, curr_manage_index)

    # 初始化规则生产维度，生成维度包括层级和合并关系。
    return render(request, 'views/rule/cus_rules/many_obj_condi_conclu.html',
                  {'audit_item_id': audit_item_id, 'audit_item_name': audit_item_id,
                   'curr_manage_index': curr_manage_index, 'manage_index_list': manage_index_list,
                   'search_condition_list': search_condition_list, 'show_col_list': show_col_list})


def getManageIndexList(audit_item_id):
    manage_index_list = None
    if audit_item_id == '抗菌药物分级管理':
        manage_index_list = ['按抗菌药物分级管理', '本院药品通用名']
    elif audit_item_id == '药物送检提醒':
        manage_index_list = ['本院药品通用名']
        # manage_index_list = ['按抗菌药物分级管理',
        #                      '本院药品通用名', '本院药品通用名规格', '本院药品通用名规格厂家', '本院药品编码']
    elif audit_item_id == '用法用量推荐':
        manage_index_list = ['本院药品通用名']
        # manage_index_list = ['本院药品通用名', '本院药品通用名规格', '本院药品通用名规格厂家', '本院药品编码']
    else:
        manage_index_list = ['按全院管理', '按就诊类型管理', '按科室管理', '按病区管理', '按医生管理', '按患者管理', '按药品分类管理', '按抗菌药物分级管理',
                             '药品通用名', '药品通用名规格', '药品通用名规格厂家', '药监局药品本位码', '本院药品编码']

    return manage_index_list


def get_search_condition_list(audit_item_id, curr_manage_index):
    search_condition_list = None
    if audit_item_id == '抗菌药物分级管理':
        if curr_manage_index == '按抗菌药物分级管理':
            search_condition_list = [
                {'name': '抗菌药物分级', 'input_type': '输入框', 'code': '抗菌药物分级'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名':
            search_condition_list = [
                {'name': '本院药品通用名', 'input_type': '输入框', 'code': '本院药品通用名'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格':
            search_condition_list = [
                {'name': '本院药品通用名规格', 'input_type': '输入框', 'code': '本院药品通用名规格'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格厂家':
            search_condition_list = [
                {'name': '本院药品通用名规格厂家', 'input_type': '输入框', 'code': '本院药品通用名规格厂家'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品编码':
            search_condition_list = [
                {'name': '本院药品编码', 'input_type': '输入框', 'code': '本院药品编码'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
    elif audit_item_id == '药物送检提醒':
        if curr_manage_index == '按抗菌药物分级管理':
            search_condition_list = [
                {'name': '抗菌药物分级', 'input_type': '输入框', 'code': '抗菌药物分级'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名':
            search_condition_list = [
                {'name': '本院药品通用名', 'input_type': '输入框', 'code': '本院药品通用名'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格':
            search_condition_list = [
                {'name': '本院药品通用名规格', 'input_type': '输入框', 'code': '本院药品通用名规格'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格厂家':
            search_condition_list = [
                {'name': '本院药品通用名规格厂家', 'input_type': '输入框', 'code': '本院药品通用名规格厂家'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品编码':
            search_condition_list = [
                {'name': '本院药品编码', 'input_type': '输入框', 'code': '本院药品编码'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
    elif audit_item_id == '用法用量推荐':
        if curr_manage_index == '本院药品通用名':
            search_condition_list = [
                {'name': '本院药品通用名', 'input_type': '输入框', 'code': '本院药品通用名'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格':
            search_condition_list = [
                {'name': '本院药品通用名规格', 'input_type': '输入框', 'code': '本院药品通用名规格'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品通用名规格厂家':
            search_condition_list = [
                {'name': '本院药品通用名规格厂家', 'input_type': '输入框', 'code': '本院药品通用名规格厂家'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}
            ]
        elif curr_manage_index == '本院药品编码':
            search_condition_list = [
                {'name': '本院药品编码', 'input_type': '输入框', 'code': '本院药品编码'},
                {'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}]
    else:
        search_condition_list = [{'name': '状态', 'input_type': '下拉列表框', 'code': '状态'},
                                 {'name': '级别', 'input_type': '下拉列表框', 'code': '级别'},
                                 {'name': '备注', 'input_type': '输入框', 'code': '备注'},
                                 {'name': '操作时间', 'input_type': '日期区间', 'code': '操作时间'},
                                 {'name': '操作人', 'input_type': '输入框', 'code': '操作人'},
                                 {'name': '升级时间', 'input_type': '日期区间', 'code': '升级时间'}]

    return search_condition_list


def get_show_col_list(audit_item_id, curr_manage_index):
    show_col_list = None
    if audit_item_id == '药物送检提醒':
        # if curr_manage_index == '本院药品通用名':
        show_col_list = [
            {'name': 'checkbox', 'hide': 'true', 'title': 'checkbox', 'width': '100', 'fixed': 'left'},
            {'name': 'ruleId', 'hide': 'true', 'title': 'ruleId', 'width': '100', 'fixed': 'left'},
            {'name': '项目', 'hide': 'false', 'title': '项目', 'width': '300', 'fixed': 'left'},
            {'name': '状态', 'hide': 'false', 'title': '状态', 'width': '60', 'fixed': ''},
            {'name': '触发条件', 'hide': 'false', 'title': '触发条件', 'width': '100', 'fixed': ''},
            {'name': '判断因素', 'hide': 'false', 'title': '判断因素', 'width': '100', 'fixed': ''},
            {'name': '依据', 'hide': 'false', 'title': '依据', 'width': '80', 'fixed': ''},
            {'name': '结果', 'hide': 'false', 'title': '结果', 'width': '80', 'fixed': ''},
            {'name': '提示级别', 'hide': 'false', 'title': '提示级别', 'width': '100', 'fixed': ''},
            {'name': '提示信息', 'hide': 'false', 'title': '提示信息', 'width': '280', 'fixed': ''},
            {'name': '备注', 'hide': 'false', 'title': '备注', 'width': '100', 'fixed': ''},
            {'name': '最后操作时间', 'hide': 'false', 'title': '最后操作时间', 'width': '120', 'fixed': ''},
            {'name': '最后操作人', 'hide': 'false', 'title': '最后操作人', 'width': '120', 'fixed': ''},
            {'name': '升级时间', 'hide': 'false', 'title': '升级时间', 'width': '120', 'fixed': ''},
            {'name': '生效时间', 'hide': 'true', 'title': '生效时间', 'width': '120', 'fixed': ''},
            {'name': '停用时间', 'hide': 'true', 'title': '停用时间', 'width': '120', 'fixed': ''},
        ]
    elif audit_item_id == '用法用量推荐':
        # if curr_manage_index == '本院药品通用名':
        show_col_list = [
            {'name': 'checkbox', 'hide': 'true', 'title': 'checkbox', 'width': '100', 'fixed': 'left'},
            {'name': 'ruleId', 'hide': 'true', 'title': 'ruleId', 'width': '100', 'fixed': 'left'},
            {'name': '项目', 'hide': 'false', 'title': '项目', 'width': '300', 'fixed': 'left'},
            {'name': '状态', 'hide': 'false', 'title': '状态', 'width': '60', 'fixed': ''},
            {'name': '触发条件', 'hide': 'false', 'title': '触发条件', 'width': '100', 'fixed': ''},
            {'name': '判断因素', 'hide': 'true', 'title': '判断因素', 'width': '100', 'fixed': ''},
            {'name': '依据', 'hide': 'false', 'title': '依据', 'width': '80', 'fixed': ''},
            {'name': '结果', 'hide': 'true', 'title': '结果', 'width': '80', 'fixed': ''},
            {'name': '提示级别', 'hide': 'true', 'title': '提示级别', 'width': '100', 'fixed': ''},
            {'name': '提示信息', 'hide': 'false', 'title': '提示信息', 'width': '280', 'fixed': ''},
            {'name': '备注', 'hide': 'false', 'title': '备注', 'width': '100', 'fixed': ''},
            {'name': '最后操作时间', 'hide': 'false', 'title': '最后操作时间', 'width': '120', 'fixed': ''},
            {'name': '最后操作人', 'hide': 'false', 'title': '最后操作人', 'width': '120', 'fixed': ''},
            {'name': '升级时间', 'hide': 'false', 'title': '升级时间', 'width': '120', 'fixed': ''},
            {'name': '生效时间', 'hide': 'true', 'title': '生效时间', 'width': '120', 'fixed': ''},
            {'name': '停用时间', 'hide': 'true', 'title': '停用时间', 'width': '120', 'fixed': ''},
        ]
    elif audit_item_id == '抗菌药物分级管理':
        # if curr_manage_index == '本院药品通用名':
        show_col_list = [
            {'name': 'checkbox', 'hide': 'true', 'title': 'checkbox', 'width': '100', 'fixed': 'left'},
            {'name': 'ruleId', 'hide': 'true', 'title': 'ruleId', 'width': '100', 'fixed': 'left'},
            {'name': '项目', 'hide': 'false', 'title': '项目', 'width': '300', 'fixed': 'left'},
            {'name': '状态', 'hide': 'false', 'title': '状态', 'width': '60', 'fixed': ''},
            {'name': '触发条件', 'hide': 'false', 'title': '触发条件', 'width': '100', 'fixed': ''},
            {'name': '判断因素', 'hide': 'false', 'title': '判断因素', 'width': '100', 'fixed': ''},
            {'name': '依据', 'hide': 'false', 'title': '依据', 'width': '80', 'fixed': ''},
            {'name': '结果', 'hide': 'true', 'title': '结果', 'width': '80', 'fixed': ''},
            {'name': '提示级别', 'hide': 'true', 'title': '提示级别', 'width': '100', 'fixed': ''},
            {'name': '提示信息', 'hide': 'false', 'title': '提示信息', 'width': '280', 'fixed': ''},
            {'name': '备注', 'hide': 'false', 'title': '备注', 'width': '100', 'fixed': ''},
            {'name': '最后操作时间', 'hide': 'false', 'title': '最后操作时间', 'width': '120', 'fixed': ''},
            {'name': '最后操作人', 'hide': 'false', 'title': '最后操作人', 'width': '120', 'fixed': ''},
            {'name': '升级时间', 'hide': 'false', 'title': '升级时间', 'width': '120', 'fixed': ''},
            {'name': '生效时间', 'hide': 'true', 'title': '生效时间', 'width': '120', 'fixed': ''},
            {'name': '停用时间', 'hide': 'true', 'title': '停用时间', 'width': '120', 'fixed': ''},
        ]

    return show_col_list


def get_rule_object_list(audit_item_id, curr_manage_index):
    if curr_manage_index == '按抗菌药物分级管理':
        return [{'name': '抗菌药物分级', 'input_type': '日期时间区间', 'isNull': '1'}]
    elif curr_manage_index == '本院药品通用名':
        return [{'name': '本院药品通用名', 'input_type': '日期时间区间', 'isNull': '1'}]
    elif curr_manage_index == '本院药品通用名规格':
        return [{'name': '本院药品通用名规格', 'input_type': '日期时间区间', 'isNull': '1'}]
    elif curr_manage_index == '本院药品通用名规格厂家':
        return [{'name': '本院药品通用名规格厂家', 'input_type': '日期时间区间', 'isNull': '1'}]
    elif curr_manage_index == '本院药品编码':
        return [{'name': '本院药品编码', 'input_type': '日期时间区间', 'isNull': '1'}]


def get_rule_condition_list(audit_item_id, curr_manage_index):
    condition_list = []
    if audit_item_id == '抗菌药物分级管理':
        condition_list = [{'name': '开始生效时间', 'input_type': '日期时间区间', 'isNull': '1'},
                          {'name': '结束生效时间', 'input_type': '日期时间区间', 'isNull': '1'},
                          # {'name': '性别', 'input_type': '下拉列表框', 'isNull': '1'},
                          # {'name': '年龄', 'input_type': '', 'isNull': '1'},
                          # {'name': '特殊人群', 'input_type': '', 'isNull': '1'},
                          # {'name': '体重', 'input_type': '', 'isNull': '1'},
                          # {'name': '体表面积', 'input_type': '', 'isNull': '1'},
                          # {'name': '换行', 'input_type': '', 'isNull': '1'},
                          # {'name': '诊断', 'input_type': '', 'isNull': '1'},
                          # {'name': '指标', 'input_type': '', 'isNull': '1'},
                          {'name': '就诊类别', 'input_type': '', 'isNull': '1'},
                          {'name': '科室', 'input_type': '', 'isNull': '1'},
                          {'name': '病区', 'input_type': '', 'isNull': '1'},
                          ]
    elif audit_item_id == '药物送检提醒':
        condition_list = [
            # {'name': '生效时间', 'input_type': '日期时间区间', 'isNull': '1'},
            # {'name': '就诊类别', 'input_type': '', 'isNull': '1'},
            {'name': '科室', 'input_type': '', 'isNull': '1'},
            {'name': '病区', 'input_type': '', 'isNull': '1'}]
    elif audit_item_id == '用法用量推荐':
        condition_list = [
            # {'name': '生效时间', 'input_type': '日期时间区间', 'isNull': '1'},
            # {'name': '就诊类别', 'input_type': '', 'isNull': '1'},
            {'name': '科室', 'input_type': '', 'isNull': '1'},
            {'name': '病区', 'input_type': '', 'isNull': '1'},
            # {'name': '性别', 'input_type': '下拉列表框', 'isNull': '1'},
            {'name': '年龄', 'input_type': '', 'isNull': '1'},
            {'name': '特殊人群', 'input_type': '', 'isNull': '1'},
            {'name': '体重', 'input_type': '', 'isNull': '1'},
            {'name': '体表面积', 'input_type': '', 'isNull': '1'},
            # {'name': '换行', 'input_type': '', 'isNull': '1'},
            {'name': '诊断', 'input_type': '', 'isNull': '1'},
            {'name': '指标', 'input_type': '', 'isNull': '1'},
        ]

    return condition_list


def get_rule_judgment_element_list(audit_item_id, curr_manage_index):
    judgment_element_list = []
    if audit_item_id == '抗菌药物分级管理':
        judgment_element_list = [{'name': '医生职称', 'input_type': '', 'isNull': '1'},
                                 {'name': '医生', 'input_type': '', 'isNull': '1'},
                                 {'name': '会诊记录', 'input_type': '', 'isNull': '1'}
                                 ]
    elif audit_item_id == '药物送检提醒':
        judgment_element_list = [{'name': '病原学送检', 'input_type': '', 'isNull': '1'}]

    return judgment_element_list


def get_rule_result_list(audit_item_id, curr_manage_index):
    result_list = []
    if audit_item_id == '抗菌药物分级管理':
        result_list = [{'name': '规范结果', 'input_type': '', 'isNull': '1'},
                       {'name': '提示级别', 'input_type': '', 'isNull': '1'},
                       {'name': '提示原因', 'input_type': '', 'isNull': '1'},
                       {'name': '备注', 'input_type': '', 'isNull': '1'}]
    elif audit_item_id == '药物送检提醒':
        result_list = [{'name': '规范结果', 'input_type': '', 'isNull': '1'},
                       {'name': '提示级别', 'input_type': '', 'isNull': '1'},
                       {'name': '提示信息', 'input_type': '', 'isNull': '1'},
                       {'name': '备注', 'input_type': '', 'isNull': '1'}]
    elif audit_item_id == '用法用量推荐':
        result_list = [{'name': '提示信息', 'input_type': '', 'isNull': '1'},
                       {'name': '备注', 'input_type': '', 'isNull': '1'}]

    return result_list


def rules_add_not_only_object(request):
    """
    新增规则
    :param request:
    :return:
    """
    audit_item_id = None
    if 'auditItem' in request.GET:
        audit_item_id = request.GET['auditItem']

    curr_manage_index = None
    if 'curr_manage_index' in request.GET:
        curr_manage_index = request.GET['curr_manage_index']

    rule_object_list = get_rule_object_list(audit_item_id, curr_manage_index)
    rule_condition_list = get_rule_condition_list(audit_item_id, curr_manage_index)
    rule_judgment_element_list = get_rule_judgment_element_list(audit_item_id, curr_manage_index)
    rule_result_list = get_rule_result_list(audit_item_id, curr_manage_index)

    return render(request, 'views/rule/cus_rules/rules_add_not_only_object.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id,
                   "curr_manage_index": curr_manage_index,
                   'rule_object_list': rule_object_list,
                   'rule_condition_list': rule_condition_list,
                   'rule_judgment_element_list': rule_judgment_element_list,
                   'rule_result_list': rule_result_list})


def rules_detail_not_only_object(request):
    """
    查看规则
    :param request:
    :return:
    """
    audit_item_id = None
    if 'auditItem' in request.GET:
        audit_item_id = request.GET['auditItem']

    curr_manage_index = None
    if 'curr_manage_index' in request.GET:
        curr_manage_index = request.GET['curr_manage_index']

    rule_object_list = get_rule_object_list(audit_item_id, curr_manage_index)
    rule_condition_list = get_rule_condition_list(audit_item_id, curr_manage_index)
    rule_judgment_element_list = get_rule_judgment_element_list(audit_item_id, curr_manage_index)
    rule_result_list = get_rule_result_list(audit_item_id, curr_manage_index)

    return render(request, 'views/rule/cus_rules/rules_detail_not_only_object.html',
                  {"audit_item_id": audit_item_id, "audit_item_name": audit_item_id,
                   "curr_manage_index": curr_manage_index,
                   'rule_object_list': rule_object_list,
                   'rule_condition_list': rule_condition_list,
                   'rule_judgment_element_list': rule_judgment_element_list,
                   'rule_result_list': rule_result_list})


def dict_manage_dict(request):
    return render(request, 'views/rule/dict/manage_dict.html', {})


def cus_copy_index(request):
    """复制个性化规则：首页"""
    return render(request, 'views/rule/cus/copy/index.html', {})


def cus_copy_index2(request):
    """复制个性化规则：首页，版本2"""
    return render(request, 'views/rule/cus/copy/index2.html', {})


def cus_copy_copy_sys_rules(request):
    """复制规则操作页：复制系统规则"""
    return render(request, 'views/rule/cus/copy/copy_sys_rules.html', {})


def cus_copy_copy_cus_rules(request):
    """复制规则操作页：复制用户规则"""
    return render(request, 'views/rule/cus/copy/copy_cus_rules.html', {})


def cus_copy_copy_sys_cus_rules(request):
    """复制规则操作页：复制用户规则"""
    return render(request, 'views/rule/cus/copy/copy_sys_cus_rules.html', {})


def dict_drug_select(request):
    """选择药品：单选"""
    return render(request, 'views/rule/dict/drug_select.html', {})

