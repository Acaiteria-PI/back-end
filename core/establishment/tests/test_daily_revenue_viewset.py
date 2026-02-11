from datetime import datetime
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from core.establishment.models import DailyRevenue, Establishment


class TestDailyRevenueViewSet(APITestCase):
    def setUp(self):
        self.establishment = Establishment.objects.create(
            name="Pe de Acai",
            cnpj="12345678901234",
            amount=Decimal("0.00"),
        )
        self.other_establishment = Establishment.objects.create(
            name="Other Store",
            cnpj="43210987654321",
            amount=Decimal("0.00"),
        )

        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email="daily@example.com",
            password="test1234",
            name="Daily User",
            establishment=self.establishment,
            is_staff=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

        self.rev_jan_10 = DailyRevenue.objects.create(
            total_amount=Decimal("10.00"),
            total_orders_count=1,
            establishment=self.establishment,
        )
        DailyRevenue.objects.filter(pk=self.rev_jan_10.pk).update(
            date=timezone.make_aware(datetime(2026, 1, 10, 12, 0, 0))
        )
        self.rev_jan_10.refresh_from_db()

        self.rev_jan_20 = DailyRevenue.objects.create(
            total_amount=Decimal("20.00"),
            total_orders_count=2,
            establishment=self.establishment,
        )
        DailyRevenue.objects.filter(pk=self.rev_jan_20.pk).update(
            date=timezone.make_aware(datetime(2026, 1, 20, 12, 0, 0))
        )
        self.rev_jan_20.refresh_from_db()

        self.rev_feb_05 = DailyRevenue.objects.create(
            total_amount=Decimal("30.00"),
            total_orders_count=3,
            establishment=self.establishment,
        )
        DailyRevenue.objects.filter(pk=self.rev_feb_05.pk).update(
            date=timezone.make_aware(datetime(2026, 2, 5, 12, 0, 0))
        )
        self.rev_feb_05.refresh_from_db()

        self.other_establishment_rev = DailyRevenue.objects.create(
            total_amount=Decimal("99.00"),
            total_orders_count=9,
            establishment=self.other_establishment,
        )
        DailyRevenue.objects.filter(pk=self.other_establishment_rev.pk).update(
            date=timezone.make_aware(datetime(2026, 1, 20, 12, 0, 0))
        )
        self.other_establishment_rev.refresh_from_db()

    def test_filters_by_date_range_inclusive(self):
        url = reverse("api:daily-revenues-list")
        response = self.client.get(
            url, {"start_date": "2026-01-15", "end_date": "2026-01-31"}
        )

        self.assertEqual(response.status_code, 200)
        returned_ids = [item["id"] for item in response.data]
        self.assertEqual(returned_ids, [self.rev_jan_20.id])

    def test_filters_with_only_start_date(self):
        url = reverse("api:daily-revenues-list")
        response = self.client.get(url, {"start_date": "2026-01-20"})

        self.assertEqual(response.status_code, 200)
        returned_ids = [item["id"] for item in response.data]
        self.assertEqual(returned_ids, [self.rev_feb_05.id, self.rev_jan_20.id])

    def test_returns_400_for_invalid_start_date_format(self):
        url = reverse("api:daily-revenues-list")
        response = self.client.get(url, {"start_date": "20-01-2026"})

        self.assertEqual(response.status_code, 400)
        self.assertIn("start_date", response.data)

    def test_returns_400_when_start_date_is_after_end_date(self):
        url = reverse("api:daily-revenues-list")
        response = self.client.get(
            url, {"start_date": "2026-02-10", "end_date": "2026-02-01"}
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("date_range", response.data)

    def test_returns_only_logged_user_establishment_records(self):
        url = reverse("api:daily-revenues-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        returned_ids = [item["id"] for item in response.data]

        self.assertEqual(
            returned_ids,
            [self.rev_feb_05.id, self.rev_jan_20.id, self.rev_jan_10.id],
        )
        self.assertNotIn(self.other_establishment_rev.id, returned_ids)
