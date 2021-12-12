from django.urls import path
# 여기는 슬러시를 안붙히고 해야함
from shop import views

app_name = "shop"
urlpatterns =[
    path("<int:pk>/",views.shop_detail, name="shop_detail"),
    path("new/",  views.shop_new, name="shop_new"),
]
