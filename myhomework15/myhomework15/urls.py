
from django.contrib import admin
from django.urls import path, include

# 이번에 내가 만들 페이지 목록  (3개)
# 1. 대문 페이지
# 2. 블로그 페이지
# 3. 자기소개 페이지
import yoona
from myhomework15 import settings
from yoona import views

urlpatterns = [
    path('<int:pk>/', views.StudyPostDetail.as_view()),
    path('', views.StudyPostList.as_view()),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/',
             include(debug_toolbar.urls)),

    ]
