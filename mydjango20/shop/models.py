from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # 이 모델에 대한 옵션을 지정
        abstract = True  # DB테이블 생성 X


class Shop(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    # 1:N 하나의 shop에 여러 개의 태그가 가능

    description = models.TextField(blank=True)  # 가게 설명이 없어도 등록 가능
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     # 정규표현식, message='패턴이 조합되지 않으면 출력될 메시지
                                     RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요.")
                                 ],
                                 help_text="입력 예) 042-1234-1234")

    photo = models.ImageField(upload_to='diary/post/%Y/%M/%d',blank=False)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:  # 타입힌트는 안써도 되지만, 인자와 리턴 타입은 명시하는 것이 좋음
        return self.name

    class Meta:
        verbose_name = "상점"  # 단수
        verbose_name_plural = "상점 목록"  # 복수


# 1:N
# 1개의 shop에 다슈의 review
class Review(TimestampedModel):  # on_delete 삭제정책
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)  # 외래키
    # 하나의 shop이 삭제가 되면,
    # 이 shop에 속해있던 review도 자동 삭제

    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "리뷰"  # 단수
        verbose_name_plural = "리뷰 목록"  # 복수


class Tag(TimestampedModel):  # 유일성을 가지기 위해, unique 옵션을 넣음
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:  # 타입힌트는 안써도 되지만, 인자와 리턴 타입은 명시하는 것이 좋음
        return self.name

    class Meta:
        verbose_name = "태그"  # 단수
        verbose_name_plural = "태그 목록"  # 복수
