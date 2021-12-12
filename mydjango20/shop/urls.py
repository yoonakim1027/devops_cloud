from django.urls import path
# 여기는 슬러시를 안붙히고 해야함
from shop import views

app_name = "shop"
urlpatterns =[
    path("<int:pk>/",views.shop_detail, name="shop_detail"),
    path("new/",  views.shop_new, name="shop_new"),
    path("", views.shop_list, name="shop_list"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
    path("review_new/", views.review_new, name="review_new"),
]
