from rest_framework import serializers
from core.establishment.models import FinalCup, Ingredient
from rest_framework.serializers import ModelSerializer
from core.establishment.serializers import IngredientSerializer


class FinalCupSerializer(ModelSerializer):
    ingredient_data = IngredientSerializer(source="ingredient", read_only=True, many=True)
    
    class Meta:
        model = FinalCup
        fields = ["name", "price", "recipient", "ingredient", "ingredient_data"]
        read_only_fields = ["id"]
