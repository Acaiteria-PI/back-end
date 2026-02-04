from rest_framework.serializers import ModelSerializer
from core.supplier.models import Supplier, Contact
from core.adress.serializers import AddressSerializer

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'business_email', 'financial_email', 'phone_number', 'whatsapp_number']

class SupplierSerializer(ModelSerializer):
    address_data = AddressSerializer(source='address', read_only=True)
    contact_data= ContactSerializer(source='contact', read_only=True)
    class Meta:
        model = Supplier
        fields = ['id', 'legal_name', 'name', 'document', 'is_active', 'type', 'contact', 'address', 'contact_data', 'address_data']
        