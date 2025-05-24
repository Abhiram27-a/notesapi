# notes/serializers.py

from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # fields = '__all__' # Don't use __all__ anymore if user should be read-only
        fields = ['id', 'title', 'content', 'created_at', 'user'] # Explicitly list fields
        read_only_fields = ['user', 'created_at'] # User and created_at are set by the system
        # Or even exclude 'user' from fields and set it in the view's perform_create
# notes/serializers.py (Alternative, cleaner)

from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at'] # User is implied by context, not exposed directly
        read_only_fields = ['created_at'] # created_at is still auto-set        