# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-04 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0021_auto_20190404_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='onOff',
            field=models.IntegerField(choices=[(0, '开'), (1, '关')], default=1, verbose_name='状态'),
        ),
    ]