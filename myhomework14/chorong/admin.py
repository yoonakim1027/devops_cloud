from django.contrib import admin
from chorong.models import ChoVideo


class ChovideoAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

    search_fields = ['title']


admin.site.register(ChoVideo, ChovideoAdmin)
