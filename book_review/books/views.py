from rest_framework.views import APIView
from .serializers import BooksSerializer
from django.http import JsonResponse
from rest_framework import status
from .models import Book
from constant import SuccessMessage, ErrorMessage
from authentication import AuthenticateUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BookView(APIView):

    authentication_classes = (AuthenticateUser,)

    @swagger_auto_schema(
        operation_description="Register Book API",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title'),
                'author': openapi.Schema(type=openapi.TYPE_STRING, description='Author'),
                'genre': openapi.Schema(type=openapi.TYPE_STRING, description='Genre'),
                'summary': openapi.Schema(type=openapi.TYPE_STRING, description='Summary')
            },
            required=['title', 'author', 'genre', 'summary']
        )
    )

    def post(self, request, *args, **kwargs):
        try:
            book_serializer = BooksSerializer(data=request.data)
            if book_serializer.is_valid():
                book_serializer.save()
                return JsonResponse({"message": SuccessMessage.BOOK_ADDED_SUCCESSFULLY, "data": book_serializer.validated_data}, status=status.HTTP_200_OK)
            return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
    @swagger_auto_schema(
        operation_description="books API endpoint with optional parameters",
        manual_parameters=[
            openapi.Parameter(
                'title',
                openapi.IN_QUERY,
                description="Title is an optional parameter.",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'author',
                openapi.IN_QUERY,
                description="Author is an optional parameter.",
                type=openapi.TYPE_STRING,
                required=False
            )
        ]
    )
    def get(self, request, *args, **kwargs):

        try:
            title = request.GET.get('title', None)
            author = request.GET.get('author', None)
            books = Book.objects.all()
            if title:
                books = Book.objects.filter(title__icontains=title)
            if author:
                books = Book.objects.filter(author__icontains=author)
            
            books_data = [{'book_id': book.book_id, 'title': book.title, 'author': book.author} for book in books]
            if books_data:
                return JsonResponse({"message": SuccessMessage.BOOK_DETAILS_FETCHED_SUCCESSFULLY, "data": books_data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": ErrorMessage.BOOK_DETAILS_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookDetailsView(APIView):

    authentication_classes = (AuthenticateUser,)
    
    def get(self, request, *args, **kwargs):
        try:
            book_id = kwargs.get('book_id')
            if not book_id:
                return JsonResponse({"error": ErrorMessage.BOOK_ID_FIELD_IS_MANDATORY}, status=status.HTTP_400_BAD_REQUEST)
            try:
                book = Book.objects.get(book_id=book_id)
                book_data = {'book_id': book.book_id, 'title': book.title, 'author': book.author, 'genre': book.genre, 'summary': book.summary}
                return JsonResponse({"message": SuccessMessage.BOOK_DETAILS_FETCHED_SUCCESSFULLY, "data": book_data}, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return JsonResponse({"message": ErrorMessage.BOOK_DETAILS_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
