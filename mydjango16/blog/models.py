from django.db import models


class Post(models.Model):  # model 상속 / pk : id(int, auto increment 정수)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # pk : id


class Comment(models.Model):
    # 위의 Post pk를 fk 로 받아야함
    # N측에다가 외래키를 심음(Post의 pk인 id)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 1 : N 관계
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 모델에서는 생성자 정의가 없음

# CASCADE -> 작은 폭포
# on_delete=models.CASCADE -> 포스팅이 pk있는 곳에서 삭제될때, 같이 삭제 됨