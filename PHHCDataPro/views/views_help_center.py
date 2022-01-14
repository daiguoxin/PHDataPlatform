from django.shortcuts import render


def page(request):
    """
        页面详细说明
    """
    return render(request, 'views/help_center/page.html', {})
