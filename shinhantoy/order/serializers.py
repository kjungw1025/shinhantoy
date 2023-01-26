from rest_framework import serializers
from .models import Order, Comment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only = True, format = '%Y-%m-%d %H:%M:%S'
    )

    def get_ord_no (self, obj):
        return obj.order.ord_no
    
    def get_member_username (self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'