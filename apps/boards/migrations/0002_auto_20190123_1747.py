# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-24 01:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boards',
            new_name='Board',
        ),
    ]
