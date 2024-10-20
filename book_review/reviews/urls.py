from django.urls import path
from .views import BooksCreateReviews, BooksUserReviews

urlpatterns = [
    path('books/<str:book_id>/reviews', BooksCreateReviews.as_view(), name="book_create_reviews"),
    path('users/<str:user_id>/reviews', BooksUserReviews.as_view(), name="book_user_reviews"),    
]