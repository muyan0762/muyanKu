# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-04 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0018_auto_20190404_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='autoSendPrize',
            field=models.IntegerField(choices=[(0, '发'), (1, '不发')], default=1, verbose_name='自动发奖'),
        ),
        migrations.AlterField(
            model_name='task',
            name='hot',
            field=models.IntegerField(choices=[(0, '热门'), (1, '不热门')], default=1, verbose_name='热门'),
        ),
        migrations.AlterField(
            model_name='task',
            name='onOff',
            field=models.IntegerField(choices=[(0, '开'), (1, '关')], default=1, verbose_name='状态'),
        ),
    ]
