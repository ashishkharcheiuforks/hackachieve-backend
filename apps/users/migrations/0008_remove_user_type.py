# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 01:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181031_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
    ]