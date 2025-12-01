from rest_framework import serializers
from core.establishment.models import Stock, Ingredient
from core.establishment.serializers import IngredientSerializer


class StockSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    ingredient_data = IngredientSerializer(source="ingredient", read_only=True)

    class Meta:
        model = Stock
        fields = [
            "id",
            "ingredient",
            "ingredient_data",
            "quantity",
            "batch",
            "expiration_date",
            "supplier",
            "batch_price",
        ]
        read_only_fields = ["id"]
