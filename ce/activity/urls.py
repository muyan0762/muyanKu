"""ce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    #登录注册
    url(r'^login/$', views.login_),
    url(r'^register/$',views.register_),
    #查询
    url(r'^scenes/$',views.scenes),
    url(r'^scenes/query/$',views.scenes_query),
    url(r'^project/query/$',views.project_query),
    url(r'^prize/query/$',views.prize_query),
    url(r'^cons/query/$',views.cons_query),
    url(r'^pooltype/query/$',views.poltype_query),
]
#任务url
urlpatterns += [
    url(r'^new_task/$',views.new_task), #新建/修改任务
    url(r'^task/query/$',views.task_query),#任务查询
    url(r'^task/detail/$',views.task_detail),#任务详情
    url(r'^task/switch/$',views.task_switch),#修改onOff
]
#项目url
urlpatterns += [
    url(r'^new_project/$',views.new_project),#新建/修改项目
    url(r'^project/all/$',views.project_all),#查询所有路径
    url(r'^project/state/$',views.project_state),#修改上下线
]
#场景url
urlpatterns += [
    url(r'^scense/all/$',views.scenes_all),#场景列表
    url(r'^scense/detail/$',views.scenes_detail),#修改场景
]
#券池url
urlpatterns += [
    url(r'^pool/download/$',views.pool_download),#下载模板
    url(r'^new_coupon/pool/$',views.new_couponpool),#新建券池
    url(r'^coupon/pool/all/$',views.couponpool_all),#券池列表
]