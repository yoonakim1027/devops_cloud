from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # 인덱스생성하겠다
    description = models.TextField(blank=True)  # 설명이 있는 경우, 없는 경우도 허용 -> blank
    address = models.CharField(max_length=100)  # address는 text보다 char이 더 맞음

    # TODO : GeoDjango의 PointField를 사용하는 것이 맞음!
    # 이를 쓰면? 위경도를 하나의 필드에 저장할 수 있음!
    latitude = models.FloatField(verbose_name="위도")  # 위도
    longitude = models.FloatField(verbose_name="경도")  # 경도

    # TODO : 전화번호 값인지 여부를 체킹 -> 다음 주쯤~
    telephone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)  # 생성시각
    updated_at = models.DateTimeField(auto_now=True)  # 수정시각


