from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # 이 모델에 대한 옵션을 지정
        abstract = True  # DB테이블 생성 X = 상속만 해주는 역할!


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    # 카테고리 이름은 일반적으로 unique속성을 줌

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = "카테고리"  # 단수
        verbose_name_plural = "카테고리 목록"  # 복수


class Shop(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    # 1:N 하나의 shop에 여러 개의 태그가 가능
    content = models.TextField(blank=True)  # 가게 설명이 없어도 등록 가능
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     # 정규표현식, message='패턴이 조합되지 않으면 출력될 메시지
                                     RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="전화번호를 입력해주세요.")
                                 ],  # 중괄호 안에 {시작범위(이상),끝날범위(이하)} {중괄호는 범위 }
                                 help_text="입력 예) 042-1234-1234")
    tag_set = models.ManyToManyField('Tag', blank=True)


    # 새로 장고3에서 추가된 TextChoices 기능
    status = models.CharField(
        max_length=1,
        choices=[
            ('D', '초안'),  # Draft // DB에 저장할 값 -> Label
            ('P', '공개'),  # Published
        ],
        db_index=True,
        default='D',  # default 값을 D로 지정하면 -> 기본 값이 D -> '초안'이 됨
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("shop:shop_detail", args=[self.pk])


    class Meta:
        ordering = ["-id"]  # 정렬
        verbose_name = "상점"  # 단수
        verbose_name_plural = "상점 목록"  # 복수


class Review(TimestampedModel):
    # shop을 외래키로 지정, on_delete(삭제정책) : 하나의 shop이 삭제 -> 이에 딸린 리뷰도 삭제
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['author_name']
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"

    def get_absolute_url(self) -> str:
        return reverse("shop:shop_detail", args=[self.pk])





class Tag(TimestampedModel):  # Tag는 유일성을 가지기 위해, unique 옵션을 넣는다.
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "태그"  # 단수
        verbose_name_plural = "태그 목록"  # 복수
