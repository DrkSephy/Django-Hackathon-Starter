# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework import routers
from api.v1.views import TestClassView

__all__ = ['urls']

def urls():
    router = routers.DefaultRouter()
    return (
        router.urls + [
            url(r'^test/$', TestClassView.as_view(), name='test'),
        ]
    )

