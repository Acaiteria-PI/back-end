from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .models import Establishment
# Create your tests here.

class EstablishmentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.establishment = Establishment.objects.create(
            name="Test Establishment",
            cnpj="12345678000195",
            amount="3000"
        )

    def test_establishment_creation(self):
        url = reverse('establishments')
        response = self.client.post(url, {
            'name': 'New Establishment',
            'cnpj': '12345678000196',
            'amount': '5000'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Establishment.objects.count(), 2)
        self.assertEqual(Establishment.objects.get(id=2).name, 'New Establishment')
        
    def test_establishment_list(self):
        url = reverse('establishments')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Establishment')
        
    def test_establishment_detail(self):
        url = reverse('establishment-detail', args=[self.establishment.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Establishment')
        
    def test_establishment_update(self):
        url = reverse('establishments', args=[self.establishment.id])
        response = self.client.put(url, {
            'name': 'Updated Establishment',
            'cnpj': '12345678000197',
            'amount': '2000'
        })
        self.assertEqual(response.status_code, 200)
        self.establishment.refresh_from_db()
        self.assertEqual(self.establishment.name, 'Updated Establishment')
        
        
