from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """首页"""
    return render(request, 'views/input/index.html', {})



