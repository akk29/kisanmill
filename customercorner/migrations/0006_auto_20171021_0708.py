# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0005_auto_20171021_0707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preproductinfo',
            old_name='Product',
            new_name='Select_Product',
        ),
    ]
