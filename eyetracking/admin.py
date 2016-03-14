from django.contrib import admin
from eyetracking.models import UserProfile, Category, GatheredData

class GatheredDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(GatheredData, GatheredDataAdmin)
