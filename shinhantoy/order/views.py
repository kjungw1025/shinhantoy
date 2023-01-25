from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Order
from .serializers import (
    OrderSerializer,
)
from .paginations import OrderLargePagination

# Create your views here.

class OrderListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView    
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, args, kwargs)