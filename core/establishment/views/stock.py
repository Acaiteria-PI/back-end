from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.establishment.models import Stock
from core.establishment.serializers import StockSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        stock_items = Stock.objects.filter(quantity__lt = 15)
        serializer = self.get_serializer(stock_items, many=True)
        return Response(serializer.data)