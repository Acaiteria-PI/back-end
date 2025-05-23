from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Establishment
from core.establishment.serializers import EstablishmentSerializer

class EstablishmentViewSet(ModelViewSet):
    """
    A viewset for viewing and editing establishment instances.
    """
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']