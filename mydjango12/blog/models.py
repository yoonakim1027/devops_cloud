from django.db import models
from blog.upload_to import uuid_name_upload_to
# Create your models here.


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField() #이렇게 하면 길이 제한 X
    # upload_to
    # - 문자열 : 파일이 저장되는 폴더의 경로
    # 파일이 저장할 때 upload_to를 사용하는 것

    photo = models.ImageField(blank=True, upload_to = uuid_name_upload_to) # 필수 필드가 아니게 됨!
    created_at = models.DateTimeField(auto_now_add=True) #생성할 때 자동 지정
    updated_at = models.DateTimeField(auto_now=True) # 수정시간 자동 지정

# 관리자만 포스트 작성을 허용하고 싶어

#     photo = models.ImageField(blank=True, upload_to = 'blog/post/%Y')
# Y로하면 입력 날짜 지정됨
# %M minute
# upload_to -> 파일이 저장되는 경로
# 함수로 지정하면 좀 더 체계적으로 관리할 수 있음
