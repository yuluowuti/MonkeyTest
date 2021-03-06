# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-16 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_projectinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50, verbose_name='\u7528\u4f8b\u540d\u79f0')),
                ('belong_project', models.CharField(max_length=50, verbose_name='\u6240\u5c5e\u9879\u76ee')),
                ('request', models.TextField(verbose_name='\u8bf7\u6c42\u4fe1\u606f')),
                ('author', models.CharField(max_length=50, verbose_name='\u7f16\u5199\u4eba\u5458')),
                ('remark', models.CharField(max_length=100, verbose_name='\u5176\u4ed6\u4fe1\u606f')),
                ('response', models.TextField(max_length=50, verbose_name='\u8fd4\u56de\u4fe1\u606f')),
                ('create_time', models.CharField(max_length=50)),
                ('update_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='projectinfo',
            name='create_time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
