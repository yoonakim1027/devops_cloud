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

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]