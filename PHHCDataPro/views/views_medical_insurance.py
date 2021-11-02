from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """首页"""
    return render(request, 'views/medical_insurance/index.html', {})


def expense_details(request):
    """首页"""
    return render(request, 'views/medical_insurance/expense_details.html', {})


def getStandardDict(request):
    """首页"""
    # return HttpResponse('{"status_code":1, "data":[{"id":"001", "name":"门诊挂号费"}, {"id":"002", "name":"住院挂号费"}]}')
    key = request.GET['term']
    return HttpResponse('[{"id":"001", "value":"门诊挂号费门诊挂号费门诊挂号费门诊挂号费门诊挂号费门诊挂号费门诊挂号费门诊挂号费门诊挂号费"}, {"id":"002", "value":"住院挂号费"}]')


