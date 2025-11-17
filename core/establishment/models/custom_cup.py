from django.db import models

from core.establishment.models import Ingredient
from core.establishment.models import Recipient

class CustomCup(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0.00, blank=True)
    recipient = models.ForeignKey(Recipient, on_delete=models.PROTECT, related_name='custom_cups')
    ingredient = models.ManyToManyField(Ingredient, related_name='custom_cups')

    def __str__(self):
        return f"CustomCup {self.id}"
    