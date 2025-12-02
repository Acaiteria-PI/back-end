from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from core.establishment.models import Combo
from core.establishment.tests.setups.setup_final_cup import setUpFinalCup


class TestComboAPI(APITestCase):
    def setUp(self):
        setUpFinalCup(self)

        self.combo = Combo.objects.create(name="Combo1", price="45.00")
        self.combo.final_cup.set([self.final_cup])
    
    def test_combo_creation(self):
        url = reverse("api:combos-list")
        response = self.client.post(
            url,
            {
                "name": "Combo1",
                "price": "50.00",
                "final_cup":[self.final_cup.id],
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Combo.objects.count(), 2)
        self.assertEqual(Combo.objects.get(id=2).name, "Combo1")

    def test_combo_list(self):
        url = reverse("api:combos-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0] ["name"], "Combo1")

    def test_combo_detail(self):
        url = reverse("api:combos-detail", args=[self.final_cup.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Combo1")

    def test_combo_update(self):
        url = reverse("api:combos-detail", args=[self.combo.id])
        response = self.client.put(
            url,
            {
                "name": "Updated combo",
                "price": "60.00",
                "final_cup": [self.final_cup.id],
            },
        )
        self.assertEqual(response.status_code, 200)
        self.combo.refresh_from_db()
        self.assertEqual(self.combo.name, "Updated combo")