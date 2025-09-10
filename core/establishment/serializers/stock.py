from rest_framework import serializers
from core.establishment.models import Stock, Ingredient


class StockSerializer(serializers.ModelSerializer):
    # accept ingredient as PK for writes
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())

    class Meta:
        model = Stock
        fields = ['id', 'ingredient', 'quantity', 'batch', 'expiration_date', 'supplier', 'batch_price', 'unit_of_measure']
        read_only_fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # present ingredient as its name in responses to match tests
        try:
            data['ingredient'] = instance.ingredient.name
        except Exception:
            pass
        return data