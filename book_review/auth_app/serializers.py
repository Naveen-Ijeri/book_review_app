from rest_framework import serializers
from utils import encrypt_password
from .models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        password = request.data.get('password')
        encrypted_password = encrypt_password(password)
        validated_data.update({"encrypted_password": encrypted_password})
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)



