# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0008_auto_20181226_1610'),
        ('user_property_filter', '0002_auto_20181228_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_property_filter',
            name='user',
        ),
        migrations.AddField(
            model_name='user_property_filter',
            name='resume',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='resumes.Resume'),
        ),
    ]
