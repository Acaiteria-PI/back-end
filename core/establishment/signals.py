from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from core.establishment.models import CustomCup


def calculate_price(instance):
    total_price = 0

    total_price += instance.recipient.price

    for ingredient in instance.ingredient.all():
        total_price += ingredient.price

    return total_price

@receiver(m2m_changed, sender=CustomCup.ingredient.through)
def calculate_custom_cup_price(sender, instance, action, **kwargs):
    print(f"Action: {action}")
    
    if action in ['post_add', 'post_remove', 'post_clear'] and not hasattr(instance, '_skip_price_update'):    
        
        total_price = calculate_price(instance)

        instance.price = total_price
        instance._skip_price_update = True
        instance.save(update_fields=['price'])
        
        if hasattr(instance, '_skip_price_update'):
            del instance._skip_price_update
            
@receiver(post_save, sender=CustomCup)
def update_custom_cup_price_on_recipient_change(sender, instance, created, **kwargs):
    print(f"Post Save Signal Triggered for CustomCup ID: {instance.id}")
    
    if created or hasattr(instance, '_skip_price_update'):
        return
    
    total_price = calculate_price(instance)
    
    instance.price = total_price
    instance._skip_price_update = True
    instance.save(update_fields=['price'])
    
    if hasattr(instance, '_skip_price_update'):
        del instance._skip_price_update