from django.db import models


# 상속받아서 정의 하기
# 필드가 정의된 부모로서만 동작하기를 기대함 .
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서, DB 테이블이 생기지 않는다.
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


# 1 : N 관계에서, 하나의 포스트가 삭제되었을때, 거기에 있을 댓글들은 어떻게 할래?
# on_delete=models.CASCADE -> 포스트가 삭제되었을때, 댓글들도 같이 지워줌
# Foreignkey추가
class Comment(TimestampedModel):
    # 외래키는 정수값을 지정해야 함

    # 밑에 처럼 지정해주면? post_id라는 필드를 자동으로 생성해줌
    # 외래키에 한해서는, 이름_id라는 필드가 생기게 됨.
    # 실제 DB의 외래키는 post_id인 거고 ~

    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # class가 위에있으니까 문자열로 지정 해도 돼
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
