# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0009_gathereddata_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gathereddata',
            name='alert',
        ),
    ]
