from rest_framework.viewsets import ModelViewSet
from core.supplier.models import Supplier, Contact
from core.supplier.serializers import SupplierSerializer, ContactSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['legal_name', 'name', 'document', 'is_active', 'type']
    search_fields = ['legal_name', 'name', 'document']
    http_method_names = ['get', 'post', 'put', 'delete']
    
class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
