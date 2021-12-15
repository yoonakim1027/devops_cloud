from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"


class Post(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    content = models.TextField(blank=True)
    telephone = models.CharField(max_length=14, validators=[
        # 정규표현식, message='패턴이 조합되지 않으면 출력될 메시지
        RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="전화번호를 입력해주세요.")
    ],  # 중괄호 안에 {시작범위(이상),끝날범위(이하)} {중괄호는 범위 }
                                 help_text="입력 예) 042-1234-1234")

    tag_set = models.ManyToManyField('Tag', blank=True)

    status = models.CharField(max_length=1,
                              choices=[
                                  ('C', '초롱'),
                                  ('K', '꼬마'), ],
                              db_index=True,
                              default='C', )

    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self) -> str:
        return reverse("blog:post_detail",args=[self.pk])

    class Meta:
        ordering = ["-id"]  # 정렬
        verbose_name = "게시글"  # 단수
        verbose_name_plural = "게시글 목록"  # 복수


class Comment(TimestampedModel):
    # post을 외래키로 지정, on_delete(삭제정책) : 하나의 shop이 삭제 -> 이에 딸린 리뷰도 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['author_name']
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):  # Tag는 유일성을 가지기 위해, unique 옵션을 넣는다.
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]  # 좀 더 유의미한 결과를 위해 name오름차순으로 정렬
        verbose_name = "태그"  # 단수
        verbose_name_plural = "태그 목록"  # 복수
