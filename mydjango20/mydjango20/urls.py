from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


# 다른 뷰로 처리
def root(request):
    return redirect("shop:shop_list")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', root, name="root"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
