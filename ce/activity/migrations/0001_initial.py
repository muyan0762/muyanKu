# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-15 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70, verbose_name='姓名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'Userinfo',
            },
        ),
    ]
