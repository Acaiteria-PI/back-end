from rest_framework.viewsets import ModelViewSet
from core.establishment.models import Combo
from core.establishment.serializers import ComboSerializer

class ComboViewSet(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    http_method_names = ['get', 'post', 'put', 'delete']