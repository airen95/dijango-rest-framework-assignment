from rest_framework import serializers
from .models import Merchant
from products.serializers import ProductSerializer

class MerchantSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='product_set')

    class Meta:
        model = Merchant
        fields = ['id', 'name', 'user', 'created_at', 'updated_at', 'products']
        

