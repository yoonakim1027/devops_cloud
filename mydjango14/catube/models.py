from django.db import models

# video _> class는 항상 대문자로 시작

class Video(models.Model):
    # 그러면 title을 입력하지 않아도 저장해버림.
    title = models.CharField(max_length=200) #blank / null을 넣는 순간 옵션 필드로 인지해버림
    description = models.TextField()# blank를 넣지 않으면 필수 필드가 됨

    # TODO : 업로드되는 파일이 비디오 파일인지 여부를 검사!
    video_file = models.FileField()
    thumbnail_file = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 제목은 최대 200글자
    # description은 글자 수 제한 없음
