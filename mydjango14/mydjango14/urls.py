from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from catube.views import index, video_detail


from mydjango14 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catube/', index), #함수만 지정
    path('catube/<int:pk>/',video_detail),
]
# 비디오는 재생은 안되지만, 생성되는 시간 정도는 생성 가능


# static은 그자체가 list

urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)

if settings.DEBUG: # DEBUG 개발 서버에서만 사용하겠다.
    import debug_toolbar # 개발할 때만, 개발 서버에서만 실행
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]