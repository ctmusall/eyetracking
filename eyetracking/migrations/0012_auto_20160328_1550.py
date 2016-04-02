# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 20:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyetracking', '0011_graph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='data',
        ),
        migrations.AddField(
            model_name='gathereddata',
            name='graph',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='eyetracking.Graph'),
        ),
        migrations.AddField(
            model_name='graph',
            name='countApril',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countAugust',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countDecember',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countFebruary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countJanuary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countJuly',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countJune',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countMay',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countNovember',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countOctober',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='graph',
            name='countSeptember',
            field=models.IntegerField(null=True),
        ),
    ]