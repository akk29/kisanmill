# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customercorner', '0009_auto_20171021_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrionalcontent',
            name='NutrionalData',
        ),
        migrations.AddField(
            model_name='nutrionalcontent',
            name='Fat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_type',
            field=models.CharField(choices=[(b'dairy', b'Dairy Product'), (b'fruits', b'Fruits'), (b'vegetables', b'Vegetables')], max_length=15),
        ),
    ]
