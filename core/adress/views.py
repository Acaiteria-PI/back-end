from rest_framework.viewsets import ModelViewSet
from core.adress.models import Address
from core.adress.serializers import AddressSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['street', 'city', 'state']
    search_fields = ['street', 'city', 'state']
    http_method_names = ['get', 'post', 'put', 'delete']
