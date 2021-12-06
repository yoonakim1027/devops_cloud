
from django.contrib import admin
from django.urls import path
from delicious.views import shop_list, shop_detail, shop_new_1, shop_new
# 2개의 뷰 생성 예정 / 특정 샵의 정보, 리스트

app_name = "delicious" # namespace -> 보통은 app이름과 같은 이름을 씀 !

# 항상 urls.py에는 urlpatterns 가 필수임! django가 알아서 하니까 우선 있어야 함

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('<int:pk>/', shop_detail, name='shop_detail'), # shop_detail이라는 뷰 호출
    path('new1/', shop_new_1, name='shop_new_1'),
    path('new/', shop_new, name='shop_new'),

]
# app 안에 있는 url은 노출되지 않음!
# 이렇게 따로 앱 안에 urls.py를 생성해줘야 함
