from django.urls import path
from shop import views

app_name = "shop"
urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("<int:pk>/", views.shop_detail, name="shop_detail"),
    path("new/", views.shop_new, name="shop_new"),
    path("<int:pk>/edit/", views.shop_edit, name="shop_edit"),
    path("<int:post_pk>/reviews/new/", views.review_new, name="review_new"),
    path("<int:post_pk>/reviews/<int:pk>/edit/", views.review_edit, name="review_edit"),
]
# views.review_edit 주소에 부합되는지
# "<int:post_pk>/reviews/<int:pk>/edit/" 주소만 보고
# 정수/edit/로 끝나면? views.의 shop_edit 함수를 호출해서 요청을 하겠다
# 이 주소가 되면 오 함수
# 정수 값을 뽑아냄 -> django에서는 capture라고 함
# 값을 뽑아내는데, 값에 대한 이름을 post_pk로 지정하는 것
# 그래서 함수를 호출할때 넘겨줌 post_pk
# 그래서 해당 함수가 post_pk 인자를 받을 수 있어야 한당