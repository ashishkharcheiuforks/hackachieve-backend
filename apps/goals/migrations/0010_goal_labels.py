# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-25 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('goals', '0009_auto_20190517_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='labels',
            field=models.ManyToManyField(default=None, to='labels.Label'),
        ),
    ]
