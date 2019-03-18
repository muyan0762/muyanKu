from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login_(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        name = req.get('username','')
        password = req.get('password','')
        try:
            olduser = Userinfo.objects.get(username=name)
        except:
            obj = {'code': 1, 'msg': '用户名不存在'}
            return HttpResponse(json.dumps(obj, ensure_ascii=False),
                                content_type="application/json;charset=utf-8")
        if name and password:
            user = check_password(password, olduser.password)
            if user:
                obj = {'code': 0, 'msg': '登录成功'}
            else:
                obj = {'code': 1, 'msg': '用户名密码不正确'}
        else:
            obj = {'code': 1, 'msg': '用户名密码不能为空'}
        return HttpResponse(json.dumps(obj, ensure_ascii=False),
                                    content_type="application/json;charset=utf-8")

@csrf_exempt
def register_(request):
    if request.method == 'POST':
        obj={'code':0,'msg':'注册成功'}
        req = json.loads(request.body.decode())
        name = req.get('username','')
        password = req.get('password','')
        cpassword=req.get('cpassword','')
        oldname = Userinfo.objects.filter(username=name)
        if oldname:
            obj['code']=1
            obj['msg']='用户名存在'
        elif len(name)<=0:
            obj['code']=1
            obj['msg'] = '用户名不能为空'
        elif password != cpassword:
            obj['code']=1
            obj['msg'] = '密码不一致'
        elif len(password)<=0:
            obj['code'] = 1
            obj['msg'] = '密码不能为空'
        else:
            user = Userinfo()
            user.username = name
            user.password = make_password(password, None, 'pbkdf2_sha1')
            user.save()
        return HttpResponse(json.dumps(obj,ensure_ascii=False),
                            content_type="application/json;charset=utf-8")
