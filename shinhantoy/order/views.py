from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Order, Comment
from .serializers import (
    OrderSerializer,
    OrderDetailSerializer,
    CommentSerializer,
    CommentCreateSerializer
)
from .paginations import OrderLargePagination, CommentPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


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
    generics.GenericAPIView,
    # mixins.RetrieveModelMixin,
):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('ord_id')
        return Order.objects.filter(id=order_id)
        # return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)   
        # return self.retrieve(request, args, kwargs)   

class CommentView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    pagination_class = CommentPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(order_id=pk)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        commentid = request.data.get('id')
        memberid = request.user.id
        comment = Comment.objects.filter(id=commentid, member_id=memberid)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)