from django.urls import path

from shop import views

app_name = 'shop'

# 설정보다는 관례
# 가장 먼저 시작할 때 이렇게 써줘야 함
urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    # pk 라는 이름으로 뷰함수에 넘기겠다.
    # 숫자가 안들어가면 url reverse가 안된다
    path("<int:pk>/", views.shop_detail, name="shop_detail"),

]
