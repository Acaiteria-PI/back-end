from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    portion = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    unit_of_measure = models.CharField(max_length=20, default="g")

    def __str__(self):
        return self.name