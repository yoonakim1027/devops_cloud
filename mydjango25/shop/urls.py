from django.urls import path

from shop import views

app_name = 'shop'

# 가장 먼저 시작할 때 이렇게 써줘야 함
urlpatterns =[
    path("", views.shop_list, name = "shop_list")

]