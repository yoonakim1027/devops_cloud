from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def root(request):
    return redirect("shop:shop_list")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include('shop.urls')), # 딴 파일에 정의되었기 때문에 include(앱이름.파일이름)
    # shop.urls에 붙은 모든 urls가 include( 앱마다 뷰 구현 따로 / url정의도 따로 )
    path("", root, name="root"),

]

urlpatterns += static(settings.MEDIA_URL,
                      documment_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
