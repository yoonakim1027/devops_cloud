from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from chorong.views import index, video_detail

from myhomework14 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chorong/', index),
    path('chorong/<int:pk>/', video_detail),

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/',
             include(debug_toolbar.urls)),

    ]
