# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('columns', '0003_column_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='order_position',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]