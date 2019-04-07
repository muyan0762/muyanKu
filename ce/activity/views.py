import datetime
import random
import time

from PIL import Image
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.core import serializers

from django.forms import model_to_dict
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from ce import settings
import json
from .models import *
import os
import base64
from django.middleware.csrf import get_token, _sanitize_token, _compare_salted_tokens, REASON_BAD_TOKEN
from django.views.decorators.csrf import csrf_exempt

def token(request):
    request_csrf_token = ""
    if request.method == "POST":
        try:
            request_csrf_token = request.POST.get('csrfmiddlewaretoken', '')
        except IOError:
            return HttpResponse('e')

    if request_csrf_token == "":
        request_csrf_token = request.META.get(settings.CSRF_HEADER_NAME, '')

    request_csrf_token = _sanitize_token(request_csrf_token)
    if not _compare_salted_tokens(request_csrf_token, csrf_token):
        return HttpResponse(request, REASON_BAD_TOKEN)

#处理存图片
def upload_img(imglist):
    namelist=[]
    for image in imglist:
        if image:
            data = image.split(',')
            lastn= data[:1][0]
            data=data[1:]
            img = base64.b64decode(data[0])
            #文件名根据时间＋随机６位数拼成名称字符串
            filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            for x in range(6):
                filename+=str(random.randint(0,10))

            basedir = 'static/img'
            #后缀
            lastn=lastn.split(';')[0][11:]
            filename=filename+'.'+lastn
            # 拼完整的保存路径
            upload_path = os.path.join(basedir, filename)
            with open(upload_path, 'wb') as f:
                f.write(img)
        else:
            filename=''
        namelist.append(filename)
    return namelist

#文件下载
def file_down(filename):
    file = open(filename, 'rb')
    #以下三种方法
    # response = StreamingHttpResponse(file)
    # response = FileResponse(file) #推荐这个,使用了缓存,更加节约资源
    response= HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="a.docx"'
    return response

@ensure_csrf_cookie
def login_(request):
    if request.method == 'POST':
        print(request.body)
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

# @csrf_exempt
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

#插入数据库场景数据
def scenes(request):
    scenes1=Scenes()
    scenes1.name=('场景1')
    scenes1.save()
    scenes2=Scenes()
    scenes2.name=('场景2')
    scenes2.save()
    scenes1 = Project()
    scenes1.name = ('项目1')
    scenes1.save()
    scenes2 = Project()
    scenes2.name = ('项目2')
    scenes2.save()
    scenes1 = PrizePool()
    scenes1.name = ('奖品1')
    scenes1.save()
    scenes2 = PrizePool()
    scenes2.name = ('奖品2')
    scenes2.save()
    scenes1 = Constraint()
    scenes1.name = ('约束1')
    scenes1.save()
    scenes2 = Constraint()
    scenes2.name = ('约束2')
    scenes2.save()
    return HttpResponse('save OK')
#场景接口
def scenes_query(request):
    obj = Scenes.objects.filter().all()
    L=[]
    for scenes in obj:
        L.append({'id':scenes.id,'name':scenes.name})
    # print(L)
    obj = {'code': 0, 'msg': '操作成功','data':L}
    return HttpResponse(json.dumps(obj,ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#项目接口
def project_query(request):
    obj = Project.objects.filter().all()
    L = []
    for scenes in obj:
        L.append({'id': scenes.id, 'name': scenes.name})
    # print(L)
    obj = {'code': 0, 'msg': '操作成功', 'data': L}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#约束接口
def cons_query(request):
    obj = Constraint.objects.filter().all()
    L = []
    for scenes in obj:
        L.append({'id': scenes.id, 'name': scenes.name})
    # print(L)
    obj = {'code': 0, 'msg': '操作成功', 'data': L}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#奖品接口
def prize_query(request):
    obj = PrizePool.objects.filter().all()
    L = []
    for scenes in obj:
        L.append({'id': scenes.id, 'name': scenes.name})
    # print(L)
    obj = {'code': 0, 'msg': '操作成功', 'data': L}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
# 券池类型接口
def poltype_query(request):
    obj = Conpontype.objects.filter().all()
    L=[]
    for type in obj:
        L.append({'id':type.id,'name':type.name})
    obj={'code':0,'msg':'操作成功','data':L}
    return HttpResponse(json.dumps(obj,ensure_ascii=False),content_type='application/json;charset=utf-8')
# def poltype_query(request):
#     obj = Conpontype.objects.filter().all()
#     L=[]
#     for type in obj:
#         L.append({'id':type.id,'name':type.name})
#     obj={'code':0,'msg':'操作成功','data':L}
#     return HttpResponse(json.dumps(obj,ensure_ascii=False),content_type='application/json;charset=utf-8')


#创建新任务

#创建新任务
def new_task(request):
    if request.method =='POST':
        req = json.loads(request.body.decode())

        L=['name','sendPushMessage',
            'pushMessage','displayOrder','sendShortMessage','sendSiteMessage','publishTime',
            'downTime','shortMessage','memo','siteMessageTitle','siteMessage',
            'buttonLabel1','buttonLabel2','onOff','hot','autoSendPrize']#'platformBean','goUrl'
        d={}
        for x in L:
            d[x]= req[x]

        task_n=req.get('id')
        print(task_n)

        #判断是新建任务还是修改
        if not task_n:
            # print('9999')
            newuser=Task(**d)
            # newuser = Task.objects.get(id=task_n)
            newuser.sceneId = Scenes.objects.get(id=req['sceneId'])
            newuser.constraintId = Constraint.objects.get(id=req['constraintId'])
            newuser.projectId = Project.objects.get(id=req['projectId'])
            newuser.prizePoolId = PrizePool.objects.get(id=req['prizePoolId'])
            newuser.createTime = int(time.time() * 1000)

            # 单独处理ｕｒｌ方面
            goUrl = req.get('goUrl')
            print(goUrl)
            print('-----*****')
            newuser.goUrl = json.dumps(goUrl)
            platformBean = req.get('platformBean')
            newuser.platformBean = json.dumps(platformBean)
            # 处理图片
            image1 = req.get('image1')
            image2 = req.get('image2')
            image3 = req.get('image3')
            image4 = req.get('image4')
            imgname = upload_img([image1, image2, image3, image4])
            # imageUrl处理
            newuser.imageUrl = json.dumps(imgname)
            newuser.image1 = imgname[0]
            newuser.image2 = imgname[1]
            newuser.image3 = imgname[2]
            newuser.image4 = imgname[3]
            # newuser.save()
        else:
            Task.objects.filter(id=task_n).update(**d)
            newuser = Task.objects.get(id=task_n)
            newuser.sceneId=Scenes.objects.get(id=req['sceneId'])
            newuser.constraintId = Constraint.objects.get(id=req['constraintId'])
            newuser.projectId = Project.objects.get(id=req['projectId'])
            newuser.prizePoolId = PrizePool.objects.get(id=req['prizePoolId'])
            newuser.createTime=int(time.time()*1000)

            #单独处理ｕｒｌ方面
            goUrl=req.get('goUrl')
            print(goUrl)
            newuser.goUrl=json.dumps(goUrl)
            platformBean = req.get('platformBean')
            newuser.platformBean = json.dumps(platformBean)
            #处理图片
            image1=req.get('image1')
            image2 = req.get('image2')
            image3= req.get('image3')
            image4 = req.get('image4')
            imgname=upload_img([image1,image2,image3,image4])
            #imageUrl处理
            newuser.imageUrl=json.dumps(imgname)
            newuser.image1=imgname[0]
            newuser.image2=imgname[1]
            newuser.image3=imgname[2]
            newuser.image4=imgname[3]
        newuser.save()
    obj = {'code': 0, 'message': '操作成功'}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#任务列表页
def task_query(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        print(req)
        print('**********')
        filter_d,limte_d={},{}
        #挑选出分页和筛选条件
        for key,value in req.items():
            if value!=None and value!='' and key!= 'sortOrder' and key != 'sortName':
                if key!= 'page' and key != 'pageSize':
                    filter_d[key]=value
                else:
                    limte_d[key]=value

        #分页条件的处理
        sta_page=(limte_d['page']-1)*limte_d['pageSize']
        stop_page=sta_page+limte_d['pageSize']
        print(sta_page,stop_page)

        #筛选条件的处理
        if filter_d:
            res = Task.objects.filter(**filter_d)
        else:
            res = Task.objects.all()
        #查询出的数据
        total=len(res)
        if len(res)>limte_d['pageSize']:
            res=res[sta_page:stop_page]

        L = []
        for o in res:
            o.goUrl=json.loads(o.goUrl)
            o.platformBean = json.loads(o.platformBean)
            print(type(o.projectId))
            u=o.projectId.name
            print(u,type(u))
            #imageUrl
            imgUrl=json.loads(o.imageUrl)
            o.imageUrl=dict([['web',imgUrl[0]],['wap',imgUrl[1]],['atv',imgUrl[2]],['ipd',imgUrl[3]]])

            dic = {}
            dic.update(o.__dict__)
            dic.pop("_state", None)  # 去除掉多余的字段_state
            dic.pop('_projectId_cache' ,None)
            dic['projectName'] = u
            L.append(dic)
        obj = {'code': 0, 'msg': '操作成功', 'data':{'rows':L,'total':total}}
        return HttpResponse(json.dumps(obj, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")
#修改onOff
def task_switch(request):
    req=json.loads(request.body.decode())
    onOff=req.get('onOff','')
    id = req.get('id','')
    if onOff==0 or onOff==1:
        print(onOff)
        print('----------')
        Task.objects.filter(id=id).update(onOff=onOff)
    obj = {'code': 0, 'message': '操作成功'}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#任务详情页
def task_detail(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        id = req.get('id','')
        user=Task.objects.get(id=id)
        user.goUrl = json.loads(user.goUrl)
        user.platformBean = json.loads(user.platformBean)

        imgUrl = json.loads(user.imageUrl)
        path='http://192.168.0.105:8000/static/img/'
        keys=['web','wap','atv', 'ipd']
        d={}
        for key,image in zip(keys,imgUrl):
            if image:
                imagepath=path+image
                print(path)
            else:
                imagepath=''
            d[key]=imagepath

        user.imageUrl = d

        n_user=model_to_dict(user)
        del(n_user['image3'])
        del(n_user['image1'])
        del(n_user['image2'])
        del(n_user['image4'])
        print(n_user)
        print('-'*10)
        obj = {'code': 0, 'msg': '操作成功', 'data': n_user}
        return HttpResponse(json.dumps(obj, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")


#创建新项目
def new_project(request):
    req=json.loads(request.body.decode())
    #去除无用字段
    delL=['_index','serialNum','_rowKey','downTimeFormat','publishTimeFormat','hotFormat','stateFormat','collectionFormat','createTimeFormat']
    for del_d in delL:
        if del_d in req:
            del(req[del_d])
    #校验信息
    if req['name']=='' or req['name']==None:
        obj ={'code':1,'message':'项目名称必填'}
    elif len(req['name'])>7:
        obj = {'code': 1, 'message': '项目名称长度超出'}
    elif req['memo'] and len(req['memo'])>12:
        obj={'code':1,'message':'项目描述长度超出'}
    elif req['buttonLabel1'] and len(req['buttonLabel1'])>9:
        obj={'code':1,'message':'项目详情文案长度超出'}
    elif req['state'] ==None:
        obj={'code':1,'message':'项目状态必填'}
    elif req['hot']== None:
        obj={'code':1,'message':'热门标签必填'}
    elif req['collection']==None:
        obj = {'code': 1, 'message': '项目类型必填'}
    elif req['displayOrder']==None:
        obj = {'code': 1, 'message': '展示顺序必填'}
    else:
        # 单独处理ｕｒｌ方面
        goUrl = req.get('goUrlBean')
        req['goUrlBean'] = json.dumps(goUrl)
        # 处理图片
        image1 = req.get('image1')
        image2 = req.get('image2')
        image3 = req.get('image3')
        image4 = req.get('image4')
        http='http://192.168.0.105:8000/static/img/'
        imgname = upload_img([image1, image2, image3, image4])
        for imgs in imgname:
            if imgs:
                imgdata=Image.open('/home/tarena/桌面/ce/static/img/'+imgs)
                print(imgdata.size, imgdata.format)
                print('--------------')
                if imgdata.size[0] != imgdata.size[1]:
                    obj = {'code': 1, 'message': imgs+'尺寸不是方形'}
                    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                                        content_type="application/json;charset=utf-8")

                elif imgdata.format != 'JPG' and imgdata.format != 'JPEG' and imgdata.format != 'PNG' and imgdata.format != 'GIF':
                    obj = {'code': 1, 'message': imgs + '格式不对'}
                    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                                    content_type="application/json;charset=utf-8")

        # imageUrl处理
        req['image1'] = imgname[0]
        req['image2'] = imgname[1]
        req['image3'] = imgname[2]
        req['image4'] = imgname[3]
        for i in range(len(imgname)):
            imgname[i]=http+imgname[i]
        req['imageUrlBean'] = json.dumps(imgname)
        #创建时间
        req['createTime']=int(time.time()*1000)
        if 'id' in req:
            newuser = Project.objects.filter(id=req.get('id')).update(**req)
        else:
            newuser = Project(**req)
            newuser.save()
        obj = {'code': 0, 'message': '操作成功'}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#查询所有项目
def project_all(request):
    req = json.loads(request.body.decode())
    filter_d, limte_d = {}, {}
    # 挑选出分页和筛选条件
    for key, value in req.items():
        if value != None and value != '' and key != 'sortOrder' and key != 'sortName':
            if key != 'page' and key != 'pageSize':
                filter_d[key] = value
            else:
                limte_d[key] = value

    if filter_d:
        res = Project.objects.filter(**filter_d)
    else:
        res = Project.objects.all()

    L = []
    for o in res:
        o.goUrlBean = json.loads(o.goUrlBean)

        imgUrl = json.loads(o.imageUrlBean)
        o.imageUrlBean = dict([['web', imgUrl[0]], ['wap', imgUrl[1]], ['atv', imgUrl[2]], ['ipd', imgUrl[3]]])

        dic = {}
        dic.update(o.__dict__)
        dic.pop("_state", None)  # 去除掉多余的字段_state
        # dic.pop('_projectId_cache', None)
        L.append(dic)

    obj = {'code': 0, 'msg': '操作成功', 'data': {'rows': L, 'total': 2}}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")
#修改上下线
def project_state(request):
    req=json.loads(request.body.decode())
    id = req.get('id')
    state=req.get('state')
    Project.objects.filter(id=id).update(state=state)
    obj = {'code': 0, 'message': '操作成功'}
    return HttpResponse(json.dumps(obj, ensure_ascii=False),
                        content_type="application/json;charset=utf-8")

#场景列表
def scenes_all(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        filter_d, limte_d = {}, {}
        # 挑选出分页和筛选条件
        for key, value in req.items():
            if value != None and value != '' and key != 'sortOrder' and key != 'sortName':
                if key != 'page' and key != 'pageSize':
                    filter_d[key] = value
                else:
                    limte_d[key] = value

                    # 分页条件的处理
                    # tiao=limte_d['page']-1
                    # 分页条件的处理
        sta_page = (limte_d['page'] - 1) * limte_d['pageSize']
        stop_page = sta_page + limte_d['pageSize']
        print(sta_page, stop_page)

        # 筛选条件的处理
        if filter_d:
            res = Scenes.objects.filter(**filter_d)
        else:
            res = Scenes.objects.all()
            # 查询出的数据
        total = len(res)
        if len(res) > limte_d['pageSize']:
                res = res[sta_page:stop_page]

        L = []
        for o in res:
            dic = {}
            dic.update(o.__dict__)
            dic.pop("_state", None)  # 去除掉多余的字段_state
            L.append(dic)
        obj = {'code': 0, 'msg': '操作成功', 'data': {'rows': L, 'total': total}}
        return HttpResponse(json.dumps(obj, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")
#场景修改
def scenes_detail(request):
    req=json.loads(request.body.decode())
    id = req.get('id')
    secret=req.get('secret')
    if not secret:
        obj = {'code': 1, 'message': '密钥不能为空'}
    elif '*' in secret:
        obj = {'code': 1, 'message': '密钥不能有＊'}
    elif len(secret) != 8:
        obj = {'code': 1, 'message': '密钥长度必须８位'}
    else:
        Scenes.objects.filter(id=id).update(secret=secret)
        obj={'code':0,'message':'修改成功'}
    return HttpResponse(json.dumps(obj,ensure_ascii=False),
                        content_type='application.json;charset=utf-8')

#券池下载模板
def pool_download(request):
    if request.method == 'GET':
        file=request.GET.get('fileType')
        if file =='1' or file =='2':

            filename='static/download/a.docx'
            data = file_down(filename)
        return data
            # 场景修改

#新建券池信息
def new_couponpool(request):
    req=json.loads(request.body.decode())
    print(req)
    #校验
    activitySecretKey=req.get('activitySecretKey','')
    activityId=req.get('activityId','')
    if req['name'] == '':
        date={'code':1,'message':'券池名称必填'}
    elif len(req['name'])>12:
        date={'code':1,'message':'券池名称长度超出'}
    elif len(req['memo'])>128:
        date={'code':1,'message':'券池描述长度超出'}
    elif len(req['provider'])>50:
        date={'code':1,'message':'券池描述长度超出'}
    elif req['endTime'] == None or req['startTime'] == None and req['prizeType'] != 11:
        date={'code':1,'message':'有效期不能空'}
    elif req['endTime']-req['startTime']< 30*1000 and req['prizeType'] != 11:
        date={'code':1,'message':'结束和开始时间间隔不得小于30'}

    elif req['prizeType'] == 6 and req['activityId'] == '':
            date={'code':1,'message':'活动编码必填'}
    elif req['prizeType'] == 6 and req['activitySecretKey']=='':
            date={'code':1,'message':'活动密钥必填'}
    else:
        req['prizeType'] = Conpontype.objects.get(id=req['prizeType'])
        if req['quantity']:
            req['quantity'] = int(req['quantity'])
        else:
            req['quantity'] = 0
        if req['number'] == '':
            req['number']=0

        new_pool=Couponpool(**req)
        new_pool.save()
        date = {'code': 0, 'message': '创建成功'}
    return HttpResponse(json.dumps(date, ensure_ascii=False),
                        content_type='application.json;charset=utf-8')

#券池列表
def couponpool_all(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        filter_d, limte_d = {}, {}
        # 挑选出分页和筛选条件
        for key, value in req.items():
            if value != None and value != '' and key != 'sortOrder' and key != 'sortName':
                if key != 'page' and key != 'pageSize':
                    filter_d[key] = value
                else:
                    limte_d[key] = value

                    # 分页条件的处理
                    # tiao=limte_d['page']-1
                    # 分页条件的处理
        sta_page = (limte_d['page'] - 1) * limte_d['pageSize']
        stop_page = sta_page + limte_d['pageSize']
        print(sta_page, stop_page)

        # 筛选条件的处理
        if filter_d:
            res = Couponpool.objects.filter(**filter_d)
        else:
            res = Couponpool.objects.all()
            # 查询出的数据
        total = len(res)
        if len(res) > limte_d['pageSize']:
            res = res[sta_page:stop_page]

        L = []
        for o in res:
            # print(o)

            dic = {}
            dic.update(o.__dict__)
            dic['number']=float(dic['number'])

            dic['prizeType']=o.prizeType_id
            # print(type(o.prizeType_id),o.prizeType.name)
            dic.pop("_state", None)  # 去除掉多余的字段_state
            # print(dic)
            # print('-----')
            L.append(dic)

        obj = {'code': 0, 'msg': '操作成功', 'data': {'rows': L, 'total': total}}
        return HttpResponse(json.dumps(obj, ensure_ascii=False),
                            content_type="application/json;charset=utf-8")
