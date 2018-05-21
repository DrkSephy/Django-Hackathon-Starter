# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import logging
import requests

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# logger = logging.getLogger(__name__)


class TestClassView(APIView):
    permission_classes = []
    http_method_names = ['get', 'post', 'options']

    def get(self, request, format=None):
        return Response(data={'request-type': 'get'}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(data={'request-type': 'post'}, status=status.HTTP_200_OK)
