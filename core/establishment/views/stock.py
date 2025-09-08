from rest_framework.viewsets import ModelViewSet

from core.establishment.models import Stock
from core.establishment.serializers import StockSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    http_method_names = ['get', 'post', 'put', 'delete']