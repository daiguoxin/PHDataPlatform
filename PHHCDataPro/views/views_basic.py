from django.shortcuts import render


def index(request):
    """
        首页
    """
    return render(request, 'views/basic/index.html', {})


def customer(request):
    """
        首页
    """
    return render(request, 'views/opt/customer.html', {})


def data_input(request):
    return render(request, 'views/basic/data_input.html', {})

