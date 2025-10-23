from core.establishment.models import FinalCup
from rest_framework.serializers import ModelSerializer
from core.establishment.serializers import IngredientSerializer, RecipientSerializer


class FinalCupSerializer(ModelSerializer):
    ingredient_data = IngredientSerializer(source="ingredient", read_only=True, many=True)
    recipient_data = RecipientSerializer(source="recipient", read_only=True)
    
    class Meta:
        model = FinalCup
        fields = ["name", "price", "recipient", "recipient_data", "ingredient", "ingredient_data"]
        read_only_fields = ["id"]
