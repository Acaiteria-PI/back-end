from django.db import models
from core.users.models import User
from core.establishment.models import Establishment, FinalCup, Combo, CustomCup



class Order(models.Model):
    class statusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        IN_PROGRESS = 'IN_PROGRESS', 'Em Preparo'
        COMPLETED = 'COMPLETED', 'Concluído'
        CANCELED = 'CANCELED', 'Cancelado'
    
    status = models.CharField(max_length=20, choices=statusChoices.choices, default=statusChoices.PENDING)
    customer = models.CharField(max_length=45)
    order_date = models.DateTimeField(auto_now_add=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.DO_NOTHING)
    responsible_person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    is_paid = models.BooleanField(default=False)
    
    
class OrderItem(models.Model):
    class typeChoices(models.TextChoices):
        FINAL_CUP = 'FINAL_CUP', 'Copo Pronto'
        CUSTOM_CUP = 'CUSTOM_CUP', 'Copo Customizado'
        COMBO = 'COMBO', 'Combo'
    
    type = models.CharField(max_length=20, choices=typeChoices.choices)
    final_cup = models.ForeignKey(FinalCup, null=True, blank=True, on_delete=models.SET_NULL)
    custom_cup = models.ForeignKey(CustomCup, null=True, blank=True, on_delete=models.SET_NULL)
    combo = models.ForeignKey(Combo, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unity_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)
