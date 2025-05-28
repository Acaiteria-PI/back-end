from django.db import models
from core.establishment.models import Ingredient

class Recipient(models.Model):
    title = models.CharField(max_length=45)
    quantity_ml = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    content = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='recipients')

    def __str__(self):
        return self.title