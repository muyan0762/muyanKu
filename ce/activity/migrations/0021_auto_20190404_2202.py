# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-04 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_task_createtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='onOff',
            field=models.IntegerField(choices=[(0, '关'), (1, '开')], default=1, verbose_name='状态'),
        ),
    ]