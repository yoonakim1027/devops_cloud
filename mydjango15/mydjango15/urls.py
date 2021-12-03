
from django.contrib import admin
from django.urls import path
from delicious.views import shop_list, shop_detail, shop_new_1, shop_new
# 2개의 뷰 생성 예정 / 특정 샵의 정보, 리스트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/', shop_list),
    path('delicious/<int:pk>/', shop_detail),
    path('delicious/new1/', shop_new_1),
    path('delicious/new/', shop_new),

]


