from django.shortcuts import render


def login(request):
    """
        登录
    """
    return render(request, 'views/user/login.html', {})


def index(request):
    """
        首页
    """
    return render(request, 'views/index.html', {})


def hos_index(request):
    """
        首页
    """
    return render(request, 'views/hos_index.html', {})


def opt_index(request):
    """
        首页
    """
    return render(request, 'views/opt_index.html', {})


def core_index(request):
    """
        首页
    """
    return render(request, 'views/core_index.html', {})


def home_console(request):
    """
        工作台
    """
    return render(request, 'views/home/console.html', {})

