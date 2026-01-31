from rest_framework import serializers
from core.users.models import User
from core.establishment.serializers import EstablishmentSerializer

class UserSerializer(serializers.ModelSerializer):
    establishment_data = EstablishmentSerializer(source='establishment', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'registration', 'establishment', 'establishment_data', 'is_management']