from rest_framework.serializers import ModelSerializer
from core.establishment.serializers.final_cup import FinalCupSerializer
from core.establishment.models import Combo

class ComboSerializer(ModelSerializer):
    final_cup_data = FinalCupSerializer(source='final_cup', read_only=True, many=True)

    class Meta:
        model = Combo
        fields = ['id', 'name', 'price', 'final_cup', 'final_cup_data']
        read_only_fields = ['id']