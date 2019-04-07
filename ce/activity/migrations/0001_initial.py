# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-30 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('memo', models.CharField(default='0', max_length=400, verbose_name='约束描述')),
                ('cycle', models.IntegerField(default=0, verbose_name='周期约束')),
                ('rows', models.IntegerField(choices=[(0, '标准规则'), (1, '每日签到规则'), (2, '新人注册规则'), (3, '邀请有礼规则')], default=0, verbose_name='约束规则')),
            ],
            options={
                'db_table': 'constraint',
                'verbose_name_plural': '约束信息表',
                'verbose_name': '约束信息表',
            },
        ),
        migrations.CreateModel(
            name='PrizePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'prizepool',
                'verbose_name_plural': '奖品池信息表',
                'verbose_name': '奖品池信息表',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='项目名称')),
                ('memo', models.TextField(default='0', verbose_name='项目描述')),
                ('state', models.IntegerField(choices=[(0, '线上'), (1, '线下')], verbose_name='项目状态')),
                ('imgmsg', models.CharField(max_length=400, null=True, verbose_name='图片信息')),
                ('publishTime', models.BigIntegerField(verbose_name='上线时间')),
                ('downTime', models.BigIntegerField(verbose_name='下线时间')),
                ('buttonLabel1', models.CharField(default='0', max_length=300, verbose_name='项目详情文案')),
                ('displayOrder', models.IntegerField(default=0, verbose_name='展示顺序')),
            ],
            options={
                'db_table': 'project',
                'verbose_name_plural': '项目信息表',
                'verbose_name': '项目信息表',
            },
        ),
        migrations.CreateModel(
            name='Scenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'scenes',
                'verbose_name_plural': '场景信息表',
                'verbose_name': '场景信息表',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='任务名称')),
                ('sendPushMessage', models.IntegerField(choices=[(0, '不发送'), (1, '发送')], default=0, verbose_name='Push')),
                ('image1', models.CharField(max_length=500, null=True, verbose_name='图片1')),
                ('image2', models.CharField(max_length=500, null=True, verbose_name='图片2')),
                ('image3', models.CharField(max_length=500, null=True, verbose_name='图片3')),
                ('image4', models.CharField(max_length=500, null=True, verbose_name='图片4')),
                ('pushMessage', models.CharField(default='', max_length=400, verbose_name='Pushmessage')),
                ('displayOrder', models.IntegerField(default=0, verbose_name='顺序')),
                ('sendShortMessage', models.IntegerField(choices=[(0, '不发送'), (1, '发送')], default=0, verbose_name='发送短信')),
                ('sendSiteMessage', models.IntegerField(choices=[(0, '不发送'), (1, '发送')], default=0, verbose_name='发送站内信')),
                ('publishTime', models.BigIntegerField(default=0)),
                ('downTime', models.BigIntegerField(default=0)),
                ('shortMessage', models.CharField(max_length=100, verbose_name='短信内容')),
                ('memo', models.TextField(verbose_name='任务描述')),
                ('siteMessageTitle', models.CharField(max_length=80, verbose_name='站内信标题')),
                ('siteMessage', models.CharField(max_length=280, verbose_name='站内信内容')),
                ('buttonLabel1', models.CharField(max_length=40, verbose_name='按钮文案1')),
                ('buttonLabel2', models.CharField(max_length=40, verbose_name='按钮文案2')),
                ('onOff', models.BooleanField(default=1, verbose_name='任务状态')),
                ('iph', models.URLField(verbose_name='iph_url')),
                ('web', models.URLField(verbose_name='web_url')),
                ('atv', models.URLField(verbose_name='atv_url')),
                ('constraintId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Constraint')),
                ('prizePoolId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.PrizePool')),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Project')),
                ('sceneId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Scenes')),
            ],
            options={
                'db_table': 'task',
                'verbose_name_plural': '任务信息',
                'verbose_name': '任务信息',
            },
        ),
        migrations.CreateModel(
            name='URLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=57, verbose_name='name')),
                ('url', models.URLField(default='', verbose_name='url')),
                ('isActive', models.BooleanField(default=0)),
                ('tasks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Task')),
            ],
            options={
                'db_table': 'urls',
                'verbose_name_plural': 'URL信息',
                'verbose_name': 'URL信息',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70, verbose_name='姓名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
            ],
            options={
                'db_table': 'Userinfo',
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
        ),
    ]
