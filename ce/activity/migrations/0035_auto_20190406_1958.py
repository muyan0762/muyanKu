# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-06 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0034_auto_20190406_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponpool',
            name='prizeType',
            field=models.IntegerField(choices=[(5, '卡密优惠券'), (6, '易购优惠券'), (7, '二维码优惠券'), (11, '购物津贴')], default=11, verbose_name='奖品类型'),
        ),
    ]
