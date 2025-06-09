from django.shortcuts import render
from rest_framework import viewsets
from core.users.models import User
from core.users.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer