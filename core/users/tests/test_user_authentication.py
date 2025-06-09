from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.users.models import User


# Create your tests here.
class TestUserAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="user@example.com", password="userpassword"
        )
        
    def authenticate_client(self):
        url = reverse("token_obtain_pair")  # ou o caminho real da sua rota JWT
        response = self.client.post(url, {
            "email": "user@example.com",
            "password": "userpassword"
        })
        self.assertEqual(response.status_code, 200)
        access_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    
    def test_user_creation(self):
        url = reverse("api:users-list")
        
        response = self.client.post(
            url,
            {"name": "testuser", "password": "testpassword", "email": "testuser@example.com"},
        )
        self.assertEqual(response.status_code, 401)
        
        self.authenticate_client()
        response = self.client.post(
            url,
            {"name": "testuser", "password": "testpassword", "email": "testuser@example.com"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(id=2).name, "testuser")

    def test_user_list(self):
        url = reverse("api:users-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["email"], "user@example.com")

    def test_user_detail(self):
        url = reverse("api:users-detail", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], "user@example.com")

    def test_user_update(self):
        url = reverse("api:users-detail", args=[self.user.id])
        response = self.client.put(
            url,
            {
                "name": "Updated User",
                "email": "updateduser@example.com",
            },
        )
        self.assertEqual(response.status_code, 401)
        
        self.authenticate_client()
        response = self.client.put(
            url,
            {
                "name": "Updated User",
                "email": "updateduser@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, "Updated User")
