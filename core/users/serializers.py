from rest_framework import serializers
from core.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'registration', 'establishment', 'is_management']