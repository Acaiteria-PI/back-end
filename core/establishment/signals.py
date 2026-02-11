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


def subtract_revenue_when_order_canceled(daily_revenue, amount):
    daily_revenue.total_amount -= amount
    daily_revenue.total_orders_count -= 1
    daily_revenue.save()


@receiver(pre_save, sender=Order)
def mark_payment_and_status_transition(sender, instance, **kwargs):
    if not instance.pk:
        instance._became_paid = False
        instance._became_canceled = False
        return

    old = Order.objects.get(pk=instance.pk)

    # PAYMENT TRANSITION
    old_was_paid = old.is_paid
    new_is_paid = instance.is_paid

    if old_was_paid is False and new_is_paid is True:
        instance._became_paid = True
    else:
        instance._became_paid = False

    # STATUS TRANSITION
    if old.status != "CANCELED" and instance.status == "CANCELED":
        instance._became_canceled = True
    else:
        instance._became_canceled = False


def handle_paid_transition(instance):
    if not getattr(instance, "_became_paid", False):
        return

    else:
        daily_revenues = DailyRevenue.objects.filter(
            establishment=instance.establishment
        )

        if len(daily_revenues) > 0:
            matched = False
            for daily_revenue in daily_revenues:
                if daily_revenue.date.date() == instance.order_date.date():
                    sum_amount_to_daily_revenue(daily_revenue, instance.total_amount)
                    matched = True
                    break  # Stops the loop, so it doesnt keep checking other rows

            if not matched:
                return create_daily_revenue(instance.total_amount, instance)

        else:
            return create_daily_revenue(instance.total_amount, instance)


def handle_canceled_transition(instance):
    if not getattr(instance, "_became_canceled", False):
        return

    order_revenue_register = DailyRevenue.objects.filter(
        establishment=instance.establishment, date__date=instance.order_date.date()
    ).first()

    if order_revenue_register is None:
        return

    else:
        subtract_revenue_when_order_canceled(order_revenue_register, instance.total_amount)


@receiver(post_save, sender=Order)
def register_daily_revenue(sender, instance, **kwargs):
    if getattr(instance, "_became_canceled", False):
        handle_canceled_transition(instance)
    elif getattr(instance, "_became_paid", False):
        handle_paid_transition(instance)