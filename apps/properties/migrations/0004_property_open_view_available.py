# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_remove_property_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='open_view_available',
            field=models.BooleanField(default=False),
        ),
    ]
