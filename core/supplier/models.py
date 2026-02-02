from django.db import models
from core.adress.models import Address

class Supplier(models.Model):
    class typeChoices(models.TextChoices):
        MANUFACTURER = 'MANUFACTURER', 'Fabricante'
        DISTRIBUTOR = 'DISTRIBUTOR', 'Distribuidor'
        RETAILER = 'RETAILER', 'Varejista'
        IMPORTER = 'IMPORTER', 'Importador'
    
    legal_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=100) # CNPJ or CPF
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=typeChoices.choices)
    
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
class Contact(models.Model):
    business_email = models.EmailField(null=True, blank=True)
    financial_email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"{self.business_email} - {self.financial_email}"