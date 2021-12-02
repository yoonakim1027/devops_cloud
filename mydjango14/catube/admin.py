from django.contrib import admin

from catube.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass



admin.site.register(Video, VideoAdmin)
# 모델에 대한 기본 옵션으로 admin에 적용이 되는 것
