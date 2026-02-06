from rest_framework import serializers
from core.establishment.models import DailyRevenue

class DailyRevenueSerializer(serializers.ModelSerializer):
  class Meta:
    model = DailyRevenue
    fields = ["date", "total_amount", "total_orders_count", "establishment"]