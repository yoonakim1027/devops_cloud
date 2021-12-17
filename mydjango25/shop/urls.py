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

    # 어떤 샵에 속한 리뷰이기 때문에 pk가 필요함.
    path("<int:shop_pk>/reviews/new/", views.review_new, name="review_new"),
]
