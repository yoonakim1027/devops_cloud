from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


# TODO : 편의상 여기에 root를 구현하지만, 차후 RedirectView CBV를 써서 이 구현을 제거할 예정
def root(request):
    return redirect("diary:post_list")
# 현재의 뷰가 아니라 다른 주소에서 처리를 하라는 것이 redirect를 통해 가능함


urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls')),
    path('', root, name="root"),  # 최상위 주소 -> 최상위 주소로 들어오면 ? post_list로 이동시켜버릴 것
]

# 확장 -> static() 함수의 반환값이 리스트
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
