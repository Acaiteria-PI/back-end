from core.establishment.models import CustomCup, Ingredient, Recipient
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from core.establishment.serializers import IngredientSerializer, RecipientSerializer


class CustomCupSerializer(ModelSerializer):
    ingredient = PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), many=True)
    recipient = PrimaryKeyRelatedField(queryset=Recipient.objects.all())
    
    ingredient_data = IngredientSerializer(source="ingredient", read_only=True, many=True)
    recipient_data = RecipientSerializer(source="recipient", read_only=True, many=False)
    
    class Meta:
        model = CustomCup
        fields = ["id", "recipient", "recipient_data", "ingredient", "ingredient_data", "price"]
        read_only_fields = ["id", "price"]
