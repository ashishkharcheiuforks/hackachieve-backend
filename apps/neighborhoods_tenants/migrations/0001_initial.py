# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighborhoods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood_tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.ManyToManyField(to='neighborhoods.Neighborhood')),
                ('tenant', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
