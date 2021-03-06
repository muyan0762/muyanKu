# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-05 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0022_auto_20190404_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Image2',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='Image3',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='Image4',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='collection',
            field=models.IntegerField(choices=[(0, '标准'), (1, '聚集')], default=0, verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='project',
            name='goUrlBean',
            field=models.CharField(max_length=700, null=True, verbose_name='goUrlBean'),
        ),
        migrations.AddField(
            model_name='project',
            name='hot',
            field=models.IntegerField(choices=[(0, '不热门'), (1, '热门')], default=0, verbose_name='热门'),
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
        migrations.AddField(
            model_name='project',
            name='imageUrl',
            field=models.CharField(max_length=700, null=True, verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.IntegerField(choices=[(0, '上线'), (1, '下线')], default=0, verbose_name='项目状态'),
        ),
    ]
