from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import Establishment


# Create your tests here.
class TestEstablishmentAPI(APITestCase):
    def setUp(self):
        self.establishment = Establishment.objects.create(
            name="Wayne Enterprises", cnpj="12345678000195", amount="10000"
        )

    def test_establishment_creation(self):
        url = reverse("api:establishments-list")
        response = self.client.post(
            url,
            {"name": "Test Establishment", "cnpj": "12345678000196", "amount": "5000"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Establishment.objects.count(), 2)
        self.assertEqual(Establishment.objects.get(id=2).name, "Test Establishment")

    def test_establishment_list(self):
        url = reverse("api:establishments-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Wayne Enterprises")

    def test_establishment_detail(self):
        url = reverse("api:establishments-detail", args=[self.establishment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Wayne Enterprises")

    def test_establishment_update(self):
        url = reverse("api:establishments-detail", args=[self.establishment.id])
        response = self.client.put(
            url,
            {
                "name": "Updated Establishment",
                "cnpj": "12345678000197",
                "amount": "2000",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.establishment.refresh_from_db()
        self.assertEqual(self.establishment.name, "Updated Establishment")
