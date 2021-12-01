from django.db import models
import datetime

# 한 가게의 정보를 담는 모델이 생성됨
# 프라이머리 키는 아직 생성 안되어 있음

class Shop(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #설명안할수도 있음
    telephone = models.CharField(max_length=13) #default 값이 의미가 없긴함
    # open_time = models.TimeField(default=datetime.time) # 필수 필드
    photo = models.ImageField(blank=True) # 사진이 없을 수도 있음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id'] # id에 대해서 내림차순 정렬이 기본 정렬값
        #관련 쿼리셋에서 order_by를 지정하지 않았을 때 정할 default 값값
# open_time = models.TimeField(default=datetime.time())
# default = 값, 함수 (두 개의 인자를 지정할 수 있음)

