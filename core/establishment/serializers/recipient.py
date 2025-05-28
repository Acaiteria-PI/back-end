from rest_framework.serializers import ModelSerializer
from core.establishment.models import Recipient

class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'id',
            'title',
            'quantity_ml',
            'price',
            'stock',
            'content',
        ]
        read_only_fields = ['id']