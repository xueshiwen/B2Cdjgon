# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_auto_20180701_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
