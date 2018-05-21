# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.urls import include, path

from hackathon import views as hack_views

urlpatterns = [
    path(r'', hack_views.index, name='index'),
    url('^hackathon/', include('hackathon.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^openid/(.*)', SessionConsumer()),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    url('^admin/', admin.site.urls),
    url('^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^hijack/', include('hijack.urls', namespace='hijack')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)), )
