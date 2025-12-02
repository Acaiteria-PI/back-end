from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from core.orders.models import OrderItem, Order
from core.orders.utils import process_order_stock

@receiver(post_save, sender=OrderItem)
def update_order_total_on_item_change(sender, instance, **kwargs):
    print(f"Post Save Signal Triggered for OrderItem ID: {instance.id}")
    if not hasattr(instance, '_skip_order_update'):
        print(f"Calculating prices for OrderItem and updating Order total. {instance.type}")
        if instance.type == 'COMBO' and instance.combo:
            item_price = instance.combo.price
        elif instance.type == 'FINAL_CUP' and instance.final_cup:
            item_price = instance.final_cup.price
        elif instance.type == 'CUSTOM_CUP' and instance.custom_cup:
            item_price = instance.custom_cup.price
        else:
            item_price = 0
        
        instance.unit_price = item_price
        instance.total_price = item_price * instance.quantity
        instance._skip_order_update = True
        
        instance.save(update_fields=['unit_price', 'total_price'])
        
        if hasattr(instance, '_skip_order_update'):
            del instance._skip_order_update
            
        order = instance.order
        total_amount = sum(item.total_price for item in order.items.all())
        order.total_amount = total_amount

        order.save(update_fields=['total_amount'])
    
@receiver(post_save, sender=Order)
def update_stock_in_progress(sender, instance, created, **kwargs):

    if instance.status != Order.statusChoices.IN_PROGRESS:
        return

    if hasattr(instance, '_stock_already_processed'):
        return

    try:
        instance._stock_already_processed = True
        process_order_stock(instance)
    finally:
        del instance._stock_already_processed