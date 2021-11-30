from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(blank=False, null=False, max_length=20, verbose_name="오늘 일기 제목")
    content = models.TextField(blank=False, null=False, verbose_name="내용") #이렇게 하면 길이 제한 X
    # upload_to
    # - 문자열 : 파일이 저장되는 폴더의 경로
    # 파일이 저장할 때 upload_to를 사용하는 것
    morning = models.BooleanField(blank=False, null=False, verbose_name=" 아침밥 먹었니?")

    photo = models.ImageField(blank=True) # 필수 필드가 아니게 됨!
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True) #생성할 때 자동 지정
    updated_at = models.DateTimeField(blank=False, null=False, auto_now=True) # 수정시간 자동 지정
