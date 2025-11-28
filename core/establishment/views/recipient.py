from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Recipient
from core.establishment.serializers import RecipientSerializer
from rest_framework.filters import SearchFilter

class RecipientViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    http_method_names = ['get', 'post', 'put', 'delete']