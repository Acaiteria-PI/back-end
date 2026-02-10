from django.utils.dateparse import parse_date
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from core.establishment.models import DailyRevenue
from core.establishment.serializers import DailyRevenueSerializer


class DailyRevenueViewSet(ModelViewSet):
    queryset = DailyRevenue.objects.all().order_by("-date")
    serializer_class = DailyRevenueSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(establishment=self.request.user.establishment)

        start_date_str = self.request.query_params.get("start_date")
        end_date_str = self.request.query_params.get("end_date")

        start_date = parse_date(start_date_str) if start_date_str else None
        end_date = parse_date(end_date_str) if end_date_str else None

        if start_date_str and not start_date:
            raise ValidationError({"start_date": "Use format YYYY-MM-DD"})

        if end_date_str and not end_date:
            raise ValidationError({"end_date": "Use format YYYY-MM-DD"})

        if start_date and end_date and start_date > end_date:
            raise ValidationError(
                {"date_range": "start_date must be less than or equal to end_date"}
            )

        if start_date:
            queryset = queryset.filter(date__date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(date__date__lte=end_date)

        return queryset