# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0010_remove_gathereddata_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countMarch', models.IntegerField(null=True)),
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eyetracking.GatheredData')),
            ],
        ),
    ]
