from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import FinalCup, Ingredient, Recipient
from core.establishment.tests.setups.setup_final_cup import setUpFinalCup


class TestFinalCupAPI(APITestCase):
    def setUp(self):
        setUpFinalCup(self)

    def test_final_cup_creation(self):
        url = reverse("api:final-cups-list")
        response = self.client.post(
            url,
            {
                "name": "CopoFeito",
                "price": "30.00",
                "recipient": self.recipient.id,
                "ingredient": [self.ingredient1.id, self.ingredient2.id],
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FinalCup.objects.count(), 2)
        self.assertEqual(FinalCup.objects.get(id=2).name, "CopoFeito")

    def test_final_cup_list(self):
        url = reverse("api:final-cups-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "CopoFeito")

    def test_final_cup_detail(self):
        url = reverse("api:final-cups-detail", args=[self.final_cup.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "CopoFeito")

    def test_final_cup_update(self):
        url = reverse("api:final-cups-detail", args=[self.final_cup.id])
        response = self.client.put(
            url,
            {
                "name": "Updated cup",
                "price": "45.00",
                "recipient": self.recipient.id,
                "ingredient": [self.ingredient1.id, self.ingredient2.id],
            },
        )
        self.assertEqual(response.status_code, 200)
        self.final_cup.refresh_from_db()
        self.assertEqual(self.final_cup.name, "Updated cup")