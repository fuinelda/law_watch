# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 08:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_watch', '0003_auto_20160802_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillInfoList',
            fields=[
                ('bill_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('bill_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'managed': False,
                'db_table': 'bill_info_list',
            },
        ),
    ]
