from django.urls import path

from diary import views
from . import views

app_name = 'diary'  # 보통 앱 이름을 한번 써줌

urlpatterns = [
    path("", views.post_list, name="post_list"),  # 함수만 지정.
]

# urlpatterns = [
# path("", list, name= ]

# 부모 layout.html은 상속을 해주기 위해서만 존재하는 것.
# 자식이 할 수 있는 일은? 부모가 정의한 block에 content를 공급하는 것 밖에 없음
