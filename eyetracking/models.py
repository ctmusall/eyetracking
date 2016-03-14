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

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.name

class GatheredData(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    url = models.URLField()

    def __unicode__(self):
        return self.title
