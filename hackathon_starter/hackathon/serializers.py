# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.forms import widgets
from rest_framework import serializers
from hackathon.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos')
