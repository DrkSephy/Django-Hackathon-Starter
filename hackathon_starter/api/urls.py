# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from api import v1

from django.urls import include, path
urlpatterns = [
    path(r'v1/', include(v1.urls(),)),
]
