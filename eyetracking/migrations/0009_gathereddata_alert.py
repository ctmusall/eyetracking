# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0008_weathertest'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathereddata',
            name='alert',
            field=models.IntegerField(null=True),
        ),
    ]
