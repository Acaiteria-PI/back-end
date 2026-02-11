from decimal import Decimal
from datetime import timedelta

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from core.establishment.models import Establishment, DailyRevenue
from core.orders.models import Order


class RegisterDailyRevenueSignalTests(TestCase):
    def setUp(self):
        self.establishment = Establishment.objects.create(
            name="Pe de acai",
            cnpj="12345678901234",
            amount=Decimal("0.00"),
        )
        User = get_user_model()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="test1234",
            name="Tester",
            establishment=self.establishment,
        )

    # === PAID TRANSITIONS ===

    def test_create_daily_revenue_on_first_order(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        order.is_paid = True
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_amount, Decimal("10.00"))
        self.assertEqual(daily.total_orders_count, 1)

    def test_aggregates_when_daily_revenue_already_created(self):

        order1 = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )
        order2 = Order.objects.create(
            customer="Bruno",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("5.00"),
            is_paid=False,
        )

        order1.is_paid = True
        order1.save()
        order2.is_paid = True
        order2.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_amount, Decimal("15.00"))
        self.assertEqual(daily.total_orders_count, 2)

    def test_not_updating_order_payment_status(self):
        # Should not create a daily revenue register
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        self.assertEqual(
            DailyRevenue.objects.filter(establishment=self.establishment).count(), 0
        )

    def test_edit_already_paid_order(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        order.is_paid = True
        order.save()
        # One more patch operation (shouldnt register one more orders_count)
        order.is_paid = True
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_amount, Decimal("10.00"))
        self.assertEqual(daily.total_orders_count, 1)

    def test_not_paid_to_not_paid_order(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        order.is_paid = False
        order.save()

        self.assertEqual(
            DailyRevenue.objects.filter(establishment=self.establishment).count(), 0
        )

    def test_create_daily_revenue_in_another_day(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        order.is_paid = True
        order.save()

        another_day_order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            is_paid=False,
        )

        another_day_order.order_date = timezone.now() + timedelta(days=1)
        another_day_order.is_paid = True
        another_day_order.save()

        self.assertEqual(
            DailyRevenue.objects.filter(establishment=self.establishment).count(), 2
        )

    # === CANCELED TRANSITIONS ===

    def test_does_not_subtract_when_order_not_canceled(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            status="PENDING",
            is_paid=False,
        )

        order.is_paid = True
        order.status = "IN_PROGRESS"
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("10.00"))

        order.status = "COMPLETED"
        order.save()

        daily.refresh_from_db()
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("10.00"))

    def test_subtracts_once_when_status_changes_to_canceled(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            status="PENDING",
            is_paid=False,
        )
        order2 = Order.objects.create(
            customer="Pedro",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("20.00"),
            status="PENDING",
            is_paid=False,
        )

        order.is_paid = True
        order.status = "IN_PROGRESS"
        order.save()
        order2.is_paid = True
        order2.status = "IN_PROGRESS"
        order2.save()

        order.status = "CANCELED"
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("20.00"))

    def test_does_not_subtract_again_when_canceled_order_is_saved_again(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            status="PENDING",
            is_paid=False,
        )
        order2 = Order.objects.create(
            customer="Pedro",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("20.00"),
            status="PENDING",
            is_paid=False,
        )

        order.is_paid = True
        order.status = "IN_PROGRESS"
        order.save()
        order2.is_paid = True
        order2.status = "IN_PROGRESS"
        order2.save()

        order.status = "CANCELED"
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("20.00"))

        order.customer = "Ana Updated"
        order.save()

        daily.refresh_from_db()
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("20.00"))

    def test_cancel_paid_order(self):
        order = Order.objects.create(
            customer="Ana",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("10.00"),
            status="PENDING",
            is_paid=False,
        )

        order1 = Order.objects.create(
            customer="Pedro",
            establishment=self.establishment,
            responsible_person=self.user,
            total_amount=Decimal("20.00"),
            status="PENDING",
            is_paid=False,
        )

        order.is_paid = True  # costumer paid the order
        order.status = "IN_PROGRESS"
        order.save()

        order1.is_paid = True
        order1.status = "IN_PROGRESS"
        order1.save()

        order.status = "CANCELED"  # costumer canceled the paid order
        order.save()

        daily = DailyRevenue.objects.get(establishment=self.establishment)
        print(daily)
        self.assertEqual(daily.total_orders_count, 1)
        self.assertEqual(daily.total_amount, Decimal("20"))
        