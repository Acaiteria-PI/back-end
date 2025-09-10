from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import Ingredient


class TestIngredientAPI(APITestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name="Morango", portion="4", price="3.50", unit_of_measure="g"
        )

    def test_ingredient_creation(self):
        url = reverse("api:ingredients-list")
        response = self.client.post(
            url,
            {
                "name": "Test Ingredient",
                "portion": "5",
                "price": "4.50",
                "unit_of_measure": "g",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ingredient.objects.count(), 2)
        self.assertEqual(Ingredient.objects.get(id=2).name, "Test Ingredient")

    def test_ingredient_list(self):
        url = reverse("api:ingredients-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Morango")

    def test_ingredient_detail(self):
        url = reverse("api:ingredients-detail", args=[self.ingredient.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Morango")

    def test_ingredient_update(self):
        url = reverse("api:ingredients-detail", args=[self.ingredient.id])
        response = self.client.put(
            url,
            {
                "name": "Updated Ingredient",
                "portion": "8",
                "price": "1.00",
                "unit_of_measure": "g",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.ingredient.refresh_from_db()
        self.assertEqual(self.ingredient.name, "Updated Ingredient")
