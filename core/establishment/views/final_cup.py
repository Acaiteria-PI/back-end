from rest_framework.viewsets import ModelViewSet

from core.establishment.models import FinalCup
from core.establishment.serializers import FinalCupSerializer

from rest_framework.filters import SearchFilter


class FinalCupViewSet(ModelViewSet):
    queryset = FinalCup.objects.all()
    serializer_class = FinalCupSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "ingredient"]
    http_method_names = ["get", "post", "put", "delete"]
