from django.conf import settings
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 다른 모델 클래스에서 사용하는 부모 클래스!


class Category(TimestampedModel):
    # 카테고리와 Shop은 외래키 관계 . 카테고리가 1 : 샵이 N
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        # 정렬기준은 한 개만 넣어주는 것이 좋음 !
        # 카테고리는 생성시점이 중요하지 않으니까 ~ 그냥 이름기준으로 오름차순 정렬
        ordering = ['name']
        verbose_name = "카테고리"
        verbose_name_plural ="카테고리 목록"


class Shop(TimestampedModel):
    # 한명의 오너가 다수의 샵을 소유할 수 있다.
    # ('blog.해당하는 앱이름')이 앱 안에 있는 모델을 참조하겠다.
    # settings.AUTH_USER_MODEL 의 티폴트 값 : 'auth_User"
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 외래키는 n측에 생성 , 삭제 정책은 CASCADE
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 소스코드를 읽어들인 시점에 실행. 위에서부터 순차적으로 실행
    # 태그는 밑에 있기 때문에, 이 시점에는 Tag가 없는상태
    # 그래서 문자열로 지정을 하면 django가 알아서 찾아서 값을 넣어줌
    name = models.CharField(max_length=200, db_index=True)
    # 이름만으로 검색할 수도 있기 때문에 db_index를 넣어줌
    description = models.TextField(blank=True)
    # upload_to = 를 통해 사진을 저장할 곳을 지정
    #
    photo = models.ImageField(upload_to="shop/shop/%Y/%m/%d", blank=True)

    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "상점"
        verbose_name_plural ="상점 목록"



# 샵과 리뷰는 외래키 관계. 샵이 1 : 리뷰가 N
class Review(TimestampedModel):
    # 외래키를  n측에 생성
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # 한 명의 유저가 여러 개의 리뷰를 작성할 수 있다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField() # 메시지 입력은 꼭 받아야하니까 블랭크 옵션 X

    def __str__(self):
        return self.message
    # 리뷰랑 샵은 생성시점이 중요하니까 내림차순
    class Meta:
        ordering = ['-id']
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 목록"


class Tag(TimestampedModel):
    # 태그는 유일해야 하니까 unique 옵션을 지정
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        # 이름을 기준으로 오름차순 정렬
        ordering = ['name']
        verbose_name = "태그"
        verbose_name_plural ="태그 목록"