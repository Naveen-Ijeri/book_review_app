from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from books.models import Book
from auth_app.models import User
from reviews.models import Reviews
from .serializers import ReviewsSerializer
from rest_framework.response import Response
from django.http import Http404
from authentication import AuthenticateUser
from constant import ErrorMessage, SuccessMessage


class BooksCreateReviews(APIView):
    def post(self, request, *args, **kwargs):

        authentication_classes = (AuthenticateUser,)

        book_id = kwargs.get('book_id')
        try:
            try:
                book = get_object_or_404(Book, book_id=book_id)
            except Http404:
                return JsonResponse({"error": ErrorMessage.BOOK_DETAILS_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
            try:
                user = get_object_or_404(User, user_id=request.user_id)
            except Http404:
                return JsonResponse({"error": ErrorMessage.USER_NOT_REGISTERED}, status=status.HTTP_404_NOT_FOUND)

            review_serializer = ReviewsSerializer(data=request.data)
            if review_serializer.is_valid():
                review_serializer.save(book=book, user=user)
                return JsonResponse({"message": SuccessMessage.REVIEW_ADDED_SUCCESSFULLY}, status=status.HTTP_200_OK)
            return JsonResponse(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):

        authentication_classes = (AuthenticateUser,)
        
        book_id = kwargs.get('book_id')
        try:
            book_id = kwargs.get('book_id')
            try:
                book = get_object_or_404(Book, book_id=book_id)
            except Http404:
                return JsonResponse({"error": ErrorMessage.BOOK_DETAILS_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
            reviews = Reviews.objects.filter(book=book)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class BooksUserReviews(APIView):
    
    authentication_classes = (AuthenticateUser,)

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            user_id = kwargs.get('user_id')
            limit = int(request.GET.get('limit', 1))
            offset = int(request.GET.get('offset', 0))
            try:
                user = get_object_or_404(User, user_id=user_id)
            except Http404:
                return JsonResponse({"error": ErrorMessage.USER_NOT_REGISTERED}, status=status.HTTP_404_NOT_FOUND)
            reviews = Reviews.objects.filter(user=user)[offset:offset+limit]
            review_serializers = ReviewsSerializer(reviews, many=True)
            return JsonResponse({"message": SuccessMessage.REVIEWS_FETCHED_SUCCESSFULLY, "data": review_serializers.data }, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
