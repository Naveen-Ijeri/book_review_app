from django.db import models
import uuid
from auth_app.models import User
from books.models import Book


class Reviews(models.Model):
    review_id = models.CharField(default=str(uuid.uuid4()), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
