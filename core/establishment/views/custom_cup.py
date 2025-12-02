from rest_framework.viewsets import ModelViewSet

from core.establishment.models import CustomCup
from core.establishment.serializers import CustomCupSerializer


class CustomCupViewSet(ModelViewSet):
    queryset = CustomCup.objects.all()
    serializer_class = CustomCupSerializer
    http_method_names = ["get", "post", "put", "delete"]
