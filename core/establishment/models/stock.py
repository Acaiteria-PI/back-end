from django.db import models
from core.establishment.models import Ingredient
from core.supplier.models import Supplier

class Stock(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    batch = models.CharField(max_length=100)
    expiration_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True, blank=True)
    batch_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.ingredient.name} - {self.batch}"