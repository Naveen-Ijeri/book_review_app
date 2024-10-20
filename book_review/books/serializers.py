from .models import Book
from rest_framework import serializers


class BooksSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    author = serializers.CharField(required=True, allow_blank=False, max_length=100)
    genre = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    summary = serializers.CharField(required=True, allow_blank=True, max_length=1000)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
