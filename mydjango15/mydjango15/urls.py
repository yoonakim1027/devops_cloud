from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/', include('delicious.urls')),
    # delicious 공통적으로 쓰이는 부분
    # 한번만 delicious 지정해두면, 한번만 해도 돼 !
]
