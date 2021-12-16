from django.urls import path
from shop import views

app_name = "shop"

urlpatterns =[
    path('', views.shop_list, name="shop_list"),
    # shop
    path('<int:pk>/', views.shop_detail, name="shop_detail"),
    path('new/', views.shop_new, name="shop_new"),
    path('<int:pk>/edit/',views.shop_edit, name= "shop_edit"),
    path('<int:pk>/delete/', views.shop_delete, name = "shop_delete"),
    # review
    path('<int:pk>/review/new/',views.review_new, name="review_new"),
    path('<int:pk>/review/<int:shop_pk>/edit/',views.review_edit,name="review_edit"),
    path('<int:pk>/review/delete/', views.review_delete, name="review_delete"),

]