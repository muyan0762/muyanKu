# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-31 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_auto_20190331_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='tasks',
        ),
        migrations.AddField(
            model_name='urls',
            name='tasks',
            field=models.ManyToManyField(null=True, to='activity.Task'),
        ),
    ]
