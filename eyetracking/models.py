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

class CollectedData(models.Model):
    user = models.ForeignKey(UserProfile)
    imported_date = models.DateTimeField(default = 'django.utils.timezone.now()')
    imported_data = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
