from django.db import models
from core.establishment.models import Establishment

class DailyRevenue(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  total_orders_count = models.IntegerField()
  establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

  def __str__(self):
    return f"Total amount: {self.total_amount}"