from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import FinalCup, Ingredient, Recipient


class TestFinalCupAPI(APITestCase):
    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(
            name='Acai', portion='200', stock='500', price='12', unity='ml'
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Morango', portion='3', stock='100', price='3', unity='un'
        )
        self.recipient = Recipient.objects.create(
            title='Medium recipient', quantity_ml='200', price='15', stock='100', content=self.ingredient1
        )
        self.final_cup = FinalCup.objects.create(
            name="CopoFeito", price="20.00", recipient=self.recipient, ingredient=[self.ingredient1, self.ingredient2]
        )

    def test_final_cup_creation(self):
        url = reverse("api:final-cups-list")
        response = self.client.post(
            url,
            {
                "name": "Copo1",
                "price": "30.00",
                "recipient": self.recipient,
                "ingredient": [self.ingredient1, self.ingredient2],
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FinalCup.objects.count(), 2)
        self.assertEqual(FinalCup.objects.get(id=2).name, "Copo1")

    def test_final_cup_list(self):
        url = reverse("api:final-cups-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Copo1")

    def test_final_cup_detail(self):
        url = reverse("api:final-cups-detail", args=[self.final_cup.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Copo1")

    def test_final_cup_update(self):
        url = reverse("api:final-cups-detail", args=[self.final_cup.id])
        response = self.client.put(
            url,
            {
                "name": "Updated cup",
                "price": "45.00",
                "recipient": self.recipient,
                "ingredient": [self.ingredient1, self.ingredient2],
            },
        )
        self.assertEqual(response.status_code, 200)
        self.final_cup.refresh_from_db()
        self.assertEqual(self.final_cup.name, "Updated cup")