# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-20 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20180716_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_name', models.TextField(verbose_name='\u73af\u5883\u540d\u79f0')),
                ('base_url', models.CharField(max_length=50, verbose_name='\u5730\u5740')),
                ('env_key', models.TextField(max_length=50, verbose_name='\u73af\u5883key')),
                ('simple_desc', models.CharField(max_length=100, verbose_name='\u7b80\u8981\u8bf4\u660e')),
                ('create_time', models.CharField(max_length=50)),
                ('update_time', models.CharField(max_length=50)),
            ],
        ),
    ]
