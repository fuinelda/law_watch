# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 09:17
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('law_watch', '0002_auto_20160802_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawsummary',
            name='law_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]