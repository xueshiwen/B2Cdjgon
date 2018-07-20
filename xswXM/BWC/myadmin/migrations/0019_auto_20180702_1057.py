# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0018_auto_20180702_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalprice', models.FloatField()),
                ('totalnum', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('addtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('addressid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Address')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Users')),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Orders'),
        ),
    ]