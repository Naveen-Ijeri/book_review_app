from django.db import models
import uuid


class Book(models.Model):
    book_id = models.CharField(default=str(uuid.uuid4()), primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

