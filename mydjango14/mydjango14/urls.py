from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from mydjango14 import settings

urlpatterns = [
    path('admin/', admin.site.urls),

]


# static은 그자체가 list

urlpatterns += static(settings.MEDIA_URLS,
                      document_root = settings.MEDIA_ROOT)

if settings.DEBUG: # DEBUG 개발 서버에서만 사용하겠다.
    import debug_toolbar # 개발할 때만, 개발 서버에서만 실행
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]