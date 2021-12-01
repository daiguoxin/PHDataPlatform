"""PHHCDataPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.url import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.url'))
"""
from django.contrib import admin
from django.urls import path, include

from PHHCDataPro.url import urls_rules, urls_phdata, urls_drug, urls_medical_insurance, urls_input, urls_opt
from PHHCDataPro.views import views, views_opt, views_basic, views_object, views_common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('', views.login),
    path('index/', views.index),
    path('hos_index/', views.hos_index),
    path('opt_index/', views.opt_index),
    path('core_index/', views.core_index),
    
    path('home/console/', views.home_console),

    path('basic/index/', views_basic.index),
    path('basic/data_input/', views_basic.data_input),

    path('object/drugproduct/', views_object.drugproduct),
    path('object/drugmanual/', views_object.drugmanual),

    path('object/uploaddrugmanual/', views_object.uploaddrugmanual),

    path('common/uploadfile/', views_common.uploadfile),
    path('common/logview/', views_common.logview),

    # 规则数据管理
    path('rule/', include(urls_rules.urlpatterns)),

    path('phdata/', include(urls_phdata.urlpatterns)),
    path('drug/', include(urls_drug.urlpatterns)),

    path('mi/', include(urls_medical_insurance.urlpatterns)),

    path('input/', include(urls_input.urlpatterns)),

    path('opt/', include(urls_opt.urlpatterns)),
]
