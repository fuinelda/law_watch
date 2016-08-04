# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 09:02
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_watch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawsummary',
            name='law_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='lawsummary',
            name='law_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
