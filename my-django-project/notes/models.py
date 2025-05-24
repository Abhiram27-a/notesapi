# notes/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's User model

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes') # New field
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title