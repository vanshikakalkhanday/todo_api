from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Note

class NoteAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="vvanshi",
            password="testpassword123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.token.key}"
        )
        self.note = Note.objects.create(
            user=self.user,
            title="Initial Note",
            description="Initial Description",
            completed=False
        )
        
    def test_get_notes(self):
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        data = {
            "title": "New Note",
            "description": "Created via test",
            "completed": False
        }
        response = self.client.post("/api/notes/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_note(self):
        data = {
            "title": "Updated Title",
            "completed": True
        }
        response = self.client.put(
            f"/api/notes/{self.note.id}/",
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        response = self.client.delete(
            f"/api/notes/{self.note.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_access(self):
        self.client.credentials()
        response = self.client.get("/api/notes/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
