"""
URL configuration for oak_build project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from signal import SIG_DFL
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

from oak_build import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),#добавление конфигурации приложения main в конфигурацию проекта, namespace - это пространство имен для приложения main
    path('catalog/', include('goods.urls', namespace='catalog')),#добавление конфигурации приложения goods в конфигурацию проекта, namespace - это пространство имен для приложения goods
    ]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

'''
www.oak-build.com/admin
www.oak-build.com
www.oak-build.comC
www.oak-build.com/catalog
www.oak-build.com/catalog/product
'''