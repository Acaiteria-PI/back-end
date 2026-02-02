from rest_framework.serializers import ModelSerializer
from core.adress.models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'city', 'state', 'zip_code']