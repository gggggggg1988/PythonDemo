"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

import app_name
from app_name import views as app_views
from project_name import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', app_views.index),
                  url(r'^index/$', app_views.home),
                  url(r'^add/$', app_name.views.add, name='add'),
                  url(r'^add/(\d+)/(\d+)/$', app_name.views.old_add2_redirect),
                  url(r'^new_add/(\d+)/(\d+)/$', app_name.views.add2, name='add2'),
                  url(r'^upload_avatar/', app_views.upload_avatar),
                  url(r'^test/', app_views.test),
                  url(r'^upload', app_views.uploadImg),
                  url(r'^show', app_views.showImg),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
