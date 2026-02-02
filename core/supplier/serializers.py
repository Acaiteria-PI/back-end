from rest_framework.serializers import ModelSerializer
from core.supplier.models import Supplier, Contact

class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'legal_name', 'name', 'document', 'is_active', 'type', 'contact', 'address']
        depth = 1
        
class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'business_email', 'financial_email', 'phone_number', 'whatsapp_number']