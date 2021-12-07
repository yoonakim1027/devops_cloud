from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # abstract=True 는 ? 이 클래스는 추상 클래스로서, DB 테이블이 생기지 않는다.
        # 단순히 부모로서만 동작한다.


class Post(TimestampedModel):  # model 상속 / pk : id(int, auto increment 정수)
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)

    content = models.TextField()

    # media 폴더 밑에 저장이 된다
    photo = models.ImageField(upload_to='diary/post/%Y/%M/%d')

    def __str__(self) -> str:  # return값은 str(문자열)
        return self.title
    # pk : id


class Comment(TimestampedModel):
    # 위의 Post pk를 fk 로 받아야함
    # N측에다가 외래키를 심음(Post의 pk인 id)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 1 : N 관계
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(TimestampedModel):
    # 보통 태그에는 태그 명 정도 ! -> name
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name
