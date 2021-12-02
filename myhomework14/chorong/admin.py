from django.contrib import admin
from chorong.models import ChoVideo

class ChovideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ChoVideo, ChovideoAdmin)