from django.db import models

# 한 가게의 정보를 담는 모델이 생성됨
# 프라이머리 키는 아직 생성 안되어 있음

class Shop(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) #설명안할수도 있음
    photo = models.ImageField(blank=True) # 사진이 없을 수도 있음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)