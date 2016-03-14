from django.contrib import admin
from eyetracking.models import UserProfile, Category, GatheredData

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(GatheredData)
