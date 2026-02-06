from rest_framework.viewsets import ModelViewSet
from core.establishment.models import DailyRevenue
from core.establishment.serializers import DailyRevenueSerializer

class DailyRevenueViewSet(ModelViewSet):
  queryset = DailyRevenue.objects.all()
  serializer_class = DailyRevenueSerializer