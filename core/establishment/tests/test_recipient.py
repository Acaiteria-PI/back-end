from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from core.establishment.models import Recipient


class TestRecipientAPI(APITestCase):
    def setUp(self):
        self.recipient = Recipient.objects.create(
            quantity_ml="10",
            price="15.00",
            title="Medium recipient",
            stock="5",
            content="2",
        )

    def test_recipient_creation(self):
        url = reverse("api:recipients-list")
        response = self.client.post(
            url,
            {
                "quantity_ml": "20",
                "price": "30.00",
                "title": "Large recipient",
                "stock": "10",
                "content": "5",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Recipient.objects.count(), 2)
        self.assertEqual(Recipient.objects.get(id=2).title, "Large recipient")

    def test_recipient_list(self):
        url = reverse("api:recipients")
        response = self.client.get(url)
        self.assertEqual(response.status.code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Medium recipient")

    def test_recipient_detail(self):
        url = reverse("api:recipients-detail", args=[self.recipient.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Medium recipient")

    def test_recipient_update(self):
        url = reverse("api:recipients-detail", args=[self.recipient.id])
        response = self.client.put(
            url,
            {
                "quantity_ml": "25",
                "price": "35.00",
                "title": "Large recipient",
                "stock": "12",
                "content": "5",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.recipient.refresh_from_db()
        self.assertEqual(self.recipient.name, 'Large recipient')
