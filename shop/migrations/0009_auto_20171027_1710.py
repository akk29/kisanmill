# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_services_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Company_Name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='services',
            name='Service_name',
            field=models.CharField(max_length=200),
        ),
    ]
