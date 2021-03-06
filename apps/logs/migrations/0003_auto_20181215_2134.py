# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-16 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_log_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='emitter',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='target',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='value',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
