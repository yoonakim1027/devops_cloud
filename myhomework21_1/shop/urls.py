from . import views
from django.urls import path

app_name = "shop"  # url reverse 적용 시, 이 이름으로 사용하게 됨
urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("<int:pk>/", views.shop_detail, name="shop_detail"),
    path("new/", views.shop_new, name="shop_new"),
    path("<int:pk>/edit/", views.shop_edit, name="shop_edit"),

]