from rest_framework.serializers import ModelSerializer

from core.establishment.models import FinalCup


class FinalCupSerializer(ModelSerializer):
    class Meta:
        model = FinalCup
        fields = ["name", "price", "recipient", "ingredient"]
        read_only_fields = ["id"]
