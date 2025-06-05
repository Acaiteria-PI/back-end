from rest_framework.serializers import ModelSerializer
from core.establishment.models import Combo

class ComboSerializer(ModelSerializer):
    class Meta:
        model = Combo
        fields = ['name', 'price', 'final_cup']
        read_only_fields = ['id']