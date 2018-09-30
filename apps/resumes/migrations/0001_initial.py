# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 04:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('zipcode', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('expected_tenancy_length', models.IntegerField(default=1)),
                ('total_household_members', models.IntegerField(default=1)),
                ('consent_criminal_check', models.BooleanField()),
                ('eviction_history', models.BooleanField()),
                ('current_property_has_bedbugs', models.BooleanField()),
                ('has_pet', models.BooleanField()),
                ('currently_working', models.BooleanField()),
                ('current_ocupation', models.CharField(max_length=255)),
                ('credit_score', models.IntegerField()),
                ('maximum_rental_budget', models.FloatField()),
                ('current_wage', models.FloatField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
