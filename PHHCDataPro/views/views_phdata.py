from django.shortcuts import render


def cus_index(request):
    """普华数据自定义数据首页"""
    return render(request, 'views/phdata/cus/index.html', {})


def xy_disease(request):
    """普华数据自定义数据首页"""
    return render(request, 'views/phdata/cus/xy_disease.html', {})


def zy_disease(request):
    """普华数据自定义数据首页"""
    return render(request, 'views/phdata/cus/zy_disease.html', {})


def cus_diseasesource(request):
    """普华数据自定义原诊断"""
    return render(request, 'views/phdata/cus/diseasesource.html', {})


def cus_frequenry(request):
    """普华数据自定义给药频率"""
    return render(request, 'views/phdata/cus/frequenry.html', {})


def cus_drugspecpackage(request):
    """普华数据自定义规格包装"""
    return render(request, 'views/phdata/cus/drugspecpackage.html', {})

