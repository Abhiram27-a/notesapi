from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteTests(APITestCase):
    def setUp(self):
        self.note_data = {
            'title': 'Test Note',
            'content': 'This is a test note content.',
        }

    def test_create_note(self):
        response = self.client.post(reverse('note-list'), self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_list_notes(self):
        Note.objects.create(**self.note_data)
        response = self.client.get(reverse('note-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)