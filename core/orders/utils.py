from decimal import Decimal
from django.db import transaction
from core.establishment.models import Stock


@transaction.atomic
def reduce_stock_by_ingredient(ingredient, required_quantity):
    
    remaining = Decimal(required_quantity)

    stocks = Stock.objects.filter(
        ingredient=ingredient,
        quantity__gt=0
    ).order_by('expiration_date')

    if not stocks.exists():
        raise Exception(f"Estoque indisponível para {ingredient.name}")

    for stock in stocks:
        if remaining <= 0:
            break

        if stock.quantity >= remaining:
            stock.quantity -= remaining
            stock.save(update_fields=['quantity'])
            remaining = 0
        else:
            remaining -= stock.quantity
            stock.quantity = 0
            stock.save(update_fields=['quantity'])

    if remaining > 0:
        raise Exception(
            f"Estoque insuficiente para {ingredient.name}. Faltaram {remaining}"
        )

def process_order_stock(order):
    for item in order.items.all():

        # ✅ FINAL CUP
        if item.type == 'FINAL_CUP' and item.final_cup:
            for ingredient in item.final_cup.ingredient.all():
                total_needed = ingredient.portion * item.quantity
                reduce_stock_by_ingredient(ingredient, total_needed)

        # ✅ CUSTOM CUP
        elif item.type == 'CUSTOM_CUP' and item.custom_cup:
            for ingredient in item.custom_cup.ingredient.all():
                total_needed = ingredient.portion * item.quantity
                reduce_stock_by_ingredient(ingredient, total_needed)

        # ✅ COMBO
        elif item.type == 'COMBO' and item.combo:

            for final_cup in item.combo.final_cup.all():
                for ingredient in final_cup.ingredient.all():
                    total_needed = ingredient.portion * item.quantity
                    reduce_stock_by_ingredient(ingredient, total_needed)
