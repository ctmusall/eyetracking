from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
import uuid

class GatheredData(models.Model):
    user = models.ForeignKey(User, default = "")
    created_date = models.DateTimeField(default = datetime.now)
    location = models.CharField(max_length = 50, null = True)
    speed = models.IntegerField(null = True)
    gaze = models.CharField(max_length = 50, null = True)
    incident = models.CharField(max_length = 50, null = True)

    def __unicode__(self):
        return self.incident

class WeatherTest(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
