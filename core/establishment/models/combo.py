from django.db import models
from core.establishment.models import FinalCup

class Combo(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    final_cup = models.ManyToManyField(FinalCup, related_name='combos')
