from django.db import models


class Post(models.Model):  # model 상속 / pk : id(int, auto increment 정수)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()

    # 문자열로 쓰면? 현재 app에서 tag를 알아서 찾음
    tag_set = models.ManyToManyField('Tag', blank=True)
    # blank=True를 설정해주지 않으면 ?

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스에 대한 문자열 표현을 기대
    # post.title
    # print(post) # 내부적으로 post.__str__을 찾아서 호출해서 반환값을 출력
    # print(post.__str__())
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


# 모델에서는 생성자 정의가 없음

# CASCADE -> 작은 폭포
# on_delete=models.CASCADE -> 포스팅이 pk 있는 곳에서 삭제될때, 같이 삭제 됨


class Tag(models.Model):
    # Tag는 일반적으로 단일 컬럼으로 문자열 정도만 저장
    # 보통 Tag의 name을 pk로 지정할 수도 있지만~

    name = models.CharField(max_length=100, unique=True)
    # 데이터베이스에서 현재 Tag 범위 내에서는 절대 같은 name의 tag가 존재 할 수 없음
    # name - > unique라는 제약사항을 걸게 되는 것
    # 하나의 태그 - > 다수의 포스팅에 속할 수 있고
    # 하나의 포스팅 - > 다수의 태그에 속할 수 있음


