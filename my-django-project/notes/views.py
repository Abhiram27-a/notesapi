from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Note
from .serializers import NoteSerializer


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]  # Enable search
    search_fields = ['title', 'content'] 

    def get_queryset(self):
        # Only return notes for the authenticated user, ordered by creation date
        return Note.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Save the note with the current user as the owner
        serializer.save(user=self.request.user)


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow the user to access their own notes
        return Note.objects.filter(user=self.request.user)
