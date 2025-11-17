from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.orders.models import Order, OrderItem
from core.orders.serializers import OrderSerializer, OrderDetailSerializer, OrderItemSerializer

# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer
    
    
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ["get", "post", "put", "delete"]