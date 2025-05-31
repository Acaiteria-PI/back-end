from rest_framework.viewsets import ModelViewSet

from core.establishment.models import FinalCup
from core.establishment.serializers import FinalCupSerializer


class FinalCupViewSet(ModelViewSet):
    queryset = FinalCup.objects.all()
    serializer_class = FinalCupSerializer
    http_method_names = ["get", "post", "put", "delete"]
