# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-12 21:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0009_auto_20160312_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collecteddata',
            name='imported_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 21, 26, 54, 873208, tzinfo=utc)),
        ),
    ]