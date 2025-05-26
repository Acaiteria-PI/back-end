from rest_framework import serializers
from core.establishment.models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'portion', 'stock', 'price', 'unit']
        read_only_fields = ['id']