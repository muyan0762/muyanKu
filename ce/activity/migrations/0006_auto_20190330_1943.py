# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-30 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20190330_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='constraintId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Constraint'),
        ),
        migrations.AlterField(
            model_name='task',
            name='prizePoolId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.PrizePool'),
        ),
        migrations.AlterField(
            model_name='task',
            name='projectId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sceneId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Scenes'),
        ),
    ]
