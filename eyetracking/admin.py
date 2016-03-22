from django.contrib import admin
from eyetracking.models import GatheredData, WeatherTest


class PageAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date', 'location', 'speed', 'gaze', 'incident')
admin.site.register(GatheredData, PageAdmin)
admin.site.register(WeatherTest)
