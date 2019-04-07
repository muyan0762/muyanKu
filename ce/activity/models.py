from django.db import models

# Create your models here.

PhoneMsg=(
    (0,'不发送'),
    (1,'发送')
)
ACTk =(
    (0,'开'),
    (1,'关'),
)
PTYPE=(
    (5,'卡密优惠券'),
    (6,'易购优惠券'),
    (7,'二维码优惠券'),
    (11,'购物津贴'),
)
ACTf =(
    (0,'发'),
    (1,'不发'),
)
ACTr =(
    (0,'热门'),
    (1,'不热门'),
)
STAC=(
    (0,'上线'),
    (1,'下线')
)
TIME=(
    (0,'不限次数'),
    (1,'一次性'),
    (2,'每天')
)
ROWSS=(
    (0,'标准规则'),
    (1,'每日签到规则'),
    (2,'新人注册规则'),
    (3,'邀请有礼规则')
)
Hot=(
    (0,'不热门'),
    (1,'热门')
)
Coll=(
    (0,'标准'),
    (1,'聚集')
)

class Userinfo(models.Model):
    username = models.CharField('姓名',max_length=70,null=False)
    password=models.CharField('密码',max_length=200,null=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table='Userinfo'
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

class Scenes(models.Model):
    name=models.CharField(max_length=30)
    memo=models.CharField('场景描述',max_length=200,null=True)
    secret=models.CharField('密钥',max_length=100,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='scenes'
        verbose_name='场景信息表'
        verbose_name_plural=verbose_name

class Constraint(models.Model):
    name = models.CharField(max_length=30)
    memo=models.CharField('约束描述',max_length=400,default='0')
    # completionTimes=models.IntegerField('完成次数')
    cycle = models.IntegerField('周期约束',default=0)
    rows=models.IntegerField('约束规则',choices=ROWSS,default=0)
    def __str__(self):
        return self.name

    class Meta:
        db_table='constraint'
        verbose_name='约束信息表'
        verbose_name_plural=verbose_name

class Project(models.Model):
    name = models.CharField('项目名称',max_length=30,null=False)
    memo=models.TextField("项目描述",null=True)
    state=models.IntegerField('项目状态',choices=STAC,default=0)
    imgmsg=models.CharField('图片信息',max_length=400,null=True)
    publishTime=models.BigIntegerField('上线时间',null=True)
    downTime=models.BigIntegerField('下线时间',null=True)
    buttonLabel1=models.CharField("项目详情文案",max_length=300,null=True)
    displayOrder=models.IntegerField('展示顺序',default=0)
    hot = models.IntegerField('热门',choices=Hot,default=0)
    collection=models.IntegerField('类型',choices=Coll,default=0)
    imageUrlBean=models.CharField('图片地址',max_length=700,null=True)
    image1=models.ImageField(upload_to='static/img',null=True)
    image2=models.ImageField(upload_to='static/img',null=True)
    image3=models.ImageField(upload_to='static/img',null=True)
    image4=models.ImageField(upload_to='static/img',null=True)
    goUrlBean=models.CharField('goUrlBean',max_length=700,null=True)
    createTime = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table='project'
        verbose_name='项目信息表'
        verbose_name_plural=verbose_name

class PrizePool(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table='prizepool'
        verbose_name='奖品池信息表'
        verbose_name_plural=verbose_name

class Task(models.Model):
    name=models.CharField('任务名称',max_length=1000)
    sendPushMessage=models.IntegerField('Push',choices=PhoneMsg,default=0,null=True)
    image1=models.ImageField('图片1',upload_to='static/img',null=True)
    image2=models.ImageField('图片2',upload_to='static/img',null=True)
    image3=models.ImageField('图片3',upload_to='static/img',null=True)
    image4=models.ImageField('图片4',upload_to='static/img',null=True)
    pushMessage=models.CharField('Pushmessage',max_length=400,null=True)
    displayOrder=models.IntegerField('顺序',null=True)
    sendShortMessage=models.IntegerField('发送短信',choices=PhoneMsg, null=True)
    sendSiteMessage=models.IntegerField('发送站内信',choices=PhoneMsg,null=True)
    publishTime=models.BigIntegerField(default=0)
    downTime=models.BigIntegerField(default=0)
    shortMessage=models.CharField('短信内容',max_length=100,null=True)
    memo=models.TextField('任务描述',null=True)
    siteMessageTitle=models.CharField('站内信标题',max_length=80,null=True)
    siteMessage=models.CharField('站内信内容',max_length=280,null=True)
    buttonLabel1=models.CharField('按钮文案1',max_length=40,null=True)
    buttonLabel2 = models.CharField('按钮文案2', max_length=40,null=True)
    onOff=models.IntegerField('状态',choices=ACTk,default=1)
    hot=models.IntegerField('热门',choices=ACTr,default=1)
    autoSendPrize=models.IntegerField('自动发奖',choices=ACTf,default=1)
    imageUrl=models.CharField('图片地址',max_length=300,null=True)
    sceneId=models.ForeignKey(Scenes,null=True)#场景id
    constraintId=models.ForeignKey(Constraint,null=True)	#约束id
    projectId =models.ForeignKey(Project,null=True)	#项目id
    prizePoolId=models.ForeignKey(PrizePool,null=True)	#奖品池id
    goUrl=models.CharField('gourl',max_length=700,null=True)
    platformBean=models.CharField('platformBean',max_length=400,null=True)
    createTime=models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table='task'
        verbose_name='任务信息'
        verbose_name_plural=verbose_name

class Conpontype(models.Model):
    name=models.CharField('奖品类型',max_length=100,null=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table='conpontype'
        verbose_name='奖品类型'
        verbose_name_plural=verbose_name

class Couponpool(models.Model):
    name=models.CharField('券池名称',max_length=30,null=False)
    activityId=models.CharField('活动编码',max_length=50,null=True)
    activitySecretKey=models.CharField('活动密钥',max_length=100,null=True)
    memo=models.CharField('券池描述',max_length=200,null=True)
    prizeType=models.ForeignKey(Conpontype)
    # prizeType=models.IntegerField('奖品类型',choices=PTYPE,default=11)
    provider=models.CharField('优惠券提供方',max_length=100,null=True)
    quantity=models.IntegerField('库存',null=True)
    number=models.DecimalField('面额',max_digits=12,decimal_places=2,default=0.00)
    type=models.CharField('单位',max_length=20,null=True)
    startTime=models.BigIntegerField('开始时间',default=0)
    endTime=models.BigIntegerField('结束时间',default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table='conponpool'
        verbose_name='券池信息'
        verbose_name_plural=verbose_name

