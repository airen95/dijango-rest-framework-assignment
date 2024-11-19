from rest_framework import serializers
from .models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'product', 'discount_percentage', 'start_date', 'end_date', 'is_active']
