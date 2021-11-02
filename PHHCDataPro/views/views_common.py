from django.shortcuts import render


def uploadfile(request):
    """
        上传文件
    """
    return render(request, 'views/common/uploadfile2.html', {})


def logview(request):
    """
        log可视化
    """
    return render(request, 'views/common/logview.html', {})
