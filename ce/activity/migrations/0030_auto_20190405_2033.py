# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-05 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0029_auto_20190405_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenes',
            name='memo',
            field=models.CharField(max_length=200, null=True, verbose_name='场景描述'),
        ),
        migrations.AddField(
            model_name='scenes',
            name='secret',
            field=models.CharField(max_length=100, null=True, verbose_name='密钥'),
        ),
    ]
