from django.forms import widgets
from rest_framework import serializers
from hackathon.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos')