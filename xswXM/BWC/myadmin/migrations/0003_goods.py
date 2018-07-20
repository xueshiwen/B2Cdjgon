# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descr', models.CharField(max_length=255, null=True)),
                ('info', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pics', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('store', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('clicknum', models.IntegerField(default=0)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Types')),
            ],
        ),
    ]
