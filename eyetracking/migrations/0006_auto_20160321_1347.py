# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-21 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0005_auto_20160315_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gathereddata',
            name='speed',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
