from django.db import models

from core.establishment.models import Ingredient
from core.establishment.models import Recipient

class FinalCup(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recipient = models.ForeignKey(Recipient, on_delete=models.PROTECT, related_name='final_cups')
    ingredient = models.ManyToManyField(Ingredient, related_name='final_cups')

    def __str__(self):
        return self.name