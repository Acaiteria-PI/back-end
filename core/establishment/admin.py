from django.contrib import admin
from core.establishment.models import Establishment, Combo, FinalCup, Ingredient, Recipient 
# Register your models here.

admin.site.register(Establishment)
admin.site.register(Combo)
admin.site.register(FinalCup)
admin.site.register(Ingredient)
admin.site.register(Recipient)