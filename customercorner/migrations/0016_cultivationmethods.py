# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0015_auto_20171024_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultivationMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=1500)),
                ('Investment_cost', models.IntegerField()),
                ('Season', models.CharField(choices=[(b'Summer', b'Summer'), (b'Winter', b'Winter')], default=None, max_length=10)),
                ('Soil_type', models.CharField(choices=[(b'alluvial', b'Alluvial'), (b'loamy', b'Loamy')], default=None, max_length=10)),
                ('Select_Product', models.ManyToManyField(to='customercorner.Product')),
            ],
        ),
    ]
