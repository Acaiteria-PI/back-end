from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from core.establishment.models import CustomCup
from core.orders.models import Order
from core.establishment.models import DailyRevenue


def calculate_price(instance):
    total_price = 0

    total_price += instance.recipient.price

    for ingredient in instance.ingredient.all():
        total_price += ingredient.price

    return total_price


@receiver(m2m_changed, sender=CustomCup.ingredient.through)
def calculate_custom_cup_price(sender, instance, action, **kwargs):
    print(f"Action: {action}")

    if action in ["post_add", "post_remove", "post_clear"] and not hasattr(
        instance, "_skip_price_update"
    ):

        total_price = calculate_price(instance)

        instance.price = total_price
        instance._skip_price_update = True
        instance.save(update_fields=["price"])

        if hasattr(instance, "_skip_price_update"):
            del instance._skip_price_update


@receiver(post_save, sender=CustomCup)
def update_custom_cup_price_on_recipient_change(sender, instance, created, **kwargs):
    print(f"Post Save Signal Triggered for CustomCup ID: {instance.id}")

    if created or hasattr(instance, "_skip_price_update"):
        return

    total_price = calculate_price(instance)

    instance.price = total_price
    instance._skip_price_update = True
    instance.save(update_fields=["price"])

    if hasattr(instance, "_skip_price_update"):
        del instance._skip_price_update


# Daily revenue signal


def create_daily_revenue(amount, order):
    DailyRevenue.objects.create(
        total_amount=amount, total_orders_count=1, establishment=order.establishment
    )


def sum_amount_to_daily_revenue(daily_revenue, amount):
    daily_revenue.total_amount += amount
    daily_revenue.total_orders_count += 1
    daily_revenue.save()


@receiver(pre_save, sender=Order)
def mark_payment_transition(sender, instance, **kwargs):
    if not instance.pk:
        instance._became_paid = False
        return
    
    old = Order.objects.get(pk=instance.pk)

    old_was_paid = old.is_paid
    new_is_paid = instance.is_paid

    if old_was_paid is False and new_is_paid is True:
        instance._became_paid = True
    else: instance._became_paid = False


@receiver(post_save, sender=Order)
def register_daily_revenue(sender, instance, **kwargs):
    if not getattr(instance, "_became_paid", False):
        print("Order didnt get paid or was already paid.")
        return

    else:
        daily_revenues = DailyRevenue.objects.filter(establishment=instance.establishment)

        if len(daily_revenues) > 0:
            matched = False
            for daily_revenue in daily_revenues:
                if daily_revenue.date.date() == instance.order_date.date():
                    print("Sum")
                    sum_amount_to_daily_revenue(daily_revenue, instance.total_amount)
                    matched = True
                    break # Stops the loop, so it doesnt keep checking other rows

            if not matched:
                print("No revenues today, creating one.")
                return create_daily_revenue(instance.total_amount, instance)
            
        else:
            print("No revenues created, creating one.")
            return create_daily_revenue(instance.total_amount, instance)
