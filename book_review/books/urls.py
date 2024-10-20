from django.urls import path
from .views import BookView, BookDetailsView

urlpatterns = [
    path('books', BookView.as_view(), name="book_view"), 
    path('books/<str:book_id>', BookDetailsView.as_view(), name="book_details_view")
]