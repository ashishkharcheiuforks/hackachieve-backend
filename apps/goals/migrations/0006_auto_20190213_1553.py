# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-13 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_remove_goal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
