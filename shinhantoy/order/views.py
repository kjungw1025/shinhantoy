from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Order, Comment
from .serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    CommentSerializer,
    CommentCreateSerializer
)
from .paginations import OrderLargePagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class OrderListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView    
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.ListModelMixin, 
    generics.GenericAPIView  
):
    serializer_class = OrderDetailSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        ord_no = self.kwargs.get('ord_no')
        return Order.objects.filter(ord_no=ord_no)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)   

class CommentListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView  
):
    serializer_class = CommentSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        ord_no = self.kwargs.get('ordno')
        if ord_no:
            return Comment.objects.filter(ord_no=ord_no)
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]

    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('-id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)