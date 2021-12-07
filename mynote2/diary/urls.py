from django.urls import path

from . import views
app_name = 'diary'  # 보통 앱 이름을 한번 써줌

# name = 이 함수의 이름은~ 이라는 뜻
urlpatterns = [
    path("", views.post_list, name="post_list"),  # 함수만 지정.

]

