import uuid
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from django.http import JsonResponse
from .models import User, UserSessions
from utils import encrypt_password
from rest_framework.response import Response
from constant import ErrorMessage, SuccessMessage


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            password = request.data.get('password')
            if not password:
                return JsonResponse({"error": ErrorMessage.PASSWORD_FIELD_IS_MANDATORY}, status=status.HTTP_400_BAD_REQUEST)
            user_serializer = UserSerializer(data=request.data, context={'request': request})
            if user_serializer.is_valid():
                user_serializer.save()
                user_serializer.validated_data.update({"password": password})
                return JsonResponse({"message": SuccessMessage.USER_REGISTERED_SUCCESSFULLY, "data": user_serializer.validated_data}, status=status.HTTP_201_CREATED)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            login_serializer = LoginSerializer(data=request.data)
            if login_serializer.is_valid():
                data = {}
                email = login_serializer.validated_data.get('email')
                password = login_serializer.validated_data.get('password')
                encrypted_password = encrypt_password(password)
                user = User.objects.filter(email=email, encrypted_password=encrypted_password).first()
                if user:
                    data.update({"user_id": user.user_id, "username": user.username, "email": user.email, "token": str(uuid.uuid4())})
                    UserSessions.objects.filter(user_id=user.user_id).delete()
                    UserSessions.objects.create(**data)
                    return JsonResponse({"message": SuccessMessage.LOGIN_SUCCESSFULLY, "data": data}, status=status.HTTP_200_OK)
                return JsonResponse({"error": ErrorMessage.USER_NOT_REGISTERED}, status=status.HTTP_403_FORBIDDEN)
            return JsonResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogOutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user_id')
            if user_id:
                UserSessions.objects.filter(user_id=user_id).delete()
                return JsonResponse({"message": SuccessMessage.LOGOUT_SUCCESSFULLY }, status=status.HTTP_200_OK)
            return JsonResponse({"error": ErrorMessage.USER_ID_FIELD_IS_MANDATORY}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
