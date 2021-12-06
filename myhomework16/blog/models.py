from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Post(models.Model):  # model 상속 / pk : id(int, auto increment 정수)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()

    # 필수 항목X
    image = models.ImageField(blank=True)
    image_file = ImageSpecField(
        source="image",
        processors=[ResizeToFill(800, 400)],
        format="JPEG",
        options={"quality": 60},
    )
    file = models.FileField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # return값은 str(문자열)
        return self.title
    # pk : id


class Comment(models.Model):
    # 위의 Post pk를 fk 로 받아야함
    # N측에다가 외래키를 심음(Post의 pk인 id)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 1 : N 관계
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
