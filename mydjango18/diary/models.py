from django.db import models


# 만들 클래스는 총 4개 -> 그 중 하나는 중복되는 항목을 상속을 해주는 상속 클래스

# 중복항목을 생성해주기 위한 부모 클래스 생성
class TimestampedModel(models.Model):
    # 처음 생성한 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시간
    updated_at = models.DateTimeField(auto_now=True)

    # 이 클래스는 추상 클래스로서, 부모로서만 동작하기 위한 필수 항목
    class Meta:
        abstract = True


# 우선 만들던 데로 만들기
class Post(TimestampedModel):
    # 글쓴이 이름
    author_name = models.CharField(max_length=20, verbose_name="글쓴이 이름")
    # 제목
    title = models.CharField(max_length=20, verbose_name="글 제목")
    # 내용
    content = models.TextField(verbose_name="내용")
    # 사진 -> 필수 항목이 아니기 때문에 for문으로 사진이 없을 때를 대비해서 적어줘야 함
    photo = models.ImageField(upload_to='diary/post/%Y/%M/%d', blank=True)

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    # 위의 post를 외래키로 받음 /
    # 1 :N 관계로, 위에서 받은 post가 삭제될 경우(on_delete) 어떻게 처리할 것인지
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # 댓글 내용
    message = models.TextField()


class Tag(TimestampedModel):
    # 태그 명 -> db_index 생성하겠느냐
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return f"[{self.pk}] {self.name}"
