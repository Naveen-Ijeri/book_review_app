import uuid
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(default=str(uuid.uuid4()), primary_key=True)
    username = models.CharField(max_length=100)
    encrypted_password = models.CharField(max_length=1000)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.user_id


class UserSessions(models.Model):
    user_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
