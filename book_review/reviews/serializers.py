from .models import Reviews
from rest_framework import serializers
from auth_app.serializers import UserSerializer
from books.serializers import BooksSerializer
from .models import Reviews


class ReviewsSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    book = BooksSerializer(read_only=True)
    rating = serializers.IntegerField(required=True)
    comment = serializers.CharField(required=True, allow_blank=True, max_length=1000)

    class Meta:
        model = Reviews
        fields = ['review_id', 'user', 'book', 'rating', 'comment']
    
    def create(self, validated_data):
        return Reviews.objects.create(**validated_data)

