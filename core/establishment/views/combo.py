from rest_framework.viewsets import ModelViewSet
from core.establishment.models import Combo
from core.establishment.serializers import ComboSerializer
from rest_framework.filters import SearchFilter

class ComboViewSet(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    http_method_names = ['get', 'post', 'put', 'delete']
