# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-30 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='publishTime',
            field=models.BigIntegerField(default=0, verbose_name='上线时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.IntegerField(choices=[(0, '线上'), (1, '线下')], default=0, verbose_name='项目状态'),
        ),
    ]
