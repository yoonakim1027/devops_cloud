from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import post_list, post_detail, mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',post_list),
    path('blog/<int:pk>/',post_detail, name="post_detail"),
]
# 꼭 링크 양옆에 / 슬러시가 필요 !! / name = 들어갈 이름 지정
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]