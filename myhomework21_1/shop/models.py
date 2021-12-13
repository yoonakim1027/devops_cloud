from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # 이 모델에 대한 옵션을 지정
        abstract = True  # DB테이블 생성 X = 상속만 해주는 역할!


class Shop(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    # 1:N 하나의 shop에 여러 개의 태그가 가능
    description = models.TextField(blank=True)  # 가게 설명이 없어도 등록 가능

    tag_set = models.ManyToManyField('Tag', blank=True)


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)  # 카테고리 이름은 일반적으로 unique속성을 줌


class Tag(TimestampedModel):  # 유일성을 가지기 위해, unique 옵션을 넣음
    name = models.CharField(max_length=100, unique=True)
