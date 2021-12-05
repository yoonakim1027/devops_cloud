from django.contrib import admin

from yoona.models import StudyPost


class StudyPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(StudyPost, StudyPostAdmin)