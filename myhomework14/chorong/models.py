from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# 초롱이 비디오 업로드 사이트
class ChoVideo(models.Model):
    # 제목 : 최대 100글자
    title = models.CharField(max_length=100)
    # 설명 : 제한 X
    description = models.TextField()
    # 비디오 업로드
    video_file = models.FileField()
    # 사진 업로드 - 썸네일
    thumbnail_file = models.ImageField()
    thumbnail_file_thumb = ImageSpecField(
        source="thumbnail_file",
        processors=[ResizeToFill(800,400)],
        format="JPEG",
        options={'quality':70},
    )


    # 업로드 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

