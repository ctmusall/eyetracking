from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile-images', blank=True)
    def __unicode__(self):
        return self.user.username

class GatheredData(models.Model):
    user = models.ForeignKey(UserProfile)
    location = models.CharField(max_length = 50, null = True)
    speed = models.CharField(max_length = 50, null = True)
    gaze = models.CharField(max_length = 50, null = True)
    incident = models.CharField(max_length = 50, null = True)

    def __unicode__(self):
        return self.title
