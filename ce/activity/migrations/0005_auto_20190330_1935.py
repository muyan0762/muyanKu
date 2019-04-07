# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-30 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20190330_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='atv',
            field=models.URLField(null=True, verbose_name='atv_url'),
        ),
        migrations.AlterField(
            model_name='task',
            name='buttonLabel1',
            field=models.CharField(max_length=40, null=True, verbose_name='按钮文案1'),
        ),
        migrations.AlterField(
            model_name='task',
            name='buttonLabel2',
            field=models.CharField(max_length=40, null=True, verbose_name='按钮文案2'),
        ),
        migrations.AlterField(
            model_name='task',
            name='displayOrder',
            field=models.IntegerField(null=True, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='task',
            name='iph',
            field=models.URLField(null=True, verbose_name='iph_url'),
        ),
        migrations.AlterField(
            model_name='task',
            name='memo',
            field=models.TextField(null=True, verbose_name='任务描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='onOff',
            field=models.BooleanField(choices=[(0, '开'), (1, '关')], default=1, verbose_name='任务状态'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pushMessage',
            field=models.CharField(max_length=400, null=True, verbose_name='Pushmessage'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sendPushMessage',
            field=models.IntegerField(choices=[(0, '不发送'), (1, '发送')], default=0, null=True, verbose_name='Push'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sendShortMessage',
            field=models.IntegerField(choices=[(0, '不发送'), (1, '发送')], null=True, verbose_name='发送短信'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sendSiteMessage',
            field=models.IntegerField(choices=[(0, '不发送'), (1, '发送')], null=True, verbose_name='发送站内信'),
        ),
        migrations.AlterField(
            model_name='task',
            name='shortMessage',
            field=models.CharField(max_length=100, null=True, verbose_name='短信内容'),
        ),
        migrations.AlterField(
            model_name='task',
            name='siteMessage',
            field=models.CharField(max_length=280, null=True, verbose_name='站内信内容'),
        ),
        migrations.AlterField(
            model_name='task',
            name='siteMessageTitle',
            field=models.CharField(max_length=80, null=True, verbose_name='站内信标题'),
        ),
        migrations.AlterField(
            model_name='task',
            name='web',
            field=models.URLField(null=True, verbose_name='web_url'),
        ),
    ]