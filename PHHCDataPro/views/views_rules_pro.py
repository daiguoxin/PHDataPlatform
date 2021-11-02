from django.shortcuts import render


def production_manage_index(request):
    """
    规则管理首页
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/manage/index.html', {})


def production_manage_prod_tasks(request):
    """
    规则管理首页
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/manage/prod_tasks.html', {})


def production_crowd_index(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/index.html', {})


def production_crowd_manual(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/manual.html', {})


def production_crowd_manualrules(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/manual_rules.html', {})


def production_crowd_genericname(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/genericname.html', {})


def production_crowd_generic(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/generic.html', {})


def production_crowd_basic(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/basic.html', {})


def production_crowd_product(request):
    """
    人群禁忌
    :param request:
    :return:
    """
    return render(request, 'views/rule/production/crowd/product.html', {})

