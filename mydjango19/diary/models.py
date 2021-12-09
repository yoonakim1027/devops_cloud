from django.db import models


# 상속받을 클래스
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 포스트 클래스
class Post(TimestampedModel):  # 모델 상속을 받아서, 모델의 개념을 가져오는 것
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='diary/post/%Y/%M/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    ip = models.GenericIPAddressField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "포스팅"  # 단수
        verbose_name_plural = "포스팅 목록"  # 복수


# 코멘트 클래스
class Comment(TimestampedModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # class가 위에있으니까 문자열로 지정 해도 돼
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"  # 단수
        verbose_name_plural = "댓글 목록"  # 복수


# 태그 클래스
class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return f"[{self.pk}] {self.name}"

    class Meta:
        verbose_name = "태그"  # 단수
        verbose_name_plural = "태그 목록"  # 복수
