from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Recipient
from core.establishment.serializers import RecipientSerializer

class RecipientViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    http_method_names = ['get', 'post', 'put', 'delete']