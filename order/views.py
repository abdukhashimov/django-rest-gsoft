from django.shortcuts import render
from rest_framework import generics
from .models import Order, BaseContact
from .serializers import OrderSerializer, BaseContactSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BaseContactCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = BaseContactSerializer
