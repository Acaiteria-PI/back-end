from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Establishment
from core.establishment.serializers import EstablishmentSerializer

from rest_framework.filters import SearchFilter

class EstablishmentViewSet(ModelViewSet):
    """
    A viewset for viewing and editing establishment instances.
    """
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    http_method_names = ['get', 'post', 'put', 'delete']