from django.shortcuts import render


def drugproduct(request):
    """
        首页
    """
    return render(request, 'views/object/drugproduct.html', {})


def drugmanual(request):
    """
        药品与说明书关联
    """
    return render(request, 'views/object/drugmanual.html', {})


def uploaddrugmanual(request):
    """
        药品与说明书关联
    """
    return render(request, 'views/object/uploaddrugmanual.html', {})


def production_manage_index(request):
    """
        首页
    """
    return render(request, 'views/object/production/manage/index.html', {})


def production_manage_prod_tasks(request):
    """
        首页
    """
    return render(request, 'views/object/production/manage/prod_tasks.html', {})


def drug(request):
    """
        首页
    """
    return render(request, 'views/object/production/drug.html', {})


def drugdetail(request):
    """
        首页
    """
    return render(request, 'views/object/production/drugdetail.html', {})


def manual(request):
    """
        首页
    """
    return render(request, 'views/object/production/manual.html', {})


def generic(request):
    """
        首页
    """
    return render(request, 'views/object/production/generic.html', {})


def basic(request):
    """
        首页
    """
    return render(request, 'views/object/production/basic.html', {})


def product(request):
    """
        首页
    """
    return render(request, 'views/object/production/product.html', {})




