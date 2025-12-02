from rest_framework import serializers
from core.establishment.models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'portion', 'price', 'unit_of_measure', 'is_addon']
        read_only_fields = ['id']