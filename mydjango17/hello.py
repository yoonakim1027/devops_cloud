from django.db import models

# 포스트가 1, 한개의 포스팅에 다수의 Tag를 가짐
# 그럴경우, 포스트가 태그에게 외래키로 됨
from django.db.models import CharField

# 한개의 포스팅은 다수의 코멘트, 다수의 태그를 가질 수 있다.

# post.comment_set.a
# 모델명.소문자_set

Comment.objects.filter(post=post)
# 전체 포스팅중에, 오른쪽의 post에 속한 comment만 filter
#  위에랑 똑같은 결과를 내는 코드는?
# post.comment_set.all()



class Post(models.Model):
    title = CharField(max_length=100)
    tag_set = models.ManyToManyField('Tag')
    # manytomanyfiel

# 여기에 tag를 설정하는 것이 더 좋음
# 여기에 'Tag'에 작은따옴표를 써서 넣어주는 이유는?
# 이 클래스가 선언될 때 Tag클래스가 밑에있기 때문에,
# 직접적으로 쓰지는 못하고, 같은 앱에서 이 이름의 모델을
# 장고가 알아서 찾아줌

# 근데 밑의 class Tag가 이 클래스 위에 써있다면 작은따옴표 없이
# 해도 돼


# 포스트 입장에서? 내가 가진 댓글목록들을 다 가져보고 싶다면?
# 포스트는 1인쪽임 코멘트가 다수 쪽
# 코멘트에 의해 필드정의가 이루어졌음.
# Post에 대해서는 ?


# 포스트와 Comment -> 1대 N 관계
class Commnet(models.Model):
    post = models.ForeignKey(Post) # 외래키
    name = CharField(max_length=100)


class Tag(models.Model):
    post = models.ForeignKey(Post) # 외래키
    name = CharField(max_length=100)
    # post_set = models.ManyToManyField(Post)

# manytomany는 별도의 테이블을 만들어야 함
# 하나의 포스팅이 다수의 포스팅을 가진다.

# 앱을 만드는 이유는 ? -> 재사용성을 위함 !


# post_list는 항상 url이 같음
# post_detail은 항상 url이 가변적!

# 댓글변경 시 필요한 path
# path("<int:post_pk>/comments/<int:pk>/edit/", views.comment_edit),
# 가변적인 부분이 2개일 수도 있고, 한개일 수도 있고..


# 가변적인 부분을 위해 {% url : ~ 여기부분 안에 들어가는거임)



# 사전
# { "key" : value }

# 값을 넣을때 함께 사전으로 넣는다면?
# render에서, contexted_type는 사전으로 받게 되어있기 때문에 !!!


# 사전형태로 키 밸류 넘기기
# 사전 자료구조로 맵핑을 해서 읽어낼 수 있음



# null - > DB입장에서, 데이터를 지정하지 않았다.
# blank -> django입장에서, 빈 경로를 허용하겠다.
# 비었다 라는 개념이 존재하려면? 문자열 필드
# 숫자에는 비었다는 개념이 없다.
