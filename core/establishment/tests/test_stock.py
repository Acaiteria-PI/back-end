from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import Stock
from core.establishment.tests.setups.setup_final_cup import setUpFinalCup
from core.establishment.tests.setups.setup_user import setUpUser


class TestFinalCupAPI(APITestCase):
    def setUp(self):
        setUpFinalCup(self)
        setUpUser(self)

    def test_stock_creation(self):
        url = reverse("api:stock-list")
        response = self.client.post(
            url,
            {
                "ingredient": self.ingredient1.id,
                "quantity": "30",
                "batch": "Batch123",
                "expiration_date": "2024-12-31",
                "supplier": "Supplier A",
                "unit_of_measure": "grams",
                "batch_price": "100.00",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Stock.objects.count(), 2)
        self.assertEqual(Stock.objects.get(id=2).ingredient.name, "Ingredient 1")

    def test_stock_list(self):
        url = reverse("api:stock-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["ingredient"], "Ingredient 1")

    def test_stock_detail(self):
        url = reverse("api:stock-detail", args=[self.stock.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["ingredient"], "Ingredient 1")

    def test_stock_update(self):
        url = reverse("api:stock-detail", args=[self.stock.id])
        response = self.client.put(
            url,
            {
                "ingredient": self.ingredient1.id,
                "quantity": "40",
                "batch": "Batch456",
                "expiration_date": "2025-12-31",
                "supplier": "Supplier B",
                "unit_of_measure": "grams",
                "batch_price": "120.00",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.stock.refresh_from_db()
        self.assertEqual(self.stock.quantity, 40)