"""mydjango13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from mydjango13 import settings
from django.conf import settings
from mall.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),


]

urlpatterns += static(settings.MEDIA_URLS,
                      document_root = settings.MEDIA_ROOT)

if settings.DEBUG: # DEBUG 개발 서버에서만 사용하겠다.
    import debug_toolbar # 개발할 때만, 개발 서버에서만 실행
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]