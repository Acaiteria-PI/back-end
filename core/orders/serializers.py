from core.orders.models import Order, OrderItem
from core.establishment.serializers import ComboSerializer, FinalCupSerializer, CustomCupSerializer, EstablishmentSerializer
from core.users.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", "customer", "order_date", "total_amount", "status", "is_paid"]
        read_only_fields = ["id"]
        
        
class OrderDetailSerializer(ModelSerializer):
    customer = UserSerializer(read_only=True)
    establishment = EstablishmentSerializer(read_only=True)
    items = ModelSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ["id", "customer", "establishment", "order_date", "total_amount", "status", "is_paid", "items"]
        read_only_fields = ["id"]
        
class OrderItemSerializer(ModelSerializer):
    order = OrderSerializer(read_only=True)
    combo = ComboSerializer(read_only=True)
    final_cup = FinalCupSerializer(read_only=True)
    custom_cup = CustomCupSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ["id", "order", "type", "combo", "final_cup", "custom_cup", "quantity", "unity_price", "total_price"]
        read_only_fields = ["id"]
        
