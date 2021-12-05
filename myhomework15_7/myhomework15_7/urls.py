from django.contrib import admin
from django.urls import path, include

from myhomework15_7 import settings
from yoona import views

urlpatterns = [
    path('<int:pk>/', views.StudyPostDetail.as_view()), #상세 페이지
    path('', views.StuyPostList.as_view()), # 리스트 페이지
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/',
             include(debug_toolbar.urls))
    ]
