# apis/serializers.py
from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    title123 = serializers.CharField(source='title')
    class Meta:
        model = models.Todo
        fields = (
            'id',
            'title123',
            'description',
        )
