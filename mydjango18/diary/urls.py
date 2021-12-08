from . import views
from django.urls import path

# 개별적인 부분의 url는 여기에 지정!


app_name = 'diary'  # 얘네들은 이제 url reverse 할 때 쓰일 것!

urlpatterns = [
    path('', views.post_list, name="post_list"),  # post_list의 뷰는 "post_list"라는 이름으로 사용 하겠다 .
    path('<int:pk>/', views.post_detail, name="post_detail"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
]
