from django.db import models
from django.core.validators import RegexValidator


# regex -> 정규표현식


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # 인덱스생성하겠다
    description = models.TextField(blank=True)  # 설명이 있는 경우, 없는 경우도 허용 -> blank
    address = models.CharField(max_length=100)  # address는 text보다 char이 더 맞음

    # TODO : GeoDjango의 PointField를 사용하는 것이 맞음!
    # 이를 쓰면? 위경도를 하나의 필드에 저장할 수 있음!
    latitude = models.FloatField(verbose_name="위도")  # 위도
    longitude = models.FloatField(verbose_name="경도")  # 경도

    # TODO : 전화번호 값인지 여부를 체킹 -> 다음 주쯤~
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{3,4}-?\d{4}-?\d{4}$",
                                                    message="전화번호를 입력해주세요"),
                                 ])
    # validators- > 이 값은 꼭 이거어야만 한다!!
    # 현재 아무 문자열이나 입력가능.
    #  RegexValidator(r"\d{4}") 숫자가 4번
    # RegexValidator(r"\d{3,4}") 3번이나 4번
    # RegexValidator(r"^\d{3,4}-?\d{4}-?\d{4}$")
    created_at = models.DateTimeField(auto_now_add=True)  # 생성시각
    updated_at = models.DateTimeField(auto_now=True)  # 수정시각
