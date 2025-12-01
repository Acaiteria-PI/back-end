from core.orders.models import Order, OrderItem
from core.establishment.models import Combo, CustomCup, FinalCup
from core.establishment.serializers import FinalCupSerializer, CustomCupSerializer, EstablishmentSerializer
from core.users.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class OrderSerializer(ModelSerializer):
    responsible_person_data = UserSerializer(source='responsible_person', read_only=True)
    class Meta:
        model = Order
        fields = ["id", "customer", "order_date", "total_amount", 'establishment', "status", "is_paid", "responsible_person", "responsible_person_data"]
        read_only_fields = ["id", "establishment", "responsible_person", "order_date", "total_amount", "responsible_person_data"]

class OrderItemSerializer(ModelSerializer):
    order = PrimaryKeyRelatedField(queryset=Order.objects.all())
    combo = PrimaryKeyRelatedField(queryset=Combo.objects.all(), required=False, allow_null=True)
    final_cup = PrimaryKeyRelatedField(queryset=FinalCup.objects.all(), required=False, allow_null=True)
    custom_cup = PrimaryKeyRelatedField(queryset=CustomCup.objects.all(), required=False, allow_null=True)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "type", "combo", "final_cup", "custom_cup", "quantity", "unit_price", "total_price"]
        read_only_fields = ["id"]


class OrderDetailSerializer(ModelSerializer):
    customer = UserSerializer(read_only=True)
    establishment = EstablishmentSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ["id", "customer", "establishment", "order_date", "total_amount", "status", "is_paid", "items"]
        read_only_fields = ["id"]
        
