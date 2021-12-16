import tablib
from django.db import models

# Create your models here.
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


# 데이터와 관련된 것은 모델에서 처리하는 것이 나음
class Post(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    # 현재 status에서 중요한 값은? default
    status = models.CharField(
        max_length=1,
        # FIXME: 장고 3에서 추가된 TextChoices 기능을 활용
        # 선택지를 정해놓고 값을 주는 것
        choices=[
            ('D', '초안'),  # Draft // DB저장값, Label
            ('P', '공개'),  # Published
        ],
        db_index=True,
        default='D',  # 위의 ('D', '초안')의 D 임
    )

    def __str__(self):
        return self.title

    # 여기서 기대하는 것 : post_detail 주소 문자열을 반환
    # detail 페이지를 구현하자마자, 즉시 아래 메서드를 구현

    # get_absolute_url 이 있으면 일일히 지정해주지 않아도 돼 !!
    def get_absolute_url(self) -> str:  # 리턴값 str문자열
        return reverse("blog:post_detail", args=[self.pk])

    # resolve_url(post) : resolve_url에 지정된 첫번째 인자가 get_absolute_url 속성이 있으면
    # .get_absolute_url 함수를 즉시 호출하여 그 값을 사용

    # 클래스로서 호출이 되어야 한다.
    # format = "xlsx" 포맷에 대한 디폴트 값. 포맷을 지정하지 않으면 xlsx로 하겠다.
    # 클래스 매서드는 어떻게 지정?
    # # # xlsx를 만드는 함수
    @classmethod  # 이렇게 하는 것이 클래스 매서드 지정
    def get_tabular_data(cls, queryset, format="xlsx") -> bytes:  # 이렇게 쓰는 것이 인스턴스 매서드
        # 이를 호출하는 방법은? 그냥 모델명.get_xlsx_data 이렇게 호춯하면 돼
        # 리턴 타입은 bytes 바이트 타입
        dataset = tablib.Dataset()
        dataset.headers = ['id', 'title', 'created_at', 'updated_at']
        for post in queryset:
            dataset.append([

                post.id,
                post.title,
                post.created_at.strftime("%Y-%m-%d %H:%M:%S"),# Y옆에 m은 소문자여야 한다
                post.updated_at.strftime("%Y-%m-%d %H:%M:%S"), ]
            )

        return dataset.export(format)

    # 이렇게 손쉽게 엑셀 데이터를 만들 수 있음

    class Meta:
        ordering = ['-id']


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']


class Tag(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
