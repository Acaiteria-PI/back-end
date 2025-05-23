from rest_framework import serializers
from core.establishment.models import Establishment

class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ['id', 'name', 'cnpj', 'amount']
        read_only_fields = ['id']