
from django.contrib import admin
from django.urls import path, include

from myhomework15_5 import settings


# 1. 대문페이지
# 2. 스터디 페이지
# 3. 저희집 강아지 사진 업로드하는 공간 (포스트 pk)- 상세 페이지
from yoona import views

urlpatterns = [
    path('', views.StudyPostList.as_view()),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/',
             include(debug_toolbar.urls)),
    ]