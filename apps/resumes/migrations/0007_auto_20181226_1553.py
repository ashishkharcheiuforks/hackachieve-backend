# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-26 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0006_resume_total_household_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='address',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='city',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='credit_score',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='zipcode',
        ),
    ]