from django.shortcuts import render


def index(request):
    """
        首页
    """
    return render(request, 'views/opt/index.html', {})


def manage(request):
    """
        运营工作管理
    """
    return render(request, 'views/opt/manage.html', {})


def my_data_mapping(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_data_mapping.html', {})


def my_data_mapping_sys(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_data_mapping_sys.html', {})


def my_data_mapping_relation(request):
    """
        运营数据映射：关联
    """
    return render(request, 'views/opt/my_data_mapping_relation.html', {})


def my_data_mapping_relation_opt(request):
    """
        运营数据映射：关联
    """
    return render(request, 'views/opt/my_data_mapping_relation_opt.html', {})


def my_data_mapping_audit(request):
    """
        运营数据映射：审核
    """
    return render(request, 'views/opt/my_data_mapping_audit.html', {})


def my_data_mapping_disease(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_data_mapping_disease.html', {})


def my_data_mapping_dict(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_data_mapping_dict.html', {})


def my_phdata_drug(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_phdata_drug.html', {})


def my_phdata_disease(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_phdata_disease.html', {})


def my_phdata_rule(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my_phdata_rule.html', {})


def opt_log(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/opt_log.html', {})


def add_opt_log(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/add_opt_log.html', {})


def opt_sys_tasks(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/opt_sys_tasks.html', {})


def opt_my_statistics(request):
    """
        运营数据映射
    """
    return render(request, 'views/opt/my/statistics.html', {})


def customer(request):
    """
        客户表
    """
    return render(request, 'views/opt/customer.html', {})


def my_drug(request):
    """
        药品
    """
    return render(request, 'views/opt/my/drugbak.html', {})


def my_disease(request):
    """
        诊断
    """
    return render(request, 'views/opt/my/disease.html', {})


def my_otherdict(request):
    """
        其他字典
    """
    return render(request, 'views/opt/my/otherdict.html', {})


def my_index(request):
    """
        首页
    """
    return render(request, 'views/opt/my/index.html', {})


def my_set_check_result(request):
    """
        设置检查结果
    """
    return render(request, 'views/opt/my/set_check_result.html', {})


def my_add_opt_task(request):
    """
        添加运营任务
    """
    return render(request, 'views/opt/my/add_opt_task.html', {})


def my_check_detail(request):
    """
        添加运营任务
    """
    return render(request, 'views/opt/my/check_detail.html', {})


def my_opt_tasks(request):
    """
        我的运营任务
    """
    return render(request, 'views/opt/my/opt_tasks.html', {})


def my_opt_tasks_detail(request):
    """
        我的运营任务
    """
    return render(request, 'views/opt/my/opt_task_detail.html', {})


def prod_tasks(request):
    """
        我的生产任务
    """
    return render(request, 'views/opt/my/prod/prod_tasks.html', {})


def data_mapping_tasks(request):
    """
        我的数据映射任务
    """
    return render(request, 'views/opt/my/prod/data_mapping_tasks.html', {})


def dict_opt_taks(request):
    """
        运营任务弹出框
    """
    return render(request, 'views/opt/my/prod/dict_opt_taks.html', {})


def data_mapping_task_detail(request):
    """
        数据映射工作
    """
    return render(request, 'views/opt/my/prod/data_mapping_task_detail.html', {})


def data_mapping_task_detail2(request):
    """
        数据映射工作
    """
    return render(request, 'views/opt/my/prod/data_mapping_task_detail2.html', {})


def data_mapping_task_detail3(request):
    """
        数据映射工作
    """
    return render(request, 'views/opt/my/prod/data_mapping_task_detail3.html', {})


def dict_customer(request):
    """
        选择医院字典
    """
    return render(request, 'views/opt/my/prod/dict_customer.html', {})


def add_dm_task(request):
    """
        添加数据关联任务
    """
    return render(request, 'views/opt/my/prod/add_dm_task.html', {})


def prod_task_detail(request):
    """
        生产任务明细：药品
    """
    return render(request, 'views/opt/my/prod/prod_task_detail.html', {})


def prod_task_detail2(request):
    """
        生产任务明细：诊断
    """
    return render(request, 'views/opt/my/prod/prod_task_detail2.html', {})


def prod_task_detail3(request):
    """
        生产任务明细：规则
    """
    return render(request, 'views/opt/my/prod/prod_task_detail3.html', {})


def prod_task_detail4(request):
    """
        生产任务明细：按医院统计
    """
    return render(request, 'views/opt/my/prod/prod_task_detail4.html', {})


def dict_check_item(request):
    """
        生产任务明细：设置检查项目
    """
    return render(request, 'views/opt/my/prod/dict_check_item.html', {})









