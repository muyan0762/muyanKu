# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-31 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_auto_20190331_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.URLField(default='', null=True, verbose_name='url'),
        ),
    ]