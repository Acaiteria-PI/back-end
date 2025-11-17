from django.contrib import admin
from core.establishment.models import Establishment, Combo, FinalCup, Ingredient, Recipient, Stock, CustomCup
# Register your models here.

admin.site.register(Establishment)
admin.site.register(Combo)
admin.site.register(FinalCup)
admin.site.register(Ingredient)
admin.site.register(Recipient)
admin.site.register(Stock)
admin.site.register(CustomCup)