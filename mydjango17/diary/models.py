from django.db import models


# 상속받아서 정의 하기
# 필드가 정의된 부모로서만 동작하기를 기대함 .
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서, DB테이블이 생기지 않는다.
        # 단순히 부모로서만 동작한다.


class Post(TimestampedModel):  # 모델 상속을 받아서, 모델의 개념을 가져오는 것
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    #  db_index=True 를 하고, makemigrations를 해야 인덱스가 생성이된다!
    content = models.TextField()

    # media 폴더 밑에 저장이 된다
    photo = models.ImageField(upload_to='diary/post/%Y/%M/%d')

    tag_set = models.ManyToManyField('Tag', blank=True)

    # Tag 클래스는 밑에있다. 그래서 ? 얘를 'tag'이렇게 문자열로 감싸주면
    # 장고에서 알아서 Tag를 찾아서 적용해준다 !

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "포스팅"  # 단수
        verbose_name_plural = "포스팅 목록"  # 복수


class Comment(TimestampedModel):
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"  # 단수
        verbose_name_plural = "댓글 목록"  # 복수


class Tag(TimestampedModel):
    # 보통 태그에는 태그 명 정도 !
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"  # 단수
        verbose_name_plural = "태그 목록"  # 복수
